from dataclasses import dataclass
import json
from datetime import datetime
from pathlib import Path
from typing import Any, List, Optional, Set

from loguru import logger
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Defaults

from mate3.devices import DeviceValues
from mate3.sunspec.fields import Field, IntegerField, Mode, Uint32Field, FieldValue
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
        self.size += field.size


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
        for field in sorted(fields, key=lambda x: x.start):
            if previous_range is None or previous_range.end != field.start or previous_range.size >= max_range_size:
                previous_range = ReadingRange(fields=[field], start=field.start, size=field.size)
                ranges.append(previous_range)
            else:
                previous_range.extend(field)
        return ranges

    def _read_model(self, address, first, only: List[Field]):

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
            return None, None, None

        model = MODEL_DEVICE_IDS[device_id]

        # get the readable fields:
        fields = [field for field in model.__model_fields__ if field.mode in (Mode.R, Mode.RW)]
        if only:
            fields = [field for field in fields if field in only or field.name in ("length", "port_number")]

        # Order fields by start registry, as this is the order in which we will receive the values
        fields = sorted(fields, key=lambda f: f.start)

        # Get registers in large ranges, as this drastically improves performance and isn't so demanding of the mate3
        field_reads = {}
        for reading_range in self._get_reading_ranges(fields):
            logger.debug(
                f"Reading range {reading_range.start} -> {reading_range.end}, of {len(reading_range.fields)} fields"
            )
            register_number = address + reading_range.start - 1
            registers = self.client.read_holding_registers(address=register_number, count=reading_range.size)
            read_time = datetime.now()

            for field in reading_range.fields:
                try:
                    implemented, value = field.from_registers(registers[: field.size])
                    field_reads[field.name] = FieldRead(
                        value=value, implemented=implemented, time=read_time, scale_factor=None
                    )
                except Exception as e:
                    logger.warning(f"Error reading field {field.name} - so setting as not implemented. Message: {e}")
                    field_reads[field.name] = FieldRead(
                        value=None, implemented=False, time=read_time, scale_factor=None
                    )
                registers = registers[field.size :]

        for field in fields:
            if isinstance(field, IntegerField) and field.scale_factor is not None:
                scale_factor = field_reads[field.scale_factor.name]
                if not scale_factor.implemented:
                    raise RuntimeError("Scale factor isn't implemented!")
                field_reads[field.name].scale_factor = scale_factor

        return model, field_reads

    def read(self, only: Optional[List[FieldValue]] = None):
        register = self.sunspec_register
        max_models = 30
        first = True
        model_field_reads = {}
        only_fields = []
        if only is not None:
            for field in only:
                field = field.field
                if field.mode not in (Mode.R, Mode.RW):
                    raise RuntimeError("Can't read from a read-only field!")
                only_fields.append(field)
                # read the scale factor too, if needed:
                if isinstance(field, IntegerField) and field.scale_factor is not None:
                    only_fields.append(field.scale_factor)
        for _ in range(max_models):
            model, field_reads = self._read_model(register, first, only_fields)
            first = False

            # Unknown device
            if not model:
                continue

            # No more blocks to read
            if model == SunSpecEndModel:
                break

            # record for use out of loop:
            model_field_reads.setdefault(model, [])
            model_field_reads[model].append((register, field_reads))

            # move register to next block - that is, add the length of the block (which excludes DID + length) and
            # the DID and length fields lengths (each one - hence the +2)
            register += field_reads["length"].value + 2
            # TODO: why + 2 for sunspec? +1 yes, as the ID is a uint32, but that's only one extra 16 bits, not 2 ... maybe padding?
            if model == SunSpecHeaderModel:
                register += 2

        # create devices if needed:
        if self._devices is None:
            self._devices = DeviceValues()

        # update:
        self._devices.update(model_field_reads)

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

        # TODO: write in ranges?
        for device in self._devices.connected_devices:
            for field_value in device:
                if field_value.dirty:
                    if field_value.field.mode not in (Mode.RW, Mode.W):
                        raise RuntimeError(f"Can't write to field {field_value.name}")
                    logger.info(f"writing {field_value._value_to_write} to {field_value.name}")
                    address = device._address + field_value.field.start - 1  # -1 since start is 1-indexed
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
        # for d in client.devices.connected_devices:
        #     print(d.__class__.__name__, d._address)
        print("the system!")
        print(client.devices.mate3.system_name)
        print("get the voltage")
        print(client.devices.fndc.battery_voltage)
        print("read only battery voltage again and check only it's read time was updated but not system name")
        client.read(only=[client.devices.fndc.battery_voltage])
        print(client.devices.mate3.system_name)
        print(client.devices.fndc.battery_voltage)
        print("nice. what about not implememted?")
        print(client.devices.mate3.sched_1_ac_mode)
        print("can we set a new value?")
        volts = client.devices.charge_controller.config.absorb_volts
        print(volts)
        client.devices.charge_controller.config.absorb_volts.value = volts.value + 0.1
        print(volts)
        client.write()
