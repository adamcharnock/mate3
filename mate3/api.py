import pickle
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import List

from loguru import logger
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Defaults

from mate3.sunspec.fields import Field, IntegerField, Mode, Uint16Field, Uint32Field
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


class FieldValue:
    def __init__(self, field):
        self.field = field
        self.modbus_value = None
        self.parsed_value = None
        self.last_read = None
        self.dirty = False
        self.implemented = None
        self._value_to_write = None
        self._raw_value = None
        self._scale_factor = None
        self._scale_factor_cache_time = timedelta(seconds=60)

    @property
    def _should_be_scaled(self):
        return isinstance(self.field, IntegerField) and self.field.scale_factor is not None

    @property
    def value(self):
        if self.field.mode == Mode.W:
            raise RuntimeError("Can't read from a write-only field!")
        if not self.implemented:
            return None
        if not self._should_be_scaled:
            return self._raw_value
        # scale it:
        value = self._raw_value * 10 ** self._scale_factor
        # round it to what it should be after scaling:
        return round(value, -self._scale_factor if self._scale_factor < 0 else 0)

    @value.setter
    def value(self, value):
        if self.field.mode == Mode.R:
            raise RuntimeError("Can't write to a read-only field!")
        if self.last_read is None:
            raise RuntimeError("You should read a field at least once before writing")
        if not self.implemented:
            raise RuntimeError("This field is marked as not implemented, so you shouldn't write to it!")
        if self._should_be_scaled:
            # Time limit on scale_factor being applicable?
            if (datetime.now() - self.last_read) > self._scale_factor_cache_time:
                raise ValueError(
                    (
                        f"You need to read this value within {self._scale_factor_cache_time} of writing to 'ensure'",
                        " the scale factor is up-to-date before you write.",
                    )
                )
            # scale it:
            value = self._raw_value / 10 ** self._scale_factor
            # round it to what it should be after scaling:
            self._value_to_write = int(round(value, 0))
        else:
            self._value_to_write = value
        self.dirty = True

    def _update_on_read(self, value, implemented, read_time, scale_factor=None):
        """
        Assumption is that if there's a scale factor, it's read at the same time as value, so they should be in sync.
        Not really a major with Outback, as they seem to be constant anyway.
        """
        if self._should_be_scaled:
            if scale_factor is None:
                raise RuntimeError(f"scale_factor required for field {self.field}")
            if not isinstance(scale_factor, int):
                raise RuntimeError(f"scale_factor should be an integer!")
            if scale_factor < -10 or scale_factor > 10:
                raise RuntimeError(f"scale_factor should be between -10 and 10")
        else:
            if scale_factor is not None:
                raise RuntimeError(f"No scale_factor should be provided for field {self.field}")

        self._raw_value = value
        self._scale_factor = scale_factor
        self.implemented = implemented
        self.last_read = read_time
        if self._value_to_write is not None:
            logger.warning(
                f"A value has been set to be written, but was re-read after this, so the write will be ignored "
            )
            self._value_to_write = None
        self.dirty = False


class ModelValues:
    def __init__(self, model, values):
        self._model = model
        self._values = values
        # TODO: check for diffs like below ... but allow not all values to be in values?
        # diff = set([f.name for f in self._model]).symmetric_difference(set(list(self._values.keys())))
        # if diff:
        #    raise ValueError(f"Uncommon fields: {diff}!")

    def __getattr__(self, name):
        # TODO: return a field we don't have a value for but is in the model as 'not read'?
        return self._values[name]

    def __getitem__(self, name):
        return self._values[name]

    def __repr__(self):
        return f"{self._values}"

    def items(self):
        # TODO: replace this with making class iterable
        return self._values.items()

    # def __setattr__(self, name, value):
    #    raise NotImplementedError("haven't added writing yet ...")


class Mate3(object):

    sunspec_register = 40000

    def __init__(self, client):
        self.client = client
        self.values = {}

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

    def _create_empty_model_values(self, model):
        values = {}
        for field in model:
            values[field] = FieldValue(field.value)
        return ModelValues(model, values)

    def _read_model(self, address, first, model_values):

        # read the first register for the device ID:
        response = self.client.read_holding_registers(address, count=2)
        raise_modbus_exception(response)

        # if first, then this is the SunSpecHeaderModel, which has a device ID of Uint32 type not Uint16 like the rest.
        if first:
            _, device_id = Uint32Field._from_registers(None, response.registers[:2])
        else:
            _, device_id = Uint16Field._from_registers(None, response.registers[:1])

        if device_id not in MODEL_DEVICE_IDS:
            logger.warning(f"Unknown model type with device ID {device_id}")
            return None, None

        model = MODEL_DEVICE_IDS[device_id]

        # get the readable fields:
        fields = [field for field in model if field.value.mode != Mode.W]
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
                    values[field.name] = read_time, field.value.from_registers(registers[: field.value.size])
                except Exception as e:
                    print(":" * 80)
                    print(field.name, field.value)
                    print(registers[: field.value.size])
                    print(e)
                    values[field.name] = read_time, (False, None)

                registers = registers[field.value.size :]

        # Now we have all the values, update the object:
        # TODO: create values object ... or list of them if port
        # TODO: update the values properly ...

        # key for lookup is model, port or None
        device_key = values["did"][1][1], values["port_number"][1][1] if "port_number" in values else None
        if device_key not in model_values:
            model_values[device_key] = self._create_empty_model_values(model)

        device = model_values[device_key]
        for field in fields:
            d = device[field]
            read_time, (implemented, value) = values[field.name]
            scale_factor = None
            if isinstance(field.value, IntegerField) and field.value.scale_factor is not None:
                scale_factor_read_time, (scale_factor_implemented, scale_factor) = values[field.value.scale_factor.name]
                if not scale_factor_implemented:
                    raise RuntimeError("Scale factor isn't implemented!")
                # if scale_factor is not None and val is not None:
                # TODO: check scale factor read time
            d._update_on_read(value, implemented, read_time, scale_factor)

        return model, values["length"][1][1]

    def read(self, model_values):
        register = self.sunspec_register
        max_models = 30
        first = True
        for _ in range(max_models):
            model, length = self._read_model(register, first, model_values)
            first = False

            print(model, length)

            # Unknown device
            if not model:
                continue

            # No more blocks to read
            if model == SunSpecEndModel:
                break

            # model_values[model] = values
            # move register to next block - that is, add the length of the block (which excludes DID + length) and
            # the DID and length fields lengths (each one - hence the +2)
            register += length + 2
            # TODO: which + 2 for sunspec? +1 yes, as the ID is a uint32, but that's only one extra block ... maybe padding?
            if model == SunSpecHeaderModel:
                register += 2

            # if len(model_values) > 1:
            #     break
        for (did, port), values in model_values.items():
            print("-" * 100)
            print(MODEL_DEVICE_IDS[did], did, port)
            for field, field_value in values.items():
                if field.value.mode != Mode.W:
                    print(field.name.ljust(50), "NOT IMPLEMENTED" if not field_value.implemented else field_value.value)

        return model_values

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

    model_values = {}
    with Mate3Factory("192.168.1.12", cache=True, cache_only=True) as client:
        client.read(model_values)
