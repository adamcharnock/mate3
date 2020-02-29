import logging
from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from typing import NewType, NamedTuple, Type, Union, Dict, Optional, List, Tuple

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

from mate3.base_structures import int16, Device, uint32, uint16
from mate3.io import decode_int16, combine_ints, int16s_to_str, int_to_ip_address, raise_modbus_exception

logger = logging.getLogger(__name__)


class Mode(Enum):
    R = "r"
    W = "w"
    RW = "rw"


class Field(NamedTuple):
    start: int
    size: int
    type: Type
    mode: Mode = Mode.R
    description: str = ""
    units: Optional[str] = None
    scale_factor: Union[None, str, float] = None

    # Set dynamically by parser
    name: Optional[str] = None
    device: Optional[Device] = None

    @property
    def end(self):
        return self.start + self.size


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
        self.size += field.size


class BaseParserMetaclass(type):
    """Metaclass to set the name for all Field objects on the parser"""
    def __init__(cls, name, bases, attrs):
        for field_name, field in attrs.items():
            if not isinstance(field, Field):
                continue

            setattr(cls, field_name, field._replace(name=field_name, device=attrs['device']))


class BaseParser(object, metaclass=BaseParserMetaclass):

    structure = None
    device: Device = None

    def parse(self, client: ModbusClient, register_offset: int, only_fields: Optional[List[Field]] = None):
        values = {'device': self.device}

        if only_fields is None:
            fields = list(self.fields.values())
        else:
            for field in only_fields:
                assert field.device == self.device
            fields = only_fields

        # Order fields by start registry, as this is the order in which we will receive the values
        fields = sorted(fields, key=lambda f: f.start)

        # Get register values in large ranges, as this drastically improves performance
        # and isn't so demanding of the mate3
        ranges = self.get_reading_ranges(fields)

        for range in ranges:
            logger.debug(f"Reading range {range.start} -> {range.end}, of {len(range.fields)} fields")
            register_number = register_offset + range.start - 1
            response = client.read_holding_registers(register_number, range.size)
            raise_modbus_exception(response)
            all_registers: List = response.registers

            for field in range.fields:
                registers = all_registers[:field.size]
                all_registers = all_registers[field.size:]

                if field.type == str:
                    value = int16s_to_str(registers)
                elif 'tcpip' in field.name and field.type == uint32:
                    value = int_to_ip_address(combine_ints(registers))
                else:
                    value = combine_ints(registers)

                value = field.type(value)

                if field.type == int16:
                    value = decode_int16(value)

                values[field.name] = value

        # If only_fields has been specified then we are going to be missing some values.
        # Therefore set all values to a default of None
        for field_name in self.structure._fields:
            values.setdefault(field_name, None)

        # Now we have all the values, do the scaling
        for name, field in self.fields.items():
            if not field.scale_factor:
                break
            elif isinstance(field.scale_factor, str):
                scale_factor = values[field.scale_factor]
            else:
                scale_factor = field.scale_factor

            if scale_factor:
                values[name] *= scale_factor

        return self.structure(**values)

    @property
    @lru_cache()
    def fields(self) -> Dict[str, Field]:
        return {
            name: getattr(self, name)
            for name in dir(self)
            if name != "fields" and isinstance(getattr(self, name), Field)
        }

    def get_reading_ranges(self, fields: List[Field]) -> List[ReadingRange]:
        """Get the ranges of registers which can be read as a contiguous block

        This allows for greater performance than reading a single register at a time.
        """
        # Order fields by their starting registry
        fields = sorted(fields, key=lambda f: f.start)
        # We'll collect our ranges here
        ranges: List[ReadingRange] = []

        # The mate3s gets unhappy if one tries to read too much at once
        max_range_size = 100

        for field in fields:
            is_first_loop = not ranges
            is_contiguous = not is_first_loop and ranges[-1].end == field.start
            is_at_max_size = not is_first_loop and ranges[-1].size > max_range_size

            if is_first_loop or not is_contiguous or is_at_max_size:
                ranges.append(ReadingRange(
                    fields=[field],
                    start=field.start,
                    size=field.size
                ))
            else:
                ranges[-1].extend(field)

        return ranges


def parse(device: Device, client: ModbusClient, register_offset: int, only_fields: Optional[List[Field]] = None):
    # Find the parser for this device
    import mate3.parsers

    parser = None
    for value in mate3.parsers.__dict__.values():
        if hasattr(value, 'device') and issubclass(value, BaseParser) and value != BaseParser and value.device == device:
            parser = value

    if not parser:
        logger.warning(f"No parser found for device {device}, DID {device.value}")
        return

    return parser().parse(client, register_offset, only_fields)


class SunspecHeaderBlock(NamedTuple):
    device: Device
    sunspec_id: uint32
    model_id: uint16
    total_subsequent_registers: uint16
    manufacturer: str
    model: str
    options: str
    version: str
    serial_number: str


class SunspecHeaderParser(BaseParser):
    structure = SunspecHeaderBlock
    device = Device.sunspec_header

    sunspec_id = Field(start=1, size=2, type=uint32)
    model_id = Field(start=3, size=1, type=uint16)
    total_subsequent_registers = Field(start=4, size=1, type=uint16)
    manufacturer = Field(start=5, size=16, type=str)
    model = Field(start=21, size=16, type=str)
    options = Field(start=37, size=8, type=str)
    version = Field(start=45, size=8, type=str)
    serial_number = Field(start=53, size=16, type=str)
