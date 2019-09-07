import logging
from enum import Enum
from functools import lru_cache
from typing import NewType, NamedTuple, Type, Union, Dict, Optional

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

from mate3.base_structures import int16, Device
from mate3.io import decode_int16


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
            value = response.registers[0]
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
        logging.warning(f"No parser found for device {device}, DID {device.value}")
        return

    return parser().parse(client, register_offset)
