from enum import Enum
from typing import NamedTuple


class SingleInverterBlock(NamedTuple):
    port_number: int
    output_current: float
    charge_current: float
    buy_current: float
    output_ac_voltage: float
    operating_mode: int
    battery_voltage: float
    temp_compensated_target_voltage: float
    battery_temperature: float
    ac_input_voltage: float
    ac_input_state: float


class ChargeControllerBlock(NamedTuple):
    did: int
    length: int
    port_number: int
    voltage_sf: int
    current_sf: int
    power_sf: int
    ah_sf: int
    kwh_sf: int
    batt_voltage: float
    array_voltage: float
    batt_current: float
    array_current: float
    charger_state: float
    watts: float
    todays_min_battery_volts: float
    todays_max_battery_volts: float
    voc: float
    todays_peak_voc: int
    todays_kwh: float
    todays_ah: float
    lifetime_kwh_hours: int
    lifetime_kamp_hours: float
    lifetime_max_watts: float
    lifetime_max_battery_volts: float
    lifetime_max_voc: float
    temp_sf: int
    temp_output_fets: float
    temp_enclosure: float


class FlexnetDcBlock(NamedTuple):
    shunt_a_port: int
    shunt_a_current: float
    shunt_b_current: float
    shunt_c_current: float
    battery_voltage: float
    battery_temperature: float
    state_of_charge: float


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
    sunspec_inverter_single_phase: int = 101
    sunspec_inverter_split_phase: int = 102
    sunspec_inverter_three_phase: int = 103
    opticsre_statistics: int = 64255
    end_of_sun_spec: int = 65535
