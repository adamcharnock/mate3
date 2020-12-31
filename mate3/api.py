from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, List, Optional

from loguru import logger
from pymodbus.constants import Defaults

from mate3.devices import DeviceValues
from mate3.field_values import FieldValue
from mate3.modbus_client import CachingModbusClient, ModbusTcpClient, NonCachingModbusClient
from mate3.sunspec.fields import Field, IntegerField, Mode, Uint16Field, Uint32Field
from mate3.sunspec.models import MODEL_DEVICE_IDS, SunSpecEndModel, SunSpecHeaderModel


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
        self._client: ModbusTcpClient = None
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
            self._client = NonCachingModbusClient(self.host, self.port)

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
            if (
                previous_range is None
                or previous_range.end != field.start
                or previous_range.size + field.size >= max_range_size
            ):
                previous_range = ReadingRange(fields=[field], start=field.start, size=field.size)
                ranges.append(previous_range)
            else:
                previous_range.extend(field)
        return ranges

    def _read_model(self, device_address: int, first: bool):
        """
        Read an individual model at `address`. Use `first` to specify that this is the first block - see comment below.
        By default reads everything in the model - use `only` to specify a list of Fields to read, if you want to limit.
        """

        # Read the first register for the device ID:
        registers = self._client.read_holding_registers(address=device_address, count=2)

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

        # TODO: Make sure we don't read past the end of length (as reported by device). This shouldn't happen except in
        # e.g. a case where the (old) device model firmware returns only 10 fields, and then 'new' one (whatever we're
        # using in our spec) specifies 11, then we'd accidentally try to read one more.

        # Get the readable fields:
        fields = [field for field in model.__model_fields__ if field.mode in (Mode.R, Mode.RW)]

        # Order fields by start registry, as this is the order in which we will receive the values
        fields = sorted(fields, key=lambda f: f.start)

        # Get registers in large ranges, as this drastically improves performance and isn't so demanding of the mate3
        field_reads = []
        for reading_range in self._get_reading_ranges(fields):
            logger.debug(
                f"Reading range {reading_range.start} -> {reading_range.end}, of {len(reading_range.fields)} fields"
            )
            register_number = device_address + reading_range.start - 1  # -1 as starts are 1-indexed in fields
            registers = self._client.read_holding_registers(address=register_number, count=reading_range.size)

            offset = 0
            for field in reading_range.fields:
                address = register_number + offset
                try:
                    field_registers = registers[offset : offset + field.size]
                    if len(field_registers) != field.size:
                        raise RuntimeError(
                            "Didn't get the right number of registers from reading range for this field."
                        )
                    implemented, raw_value = field.from_registers(field_registers)
                    field_reads.append((field, address, raw_value, implemented))
                except Exception as e:
                    logger.warning(f"Error reading field {field.name} - so setting as not implemented. Message: {e}")
                    field_reads.append((field, address, None, False))
                offset += field.size

        # OK, convert to field values. Note that we need to process scale factors first:
        scale_factor_names = set()
        for field, *_ in field_reads:
            if isinstance(field, IntegerField) and field.scale_factor is not None:
                scale_factor_names.add(field.scale_factor.name)
        scale_factors = {}
        for field, address, raw_value, implemented in field_reads:
            if field.name in scale_factor_names:
                if isinstance(field, IntegerField) and field.scale_factor is not None:
                    raise RuntimeError(f"Scale factor {field.name} shouldn't have it's own scale factor!")
                scale_factors[field.name] = FieldValue(
                    client=self,
                    field=field,
                    scale_factor=None,
                    address=address,
                    raw_value=raw_value,
                    implemented=implemented,
                )

        # Now process remaining non-scale-factors:
        non_scale_factors = {}
        for field, address, raw_value, implemented in field_reads:
            if field.name not in scale_factor_names:
                scale_factor = None
                if isinstance(field, IntegerField) and field.scale_factor is not None:
                    scale_factor = scale_factors[field.scale_factor.name]
                non_scale_factors[field.name] = FieldValue(
                    client=self,
                    field=field,
                    scale_factor=scale_factor,
                    address=address,
                    raw_value=raw_value,
                    implemented=implemented,
                )

        # Combine 'em:
        field_values = {**scale_factors, **non_scale_factors}

        return model, field_values

    def read(self):
        """
        Read all values from all devices. If you want to read only specified fields use e.g.
            client.devices.mate3.system_name.read()
        """
        register = self.sunspec_register
        max_models = 30
        first = True
        model_field_values = {}
        model_addresses = {}
        for _ in range(max_models):
            model, field_values = self._read_model(register, first)
            first = False

            # Unknown device
            if not model:
                continue
            # No more blocks to read
            if model == SunSpecEndModel:
                break

            # record for use out of loop:
            model_field_values.setdefault(model, [])
            model_field_values[model].append(field_values)
            model_addresses.setdefault(model, [])
            model_addresses[model].append(register)

            # Move register to next block - that is, add the length of the block, which is what follows after the length
            # field. For normal fields, we'll already have read 2 registers (DI and length) so we must add this to our
            # total increment. For the SunSpecHeaderModel, we need to add 4 as DID is a UInt32 in this case (i.e. 2
            # registers) and there's a model ID field (1 register) and length (1 register)
            register += field_values["length"].value + (4 if model == SunSpecHeaderModel else 2)

        # create devices if needed:
        if self._devices is None:
            self._devices = DeviceValues()

        # update:
        self._devices.update(model_field_values, model_addresses)

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
                    self._client.write_registers(address, registers)

    def read_all_modbus_values_unparsed(self):
        """
        This method just reads all of the values from the modbus devices, with no care about parsing them. All it
        assumes is the standard structure of two registers (DID + length), except for the header.
        """
        register = self.sunspec_register
        max_models = 30
        first = True
        reads = {}
        for _ in range(max_models):
            # Data starts generally at 3rd register, except for start (SunSpecHeaderModel) where it starts at 5th
            data_offset = 4 if first else 2
            registers = self._client.read_holding_registers(address=register, count=data_offset)
            # The length is the last register (i.e. the one before data)
            _, length = Uint16Field._from_registers(None, registers[-1:])

            # We're done when length == 0 i.e. SunSpecEndModel
            if length == 0:
                break

            # Now read everything (in maximum bunches of 100)
            batch = 100
            for start_offset in range(0, length, batch):
                count = min(batch, length - start_offset)
                registers = self._client.read_holding_registers(
                    address=register + data_offset + start_offset, count=count
                )
                addresses = [register + i for i in range(count)]
                for addr, bites in zip(addresses, registers):
                    reads[addr] = bites

            # See comment in self.read re the increment of 2 or 4
            register += length + (4 if first else 2)
            first = False

        return reads
