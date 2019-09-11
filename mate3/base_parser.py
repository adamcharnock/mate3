import logging
from enum import Enum
from functools import lru_cache
from typing import NewType, NamedTuple, Type, Union, Dict, Optional

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

from mate3.base_structures import int16, Device, uint32, uint16
from mate3.io import decode_int16, combine_ints, int16s_to_str, int_to_ip_address

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


class BaseParser(object):

    structure = None
    device: Device = None

    def parse(self, client: ModbusClient, register_offset: int):
        values = {}
        for name, field in self.fields.items():
            register_number = register_offset + field.start - 1
            response = client.read_holding_registers(register_number, field.size)

            if field.type == str:
                value = int16s_to_str(response.registers)
            elif 'tcpip' in name and field.type == uint32:
                value = int_to_ip_address(combine_ints(response.registers))
            else:
                value = combine_ints(response.registers)

            value = field.type(value)

            if field.type == int16:
                value = decode_int16(value)

            values[name] = value

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


def parse(device: Device, client: ModbusClient, register_offset: int):
    # Find the parser for this device
    import mate3.parsers

    parser = None
    for value in mate3.parsers.__dict__.values():
        if hasattr(value, 'device') and issubclass(value, BaseParser) and value != BaseParser and value.device == device:
            parser = value

    if not parser:
        logger.warning(f"No parser found for device {device}, DID {device.value}")
        return

    return parser().parse(client, register_offset)


class SunspecHeaderBlock(NamedTuple):
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
