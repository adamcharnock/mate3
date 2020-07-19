import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, List, Optional

from loguru import logger
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Defaults

from mate3.devices import DeviceValues
from mate3.field_values import FieldRead, FieldValue
from mate3.sunspec.fields import Field, IntegerField, Mode, Uint32Field
from mate3.sunspec.models import MODEL_DEVICE_IDS, SunSpecEndModel, SunSpecHeaderModel


class CachingModbusClient(ModbusClient):
    """
    This is a simple wrapper around ModbusClient that can cache values during use, write them to disk, and then read
    those values. It's particularly useful for:

        - Testing/debugging if you don't have the same physical Outback gear as others.
        - Not hammering your Mate3 while developing, and continually having to restart it!

    If cache_only is False, the cache will be continually updated with anything not in the cache, whereas if True, then
    the cache won't be updated i.e. it's never hit the Mate3 directly and only rely on the cache.
    """

    def __init__(self, cache_path: str, *args, cache_only: bool = False, **kwargs):
        self._cache_path = Path(cache_path)
        self._cache = {}
        self._cache_only = cache_only
        if self._cache_path.exists():
            self._cache = self._read_cache()
        else:
            if self._cache_only:
                raise RuntimeError("Cache doesn't exist!")
        self._cache_only = cache_only
        if not self._cache_only:
            super().__init__(*args, **kwargs)

    def _read_cache(self):
        with open(self._cache_path) as f:
            cache = json.load(f)
            cache = {int(addr): val for addr, val in cache.items()}
        return cache

    def _write_cache(self):
        with open(self._cache_path, "w") as f:
            json.dump(self._cache, f)

    def read_holding_registers(self, address, count):
        """
        Replace the existing method with our own to do the caching.
        """
        # Get all the addresses:
        addresses = [address + i for i in range(count)]
        # If there are any uncached, then we read the whole lot again:
        if any(addr not in self._cache for addr in addresses):
            if self._cache_only:
                # If we're cache_only, then cache miss is an error
                raise ValueError("Uncached lookup!")
            response = super().read_holding_registers(address=address, count=count)
            if isinstance(response, Exception):
                raise response
            for addr, bites in zip(addresses, response.registers):
                self._cache[addr] = bites
        # Return results from cache:
        return [self._cache[addr] for addr in addresses]

    def close(self, *args, **kwargs):
        """
        On close, write the cache then close properly.
        """
        self._write_cache()
        if not self._cache_only:
            super().close(*args, **kwargs)


@dataclass(frozen=False)
class ReadingRange:
    """
    Mate's work better reading a contiguous range of values at once as opposed to indivudally. This is a simple wrapper
    for such a contiguous range.
    """

    fields: List[Field]
    start: int
    size: int

    @property
    def end(self):
        return self.start + self.size

    def extend(self, field: Field):
        self.fields.append(field)
        self.size += field.size


class Mate3Client:
    """
    The main Mate3 object users will interact with. Can (and should) be used as a context manager.
    """

    sunspec_register: int = 40000

    def __init__(self, host: str, port: int = Defaults.Port, cache_path: str = None, cache_only: bool = False):
        self.host: str = host
        self.port: int = port
        self._cache_path: str = cache_path
        self._cache_only: bool = cache_only
        self._client: ModbusClient = None
        self._devices: DeviceValues = None

    def connect(self):
        """
        Connect to the mate over modbus.
        """
        if self._cache_path is not None:
            self._client = CachingModbusClient(
                host=self.host, port=self.port, cache_path=self._cache_path, cache_only=self._cache_only
            )
        else:
            self._client = ModbusClient(self.host, self.port)

    def close(self):
        """
        Close the modbus connection to the mate.
        """
        self._client.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def devices(self) -> DeviceValues:
        if self._devices is None:
            raise RuntimeError("Can't access devices until after first read")
        return self._devices

    def _get_reading_ranges(self, fields):
        """
        Get the ranges of registers which can be read as a contiguous block, which  allows for greater performance than
        reading a single register at a time.
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

    def _read_model(self, address: int, first: bool, only: Optional[List[Field]] = None):
        """
        Read an individual model at `address`. Use `first` to specify that this is the first block - see comment below.
        By default reads everything in the model - use `only` to specify a list of Fields to read, if you want to limit.
        """

        # Read the first register for the device ID:
        registers = self._client.read_holding_registers(address=address, count=2)

        # If first, then this is the SunSpecHeaderModel, which has a device ID of Uint32 type not Uint16 like the rest.
        if first:
            _, device_id = Uint32Field._from_registers(None, registers[:2])
        else:
            # Don't use the Uint16Field parser as for the SunSpec end block the value is 65535, which is actually the
            # 'not implemented' value, so None is returned.
            device_id = registers[0]

        if device_id not in MODEL_DEVICE_IDS:
            logger.warning(f"Unknown model type with device ID {device_id}")
            return None, None

        model = MODEL_DEVICE_IDS[device_id]

        # Get the readable fields:
        fields = [field for field in model.__model_fields__ if field.mode in (Mode.R, Mode.RW)]
        if only is not None:
            # Make sure we include the length and port number, as we need that elsewhere:
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
            registers = self._client.read_holding_registers(address=register_number, count=reading_range.size)
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

    def read(self, only: Optional[Iterable[FieldValue]] = None):
        """
        Read values from the mate. By default (`only=None`), everything is read, but if you want to read only specified
        fields (which puts less strain on the mate), list the in `only`.
        """
        register = self.sunspec_register
        max_models = 30
        first = True
        model_field_reads = {}
        model_addresses = {}
        if only is not None:
            only_fields = []
            for field in only:
                field = field.field
                if field.mode not in (Mode.R, Mode.RW):
                    raise RuntimeError("Can't read from a read-only field!")
                only_fields.append(field)
                # Read the scale factor too, if needed:
                if isinstance(field, IntegerField) and field.scale_factor is not None:
                    only_fields.append(field.scale_factor)
        else:
            only_fields = None
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
            model_field_reads[model].append(field_reads)
            model_addresses.setdefault(model, [])
            model_addresses[model].append(register)

            # Move register to next block - that is, add the length of the block (which excludes DID + length) and
            # the DID and length fields lengths (each one - hence the +2)
            register += field_reads["length"].value + 2
            # TODO: why + 2 for sunspec? +1 yes, as the ID is a uint32, but that's only one extra 16 bits, not 2 ...
            # maybe padding?
            if model == SunSpecHeaderModel:
                register += 2

        # create devices if needed:
        if self._devices is None:
            self._devices = DeviceValues()

        # update:
        self._devices.update(model_field_reads, model_addresses)

    def write(self):
        """
        After having updated values on self.devices, call this function to write them to the mate itself.

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
            for field_value in device.fields():
                if field_value.dirty:
                    if field_value.field.mode not in (Mode.RW, Mode.W):
                        raise RuntimeError(f"Can't write to field {field_value.name}")
                    logger.info(f"writing {field_value._value_to_write} to {field_value.name}")
                    address = device.address + field_value.field.start - 1  # -1 since start is 1-indexed
                    # TODO: should we check that the device at the given address still has the right port?
                    registers = field_value.field.to_registers(field_value._value_to_write)
                    logger.debug(f"Setting register {address} to value {registers}")

                    # Do the write
                    self.client.write_registers(address, registers)
