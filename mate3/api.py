import pickle
from dataclasses import dataclass, fields
from datetime import datetime
from pathlib import Path
from typing import Any, List, Optional

from loguru import logger
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Defaults

from mate3.devices import DeviceValues
from mate3.sunspec.fields import Field, IntegerField, Mode, Uint32Field
from mate3.sunspec.models import MODEL_DEVICE_IDS, SunSpecEndModel, SunSpecHeaderModel


class CachingModbusClient(ModbusClient):
    def __init__(self, cache_path, cache_only=False, *args, **kwargs):
        self.cache_path = cache_path
        self.cache = {}
        self.cache_only = cache_only
        if self.cache_path.exists():
            with open(self.cache_path, "rb") as f:
                self.cache = pickle.load(f)
        else:
            if self.cache_only:
                raise RuntimeError("Cache doesn't exist!")
        self.cache_only = cache_only
        if not self.cache_only:
            super().__init__(*args, **kwargs)

    def read_holding_registers(self, *args, **kwargs):
        k = (args, tuple(sorted(kwargs.items())))
        if k in self.cache:
            return self.cache[k]
        if self.cache_only:
            raise ValueError(f"Uncached lookup at {k}")
        response = super().read_holding_registers(*args, **kwargs)
        self.cache[k] = response
        return response

    def close(self, *args, **kwargs):
        with open(self.cache_path, "wb") as f:
            pickle.dump(self.cache, f)
        if not self.cache_only:
            super().close(*args, **kwargs)


class Mate3Factory:
    def __init__(self, host: str, port: int = Defaults.Port, cache=False, cache_only=False):
        self.host = host
        self.port = port
        self.cache = cache
        self.cache_only = cache_only

    def __enter__(self) -> "Mate3":
        if self.cache:
            path = Path(__file__).parent / ".modbus_client_cache"
            self.client = CachingModbusClient(
                host=self.host, port=self.port, cache_path=path, cache_only=self.cache_only
            )
        else:
            self.client = ModbusClient(self.host, self.port)
        return Mate3(self.client)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()


mate3_connection = Mate3Factory


def raise_modbus_exception(response):
    if isinstance(response, Exception):
        raise response


@dataclass(frozen=False)
class ReadingRange(object):
    fields: List[Field]
    start: int
    size: int

    @property
    def end(self):
        return self.start + self.size

    def extend(self, field: Field):
        self.fields.append(field)
        self.size += field.value.size


@dataclass
class FieldRead:
    value: Any
    implemented: bool
    time: datetime
    scale_factor: Optional[Any] = None


class Mate3(object):

    sunspec_register = 40000

    def __init__(self, client):
        self.client = client
        self._devices = None

    @property
    def devices(self) -> DeviceValues:
        if self._devices is None:
            raise RuntimeError("Can't access devices until after first read")
        return self._devices

    def _get_reading_ranges(self, fields):
        """
        Get the ranges of registers which can be read as a contiguous block
        This allows for greater performance than reading a single register at a time.
        """

        # The mate3s gets unhappy if one tries to read too much at once
        max_range_size = 100

        # Loop through fields in start order, finding contiguous blocks of registers:
        ranges = []
        previous_range = None
        for field in sorted(fields, key=lambda x: x.value.start):
            value = field.value
            if previous_range is None or previous_range.end != value.start or previous_range.size >= max_range_size:
                previous_range = ReadingRange(fields=[field], start=value.start, size=value.size)
                ranges.append(previous_range)
            else:
                previous_range.extend(field)
        return ranges

    def _read_model(self, address, first, model_values):

        # read the first register for the device ID:
        response = self.client.read_holding_registers(address, count=2)
        raise_modbus_exception(response)

        # if first, then this is the SunSpecHeaderModel, which has a device ID of Uint32 type not Uint16 like the rest.
        if first:
            _, device_id = Uint32Field._from_registers(None, response.registers[:2])
        else:
            # don't use the Uint16Field parser as for the SunSpec end block the value is 65535, which is actually the
            # 'not implemented' value, so None is returned.
            device_id = response.registers[0]

        if device_id not in MODEL_DEVICE_IDS:
            logger.warning(f"Unknown model type with device ID {device_id}")
            return None, None

        model = MODEL_DEVICE_IDS[device_id]

        # get the readable fields:
        fields = [field for field in model if field.value.mode in (Mode.R, Mode.RW)]
        # Order fields by start registry, as this is the order in which we will receive the values
        fields = sorted(fields, key=lambda f: f.value.start)

        # Get registers in large ranges, as this drastically improves performance and isn't so demanding of the mate3
        values = {}
        for range in self._get_reading_ranges(fields):
            # logger.debug(f"Reading range {range.start} -> {range.end}, of {len(range.fields)} fields")
            register_number = address + range.start - 1
            response = self.client.read_holding_registers(register_number, range.size)
            read_time = datetime.now()
            raise_modbus_exception(response)
            registers = response.registers

            for field in range.fields:
                try:
                    implemented, value = field.value.from_registers(registers[: field.value.size])
                    values[field.name] = FieldRead(
                        value=value, implemented=implemented, time=read_time, scale_factor=None
                    )
                except Exception as e:
                    print(":" * 80)
                    print(field.name, field.value)
                    print(registers[: field.value.size])
                    print(e)
                    values[field.name] = FieldRead(value=None, implemented=False, time=read_time, scale_factor=None)

                registers = registers[field.value.size :]

        # Now we have all the values, update the object:
        # TODO: create values object ... or list of them if port
        # TODO: update the values properly ...

        # key for lookup is model, port or None
        # device_key = values["did"].value, values["port_number"].value if "port_number" in values else None
        # if device_key not in model_values:
        #     model_values[device_key] = self._create_empty_model_values(model)

        # device = model_values[device_key]
        for field in fields:
            if isinstance(field.value, IntegerField) and field.value.scale_factor is not None:
                scale_factor = values[field.value.scale_factor.name]
                if not scale_factor.implemented:
                    raise RuntimeError("Scale factor isn't implemented!")
                values[field.name].scale_factor = scale_factor

        return model, values

    def read(self):
        register = self.sunspec_register
        max_models = 30
        first = True
        model_values = []
        for _ in range(max_models):
            model, values = self._read_model(register, first, model_values)
            first = False
            print(model.__name__.ljust(50))

            # Unknown device
            if not model:
                continue

            # No more blocks to read
            if model == SunSpecEndModel:
                break

            # move register to next block - that is, add the length of the block (which excludes DID + length) and
            # the DID and length fields lengths (each one - hence the +2)
            register += values["length"].value + 2
            # TODO: which + 2 for sunspec? +1 yes, as the ID is a uint32, but that's only one extra 16 bits, not 2 ... maybe padding?
            if model == SunSpecHeaderModel:
                register += 2

            # if len(model_values) > 1:
            #     break
            # for (did, port), values in model_values.items():
            #     print("-" * 100)
            #     print(MODEL_DEVICE_IDS[did], did, port)  # TODO: tidy this up
            #     for field, field_value in values.items():
            #         if field.value.mode in (Mode.R, Mode.RW):
            #             print(field.name.ljust(50), "NOT IMPLEMENTED" if not field_value.implemented else field_value.value)

            model_values.append((model, values))

        # create devices if needed:
        devices = self._devices
        if devices is None:
            devices = DeviceValues.create_empty()

        # update:
        devices.update(model_values)

        # assign back:
        self._devices = devices

        return model_values

    def write(self):
        # TODO: write in ranges?
        for port, values in self._devices.charge_controllers.items():
            # TODO: iterating through dataclasses is gross ...
            config = values.config
            for field in fields(config):
                field_name = field.name
                field_value = getattr(config, field_name)
                if field_value.dirty:
                    if field_value.field.mode not in (Mode.RW, Mode.W):
                        raise RuntimeError(f"Can't write to field {field_name}")
                    logger.info(f"writing {field_value._value_to_write} to {field_name}")

        raise NotImplementedError()

    def _set_value(self, field: Field, value: int, port: int = None):
        """Set the value for the specified field

        The value must be an integer. To discover the correct format for this
        integer you should read the data using all_blocks().

        Example:

            >>> client.set_value(
            >>>     field=ChargeControllerConfigurationDefinition.absorb_volts,
            >>>     value=330,  # 33.0 volts
            >>>     port=3,  # Optional, required when multiple devices of the same type are present
            >>> )

        Warning:

            Ensure you have read the LICENSE file before using this feature. Note the
            section which begins:

                THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
                EXPRESS OR IMPLIED

            Specifically, it is quite possible that you can cause damage to your equipment
            through use of this feature. Be careful!

        """

        raise NotImplementedError()

        if field.mode == Mode.R:
            raise Exception(f"{field.name} is read-only. You cannot set the value of this field.")

        # Look for devices which math the field and port (if specified)
        found_devices = []
        for device, start_register in self._block_information():
            if field.device != device:
                continue

            definition = get_definition(device)
            if hasattr(definition, "port_number"):
                structure = parse(device, self.client, start_register, only_fields=[definition.port_number])
                if port is not None and structure.port_number != port:
                    continue

                found_devices.append(start_register)
            else:
                found_devices.append(start_register)

        # Throw some sensible errors
        if not found_devices:
            raise Exception(f"No device of type {field.device.name} found on hub port {port}")
        if len(found_devices) > 1:
            if port:
                raise Exception(
                    f"Multiple devices of type {field.device.name} found on hub port {port}. "
                    f"This is very unexpected, please raise an issue in GitHub if you see this, "
                    f"including details of the device you are trying to set values on."
                )
            else:
                raise Exception(
                    f"Multiple devices of type {field.device.name} found. Please specify a hub port number "
                    f"using the `port` parameter."
                )

        # What register do we need to write to?
        field_register = found_devices[0] + field.start - 1

        # Split the integer into multiple values according to the field's type.
        # This will also raise an error if the provided value is to big/small.
        prepared_values = split_int(value, field.type)

        logger.debug(
            f"Setting register {field_register} to value {value} "
            f"(which is a {field.type.__name__} represented as {len(prepared_values)} values: {prepared_values})"
        )

        # Do the write
        self.client.write_registers(field_register, prepared_values)


if __name__ == "__main__":

    from mate3.sunspec.models import ChargeControllerConfigurationModel

    with Mate3Factory("192.168.1.12", cache=True, cache_only=True) as client:
        client.read()
        print(client.devices.mate3.system_name)
        volts = client.devices.charge_controller.config.absorb_volts
        print(volts)
        print(client.devices.fndc.battery_voltage.value)
        for port, values in client.devices.inverters.fxs.items():
            print(port, values.transformer_temperature)
        client.devices.charge_controller.config.absorb_volts.value = volts.value
        client.write()
