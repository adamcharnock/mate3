from typing import Union, Iterable, List, Tuple, Dict

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Defaults

from mate3.base_parser import parse, Field
from mate3.io import read_block_information, SUNSPEC_REGISTER_OFFSET
from mate3.structures import *


AnyBlock = Union[
    SunspecCommonModelBlock,
    SunspecInverterSinglePhaseBlock,
    SunspecInverterSplitPhaseBlock,
    SunspecInverterThreePhaseBlock,
    Mate3Block,
    ChargeControllerBlock,
    ChargeControllerConfigurationBlock,
    FxInverterBlock,
    FxInverterConfigurationBlock,
    SplitPhaseRadianInverterBlock,
    RadianInverterConfigurationBlock,
    SinglePhaseRadianInverterBlock,
    FlexnetDcBlock,
    FlexnetDcConfigurationBlock,
    OutbackSystemControlBlock,
]


class Mate3Factory(object):

    def __init__(self, host: str, port: int=Defaults.Port):
        self.host = host
        self.port = port

    def __enter__(self) -> "Mate3":
        self.client = ModbusClient(self.host, self.port)
        return Mate3(self.client)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()


mate3_connection = Mate3Factory


class Mate3(object):
    def __init__(self, client: ModbusClient):
        self.client = client

    def _block_information(self) -> List[Tuple[Device, int]]:
        """Get information for all available blocks

        Returns a list of 2-tuples. The first value is the Device instance, the
        second is the starting modbus register for that device
        """
        register: int = SUNSPEC_REGISTER_OFFSET
        blocks = []
        for _ in range(0, 30):
            block_size, device = read_block_information(self.client, register)

            if device is Device.end_of_sun_spec:
                # No more blocks to read
                break

            if not device:
                # Unknown device
                continue

            blocks.append((device, register))

            register = register + block_size + 2

        return blocks

    def all_blocks(self) -> Iterable[AnyBlock]:
        """Get all blocks from the mate3

        This gets all available information
        """
        for device, start_register in self._block_information():
            structure = parse(device, self.client, start_register)
            if structure:
                yield structure

    def get_device_blocks(self, device: Device):
        """Get all blocks for the given device"""
        for device, start_register in self._block_information():
            if device != device:
                continue

            structure = parse(device, self.client, start_register)
            if structure:
                yield structure

    def get_values(self, *fields: Field) -> Dict[Field, List]:
        fields_by_device: Dict[Device, List[Field]] = {}
        values_by_field: Dict[Field, List] = {}

        for field in fields:
            fields_by_device.setdefault(field.device, [])
            fields_by_device[field.device].append(field)

        for device, start_register in self._block_information():
            if device not in fields_by_device:
                continue

            fields_ = fields_by_device[device]
            structure = parse(device, self.client, start_register, only_fields=fields_)
            for field in fields_:
                values_by_field.setdefault(field, [])
                values_by_field[field].append(getattr(structure, field.name))

        return values_by_field

