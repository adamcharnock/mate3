from dataclasses import dataclass, fields
import json
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
            self.cache = self._read_cache()
        else:
            if self.cache_only:
                raise RuntimeError("Cache doesn't exist!")
        self.cache_only = cache_only
        if not self.cache_only:
            super().__init__(*args, **kwargs)

    def _read_cache(self):
        with open(self.cache_path) as f:
            cache = json.load(f)
            cache = {int(addr): val for addr, val in cache.items()}
        return cache

    def _write_cache(self):
        with open(self.cache_path, "w") as f:
            json.dump(self.cache, f)

    def read_holding_registers(self, address, count):
        addresses = [address + i for i in range(count)]
        # ok, need to handle uncached stuff:
        if any(addr not in self.cache for addr in addresses):
            if self.cache_only:
                # if we're cache_only, then cache miss is an error
                raise ValueError(f"Uncached lookup at {k}")
            response = super().read_holding_registers(address=address, count=count)
            if isinstance(response, Exception):
                raise response
            for addr, bites in zip(addresses, response.registers):
                self.cache[addr] = bites
        # done!
        return [self.cache[addr] for addr in addresses]

    def close(self, *args, **kwargs):
        self._write_cache()
        if not self.cache_only:
            super().close(*args, **kwargs)


class Mate3Factory:
    def __init__(self, host: str, port: int = Defaults.Port, cache_path=None, cache_only=False):
        self.host = host
        self.port = port
        self.cache_path = cache_path
        self.cache_only = cache_only
        self._client = None

    def __enter__(self) -> "Mate3":
        if self.cache_path is not None:
            self._client = CachingModbusClient(
                host=self.host, port=self.port, cache_path=self.cache_path, cache_only=self.cache_only
            )
        else:
            self._client = ModbusClient(self.host, self.port)
        return Mate3(self._client)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.close()


mate3_connection = Mate3Factory


@dataclass(frozen=False)
class ReadingRange:
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

    def _read_model(self, address, first):

        # read the first register for the device ID:
        registers = self.client.read_holding_registers(address=address, count=2)

        # if first, then this is the SunSpecHeaderModel, which has a device ID of Uint32 type not Uint16 like the rest.
        if first:
            _, device_id = Uint32Field._from_registers(None, registers[:2])
        else:
            # don't use the Uint16Field parser as for the SunSpec end block the value is 65535, which is actually the
            # 'not implemented' value, so None is returned.
            device_id = registers[0]

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
            logger.debug(f"Reading range {range.start} -> {range.end}, of {len(range.fields)} fields")
            register_number = address + range.start - 1
            registers = self.client.read_holding_registers(address=register_number, count=range.size)
            read_time = datetime.now()

            for field in range.fields:
                try:
                    implemented, value = field.value.from_registers(registers[: field.value.size])
                    values[field.name] = FieldRead(
                        value=value, implemented=implemented, time=read_time, scale_factor=None
                    )
                except Exception as e:
                    logger.warning(f"Error reading field {field.name} - so setting as not implemented. Message: {e}")
                    values[field.name] = FieldRead(value=None, implemented=False, time=read_time, scale_factor=None)
                registers = registers[field.value.size :]

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
            model, values = self._read_model(register, first)
            first = False

            # Unknown device
            if not model:
                continue

            # No more blocks to read
            if model == SunSpecEndModel:
                break

            # record for use out of loop:
            model_values.append((register, model, values))

            # move register to next block - that is, add the length of the block (which excludes DID + length) and
            # the DID and length fields lengths (each one - hence the +2)
            register += values["length"].value + 2
            # TODO: which + 2 for sunspec? +1 yes, as the ID is a uint32, but that's only one extra 16 bits, not 2 ... maybe padding?
            if model == SunSpecHeaderModel:
                register += 2

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
        """
        Warning:

            Ensure you have read the LICENSE file before using this feature. Note the
            section which begins:

                THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
                EXPRESS OR IMPLIED

            Specifically, it is quite possible that you can cause damage to your equipment
            through use of this feature. Be careful!
        """

        # TODO: we want the address of the device ...
        # TODO: write in ranges?
        for device in self._devices.connected_devices:
            # TODO: iterating through dataclasses is gross ...
            # ew, this will fail iterating over non-config ones, as it'll include config TODO
            for field in fields(device):
                field_name = field.name
                field_value = getattr(device, field_name)
                if field_name not in ("config", "address") and field_value.dirty:
                    if field_value.field.mode not in (Mode.RW, Mode.W):
                        raise RuntimeError(f"Can't write to field {field_name}")
                    logger.info(f"writing {field_value._value_to_write} to {field_name}")
                    address = device.address + field_value.field.start
                    registers = field_value.field.to_registers(field_value._value_to_write)
                    logger.debug(f"Setting register {address} to value {registers}")

                    # # Do the write
                    # self.client.write_registers(address, registers)
                    # raise NotImplementedError()


if __name__ == "__main__":

    import sys

    logger.remove()
    logger.add(sys.stderr, level="INFO")

    cache_path = Path(__file__).parent / ".modbus_client_cache.json"
    with Mate3Factory("192.168.1.12", cache_path=cache_path, cache_only=True) as client:
        client.read()
        for d in client.devices.connected_devices:
            print(d.__class__.__name__, d.address)
        # print(client.devices.mate3.system_name)
        # print(client.devices.mate3.sched_1_ac_mode)
        # print(client.devices.fndc.battery_voltage.value)
        # for port, values in client.devices.inverters.fxs.items():
        #     print(port, values.transformer_temperature)
        volts = client.devices.charge_controller.config.absorb_volts
        print(volts)
        client.devices.charge_controller.config.absorb_volts.value = volts.value
        print(volts)
        client.write()
