from enum import Enum
from typing import NewType

int16 = NewType("int16", int)
uint16 = NewType("uint16", int)
int32 = NewType("int32", int)
uint32 = NewType("uint32", int)


class Device(Enum):
    """Outback devices by device ID (DID)

    AXS_APP_NOTE.PDF from Outback website has the data
    """

    mate3: int = 64110
    charge_controller: int = 64111
    charge_controller_configuration: int = 64112
    split_phase_radian_inverter: int = 64115
    radian_inverter_configuration: int = 64116
    single_phase_radian_inverter: int = 64117
    fx_inverter: int = 64113
    fx_inverter_configuration: int = 64114
    flexnet_dc_configuration: int = 64119
    flexnet_dc: int = 64118
    outback_system_control: int = 64120
    sunspec_common_model: int = 1
    sunspec_inverter_single_phase: int = 101
    sunspec_inverter_split_phase: int = 102
    sunspec_inverter_three_phase: int = 103
    opticsre_statistics: int = 64255
    end_of_sun_spec: int = 65535
