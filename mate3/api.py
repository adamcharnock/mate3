from typing import Union, Iterable

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Defaults

from mate3.base_parser import parse
from mate3.io import read_block, SUNSPEC_REGISTER_OFFSET
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

    def all_blocks(self) -> Iterable[AnyBlock]:
        register: int = SUNSPEC_REGISTER_OFFSET
        for _ in range(0, 30):
            block_size, device = read_block(self.client, register)

            if device is Device.end_of_sun_spec:
                # No more blocks to read
                return

            if not device:
                # Unknown device
                continue

            structure = parse(device, self.client, register)

            if structure:
                yield structure

            register = register + block_size + 2

