"""This file is auto generated, do not edit. The generation code can be found in code_generator.py"""

from mate3.base_definitions import *
from mate3.base_structures import *
from mate3.structures import *


# This file is auto generated, do not edit. The generation code can be found in code_generator.py
class SunspecCommonModelDefinition(BaseDefinition):
    sunspec_did = Field(
        start=1,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Uniquely identifies this as a SunSpec  Common Model block",
        units=None,
        scale_factor=None,
    )
    sunspec_length = Field(
        start=2,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Length of block in 16-bit registers",
        units="Registers",
        scale_factor=None,
    )
    manufacturer = Field(
        start=3,
        size=16,
        type=str,
        mode=Mode.R,
        description="—",
        units=None,
        scale_factor=None,
    )
    model = Field(
        start=19,
        size=16,
        type=str,
        mode=Mode.R,
        description="—",
        units=None,
        scale_factor=None,
    )
    options = Field(
        start=35,
        size=8,
        type=str,
        mode=Mode.R,
        description="—",
        units=None,
        scale_factor=None,
    )
    version = Field(
        start=43,
        size=8,
        type=str,
        mode=Mode.R,
        description="—",
        units=None,
        scale_factor=None,
    )
    serialnumber = Field(
        start=51,
        size=16,
        type=str,
        mode=Mode.R,
        description="—",
        units=None,
        scale_factor=None,
    )
    deviceaddress = Field(
        start=67,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="—",
        units=None,
        scale_factor=None,
    )

    structure = SunspecCommonModelBlock
    device = Device.sunspec_common_model


# This file is auto generated, do not edit. The generation code can be found in code_generator.py
class SunspecInverterSinglePhaseDefinition(BaseDefinition):
    did = Field(
        start=1,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Uniquely identifies this as a SunSpec Single  Phase Inverter",
        units=None,
        scale_factor=None,
    )
    length = Field(
        start=2,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Length of model block",
        units="Registers",
        scale_factor=None,
    )
    ac_current = Field(
        start=3,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Total Current value",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    ac_currenta = Field(
        start=4,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Phase-A Current value",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    ac_currentb = Field(
        start=5,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Phase-B Current value",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    ac_currentc = Field(
        start=6,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Phase-C Current value",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    ac_current_scale_factor = Field(
        start=7,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Current Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_voltageab = Field(
        start=8,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase-AB value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltagebc = Field(
        start=9,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase BC value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltageca = Field(
        start=10,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase CA value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltagean = Field(
        start=11,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase-A-to-neutral value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltagebn = Field(
        start=12,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase B-to-neutral value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltagecn = Field(
        start=13,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase C-to-neutral value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltage_scale_factor = Field(
        start=14,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Voltage Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_power = Field(
        start=15,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Power value",
        units="Watts",
        scale_factor="ac_power_scale_factor",
    )
    ac_power_scale_factor = Field(
        start=16,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Power Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_frequency = Field(
        start=17,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Frequency value",
        units="Hertz",
        scale_factor="ac_frequency_scale_factor",
    )
    ac_frequency_scale_factor = Field(
        start=18,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_va = Field(
        start=19,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Apparent Power",
        units="VA",
        scale_factor="ac_va_scale_factor",
    )
    ac_va_scale_factor = Field(
        start=20,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_var = Field(
        start=21,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Reactive Power",
        units="VAR",
        scale_factor="ac_var_scale_factor",
    )
    ac_var_scale_factor = Field(
        start=22,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_pf = Field(
        start=23,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Power Factor",
        units="%",
        scale_factor="ac_pf_scale_factor",
    )
    ac_pf_scale_factor = Field(
        start=24,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_energy_wh = Field(
        start=25,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="AC Lifetime Energy production",
        units="WattHours",
        scale_factor="ac_energy_wh_scale_factor",
    )
    ac_energy_wh_scale_factor = Field(
        start=27,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Lifetime Energy production scale factor",
        units="SF",
        scale_factor=None,
    )
    dc_current = Field(
        start=28,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="DC Current value",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    dc_current_scale_factor = Field(
        start=29,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    dc_voltage = Field(
        start=30,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="DC Voltage value",
        units="Volts",
        scale_factor="dc_voltage_scale_factor",
    )
    dc_voltage_scale_factor = Field(
        start=31,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    dc_power = Field(
        start=32,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Power value",
        units="Watts",
        scale_factor="dc_power_scale_factor",
    )
    dc_power_scale_factor = Field(
        start=33,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    temperature_cab = Field(
        start=34,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Cabinet Temperature",
        units="DegreesC",
        scale_factor="temperature_scale_factor",
    )
    temperature_sink = Field(
        start=35,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Coolant or Heat Sink Temperature",
        units="DegreesC",
        scale_factor="temperature_scale_factor",
    )
    temperature_trans = Field(
        start=36,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Transformer Temperature",
        units="DegreesC",
        scale_factor="temperature_scale_factor",
    )
    temperature_other = Field(
        start=37,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Other Temperature",
        units="DegreesC",
        scale_factor="temperature_scale_factor",
    )
    temperature_scale_factor = Field(
        start=38,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    status = Field(
        start=39,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Operating State",
        units="Enumerated",
        scale_factor=None,
    )
    status_vendor = Field(
        start=40,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Vendor Defined Operating State",
        units="Enumerated",
        scale_factor=None,
    )
    event_1 = Field(
        start=41,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Event Flags (bits 0-31)",
        units="Bitfield",
        scale_factor=None,
    )
    event_2 = Field(
        start=43,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Event Flags (bits 32-63)  Future Use, set to 0",
        units="Bitfield",
        scale_factor=None,
    )
    event_1_vendor = Field(
        start=45,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Vendor Defined Event Flags (bits 0-31)",
        units="Bitfield",
        scale_factor=None,
    )
    event_2_vendor = Field(
        start=47,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Vendor Defined Event Flags (bits 32-63)    Future Use",
        units="Bitfield",
        scale_factor=None,
    )
    event_3_vendor = Field(
        start=49,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Vendor Defined Event Flags (bits 64-95)    Future Use",
        units="Bitfield",
        scale_factor=None,
    )
    event_4_vendor = Field(
        start=51,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Vendor Defined Event Flags (bits 96-127)   Future Use",
        units="Bitfield",
        scale_factor=None,
    )

    structure = SunspecInverterSinglePhaseBlock
    device = Device.sunspec_inverter_single_phase


# This file is auto generated, do not edit. The generation code can be found in code_generator.py
class SunspecInverterSplitPhaseDefinition(BaseDefinition):
    did = Field(
        start=1,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Uniquely identifies this as a SunSpec Split  Phase Inverter",
        units=None,
        scale_factor=None,
    )
    length = Field(
        start=2,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Length of model block",
        units="Registers",
        scale_factor=None,
    )
    ac_current = Field(
        start=3,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Total Current value",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    ac_currenta = Field(
        start=4,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Phase-A Current value",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    ac_currentb = Field(
        start=5,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Phase-B Current value",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    ac_currentc = Field(
        start=6,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Phase-C Current value",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    ac_current_scale_factor = Field(
        start=7,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Current Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_voltageab = Field(
        start=8,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase-AB value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltagebc = Field(
        start=9,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase BC value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltageca = Field(
        start=10,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase CA value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltagean = Field(
        start=11,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase-A-to-neutral value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltagebn = Field(
        start=12,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase B-to-neutral value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltagecn = Field(
        start=13,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase C-to-neutral value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltage_scale_factor = Field(
        start=14,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Voltage Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_power = Field(
        start=15,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Power value",
        units="Watts",
        scale_factor="ac_power_scale_factor",
    )
    ac_power_scale_factor = Field(
        start=16,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Power Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_frequency = Field(
        start=17,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Frequency value",
        units="Hertz",
        scale_factor="ac_frequency_scale_factor",
    )
    ac_frequency_scale_factor = Field(
        start=18,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_va = Field(
        start=19,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Apparent Power",
        units="VA",
        scale_factor="ac_va_scale_factor",
    )
    ac_va_scale_factor = Field(
        start=20,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_var = Field(
        start=21,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Reactive Power",
        units="VAR",
        scale_factor="ac_var_scale_factor",
    )
    ac_var_scale_factor = Field(
        start=22,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_pf = Field(
        start=23,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Power Factor",
        units="%",
        scale_factor="ac_pf_scale_factor",
    )
    ac_pf_scale_factor = Field(
        start=24,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_energy_wh = Field(
        start=25,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="AC Lifetime Energy production",
        units="WattHours",
        scale_factor="ac_energy_wh_scale_factor",
    )
    ac_energy_wh_scale_factor = Field(
        start=27,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Lifetime Energy production scale factor",
        units="SF",
        scale_factor=None,
    )
    dc_current = Field(
        start=28,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="DC Current value",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    dc_current_scale_factor = Field(
        start=29,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    dc_voltage = Field(
        start=30,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="DC Voltage value",
        units="Volts",
        scale_factor="dc_voltage_scale_factor",
    )
    dc_voltage_scale_factor = Field(
        start=31,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    dc_power = Field(
        start=32,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Power value",
        units="Watts",
        scale_factor="dc_power_scale_factor",
    )
    dc_power_scale_factor = Field(
        start=33,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    temperature_cab = Field(
        start=34,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Cabinet Temperature",
        units="DegreesC",
        scale_factor="temperature_scale_factor",
    )
    temperature_sink = Field(
        start=35,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Coolant or Heat Sink Temperature",
        units="DegreesC",
        scale_factor="temperature_scale_factor",
    )
    temperature_trans = Field(
        start=36,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Transformer Temperature",
        units="DegreesC",
        scale_factor="temperature_scale_factor",
    )
    temperature_other = Field(
        start=37,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Other Temperature",
        units="DegreesC",
        scale_factor="temperature_scale_factor",
    )
    temperature_scale_factor = Field(
        start=38,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    status = Field(
        start=39,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Operating State",
        units="Enumerated",
        scale_factor=None,
    )
    status_vendor = Field(
        start=40,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Vendor Defined Operating State",
        units="Enumerated",
        scale_factor=None,
    )
    event_1 = Field(
        start=41,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Event Flags (bits 0-31)",
        units="Bitfield",
        scale_factor=None,
    )
    event_2 = Field(
        start=43,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Event Flags (bits 32-63); Future Use, set to 0",
        units="Bitfield",
        scale_factor=None,
    )
    event_1_vendor = Field(
        start=45,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Vendor Defined Event Flags (bits 0-31)",
        units="Bitfield",
        scale_factor=None,
    )
    event_2_vendor = Field(
        start=47,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Vendor Defined Event Flags (bits 32-63)    Future Use",
        units="Bitfield",
        scale_factor=None,
    )
    event_3_vendor = Field(
        start=49,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Vendor Defined Event Flags (bits 64-95)    Future Use",
        units="Bitfield",
        scale_factor=None,
    )
    event_4_vendor = Field(
        start=51,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Vendor Defined Event Flags (bits 96-127)   Future Use",
        units="Bitfield",
        scale_factor=None,
    )

    structure = SunspecInverterSplitPhaseBlock
    device = Device.sunspec_inverter_split_phase


# This file is auto generated, do not edit. The generation code can be found in code_generator.py
class SunspecInverterThreePhaseDefinition(BaseDefinition):
    did = Field(
        start=1,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Uniquely identifies this as a SunSpec Three  Phase Inverter",
        units=None,
        scale_factor=None,
    )
    length = Field(
        start=2,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Length of model block",
        units="Registers",
        scale_factor=None,
    )
    ac_current = Field(
        start=3,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Total Current value",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    ac_currenta = Field(
        start=4,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Phase-A Current value",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    ac_currentb = Field(
        start=5,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Phase-B Current value",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    ac_currentc = Field(
        start=6,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Phase-C Current value",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    ac_current_scale_factor = Field(
        start=7,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Current Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_voltageab = Field(
        start=8,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase-AB value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltagebc = Field(
        start=9,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase BC value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltageca = Field(
        start=10,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase CA value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltagean = Field(
        start=11,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase-A-to-neutral value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltagebn = Field(
        start=12,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase B-to-neutral value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltagecn = Field(
        start=13,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Voltage Phase C-to-neutral value",
        units="Volts",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_voltage_scale_factor = Field(
        start=14,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Voltage Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_power = Field(
        start=15,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Power value",
        units="Watts",
        scale_factor="ac_power_scale_factor",
    )
    ac_power_scale_factor = Field(
        start=16,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Power Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_frequency = Field(
        start=17,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Frequency value",
        units="Hertz",
        scale_factor="ac_frequency_scale_factor",
    )
    ac_frequency_scale_factor = Field(
        start=18,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_va = Field(
        start=19,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Apparent Power",
        units="VA",
        scale_factor="ac_va_scale_factor",
    )
    ac_va_scale_factor = Field(
        start=20,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_var = Field(
        start=21,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Reactive Power",
        units="VAR",
        scale_factor="ac_var_scale_factor",
    )
    ac_var_scale_factor = Field(
        start=22,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_pf = Field(
        start=23,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Power Factor",
        units="%",
        scale_factor="ac_pf_scale_factor",
    )
    ac_pf_scale_factor = Field(
        start=24,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    ac_energy_wh = Field(
        start=25,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="AC Lifetime Energy production",
        units="WattHours",
        scale_factor="ac_energy_wh_scale_factor",
    )
    ac_energy_wh_scale_factor = Field(
        start=27,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Lifetime Energy production scale factor",
        units="SF",
        scale_factor=None,
    )
    dc_current = Field(
        start=28,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="DC Current value",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    dc_current_scale_factor = Field(
        start=29,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    dc_voltage = Field(
        start=30,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="DC Voltage value",
        units="Volts",
        scale_factor="dc_voltage_scale_factor",
    )
    dc_voltage_scale_factor = Field(
        start=31,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    dc_power = Field(
        start=32,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Power value",
        units="Watts",
        scale_factor="dc_power_scale_factor",
    )
    dc_power_scale_factor = Field(
        start=33,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    temperature_cab = Field(
        start=34,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Cabinet Temperature",
        units="DegreesC",
        scale_factor="temperature_scale_factor",
    )
    temperature_sink = Field(
        start=35,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Coolant or Heat Sink Temperature",
        units="DegreesC",
        scale_factor="temperature_scale_factor",
    )
    temperature_trans = Field(
        start=36,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Transformer Temperature",
        units="DegreesC",
        scale_factor="temperature_scale_factor",
    )
    temperature_other = Field(
        start=37,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Other Temperature",
        units="DegreesC",
        scale_factor="temperature_scale_factor",
    )
    temperature_scale_factor = Field(
        start=38,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Scale factor",
        units="SF",
        scale_factor=None,
    )
    status = Field(
        start=39,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Operating State",
        units="Enumerated",
        scale_factor=None,
    )
    status_vendor = Field(
        start=40,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Vendor Defined Operating State",
        units="Enumerated",
        scale_factor=None,
    )
    event_1 = Field(
        start=41,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Event Flags (bits 0-31)",
        units="Bitfield",
        scale_factor=None,
    )
    event_2 = Field(
        start=43,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Event Flags (bits 32-63); Future Use, set to 0",
        units="Bitfield",
        scale_factor=None,
    )
    event_1_vendor = Field(
        start=45,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Vendor Defined Event Flags (bits 0-31)",
        units="Bitfield",
        scale_factor=None,
    )
    event_2_vendor = Field(
        start=47,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Vendor Defined Event Flags (bits 32-63)    Future Use",
        units="Bitfield",
        scale_factor=None,
    )
    event_3_vendor = Field(
        start=49,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Vendor Defined Event Flags (bits 64-95)    Future Use",
        units="Bitfield",
        scale_factor=None,
    )
    event_4_vendor = Field(
        start=51,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Vendor Defined Event Flags (bits 96-127)   Future Use",
        units="Bitfield",
        scale_factor=None,
    )

    structure = SunspecInverterThreePhaseBlock
    device = Device.sunspec_inverter_three_phase


# This file is auto generated, do not edit. The generation code can be found in code_generator.py
class Mate3Definition(BaseDefinition):
    ags_quiet_time_weekday_stop_hour = Field(
        start=322,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Quiet Time Weekday Stop Hour 0-23",
        units="Hour",
        scale_factor=None,
    )
    ags_quiet_time_weekday_stop_minute = Field(
        start=323,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Quiet Time Weekday Stop Minute 0-59",
        units="Minute",
        scale_factor=None,
    )
    ags_quiet_time_weekend_start_hour = Field(
        start=324,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Quiet Time Weekend Start Hour 0-23",
        units="Hour",
        scale_factor=None,
    )
    ags_quiet_time_weekend_start_minute = Field(
        start=325,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Quiet Time Weekend Start Minute 0-59",
        units="Minute",
        scale_factor=None,
    )
    ags_quiet_time_weekend_stop_hour = Field(
        start=326,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Quiet Time Weekend Stop Hour 0-23",
        units="Hour",
        scale_factor=None,
    )
    ags_quiet_time_weekend_stop_minute = Field(
        start=327,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Quiet Time Weekend Stop Minute 0-59",
        units="Minute",
        scale_factor=None,
    )
    ags_total_generator_run_time = Field(
        start=328,
        size=2,
        type=uint32,
        mode=Mode.RW,
        description="AGS Generator Total Run Time in Seconds",
        units="Hours",
        scale_factor=None,
    )
    hbx_mode = Field(
        start=330,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Voltage Only, 2=SOC Only,  3=Both",
        units="Enumerated",
        scale_factor=None,
    )
    hbx_grid_connect_voltage = Field(
        start=331,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="HBX Grid Connect Voltage",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    hbx_grid_connect_delay = Field(
        start=332,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="HBX Grid Connect Delay",
        units="Hours",
        scale_factor="hour_scale_factor",
    )
    hbx_grid_disconnect_voltage = Field(
        start=333,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="HBX Grid Disconnect Voltage",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    hbx_grid_disconnect_delay = Field(
        start=334,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="HBX Grid Disconnect Delay",
        units="Hours",
        scale_factor="hour_scale_factor",
    )
    hbx_grid_connect_soc = Field(
        start=335,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="HBX Grid Connect SOC Percentage",
        units="Percent",
        scale_factor=None,
    )
    hbx_grid_disconnect_soc = Field(
        start=336,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="HBX Grid Disconnect SOC Percentage",
        units="Percent",
        scale_factor=None,
    )
    grid_use_interval_1_mode = Field(
        start=337,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    grid_use_interval_1_weekday_start_hour = Field(
        start=338,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 1 Weekday Start Hour  0-23",
        units="Hour",
        scale_factor=None,
    )
    grid_use_interval_1_weekday_start_minute = Field(
        start=339,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 1 Weekday Start Minute  0-59",
        units="Hour",
        scale_factor=None,
    )
    grid_use_interval_1_weekday_stop_hour = Field(
        start=340,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 1 Weekday Stop Hour  0-23",
        units="Hour",
        scale_factor=None,
    )
    grid_use_interval_1_weekday_stop_minute = Field(
        start=341,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 1 Weekday Stop Minute  0-59",
        units="Hour",
        scale_factor=None,
    )
    grid_use_interval_1_weekend_start_hour = Field(
        start=342,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 1 Weekend Start Hour  0-23",
        units="Hour",
        scale_factor=None,
    )
    grid_use_interval_1_weekend_start_minute = Field(
        start=343,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 1 Weekend Start Minute  0-59",
        units="Hour",
        scale_factor=None,
    )
    grid_use_interval_1_weekend_stop_hour = Field(
        start=344,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 1 Weekend Stop Hour | 0-23",
        units="Hour",
        scale_factor=None,
    )
    grid_use_interval_1_weekend_stop_minute = Field(
        start=345,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 1 Weekend Stop Minute  0-59",
        units="Hour",
        scale_factor=None,
    )
    grid_use_interval_2_mode = Field(
        start=346,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    grid_use_interval_2_weekday_start_hour = Field(
        start=347,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 2 Weekday Start Hour  0-23",
        units="Hour",
        scale_factor=None,
    )
    grid_use_interval_2_weekday_start_minute = Field(
        start=348,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 2 Weekday Start Minute  0-59",
        units="Hour",
        scale_factor=None,
    )
    grid_use_interval_2_weekday_stop_hour = Field(
        start=349,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 2 Weekday Stop Hour  0-23",
        units="Hour",
        scale_factor=None,
    )
    grid_use_interval_2_weekday_stop_minute = Field(
        start=350,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 2 Weekday Stop Minute  0-59",
        units="Hour",
        scale_factor=None,
    )
    grid_use_interval_3_mode = Field(
        start=351,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    grid_use_interval_3_weekday_start_hour = Field(
        start=352,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 3 Weekday Start Hour  0-23",
        units="Hour",
        scale_factor=None,
    )
    grid_use_interval_3_weekday_start_minute = Field(
        start=353,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 3 Weekday Start Minute  0-59",
        units="Hour",
        scale_factor=None,
    )
    grid_use_interval_3_weekday_stop_hour = Field(
        start=354,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 3 Weekday Stop Hour  0-23",
        units="Hour",
        scale_factor=None,
    )
    grid_use_interval_3_weekday_stop_minute = Field(
        start=355,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Use Interval 3 Weekday Stop Minute  0-59",
        units="Hour",
        scale_factor=None,
    )
    load_grid_transfer_mode = Field(
        start=356,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    load_grid_transfer_threshold = Field(
        start=357,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Load Grid Transfer Threshold kW",
        units="kWatts",
        scale_factor="voltage_scale_factor",
    )
    load_grid_transfer_connect_delay = Field(
        start=358,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Load Grid Transfer Connect Delay Seconds",
        units="Seconds",
        scale_factor=None,
    )
    load_grid_transfer_disconnect_delay = Field(
        start=359,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Load Grid Transfer Disconnect Delay  Seconds",
        units="Seconds",
        scale_factor=None,
    )
    did = Field(
        start=1,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Uniquely identifies this as a SunSpec  Outback Interface",
        units=None,
        scale_factor=None,
    )
    length = Field(
        start=2,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Length of block in 16-bit registers",
        units="Registers",
        scale_factor=None,
    )
    major_firmware_number = Field(
        start=3,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="OutBack Major firmware revision",
        units=None,
        scale_factor=None,
    )
    mid_firmware_number = Field(
        start=4,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="OutBack Mid firmware revision",
        units=None,
        scale_factor=None,
    )
    minor_firmware_number = Field(
        start=5,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="OutBack Minor firmware revision",
        units=None,
        scale_factor=None,
    )
    encryption_key = Field(
        start=6,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Encryption key for current session (0 =  Encryption not enabled)",
        units=None,
        scale_factor=None,
    )
    mac_address = Field(
        start=7,
        size=7,
        type=str,
        mode=Mode.R,
        description="Ethernet MAC address",
        units=None,
        scale_factor=None,
    )
    write_password = Field(
        start=14,
        size=8,
        type=str,
        mode=Mode.W,
        description="Password required to write to any register",
        units=None,
        scale_factor=None,
    )
    enable_dhcp = Field(
        start=22,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = DHCP Disabled, use configured network  parameter; 1 = DHCP Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    tcpip_address = Field(
        start=23,
        size=2,
        type=uint32,
        mode=Mode.RW,
        description="TCP/IP Address xxx.xxx.xxx.xxx",
        units="Address",
        scale_factor=None,
    )
    tcpip_gateway_msw = Field(
        start=25,
        size=2,
        type=uint32,
        mode=Mode.RW,
        description="TCP/IP Gateway xxx.xxx.xxx.xxx",
        units="Address",
        scale_factor=None,
    )
    tcpip_netmask_msw = Field(
        start=27,
        size=2,
        type=uint32,
        mode=Mode.RW,
        description="TCP/IP Netmask xxx.xxx.xxx.xxx",
        units="Address",
        scale_factor=None,
    )
    tcpip_dns_1_msw = Field(
        start=29,
        size=2,
        type=uint32,
        mode=Mode.RW,
        description="TCP/IP DNS 1 xxx.xxx.xxx.xxx",
        units="Address",
        scale_factor=None,
    )
    tcpip_dns_2_msw = Field(
        start=31,
        size=2,
        type=uint32,
        mode=Mode.RW,
        description="TCP/IP DNS 2 xxx.xxx.xxx.xxx",
        units="Address",
        scale_factor=None,
    )
    modbus_port = Field(
        start=33,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Outback MODBUS IP port, default 502",
        units=None,
        scale_factor=None,
    )
    smtp_server_name = Field(
        start=34,
        size=20,
        type=str,
        mode=Mode.RW,
        description="Email server name",
        units=None,
        scale_factor=None,
    )
    smtp_account_name = Field(
        start=54,
        size=16,
        type=str,
        mode=Mode.RW,
        description="Email account name",
        units=None,
        scale_factor=None,
    )
    smtp_ssl_enable = Field(
        start=70,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = SSL Disabled; 1 = SSL Enabled (not  implemented)",
        units="Enumerated",
        scale_factor=None,
    )
    smtp_email_password = Field(
        start=71,
        size=8,
        type=str,
        mode=Mode.W,
        description="Email account password",
        units=None,
        scale_factor=None,
    )
    smtp_email_user_name = Field(
        start=79,
        size=20,
        type=str,
        mode=Mode.RW,
        description="Email account User Name",
        units=None,
        scale_factor=None,
    )
    status_email_interval = Field(
        start=99,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Status Email Disabled, 1-23 Status Email  every n hours",
        units=None,
        scale_factor=None,
    )
    status_email_status_time = Field(
        start=100,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Hour of first status email of the day",
        units=None,
        scale_factor=None,
    )
    status_email_subject_line = Field(
        start=101,
        size=25,
        type=str,
        mode=Mode.RW,
        description="Status Email Subject Line",
        units=None,
        scale_factor=None,
    )
    status_email_to_address_1 = Field(
        start=126,
        size=20,
        type=str,
        mode=Mode.RW,
        description="Status Email to Address 1",
        units=None,
        scale_factor=None,
    )
    status_email_to_address_2 = Field(
        start=146,
        size=20,
        type=str,
        mode=Mode.RW,
        description="Status Email to Address 2",
        units=None,
        scale_factor=None,
    )
    alarm_email_enable = Field(
        start=166,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Disabled; 1 = Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    alarm_email_subject_line = Field(
        start=167,
        size=25,
        type=str,
        mode=Mode.RW,
        description="Status Alarm_Subject Line",
        units=None,
        scale_factor=None,
    )
    alarm_email_to_address_1 = Field(
        start=192,
        size=20,
        type=str,
        mode=Mode.RW,
        description="Status Alarm to Address 1",
        units=None,
        scale_factor=None,
    )
    alarm_email_to_address_2 = Field(
        start=212,
        size=20,
        type=str,
        mode=Mode.RW,
        description="Status Alarm to Address 2",
        units=None,
        scale_factor=None,
    )
    ftp_password = Field(
        start=232,
        size=8,
        type=str,
        mode=Mode.W,
        description="FTP password",
        units=None,
        scale_factor=None,
    )
    telnet_password = Field(
        start=240,
        size=8,
        type=str,
        mode=Mode.W,
        description="Telnet password (not implemented)",
        units=None,
        scale_factor=None,
    )
    sd_card_data_log_write_interval = Field(
        start=248,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = SD-Card Data Logging disabled,  1-60 seconds",
        units=None,
        scale_factor=None,
    )
    sd_card_data_log_retain_days = Field(
        start=249,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Log until SD-Card is full then erase oldest,  1-731 Number of days to retain data logs",
        units=None,
        scale_factor=None,
    )
    sd_card_data_logging_mode = Field(
        start=250,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Disabled; 1 = Excel Format;  2 = Compact Format",
        units="Enumerated",
        scale_factor=None,
    )
    time_server_name = Field(
        start=251,
        size=20,
        type=str,
        mode=Mode.RW,
        description="Timeserver domain name",
        units=None,
        scale_factor=None,
    )
    enable_time_server = Field(
        start=271,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Time Server Disabled, use configured  time parameters; 1 = Time  Server Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    set_time_zone = Field(
        start=272,
        size=1,
        type=int16,
        mode=Mode.RW,
        description="Time Zone -12-11",
        units="Hours",
        scale_factor=None,
    )
    enable_float_coordination = Field(
        start=273,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units=None,
        scale_factor=None,
    )
    enable_fndc_charge_termination = Field(
        start=274,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units=None,
        scale_factor=None,
    )
    enable_fndc_grid_tie_control = Field(
        start=275,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units=None,
        scale_factor=None,
    )
    voltage_scale_factor = Field(
        start=276,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    hour_scale_factor = Field(
        start=277,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Hours Scale Factor",
        units=None,
        scale_factor=None,
    )
    ags_mode = Field(
        start=278,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    ags_port = Field(
        start=279,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS device port number 0-10",
        units=None,
        scale_factor=None,
    )
    ags_port_type = Field(
        start=280,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Radian AUX Relay, 1=Radian AUX Output",
        units="Enumerated",
        scale_factor=None,
    )
    load_grid_transfer_connect_battery_voltage = Field(
        start=360,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Load Grid Transfer Low Battery Connect  Voltage",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    load_grid_transfer_re_connect_battery_voltage = Field(
        start=361,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Load Grid Transfer Low Battery Re-Connect  Voltage",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    global_charger_control_mode = Field(
        start=362,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    global_charger_control_output_limit = Field(
        start=363,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Global Charger Output Limit Amps",
        units="Amps",
        scale_factor=None,
    )
    radian_ac_coupled_control_mode = Field(
        start=364,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    radian_ac_coupled_aux_port = Field(
        start=365,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Radian Inverter Port Number for AUX  Control 0-10",
        units="Port",
        scale_factor=None,
    )
    url_update_lock = Field(
        start=366,
        size=2,
        type=uint32,
        mode=Mode.W,
        description="Unlock Key",
        units="key",
        scale_factor=None,
    )
    web_reporting_base_url = Field(
        start=368,
        size=20,
        type=str,
        mode=Mode.RW,
        description="WEB Reporting Base URL",
        units=None,
        scale_factor=None,
    )
    web_user_logged_in_status = Field(
        start=388,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=WEB User NOT logged in, 1=WEB user  logged in",
        units="Enumerated",
        scale_factor=None,
    )
    hub_type = Field(
        start=389,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="0=Legacy HUB, 4= HUB4, 10=HUB10.3,  11=HUB3PH",
        units="Enumerated",
        scale_factor=None,
    )
    hub_major_firmware_number = Field(
        start=390,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="HUB Major firmware revision",
        units=None,
        scale_factor=None,
    )
    hub_mid_firmware_number = Field(
        start=391,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="HUB Mid firmware revision",
        units=None,
        scale_factor=None,
    )
    hub_minor_firmware_number = Field(
        start=392,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="HUB Minor firmware revision",
        units=None,
        scale_factor=None,
    )
    year = Field(
        start=393,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Clock year (4 digit)",
        units=None,
        scale_factor=None,
    )
    month = Field(
        start=394,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Clock Month (1 - 12)",
        units=None,
        scale_factor=None,
    )
    day = Field(
        start=395,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Clock Day (1 - 31)",
        units=None,
        scale_factor=None,
    )
    hour = Field(
        start=396,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Clock Hour (0 - 23)",
        units=None,
        scale_factor=None,
    )
    minute = Field(
        start=397,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Clock Minute (0 - 59)",
        units=None,
        scale_factor=None,
    )
    second = Field(
        start=398,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Clock Second (0 - 59)",
        units=None,
        scale_factor=None,
    )
    temperature_battery = Field(
        start=399,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Battery temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    temperature_ambient = Field(
        start=400,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Ambient temp from temp sensor  connected to device, in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    temperature_scale_factor = Field(
        start=401,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Temperature Scale Factor",
        units=None,
        scale_factor=None,
    )
    error = Field(
        start=402,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Bit field for errors. See Outback_Error Table",
        units="Bitfield",
        scale_factor=None,
    )
    status = Field(
        start=403,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Bit field for status. See Outback_Status Table",
        units="Bitfield",
        scale_factor=None,
    )
    update_device_firmware_port = Field(
        start=404,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Device Firmware update See  Device_FW_Update",
        units="Bitfield",
        scale_factor=None,
    )
    gateway_type = Field(
        start=405,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="1=AXS Port, 2= MATE3",
        units="Enumerated",
        scale_factor=None,
    )
    system_voltage = Field(
        start=406,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="12, 24, 26, 48 or 60 VDC",
        units="Volts",
        scale_factor=None,
    )
    measured_system_voltage = Field(
        start=407,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Current system battery voltage computed  by gateway",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    ags_ac_reconnect_delay = Field(
        start=408,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS AC Reconnect Delay",
        units="Minute",
        scale_factor=None,
    )
    multi_phase_coordination = Field(
        start=409,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    sched_1_ac_mode = Field(
        start=410,
        size=1,
        type=int16,
        mode=Mode.RW,
        description="Scheduled Input Mode: -1=Disable,  0=Generator, 1=Support, 2=Grid Tied,  3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero",
        units="Enumerated",
        scale_factor=None,
    )
    sched_1_ac_mode_hour = Field(
        start=411,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Start Hour for AC Input Mode schedule 1",
        units="Hour",
        scale_factor=None,
    )
    sched_1_ac_mode_minute = Field(
        start=412,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Start Minute for AC Input Mode schedule 1",
        units="Minute",
        scale_factor=None,
    )
    sched_2_ac_mode = Field(
        start=413,
        size=1,
        type=int16,
        mode=Mode.RW,
        description="Scheduled Input Mode: -1=Disable,  0=Generator, 1=Support, 2=Grid Tied,  3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero",
        units="Enumerated",
        scale_factor=None,
    )
    sched_2_ac_mode_hour = Field(
        start=414,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Start Hour for AC Input Mode schedule 2",
        units="Hour",
        scale_factor=None,
    )
    sched_2_ac_mode_minute = Field(
        start=415,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Start Minute for AC Input Mode schedule 2",
        units="Minute",
        scale_factor=None,
    )
    sched_3_ac_mode = Field(
        start=416,
        size=1,
        type=int16,
        mode=Mode.RW,
        description="Scheduled Input Mode: -1=Disable,  0=Generator, 1=Support, 2=Grid Tied,  3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero",
        units="Enumerated",
        scale_factor=None,
    )
    sched_3_ac_mode_hour = Field(
        start=417,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Start Hour for AC Input Mode schedule 3",
        units="Hour",
        scale_factor=None,
    )
    sched_3_ac_mode_minute = Field(
        start=418,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Start Minute for AC Input Mode schedule 3",
        units="Minute",
        scale_factor=None,
    )
    auto_reboot = Field(
        start=419,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="OPTICS auto reboot every 24 hours  0=Disable, 1=24, 2=20, 3=16, 4=12, 5=8,  6=4 (hours)",
        units="Enumerated",
        scale_factor=None,
    )
    spare_reg_2 = Field(
        start=420,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Spare Register 2",
        units=None,
        scale_factor=None,
    )
    spare_reg_3 = Field(
        start=421,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Spare Register 3",
        units=None,
        scale_factor=None,
    )
    spare_reg_4 = Field(
        start=422,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Spare Register 4",
        units=None,
        scale_factor=None,
    )
    ags_generator_type = Field(
        start=281,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=AC Gen, 1=DC Gen, 2=No Gen",
        units="Enumerated",
        scale_factor=None,
    )
    ags_dc_gen_absorb_voltage = Field(
        start=282,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="DC Generator Absorb Voltage",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    ags_dc_gen_absorb_time = Field(
        start=283,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="DC Generator Absorb Time",
        units="Hour",
        scale_factor="hour_scale_factor",
    )
    ags_fault_time = Field(
        start=284,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Generator fault time delay",
        units="Minutes",
        scale_factor=None,
    )
    ags_gen_cool_down_time = Field(
        start=285,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Generator Cool Down Time",
        units="Minutes",
        scale_factor=None,
    )
    ags_gen_warm_up_time = Field(
        start=286,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Generator Warm Up Time",
        units="Minutes",
        scale_factor=None,
    )
    ags_generator_exercise_mode = Field(
        start=287,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    ags_exercise_start_hour = Field(
        start=288,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Exercise Start Hour 0-23",
        units="Hour",
        scale_factor=None,
    )
    ags_exercise_start_minute = Field(
        start=289,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Exercise Start Minute 0-59",
        units="Minutes",
        scale_factor=None,
    )
    ags_exercise_day = Field(
        start=290,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Sun, 1=Mon, 2=Tue, 3=Wed, 4=Thr,  5=Fri, 6=Sat",
        units="Enumerated",
        scale_factor=None,
    )
    ags_exercise_period = Field(
        start=291,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Exercise Period 1-240 minutes",
        units="Minutes",
        scale_factor=None,
    )
    ags_exercise_interval = Field(
        start=292,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Exercise interval 1-8 Weeks",
        units="Weeks",
        scale_factor=None,
    )
    ags_sell_mode = Field(
        start=293,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Sell During Generator Exercise Period,  0=Selling Enabled, 1=Selling Disabled",
        units="Enumerated",
        scale_factor=None,
    )
    ags_2_min_start_mode = Field(
        start=294,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    ags_2_min_start_voltage = Field(
        start=295,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Two Minute AGS Start Voltage",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    ags_2_hour_start_mode = Field(
        start=296,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    ags_2_hour_start_voltage = Field(
        start=297,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Two Hour AGS Start Voltage",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    ags_24_hour_start_mode = Field(
        start=298,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    ags_24_hour_start_voltage = Field(
        start=299,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Twenty Four Hour AGS Start Voltage",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    ags_load_start_mode = Field(
        start=300,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    ags_load_start_kw = Field(
        start=301,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Load Start kWatts",
        units="kWatts",
        scale_factor=None,
    )
    ags_load_start_delay = Field(
        start=302,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Load Start Delay",
        units="Minutes",
        scale_factor=None,
    )
    ags_load_stop_kw = Field(
        start=303,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Load Stop kWatts",
        units="kWatts",
        scale_factor=None,
    )
    ags_load_stop_delay = Field(
        start=304,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Load Stop Delay",
        units="Minutes",
        scale_factor=None,
    )
    ags_soc_start_mode = Field(
        start=305,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    ags_soc_start_percentage = Field(
        start=306,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS SOC Start Percentage",
        units="Percent",
        scale_factor=None,
    )
    ags_soc_stop_percentage = Field(
        start=307,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS SOC Stop Percentage",
        units="Percent",
        scale_factor=None,
    )
    ags_enable_full_charge_mode = Field(
        start=308,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    ags_full_charge_interval = Field(
        start=309,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS SOC Full Charge Interval",
        units="Days",
        scale_factor=None,
    )
    ags_must_run_mode = Field(
        start=310,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    ags_must_run_weekday_start_hour = Field(
        start=311,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Must Run Weekday Start Hour 0-23",
        units="Hour",
        scale_factor=None,
    )
    ags_must_run_weekday_start_minute = Field(
        start=312,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Must Run Weekday Start Minute 0-59",
        units="Minute",
        scale_factor=None,
    )
    ags_must_run_weekday_stop_hour = Field(
        start=313,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Must Run Weekday Stop Hour 0-23",
        units="Hour",
        scale_factor=None,
    )
    ags_must_run_weekday_stop_minute = Field(
        start=314,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Must Run Weekday Stop Minute 0-59",
        units="Minute",
        scale_factor=None,
    )
    ags_must_run_weekend_start_hour = Field(
        start=315,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Must Run Weekend Start Hour 0-23",
        units="Hour",
        scale_factor=None,
    )
    ags_must_run_weekend_start_minute = Field(
        start=316,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Must Run Weekend Start Minute 0-59",
        units="Minute",
        scale_factor=None,
    )
    ags_must_run_weekend_stop_hour = Field(
        start=317,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Must Run Weekend Stop Hour 0-23",
        units="Hour",
        scale_factor=None,
    )
    ags_must_run_weekend_stop_minute = Field(
        start=318,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Must Run Weekend Stop Minute 0-59",
        units="Minute",
        scale_factor=None,
    )
    ags_quiet_time_mode = Field(
        start=319,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Disabled, 1=Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    ags_quiet_time_weekday_start_hour = Field(
        start=320,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Quiet Time Weekday Start Hour 0-23",
        units="Hour",
        scale_factor=None,
    )
    ags_quiet_time_weekday_start_minute = Field(
        start=321,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Quiet Time Weekday Start Minute 0-59",
        units="Minute",
        scale_factor=None,
    )

    structure = Mate3Block
    device = Device.mate3


# This file is auto generated, do not edit. The generation code can be found in code_generator.py
class ChargeControllerDefinition(BaseDefinition):
    did = Field(
        start=1,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Uniquely identifies this as a SunSpec Basic  Charge Controller",
        units=None,
        scale_factor=None,
    )
    length = Field(
        start=2,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Length of block in 16-bit registers",
        units="Registers",
        scale_factor=None,
    )
    port_number = Field(
        start=3,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Port number on Outback network",
        units=None,
        scale_factor=None,
    )
    voltage_scale_factor = Field(
        start=4,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    current_scale_factor = Field(
        start=5,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Current Scale Factor",
        units=None,
        scale_factor=None,
    )
    power_scale_factor = Field(
        start=6,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Power Scale Factor",
        units=None,
        scale_factor=None,
    )
    ah_scale_factor = Field(
        start=7,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Amp Hours Scale Factor",
        units=None,
        scale_factor=None,
    )
    kwh_scale_factor = Field(
        start=8,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC kWH Scale Factor",
        units=None,
        scale_factor=None,
    )
    battery_voltage = Field(
        start=9,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Battery Voltage",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    array_voltage = Field(
        start=10,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="DC Source Voltage",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    battery_current = Field(
        start=11,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Battery Current",
        units="Amps",
        scale_factor="current_scale_factor",
    )
    array_current = Field(
        start=12,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="DC Source Current",
        units="Amps",
        scale_factor="power_scale_factor",
    )
    charger_state = Field(
        start=13,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="0 = Silent; 1 = Float; 2 = Bulk; 3 = Absorb;  4 = EQ",
        units="Enumerated",
        scale_factor=None,
    )
    watts = Field(
        start=14,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="CC Wattage Output",
        units="Watts",
        scale_factor="power_scale_factor",
    )
    todays_min_battery_volts = Field(
        start=15,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Minimum Voltage for battery today",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    todays_max_battery_volts = Field(
        start=16,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Maximum Voltage for battery today",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    voc = Field(
        start=17,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Last Open Circuit Voltage (array)",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    todays_peak_voc = Field(
        start=18,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Highest VOC today",
        units="Volts",
        scale_factor=None,
    )
    todays_kwh = Field(
        start=19,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily accumulated Kwatt hours output",
        units="KWH",
        scale_factor="kwh_scale_factor",
    )
    todays_ah = Field(
        start=20,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily accumulated amp hours output",
        units="AH",
        scale_factor="ah_scale_factor",
    )
    lifetime_kwh_hours = Field(
        start=21,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Lifetime Total Kwatt Hours",
        units="KWH",
        scale_factor=None,
    )
    lifetime_kamp_hours = Field(
        start=22,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Lifetime Total K-Amp Hours",
        units="Amps",
        scale_factor="kwh_scale_factor",
    )
    lifetime_max_watts = Field(
        start=23,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Lifetime Maximum Wattage",
        units="Watts",
        scale_factor="power_scale_factor",
    )
    lifetime_max_battery_volts = Field(
        start=24,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Lifetime Maximum Battery Voltage",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    lifetime_max_voc = Field(
        start=25,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Lifetime Maximum VOC",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    temperature_scale_factor = Field(
        start=26,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="FM80 Extreme Temperature scale factor",
        units=None,
        scale_factor=None,
    )
    temperature_output_fets = Field(
        start=27,
        size=1,
        type=int16,
        mode=Mode.R,
        description="FM80 Extreme Output FET Temperature",
        units="DegreesC",
        scale_factor="power_scale_factor",
    )
    temperature_enclosure = Field(
        start=28,
        size=1,
        type=int16,
        mode=Mode.R,
        description="FM80 Extreme Enclosure Temperature",
        units="DegreesC",
        scale_factor="power_scale_factor",
    )

    structure = ChargeControllerBlock
    device = Device.charge_controller


# This file is auto generated, do not edit. The generation code can be found in code_generator.py
class ChargeControllerConfigurationDefinition(BaseDefinition):
    night_light_on_hours = Field(
        start=44,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Night Light ON Time",
        units="Hours",
        scale_factor=None,
    )
    night_light_on_hyst_time = Field(
        start=45,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Night Light ON Hyst Time",
        units="Mins",
        scale_factor=None,
    )
    night_light_off_hyst_time = Field(
        start=46,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Night Light OFF Hyst Time",
        units="Mins",
        scale_factor=None,
    )
    aux_error_battery_volts = Field(
        start=47,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Battery voltage at which Aux Error occurs",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    aux_divert_hold_time = Field(
        start=48,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AUX Diver Hold Time",
        units="Seconds",
        scale_factor="hours_scale_factor",
    )
    aux_divert_delay_time = Field(
        start=49,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AUX Divert Delay",
        units="Secs",
        scale_factor=None,
    )
    aux_divert_relative_volts = Field(
        start=50,
        size=1,
        type=int16,
        mode=Mode.RW,
        description="AUX Divert Relative Volts",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    aux_divert_hyst_volts = Field(
        start=51,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AUX Divert Hyst Volts",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    major_firmware_number = Field(
        start=52,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Charge Controller Major firmware revision",
        units=None,
        scale_factor=None,
    )
    mid_firmware_number = Field(
        start=53,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Charge Controller Mid firmware revision",
        units=None,
        scale_factor=None,
    )
    minor_firmware_number = Field(
        start=54,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Charge Controller Minor firmware revision",
        units=None,
        scale_factor=None,
    )
    set_data_log_day_offset = Field(
        start=55,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Day offset 0-128, 0 =Today, 1 = -1 day …",
        units="Days",
        scale_factor=None,
    )
    get_current_data_log_day_offset = Field(
        start=56,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Current Data Log Day Offset",
        units="Days",
        scale_factor=None,
    )
    data_log_daily_ah = Field(
        start=57,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Data Log AH",
        units="AH",
        scale_factor="ah_scale_factor",
    )
    data_log_daily_kwh = Field(
        start=58,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Data Log kWH",
        units="KWH",
        scale_factor="kwh_scale_factor",
    )
    data_log_daily_max_output_amps = Field(
        start=59,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Data Log maximum Output Amps",
        units="Amps",
        scale_factor="voltage_scale_factor",
    )
    data_log_daily_max_output_watts = Field(
        start=60,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Data Log maximum Output Wattage",
        units="Watts",
        scale_factor="power_scale_factor",
    )
    data_log_daily_absorb_time = Field(
        start=61,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Data Log Absorb Time Minutes",
        units="Mins",
        scale_factor=None,
    )
    data_log_daily_float_time = Field(
        start=62,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Data Log Float Time Minutes",
        units="Mins",
        scale_factor=None,
    )
    data_log_daily_min_battery_volts = Field(
        start=63,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Data Log minimum daily battery voltage",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    data_log_daily_max_battery_volts = Field(
        start=64,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Data Log maximum daily battery voltage",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    data_log_daily_max_input_volts = Field(
        start=65,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Data Log maximum daily input voltage",
        units="Volts",
        scale_factor=None,
    )
    clear_data_log_read = Field(
        start=66,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Read value needed to clear data log",
        units=None,
        scale_factor=None,
    )
    clear_data_log_write_complement = Field(
        start=67,
        size=1,
        type=uint16,
        mode=Mode.W,
        description="Write value's complement to clear data log",
        units=None,
        scale_factor=None,
    )
    stats_maximum_reset_read = Field(
        start=68,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Read value needed to clear Stats  Maximums",
        units=None,
        scale_factor=None,
    )
    stats_maximum_write_complement = Field(
        start=69,
        size=1,
        type=uint16,
        mode=Mode.W,
        description="Write value's complement to clear Stats  Maximums",
        units=None,
        scale_factor=None,
    )
    stats_totals_reset_read = Field(
        start=70,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Read value nneded to clear Stats Totals",
        units=None,
        scale_factor=None,
    )
    stats_totals_write_complement = Field(
        start=71,
        size=1,
        type=uint16,
        mode=Mode.W,
        description="Write value's complement to clear Stats  Totals",
        units=None,
        scale_factor=None,
    )
    battery_voltage_calibrate_offset = Field(
        start=72,
        size=1,
        type=int16,
        mode=Mode.RW,
        description="Battery voltage calibration offset",
        units="DCVolts",
        scale_factor="voltage_scale_factor",
    )
    serial_number = Field(
        start=73,
        size=9,
        type=str,
        mode=Mode.R,
        description="Device serial number",
        units=None,
        scale_factor=None,
    )
    model_number = Field(
        start=82,
        size=9,
        type=str,
        mode=Mode.R,
        description="Device model",
        units=None,
        scale_factor=None,
    )
    did = Field(
        start=1,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Vendor Extension for OutBack FM Series  Charge Controllers",
        units=None,
        scale_factor=None,
    )
    length = Field(
        start=2,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Length of block in 16-bit registers",
        units="Registers",
        scale_factor=None,
    )
    port_number = Field(
        start=3,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Port number on Outback network",
        units=None,
        scale_factor=None,
    )
    voltage_scale_factor = Field(
        start=4,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    current_scale_factor = Field(
        start=5,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Current Scale Factor",
        units=None,
        scale_factor=None,
    )
    hours_scale_factor = Field(
        start=6,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Time in Hours Scale Factor",
        units=None,
        scale_factor=None,
    )
    power_scale_factor = Field(
        start=7,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Power Scale Factor",
        units=None,
        scale_factor=None,
    )
    ah_scale_factor = Field(
        start=8,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Amp Hours Scale Factor",
        units=None,
        scale_factor=None,
    )
    kwh_scale_factor = Field(
        start=9,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC kWH Scale Factor",
        units=None,
        scale_factor=None,
    )
    faults = Field(
        start=10,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="CC Error Flags: 0x0080=High VOC,  0x0040=Over Temp,  0x0020=Shorted Battery  Temp Sensor, 0x0010=Fault Input Active",
        units="Bitfield",
        scale_factor=None,
    )
    absorb_volts = Field(
        start=11,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Absorb Voltage Target",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    absorb_time_hours = Field(
        start=12,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Absorb Time Hours",
        units="Hours",
        scale_factor="hours_scale_factor",
    )
    absorb_end_amps = Field(
        start=13,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Amperage to end Absorbing",
        units="Amps",
        scale_factor=None,
    )
    rebulk_volts = Field(
        start=14,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Voltage to re-initiate Bulk charge",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    float_volts = Field(
        start=15,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Float Voltage Target",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    bulk_current = Field(
        start=16,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Max Output Current Limit",
        units="Amps",
        scale_factor="current_scale_factor",
    )
    eq_volts = Field(
        start=17,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Target Voltage for Equalize",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    eq_time_hours = Field(
        start=18,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="EQ Time Hours",
        units="Hours",
        scale_factor=None,
    )
    auto_eq_days = Field(
        start=19,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Auto EQ Interval Days",
        units="Days",
        scale_factor=None,
    )
    mppt_mode = Field(
        start=20,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Auto; 1 = U-Pick",
        units="Enumerated",
        scale_factor=None,
    )
    sweep_width = Field(
        start=21,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Full; 1 = Half",
        units="Enumerated",
        scale_factor=None,
    )
    sweep_max_percentage = Field(
        start=22,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = 80; 1 = 85; 2 = 90; 3 = 99",
        units="Enumerated",
        scale_factor=None,
    )
    u_pick_pwm_duty_cycle = Field(
        start=23,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Park Duty Cycle (%) (40% - 90%)",
        units="Percentage",
        scale_factor="voltage_scale_factor",
    )
    grid_tie_mode = Field(
        start=24,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Grid Tie Mode disabled; 1 = Grid Tie  Mode enabled",
        units="Enumerated",
        scale_factor=None,
    )
    temperature_comp_mode = Field(
        start=25,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Wide; 1 = User Limited",
        units="Enumerated",
        scale_factor=None,
    )
    temperature_comp_lower_limit_volts = Field(
        start=26,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="RTS compensation lower voltage limit",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    temperature_comp_upper_limit_volts = Field(
        start=27,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="RTS compensation upper voltage limit",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    temperature_comp_slope = Field(
        start=28,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="RTS temp compensation Slope 2-6 mV per  Degree C",
        units="MilliVolts",
        scale_factor=None,
    )
    auto_restart_mode = Field(
        start=29,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Off; 1 = Restart every 90 minutes; 2 =  Restart every 90 minutes if absorb charging  or float charging",
        units="Enumerated",
        scale_factor=None,
    )
    wakeup_voc = Field(
        start=30,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="VOC change which causes Wakeup occurs",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    snooze_mode_amps = Field(
        start=31,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Snooze Mode Amps",
        units="Amps",
        scale_factor="voltage_scale_factor",
    )
    wakeup_interval = Field(
        start=32,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="How often to check for Wakeup condition",
        units="Mins",
        scale_factor=None,
    )
    aux_mode = Field(
        start=33,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Float; 1 = Diversion: Relay; 2 =  Diversion: Solid St; 3 = Low Batt Disconnect;  4 = Remote; 5 = Vent Fan; 6 = PV Trigger; 7  = Error Output; 8 = Night Light",
        units="Enumerated",
        scale_factor=None,
    )
    aux_control = Field(
        start=34,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Off; 1 = Auto; 2 = On",
        units="Enumerated",
        scale_factor=None,
    )
    aux_state = Field(
        start=35,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="0 = Disabled; 1 = Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    aux_polarity = Field(
        start=36,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Low; 1 = High",
        units="Enumerated",
        scale_factor=None,
    )
    aux_low_battery_disconnect = Field(
        start=37,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Low Battery Disconnect Voltage",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    aux_low_battery_reconnect = Field(
        start=38,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Low Battery Reconnect Volts",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    aux_low_battery_disconnect_delay = Field(
        start=39,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Low Battery Disconnect Delay (secs)",
        units="Secs",
        scale_factor=None,
    )
    aux_vent_fan_volts = Field(
        start=40,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Vent Fan Voltage",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    aux_pv_limit_volts = Field(
        start=41,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Voltage at which PV disconnect occurs",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )
    aux_pv_limit_hold_time = Field(
        start=42,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AUX PV Trigger Hold Time",
        units="Secs",
        scale_factor="hours_scale_factor",
    )
    aux_night_light_thres_volts = Field(
        start=43,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Voltage Threshold for AUX Night Light",
        units="Volts",
        scale_factor="voltage_scale_factor",
    )

    structure = ChargeControllerConfigurationBlock
    device = Device.charge_controller_configuration


# This file is auto generated, do not edit. The generation code can be found in code_generator.py
class FxInverterDefinition(BaseDefinition):
    did = Field(
        start=1,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Vendor Extension for OutBack FX Series  Inverter Status Block",
        units=None,
        scale_factor=None,
    )
    length = Field(
        start=2,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Length of block in 16-bit registers",
        units="Registers",
        scale_factor=None,
    )
    port_number = Field(
        start=3,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Port number on Outback network",
        units=None,
        scale_factor=None,
    )
    dc_voltage_scale_factor = Field(
        start=4,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    ac_current_scale_factor = Field(
        start=5,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Current Scale Factor",
        units=None,
        scale_factor=None,
    )
    ac_voltage_scale_factor = Field(
        start=6,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    ac_frequency_scale_factor = Field(
        start=7,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Frequency Scale Factor",
        units=None,
        scale_factor=None,
    )
    inverter_output_current = Field(
        start=8,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Inverter output current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    inverter_charge_current = Field(
        start=9,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Inverter charger current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    inverter_buy_current = Field(
        start=10,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Inverter buy current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    inverter_sell_current = Field(
        start=11,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Inverter sell current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    output_ac_voltage = Field(
        start=12,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Output AC Voltage",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    inverter_operating_mode = Field(
        start=13,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="0=Off, 1=Searching, 2=Inverting,  3=Charging, 4=Silent, 5=Float, 6=EQ,  7=Charger Off, 8=Support, 9=Selling,  10=Pass through, 14=Offsetting",
        units="Enumerated",
        scale_factor=None,
    )
    error_flags = Field(
        start=14,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Bit field for errors  (see FX_Error Table)",
        units="Bitfield",
        scale_factor=None,
    )
    warning_flags = Field(
        start=15,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Bit field for warnings (see FX_Warning Table)",
        units="Bitfield",
        scale_factor=None,
    )
    battery_voltage = Field(
        start=16,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Battery Voltage",
        units="VoltsDC",
        scale_factor="dc_voltage_scale_factor",
    )
    temperature_compensated_target_voltage = Field(
        start=17,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Temperature compensated target battery  voltage",
        units="VoltsDC",
        scale_factor="dc_voltage_scale_factor",
    )
    aux_output_state = Field(
        start=18,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="0 = Disabled; 1 = Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    transformer_temperature = Field(
        start=19,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Transformer temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    capacitor_temperature = Field(
        start=20,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Capacitor temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    fet_temperature = Field(
        start=21,
        size=1,
        type=int16,
        mode=Mode.R,
        description="FET temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    ac_input_frequency = Field(
        start=22,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Selected AC Input frequency HZ",
        units="Hz",
        scale_factor="ac_frequency_scale_factor",
    )
    ac_input_voltage = Field(
        start=23,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Selected Input AC Voltage",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_input_state = Field(
        start=24,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="1=AC Use, 0=AC_Drop",
        units="Enumerated",
        scale_factor=None,
    )
    minimum_ac_input_voltage = Field(
        start=25,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Minimum Input AC Voltage  (Write to clear value)",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    maximum_ac_input_voltage = Field(
        start=26,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Maximum Input AC Voltage  (Write to clear value)",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    sell_status = Field(
        start=27,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Bit field for sell status   (see FX_Sell_Status Table)",
        units="Bitfield",
        scale_factor=None,
    )
    kwh_scale_factor = Field(
        start=28,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC kWh scale factor",
        units=None,
        scale_factor=None,
    )
    buy_kwh = Field(
        start=29,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily Buy kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    sell_kwh = Field(
        start=30,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily Sell kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    output_kwh = Field(
        start=31,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily Output kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    charger_kwh = Field(
        start=32,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily Output kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    output_kw = Field(
        start=33,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Output kW",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    buy_kw = Field(
        start=34,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Buy kW",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    sell_kw = Field(
        start=35,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Sell kW",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    charge_kw = Field(
        start=36,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Charger kW",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    load_kw = Field(
        start=37,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Load kW",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    ac_couple_kw = Field(
        start=38,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Coupled kW",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )

    structure = FxInverterBlock
    device = Device.fx_inverter


# This file is auto generated, do not edit. The generation code can be found in code_generator.py
class FxInverterConfigurationDefinition(BaseDefinition):
    grid_ac_input_current_limit = Field(
        start=23,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid AC input current limit",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    gen_ac_input_current_limit = Field(
        start=24,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Gen AC input current limit",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    charger_ac_input_current_limit = Field(
        start=25,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Charger AC input current limit",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    charger_operating_mode = Field(
        start=26,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Charger Off, 1=Charger Auto, 2=Charger  On",
        units="Enumerated",
        scale_factor=None,
    )
    grid_lower_input_voltage_limit = Field(
        start=27,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Input AC voltage lower limit",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    grid_upper_input_voltage_limit = Field(
        start=28,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Input AC voltage upper limit",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    grid_transfer_delay = Field(
        start=29,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Input AC connect delay",
        units="Minutes",
        scale_factor=None,
    )
    gen_lower_input_voltage_limit = Field(
        start=30,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Gen Input AC voltage lower limit",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    gen_upper_input_voltage_limit = Field(
        start=31,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Gen Input AC voltage upper limit",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    gen_transfer_delay = Field(
        start=32,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Gen Input AC transfer delay",
        units="Cycles",
        scale_factor=None,
    )
    gen_connect_delay = Field(
        start=33,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Gen Input AC connect delay",
        units="Minutes",
        scale_factor="time_scale_factor",
    )
    ac_output_voltage = Field(
        start=34,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AC output Voltage",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    low_battery_cut_out_voltage = Field(
        start=35,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Battery cut-out voltage",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    low_battery_cut_in_voltage = Field(
        start=36,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Battery cut-in voltage",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    aux_mode = Field(
        start=37,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Remote, 1=Load Shed, 2=Gen Alert,  3=Fault, 4=Vent Fan, 5=Cool Fan, 6=Divert  DC, 7=Divert AC, 8=AC Drop",
        units="Enumerated",
        scale_factor=None,
    )
    aux_control = Field(
        start=38,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Off; 1 = Auto; 2 = On",
        units="Enumerated",
        scale_factor=None,
    )
    aux_load_shed_enable_voltage = Field(
        start=39,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Load Shed enable voltage",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    aux_gen_alert_on_voltage = Field(
        start=40,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Gen Alert On voltage",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    aux_gen_alert_on_delay = Field(
        start=41,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Gen Alert On delay minutes",
        units="Minutes",
        scale_factor=None,
    )
    aux_gen_alert_off_voltage = Field(
        start=42,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Gen Alert Off voltage",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    aux_gen_alert_off_delay = Field(
        start=43,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Gen Alert Off delay minutes",
        units="Minutes",
        scale_factor=None,
    )
    aux_vent_fan_enable_voltage = Field(
        start=44,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Vent Fan enable voltage",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    aux_vent_fan_off_period = Field(
        start=45,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Van Fan Off delay minutes",
        units="Minutes",
        scale_factor=None,
    )
    aux_divert_enable_voltage = Field(
        start=46,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="DC Divert enable voltage",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    aux_divert_off_delay = Field(
        start=47,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Divert Off delay minutes",
        units="Minutes",
        scale_factor=None,
    )
    stacking_mode = Field(
        start=48,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="0=1-2phase Master, 1=Classic Slave, 2=OB  Slave L1, 3=OB Slave L2, 4=3phase Master,  5=3phase Slave,10=Master, 11=Classic  Slave, 12=OB Slave L1, 13=OB Slave L2,  14=3phase OB Slave A, 15=3phase OB Slave  B, 16=3phase OB Slave C, 17=3phase  Classic B, 18=3phase Classic C,  19=Independent",
        units="Enumerated",
        scale_factor=None,
    )
    master_power_save_level = Field(
        start=49,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Master inverter power save level",
        units=None,
        scale_factor=None,
    )
    slave_power_save_level = Field(
        start=50,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Slave inverter power save level",
        units=None,
        scale_factor=None,
    )
    sell_volts = Field(
        start=51,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Sell Voltage Target",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    grid_tie_window = Field(
        start=52,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=IEEE, 1=User",
        units="Enumerated",
        scale_factor=None,
    )
    grid_tie_enable = Field(
        start=53,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="1=Yes, 0=No",
        units="Enumerated",
        scale_factor=None,
    )
    ac_input_voltage_calibrate_factor = Field(
        start=54,
        size=1,
        type=int16,
        mode=Mode.RW,
        description="AC input voltage calibration factor",
        units="VoltsAC",
        scale_factor=None,
    )
    ac_output_voltage_calibrate_factor = Field(
        start=55,
        size=1,
        type=int16,
        mode=Mode.RW,
        description="AC output voltage calibration factor",
        units="VoltsAC",
        scale_factor=None,
    )
    battery_voltage_calibrate_factor = Field(
        start=56,
        size=1,
        type=int16,
        mode=Mode.RW,
        description="Battery voltage calibration factor",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    serial_number = Field(
        start=57,
        size=9,
        type=str,
        mode=Mode.R,
        description="Device serial number",
        units=None,
        scale_factor=None,
    )
    model_number = Field(
        start=66,
        size=9,
        type=str,
        mode=Mode.R,
        description="Device model",
        units=None,
        scale_factor=None,
    )
    did = Field(
        start=1,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Vendor Extension for OutBack FX Series  Inverter  Configuration Block",
        units=None,
        scale_factor=None,
    )
    length = Field(
        start=2,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Length of block in 16-bit registers",
        units="Registers",
        scale_factor=None,
    )
    port_number = Field(
        start=3,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Port number on Outback network",
        units=None,
        scale_factor=None,
    )
    dc_voltage_scale_factor = Field(
        start=4,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    ac_current_scale_factor = Field(
        start=5,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Current Scale Factor",
        units=None,
        scale_factor=None,
    )
    ac_voltage_scale_factor = Field(
        start=6,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    time_scale_factor = Field(
        start=7,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Time Scale Factor",
        units=None,
        scale_factor=None,
    )
    major_firmware_number = Field(
        start=8,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Inverter Major firmware revision",
        units=None,
        scale_factor=None,
    )
    mid_firmware_number = Field(
        start=9,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Inverter Mid firmware revision",
        units=None,
        scale_factor=None,
    )
    minor_firmware_number = Field(
        start=10,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Inverter Minor firmware revision",
        units=None,
        scale_factor=None,
    )
    absorb_volts = Field(
        start=11,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Absorb Voltage Target",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    absorb_time_hours = Field(
        start=12,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Absorb Time Hours",
        units="Hours",
        scale_factor="time_scale_factor",
    )
    float_volts = Field(
        start=13,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Float Voltage Target",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    float_time_hours = Field(
        start=14,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Float Time Hours",
        units="Hours",
        scale_factor="time_scale_factor",
    )
    refloat_volts = Field(
        start=15,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="ReFloat Voltage Target",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    eq_volts = Field(
        start=16,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="EQ Voltage Target",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    eq_time_hours = Field(
        start=17,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="EQ Time Hours",
        units="Hours",
        scale_factor="time_scale_factor",
    )
    search_sensitivity = Field(
        start=18,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Search sensitivity",
        units=None,
        scale_factor=None,
    )
    search_pulse_length = Field(
        start=19,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Search pulse length",
        units="Cycles",
        scale_factor=None,
    )
    search_pulse_spacing = Field(
        start=20,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Search pulse spacing",
        units="Cycles",
        scale_factor=None,
    )
    ac_input_type = Field(
        start=21,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Grid, 1=Gen, 2=Grid Zero",
        units="Enumerated",
        scale_factor=None,
    )
    input_support = Field(
        start=22,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="1=Yes, 0=No (only valid if AC Input Type is  Gen)",
        units="Enumerated",
        scale_factor=None,
    )

    structure = FxInverterConfigurationBlock
    device = Device.fx_inverter_configuration


# This file is auto generated, do not edit. The generation code can be found in code_generator.py
class SplitPhaseRadianInverterDefinition(BaseDefinition):
    did = Field(
        start=1,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Vendor Extension for OutBack Radian Series  Split Phase Inverter Status Block",
        units=None,
        scale_factor=None,
    )
    length = Field(
        start=2,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Length of block in 16-bit registers",
        units="Registers",
        scale_factor=None,
    )
    port_number = Field(
        start=3,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Port number on Outback network",
        units=None,
        scale_factor=None,
    )
    dc_voltage_scale_factor = Field(
        start=4,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    ac_current_scale_factor = Field(
        start=5,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Current Scale Factor",
        units=None,
        scale_factor=None,
    )
    ac_voltage_scale_factor = Field(
        start=6,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    ac_frequency_scale_factor = Field(
        start=7,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Frequency Scale Factor",
        units=None,
        scale_factor=None,
    )
    l1_inverter_output_current = Field(
        start=8,
        size=1,
        type=int16,
        mode=Mode.R,
        description="L1 inverter output current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    l1_inverter_charge_current = Field(
        start=9,
        size=1,
        type=int16,
        mode=Mode.R,
        description="L1 inverter charger current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    l1_inverter_buy_current = Field(
        start=10,
        size=1,
        type=int16,
        mode=Mode.R,
        description="L1 inverter buy current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    l1_inverter_sell_current = Field(
        start=11,
        size=1,
        type=int16,
        mode=Mode.R,
        description="L1 inverter sell current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    l1_grid_input_ac_voltage = Field(
        start=12,
        size=1,
        type=int16,
        mode=Mode.R,
        description="L1 Grid Input AC Voltage",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    l1_gen_input_ac_voltage = Field(
        start=13,
        size=1,
        type=int16,
        mode=Mode.R,
        description="L1 Gen Input AC Voltage",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    l1_output_ac_voltage = Field(
        start=14,
        size=1,
        type=int16,
        mode=Mode.R,
        description="L1 Output AC Voltage",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    l2_inverter_output_current = Field(
        start=15,
        size=1,
        type=int16,
        mode=Mode.R,
        description="L2 inverter output current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    l2_inverter_charge_current = Field(
        start=16,
        size=1,
        type=int16,
        mode=Mode.R,
        description="L2 inverter charger current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    l2_inverter_buy_current = Field(
        start=17,
        size=1,
        type=int16,
        mode=Mode.R,
        description="L2 inverter buy current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    l2_inverter_sell_current = Field(
        start=18,
        size=1,
        type=int16,
        mode=Mode.R,
        description="L2 inverter sell current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    l2_grid_input_ac_voltage = Field(
        start=19,
        size=1,
        type=int16,
        mode=Mode.R,
        description="L2 Grid Input AC Voltage",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    l2_gen_input_ac_voltage = Field(
        start=20,
        size=1,
        type=int16,
        mode=Mode.R,
        description="L2 Gen Input AC Voltage",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    l2_output_ac_voltage = Field(
        start=21,
        size=1,
        type=int16,
        mode=Mode.R,
        description="L2 Output AC Voltage",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    inverter_operating_mode = Field(
        start=22,
        size=1,
        type=int16,
        mode=Mode.R,
        description="0=Off, 1=Searching, 2=Inverting,  3=Charging, 4=Silent, 5=Float, 6=EQ,  7=Charger Off, 8=Support, 9=Selling,  10=Pass through, 14=Offsetting",
        units="Enumerated",
        scale_factor=None,
    )
    error_flags = Field(
        start=23,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Bit field for errors. See GS_Error table",
        units="Bitfield",
        scale_factor=None,
    )
    warning_flags = Field(
        start=24,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Bit field for warnings See GS_Warning table",
        units="Bitfield",
        scale_factor=None,
    )
    battery_voltage = Field(
        start=25,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Battery Voltage",
        units="VoltsDC",
        scale_factor="dc_voltage_scale_factor",
    )
    temperature_compensated_target_voltage = Field(
        start=26,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Temperature compensated target battery  voltage",
        units="VoltsDC",
        scale_factor="dc_voltage_scale_factor",
    )
    aux_output_state = Field(
        start=27,
        size=1,
        type=int16,
        mode=Mode.R,
        description="0 = Disabled; 1 = Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    aux_relay_output_state = Field(
        start=28,
        size=1,
        type=int16,
        mode=Mode.R,
        description="0 = Disabled; 1 = Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    l_module_transformer_temperature = Field(
        start=29,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Left module transformer temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    l_module_capacitor_temperature = Field(
        start=30,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Left module capacitor temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    l_module_fet_temperature = Field(
        start=31,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Left module FET temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    r_module_transformer_temperature = Field(
        start=32,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Right module transformer temp in degrees  C",
        units="DegreesC",
        scale_factor=None,
    )
    r_module_capacitor_temperature = Field(
        start=33,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Right module capacitor temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    r_module_fet_temperature = Field(
        start=34,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Right module FET temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    battery_temperature = Field(
        start=35,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Battery temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    ac_input_selection = Field(
        start=36,
        size=1,
        type=int16,
        mode=Mode.R,
        description="0=Grid, 1=Gen",
        units="Enumerated",
        scale_factor=None,
    )
    ac_input_frequency = Field(
        start=37,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Selected AC Input frequency HZ",
        units="Hz",
        scale_factor="ac_frequency_scale_factor",
    )
    ac_input_voltage = Field(
        start=38,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Selected Input AC Voltage",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_input_state = Field(
        start=39,
        size=1,
        type=int16,
        mode=Mode.R,
        description="1=AC Use, 0=AC_Drop",
        units="Enumerated",
        scale_factor=None,
    )
    minimum_ac_input_voltage = Field(
        start=40,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Minimum Input AC Voltage (Write to clear  stored value)",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    maximum_ac_input_voltage = Field(
        start=41,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Maximum Input AC Voltage (Write to clear  stored value)",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    sell_status = Field(
        start=42,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Bit field for sell status  (See GS_Sell_Status table)",
        units="Bitfield",
        scale_factor=None,
    )
    kwh_scale_factor = Field(
        start=43,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC kWh scale factor",
        units=None,
        scale_factor=None,
    )
    ac1_l1_buy_kwh = Field(
        start=44,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily AC1 Buy L1 kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    ac2_l1_buy_kwh = Field(
        start=45,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily AC2 Buy L1 kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    ac1_l1_sell_kwh = Field(
        start=46,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily AC1 Sell L1 kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    ac2_l1_sell_kwh = Field(
        start=47,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily AC2 Sell L1 kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    l1_output_kwh = Field(
        start=48,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily Output L1 kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    ac1_l2_buy_kwh = Field(
        start=49,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily AC1 Buy L2 kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    ac2_l2_buy_kwh = Field(
        start=50,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily AC1 Sell L2 kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    ac1_l2_sell_kwh = Field(
        start=51,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily AC1 Sell L2 kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    ac2_l2_sell_kwh = Field(
        start=52,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily AC2 Sell L2 kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    l2_output_kwh = Field(
        start=53,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily Output L2 kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    charger_kwh = Field(
        start=54,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily Charger kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    output_kw = Field(
        start=55,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Output kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    buy_kw = Field(
        start=56,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Buy kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    sell_kw = Field(
        start=57,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Sell kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    charge_kw = Field(
        start=58,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Charge kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    load_kw = Field(
        start=59,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Load kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    ac_couple_kw = Field(
        start=60,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Coupled kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )

    structure = SplitPhaseRadianInverterBlock
    device = Device.split_phase_radian_inverter


# This file is auto generated, do not edit. The generation code can be found in code_generator.py
class RadianInverterConfigurationDefinition(BaseDefinition):
    aux_on_battery_voltage = Field(
        start=42,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AUX ON battery voltage",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    aux_on_delay_time = Field(
        start=43,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AUX ON Delay",
        units="Minutes",
        scale_factor="time_scale_factor",
    )
    aux_off_battery_voltage = Field(
        start=44,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AUX OFF battery voltage",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    aux_off_delay_time = Field(
        start=45,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AUX OFF Delay",
        units="Minutes",
        scale_factor="time_scale_factor",
    )
    aux_relay_mode = Field(
        start=46,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="1=Load Shed, 2=Gen Alert, 3=Fault, 4=Vent  Fan, 5=Cool Fan, 6=DC Divert, 7=Grid  Limit/IEEE ,8=AC Source Status,9=AC Divert",
        units="Enumerated",
        scale_factor=None,
    )
    aux_relay_control = Field(
        start=47,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Off; 1 = On; 2 = Auto",
        units="Enumerated",
        scale_factor=None,
    )
    aux_relay_on_battery_voltage = Field(
        start=48,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AUX Relay ON battery voltage",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    aux_relay_on_delay_time = Field(
        start=49,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AUX Relay ON Delay",
        units="Minutes",
        scale_factor="time_scale_factor",
    )
    aux_relay_off_battery_voltage = Field(
        start=50,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AUX Relay OFF battery voltage",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    aux_relay_off_delay_time = Field(
        start=51,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AUX Relay OFF Delay",
        units="Minutes",
        scale_factor="time_scale_factor",
    )
    stacking_mode = Field(
        start=52,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="10=Master, 12=Slave, 17=B Phase Master,  18=C Phase Master",
        units="Enumerated",
        scale_factor=None,
    )
    master_power_save_level = Field(
        start=53,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Master inverter power save level",
        units=None,
        scale_factor=None,
    )
    slave_power_save_level = Field(
        start=54,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Slave inverter power save level",
        units=None,
        scale_factor=None,
    )
    sell_volts = Field(
        start=55,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Sell Voltage Target",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    grid_tie_window = Field(
        start=56,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=IEEE, 1=User (GS8048 Only)",
        units="Enumerated",
        scale_factor=None,
    )
    grid_tie_enable = Field(
        start=57,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="1=Yes, 0=No",
        units="Enumerated",
        scale_factor=None,
    )
    grid_ac_input_voltage_calibrate_factor = Field(
        start=58,
        size=1,
        type=int16,
        mode=Mode.RW,
        description="Grid AC input voltage calibration factor",
        units="VoltsAC",
        scale_factor=None,
    )
    gen_ac_input_voltage_calibrate_factor = Field(
        start=59,
        size=1,
        type=int16,
        mode=Mode.RW,
        description="Gen AC input voltage calibration factor",
        units="VoltsAC",
        scale_factor=None,
    )
    ac_output_voltage_calibrate_factor = Field(
        start=60,
        size=1,
        type=int16,
        mode=Mode.RW,
        description="AC output voltage calibration factor",
        units="VoltsAC",
        scale_factor=None,
    )
    battery_voltage_calibrate_factor = Field(
        start=61,
        size=1,
        type=int16,
        mode=Mode.RW,
        description="Battery voltage calibration factor",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    rebulk_volts = Field(
        start=62,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="ReBulk Voltage Target",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    mini_grid_lbx_volts = Field(
        start=63,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Mini Grid LBX reconnect to Grid Battery  Voltage",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    mini_grid_lbx_delay = Field(
        start=64,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Mini Grid LBX reconnect to Grid Delay Time",
        units="Hours",
        scale_factor=None,
    )
    grid_zero_dod_volts = Field(
        start=65,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Zero DoD Voltage",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    grid_zero_dod_max_offset_ac_amps = Field(
        start=66,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Zero Maximum Offset AC Amps",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    serial_number = Field(
        start=67,
        size=9,
        type=str,
        mode=Mode.RW,
        description="Device serial number",
        units=None,
        scale_factor=None,
    )
    model_number = Field(
        start=76,
        size=9,
        type=str,
        mode=Mode.R,
        description="Device model",
        units=None,
        scale_factor=None,
    )
    module_control = Field(
        start=85,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Module Control: 0 = Auto, 1 = Left, 2 =  Right, 3 = Both",
        units="Enumerated",
        scale_factor=None,
    )
    model_select = Field(
        start=86,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Model Select: 0 = Dual Module, 1 = Single  Module",
        units="Enumerated",
        scale_factor=None,
    )
    low_battery_cut_out_delay = Field(
        start=87,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Seconds delay before inverter shutdown  upon low battery voltage",
        units="Seconds",
        scale_factor="dc_voltage_scale_factor",
    )
    high_battery_cut_out_voltage = Field(
        start=88,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="High Battery Voltage Cut Out",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    high_battery_cut_in_voltage = Field(
        start=89,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="High Battery Voltage Cut In",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    high_battery_cut_out_delay = Field(
        start=90,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Seconds delay before inverter shutdown  upon high battery voltage",
        units="Seconds",
        scale_factor="dc_voltage_scale_factor",
    )
    did = Field(
        start=1,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Vendor Extension for OutBack Radian Series  Split Phase Inverter Configuration Block",
        units=None,
        scale_factor=None,
    )
    length = Field(
        start=2,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Length of block in 16-bit registers",
        units="Registers",
        scale_factor=None,
    )
    port_number = Field(
        start=3,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Port number on Outback network",
        units=None,
        scale_factor=None,
    )
    dc_voltage_scale_factor = Field(
        start=4,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    ac_current_scale_factor = Field(
        start=5,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Current Scale Factor",
        units=None,
        scale_factor=None,
    )
    ac_voltage_scale_factor = Field(
        start=6,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    time_scale_factor = Field(
        start=7,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Time Scale Factor",
        units=None,
        scale_factor=None,
    )
    major_firmware_number = Field(
        start=8,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Inverter Major firmware revision",
        units=None,
        scale_factor=None,
    )
    mid_firmware_number = Field(
        start=9,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Inverter Mid firmware revision",
        units=None,
        scale_factor=None,
    )
    minor_firmware_number = Field(
        start=10,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Inverter Minor firmware revision",
        units=None,
        scale_factor=None,
    )
    absorb_volts = Field(
        start=11,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Absorb Voltage Target",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    absorb_time_hours = Field(
        start=12,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Absorb Time Hours",
        units="Hours",
        scale_factor="time_scale_factor",
    )
    float_volts = Field(
        start=13,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Float Voltage Target",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    float_time_hours = Field(
        start=14,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Float Time Hours",
        units="Hours",
        scale_factor="time_scale_factor",
    )
    refloat_volts = Field(
        start=15,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="ReFloat Voltage Target",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    eq_volts = Field(
        start=16,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="EQ Voltage Target",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    eq_time_hours = Field(
        start=17,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="EQ Time Hours",
        units="Hours",
        scale_factor="time_scale_factor",
    )
    search_sensitivity = Field(
        start=18,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Search sensitivity",
        units=None,
        scale_factor=None,
    )
    search_pulse_length = Field(
        start=19,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Search pulse length",
        units="Cycles",
        scale_factor=None,
    )
    search_pulse_spacing = Field(
        start=20,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Search pulse spacing",
        units="Cycles",
        scale_factor=None,
    )
    ac_input_select_priority = Field(
        start=21,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Grid, 1=Gen",
        units="Enumerated",
        scale_factor=None,
    )
    grid_ac_input_current_limit = Field(
        start=22,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid AC input current limit",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    gen_ac_input_current_limit = Field(
        start=23,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Gen AC input current limit",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    charger_ac_input_current_limit = Field(
        start=24,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Charger AC input current limit",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    charger_operating_mode = Field(
        start=25,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=All Inverter Charging Disabled, 1=Bulk  and Float Charging Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    ac_coupled = Field(
        start=26,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=No, 1=Yes (not implemented)",
        units="Enumerated",
        scale_factor=None,
    )
    grid_input_mode = Field(
        start=27,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Input Mode: 0=Generator, 1=Support,  2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid,  6=Grid Zero",
        units="Enumerated",
        scale_factor=None,
    )
    grid_lower_input_voltage_limit = Field(
        start=28,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Input AC voltage lower limit",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    grid_upper_input_voltage_limit = Field(
        start=29,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Input AC voltage upper limit",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    grid_transfer_delay = Field(
        start=30,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Input AC transfer delay",
        units="msecs",
        scale_factor=None,
    )
    grid_connect_delay = Field(
        start=31,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Input AC connect delay",
        units="Minutes",
        scale_factor="time_scale_factor",
    )
    gen_input_mode = Field(
        start=32,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Grid Input Mode: 0=Generator, 1=Support,  2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid,  6=Grid Zero",
        units="Enumerated",
        scale_factor=None,
    )
    gen_lower_input_voltage_limit = Field(
        start=33,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Gen Input AC voltage lower limit",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    gen_upper_input_voltage_limit = Field(
        start=34,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Gen Input AC voltage upper limit",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    gen_transfer_delay = Field(
        start=35,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Gen Input AC transfer delay",
        units="msecs",
        scale_factor=None,
    )
    gen_connect_delay = Field(
        start=36,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Gen Input AC connect delay",
        units="Minutes",
        scale_factor="time_scale_factor",
    )
    ac_output_voltage = Field(
        start=37,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AC output Voltage",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    low_battery_cut_out_voltage = Field(
        start=38,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Low Battery Voltage Cut Out",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    low_battery_cut_in_voltage = Field(
        start=39,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Low Battery Voltage Cut In",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    aux_mode = Field(
        start=40,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="1=Load Shed, 2=Gen Alert, 3=Fault, 4=Vent  Fan, 5=Cool Fan, 6=DC Divert, 7=Grid  Limit/IEEE ,8=AC Source Status,9=AC Divert",
        units="Enumerated",
        scale_factor=None,
    )
    aux_control = Field(
        start=41,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Off; 1 = Auto; 2 = On",
        units="Enumerated",
        scale_factor=None,
    )

    structure = RadianInverterConfigurationBlock
    device = Device.radian_inverter_configuration


# This file is auto generated, do not edit. The generation code can be found in code_generator.py
class SinglePhaseRadianInverterDefinition(BaseDefinition):
    output_kw = Field(
        start=43,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Output kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    buy_kw = Field(
        start=44,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Buy kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    sell_kw = Field(
        start=45,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Sell kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    charge_kw = Field(
        start=46,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Charger kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    load_kw = Field(
        start=47,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Load kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    ac_couple_kw = Field(
        start=48,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="AC Coupled kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    did = Field(
        start=1,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Vendor Extension for OutBack Radian Series  Split Phase Inverter Status Block",
        units=None,
        scale_factor=None,
    )
    length = Field(
        start=2,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Length of block in 16-bit registers",
        units="Registers",
        scale_factor=None,
    )
    port_number = Field(
        start=3,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Port number on Outback network",
        units=None,
        scale_factor=None,
    )
    dc_voltage_scale_factor = Field(
        start=4,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    ac_current_scale_factor = Field(
        start=5,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Current Scale Factor",
        units=None,
        scale_factor=None,
    )
    ac_voltage_scale_factor = Field(
        start=6,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    ac_frequency_scale_factor = Field(
        start=7,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Frequency Scale Factor",
        units=None,
        scale_factor=None,
    )
    inverter_output_current = Field(
        start=8,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Inverter output current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    inverter_charge_current = Field(
        start=9,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Inverter charger current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    inverter_buy_current = Field(
        start=10,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Inverter buy current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    inverter_sell_current = Field(
        start=11,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Inverter sell current",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    grid_input_ac_voltage = Field(
        start=12,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Grid Input AC Voltage",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    gen_input_ac_voltage = Field(
        start=13,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Gen Input AC Voltage",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    output_ac_voltage = Field(
        start=14,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Output AC Voltage",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    inverter_operating_mode = Field(
        start=15,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="0=Off, 1=Searching, 2=Inverting,  3=Charging, 4=Silent, 5=Float, 6=EQ,  7=Charger Off, 8=Support, 9=Selling,  10=Pass through, 14=Offsetting",
        units="Enumerated",
        scale_factor=None,
    )
    error_flags = Field(
        start=16,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Bit field for errors  (See GS_Error Table)",
        units="Bitfield",
        scale_factor=None,
    )
    warning_flags = Field(
        start=17,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Bit field for warnings (See GS_Warning Table)",
        units="Bitfield",
        scale_factor=None,
    )
    battery_voltage = Field(
        start=18,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Battery Voltage",
        units="VoltsDC",
        scale_factor="dc_voltage_scale_factor",
    )
    temperature_compensated_target_voltage = Field(
        start=19,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Temperature compensated target battery  voltage",
        units="VoltsDC",
        scale_factor="dc_voltage_scale_factor",
    )
    aux_output_state = Field(
        start=20,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="0 = Disabled; 1 = Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    aux_relay_output_state = Field(
        start=21,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="0 = Disabled; 1 = Enabled",
        units="Enumerated",
        scale_factor=None,
    )
    l_module_transformer_temperature = Field(
        start=22,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Left module transformer temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    l_module_capacitor_temperature = Field(
        start=23,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Left module capacitor temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    l_module_fet_temperature = Field(
        start=24,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Left module FET temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    r_module_transformer_temperature = Field(
        start=25,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Right module transformer temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    r_module_capacitor_temperature = Field(
        start=26,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Right module capacitor temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    r_module_fet_temperature = Field(
        start=27,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Right module FET temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    battery_temperature = Field(
        start=28,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Battery temp in degrees C",
        units="DegreesC",
        scale_factor=None,
    )
    ac_input_selection = Field(
        start=29,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="0=Grid, 1=Gen",
        units="Enumerated",
        scale_factor=None,
    )
    ac_input_frequency = Field(
        start=30,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Selected AC Input frequency HZ",
        units="Hz",
        scale_factor="ac_frequency_scale_factor",
    )
    ac_input_voltage = Field(
        start=31,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Selected Input AC Voltage",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    ac_input_state = Field(
        start=32,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="1=AC Use, 0=AC_Drop",
        units="Enumerated",
        scale_factor=None,
    )
    minimum_ac_input_voltage = Field(
        start=33,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Minimum Input AC Voltage  (Write to clear value)",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    maximum_ac_input_voltage = Field(
        start=34,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Maximum Input AC Voltage  (Write to clear value)",
        units="VoltsAC",
        scale_factor="ac_voltage_scale_factor",
    )
    sell_status = Field(
        start=35,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Bit field for sell status  (See GS_Sell_Status Table)",
        units="Bitfield",
        scale_factor=None,
    )
    kwh_scale_factor = Field(
        start=36,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC kWh scale factor",
        units=None,
        scale_factor=None,
    )
    ac1_buy_kwh = Field(
        start=37,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily AC1 Buy kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    ac2_buy_kwh = Field(
        start=38,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily AC2 Buy kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    ac1_sell_kwh = Field(
        start=39,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily AC1 Sell kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    ac2_sell_kwh = Field(
        start=40,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily AC2 Sell kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    output_kwh = Field(
        start=41,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily Output kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    charger_kwh = Field(
        start=42,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Daily Charger kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )

    structure = SinglePhaseRadianInverterBlock
    device = Device.single_phase_radian_inverter


# This file is auto generated, do not edit. The generation code can be found in code_generator.py
class FlexnetDcDefinition(BaseDefinition):
    did = Field(
        start=1,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Vendor Extension for OutBack FLEXnet DC  Battery Monitor Status Block",
        units=None,
        scale_factor=None,
    )
    length = Field(
        start=2,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Length of block in 16-bit registers",
        units="Registers",
        scale_factor=None,
    )
    port_number = Field(
        start=3,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Port number on Outback network",
        units=None,
        scale_factor=None,
    )
    dc_voltage_scale_factor = Field(
        start=4,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    dc_current_scale_factor = Field(
        start=5,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Current Scale Factor",
        units=None,
        scale_factor=None,
    )
    time_scale_factor = Field(
        start=6,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Time Scale Factor",
        units=None,
        scale_factor=None,
    )
    kwh_scale_factor = Field(
        start=7,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Kilo Watt Hours Scale Factor",
        units=None,
        scale_factor=None,
    )
    kw_scale_factor = Field(
        start=8,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Kilo Watt Scale Factor",
        units=None,
        scale_factor=None,
    )
    shunt_a_current = Field(
        start=9,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Shunt A current",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    shunt_b_current = Field(
        start=10,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Shunt B current",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    shunt_c_current = Field(
        start=11,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Shunt C current",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    battery_voltage = Field(
        start=12,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Battery Voltage",
        units="Volts",
        scale_factor="dc_voltage_scale_factor",
    )
    battery_current = Field(
        start=13,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Battery Current",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    battery_temperature = Field(
        start=14,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Battery Temperature C",
        units="DegreesC",
        scale_factor=None,
    )
    status_flags = Field(
        start=15,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="See FN Status Table",
        units="Bitfield",
        scale_factor=None,
    )
    shunt_a_accumulated_ah = Field(
        start=16,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Shunt A Accumulated_AH",
        units="AH",
        scale_factor=None,
    )
    shunt_a_accumulated_kwh = Field(
        start=17,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Shunt A Accumulated_kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    shunt_b_accumulated_ah = Field(
        start=18,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Shunt B Accumulated_AH",
        units="AH",
        scale_factor=None,
    )
    shunt_b_accumulated_kwh = Field(
        start=19,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Shunt B Accumulated_kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    shunt_c_accumulated_ah = Field(
        start=20,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Shunt C Accumulated_AH",
        units="AH",
        scale_factor=None,
    )
    shunt_c_accumulated_kwh = Field(
        start=21,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Shunt C Accumulated_kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    input_current = Field(
        start=22,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Total_input_current",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    output_current = Field(
        start=23,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Total_output_current",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    input_kw = Field(
        start=24,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Total_input_kWatts",
        units="kW",
        scale_factor="kw_scale_factor",
    )
    output_kw = Field(
        start=25,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Total_output_kWatts",
        units="kW",
        scale_factor="kw_scale_factor",
    )
    net_kw = Field(
        start=26,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Total_net_kWatts",
        units="kW",
        scale_factor="kw_scale_factor",
    )
    days_since_charge_parameters_met = Field(
        start=27,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Days Since Charge Parameters Met",
        units="Days",
        scale_factor="time_scale_factor",
    )
    state_of_charge = Field(
        start=28,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Current Battery State of Charge",
        units="Percent",
        scale_factor=None,
    )
    todays_minimum_soc = Field(
        start=29,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Todays minimum SOC",
        units="Percent",
        scale_factor=None,
    )
    todays_maximum_soc = Field(
        start=30,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Todays maximum SOC",
        units="Percent",
        scale_factor=None,
    )
    todays_net_input_ah = Field(
        start=31,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Todays NET input AH",
        units="AH",
        scale_factor=None,
    )
    todays_net_input_kwh = Field(
        start=32,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Todays NET input kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    todays_net_output_ah = Field(
        start=33,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Todays NET output AH",
        units="AH",
        scale_factor=None,
    )
    todays_net_output_kwh = Field(
        start=34,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Todays NET output kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    todays_net_battery_ah = Field(
        start=35,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Todays NET battery AH",
        units="AH",
        scale_factor=None,
    )
    todays_net_battery_kwh = Field(
        start=36,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Todays NET battery kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    charge_factor_corrected_net_battery_ah = Field(
        start=37,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Charge factor corrected NET battery AH",
        units="AH",
        scale_factor=None,
    )
    charge_factor_corrected_net_battery_kwh = Field(
        start=38,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Charge factor corrected NET battery kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    todays_minimum_battery_voltage = Field(
        start=39,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Todays minimum battery voltage",
        units="Volts",
        scale_factor="dc_voltage_scale_factor",
    )
    todays_minimum_battery_time = Field(
        start=40,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Todays minimum battery voltage time UTC",
        units="Seconds",
        scale_factor=None,
    )
    todays_maximum_battery_voltage = Field(
        start=42,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Todays maximum battery voltage",
        units="Volts",
        scale_factor="dc_voltage_scale_factor",
    )
    todays_maximum_battery_time = Field(
        start=43,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Todays maximum battery voltage time UTC",
        units="Seconds",
        scale_factor=None,
    )
    cycle_charge_factor = Field(
        start=45,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Cycle Charge Factor",
        units="Percent",
        scale_factor=None,
    )
    cycle_kwh_charge_efficiency = Field(
        start=46,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Cycle kWh Charge Efficiency",
        units="Percent",
        scale_factor=None,
    )
    total_days_at_100_percent = Field(
        start=47,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Total days at 100% charged",
        units="Days",
        scale_factor="time_scale_factor",
    )
    lifetime_kah_removed = Field(
        start=48,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Lifetime kAH removed from battery",
        units="AH",
        scale_factor=None,
    )
    shunt_a_historical_returned_to_battery_ah = Field(
        start=49,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt A historical returned to battery AH",
        units="AH",
        scale_factor=None,
    )
    shunt_a_historical_returned_to_battery_kwh = Field(
        start=50,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt A historical returned to battery kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    shunt_a_historical_removed_from_battery_ah = Field(
        start=51,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt A historical removed from battery AH",
        units="AH",
        scale_factor=None,
    )
    shunt_a_historical_removed_from_battery_kwh = Field(
        start=52,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt A historical removed from battery  kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    shunt_a_maximum_charge_rate = Field(
        start=53,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt A historical maximum charge rate  Amps",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    shunt_a_maximum_charge_rate_kw = Field(
        start=54,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt A historical maximum charge rate kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    shunt_a_maximum_discharge_rate = Field(
        start=55,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Shunt A historical maximum discharge rate  Amps",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    shunt_a_maximum_discharge_rate_kw = Field(
        start=56,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Shunt A historical maximum discharge rate  kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    shunt_b_historical_returned_to_battery_ah = Field(
        start=57,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt B historical returned to battery AH",
        units="AH",
        scale_factor=None,
    )
    shunt_b_historical_returned_to_battery_kwh = Field(
        start=58,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt B historical returned to battery kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    shunt_b_historical_removed_from_battery_ah = Field(
        start=59,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt B historical removed from battery AH",
        units="AH",
        scale_factor=None,
    )
    shunt_b_historical_removed_from_battery_kwh = Field(
        start=60,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt B historical removed from battery  kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    shunt_b_maximum_charge_rate = Field(
        start=61,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt B historical maximum charge rate  Amps",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    shunt_b_maximum_charge_rate_kw = Field(
        start=62,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt B historical maximum charge rate kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    shunt_b_maximum_discharge_rate = Field(
        start=63,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Shunt B historical maximum discharge rate  Amps",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    shunt_b_maximum_discharge_rate_kw = Field(
        start=64,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Shunt B historical maximum discharge rate  kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    shunt_c_historical_returned_to_battery_ah = Field(
        start=65,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt C historical returned to battery AH",
        units="AH",
        scale_factor=None,
    )
    shunt_c_historical_returned_to_battery_kwh = Field(
        start=66,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt C historical returned to battery kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    shunt_c_historical_removed_from_battery_ah = Field(
        start=67,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt C historical removed from battery AH",
        units="AH",
        scale_factor=None,
    )
    shunt_c_historical_removed_from_battery_kwh = Field(
        start=68,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt C historical removed from battery  kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    shunt_c_maximum_charge_rate = Field(
        start=69,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt C historical maximum charge rate  Amps",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    shunt_c_maximum_charge_rate_kw = Field(
        start=70,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Shunt C historical maximum charge rate kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    shunt_c_maximum_discharge_rate = Field(
        start=71,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Shunt C historical maximum discharge rate  Amps",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    shunt_c_maximum_discharge_rate_kw = Field(
        start=72,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Shunt C historical maximum discharge rate  kW",
        units="kW",
        scale_factor="kwh_scale_factor",
    )
    shunt_a_reset_maximum_data = Field(
        start=73,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Read value needed to reset shunt A  maximum data",
        units=None,
        scale_factor=None,
    )
    shunt_a_reset_maximum_data_write_complement = Field(
        start=74,
        size=1,
        type=uint16,
        mode=Mode.W,
        description="Write value's complement to reset shunt A  maximum data",
        units=None,
        scale_factor=None,
    )
    shunt_b_reset_maximum_data = Field(
        start=75,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Read value needed to reset shunt B  maximum data",
        units=None,
        scale_factor=None,
    )
    shunt_b_reset_maximum_data_write_complement = Field(
        start=76,
        size=1,
        type=uint16,
        mode=Mode.W,
        description="Write value's complement to reset shunt B  maximum data",
        units=None,
        scale_factor=None,
    )
    shunt_c_reset_maximum_data = Field(
        start=77,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Read value needed to reset shunt C  maximum data",
        units=None,
        scale_factor=None,
    )
    shunt_c_reset_maximum_data_write_complement = Field(
        start=78,
        size=1,
        type=uint16,
        mode=Mode.W,
        description="Write value's complement to reset shunt C  maximum data",
        units=None,
        scale_factor=None,
    )

    structure = FlexnetDcBlock
    device = Device.flexnet_dc


# This file is auto generated, do not edit. The generation code can be found in code_generator.py
class FlexnetDcConfigurationDefinition(BaseDefinition):
    did = Field(
        start=1,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Vendor Extension for OutBack FLEXnet-DC  Battery Monitor Configuration Block",
        units=None,
        scale_factor=None,
    )
    length = Field(
        start=2,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Length of block in 16-bit registers",
        units="Registers",
        scale_factor=None,
    )
    port_number = Field(
        start=3,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Port number on OutBack network",
        units=None,
        scale_factor=None,
    )
    dc_voltage_scale_factor = Field(
        start=4,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    dc_current_scale_factor = Field(
        start=5,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Current Scale Factor",
        units=None,
        scale_factor=None,
    )
    kwh_scale_factor = Field(
        start=6,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Kilo Watt Hours Scale Factor",
        units=None,
        scale_factor=None,
    )
    major_firmware_number = Field(
        start=7,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="FLEXnet-DC Major firmware revision",
        units=None,
        scale_factor=None,
    )
    mid_firmware_number = Field(
        start=8,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="FLEXnet-DC Mid firmware revision",
        units=None,
        scale_factor=None,
    )
    minor_firmware_number = Field(
        start=9,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="FLEXnet-DC Minor firmware revision",
        units=None,
        scale_factor=None,
    )
    battery_capacity = Field(
        start=10,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Battery AH capacity",
        units="AH",
        scale_factor=None,
    )
    charged_volts = Field(
        start=11,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Battery Charged Voltage",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    charged_time = Field(
        start=12,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Battery Charged Time Minutes",
        units="Minutes",
        scale_factor=None,
    )
    battery_charged_amps = Field(
        start=13,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Battery Charged Return Amps",
        units="Amps",
        scale_factor="dc_current_scale_factor",
    )
    charge_factor = Field(
        start=14,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Battery Charge Factor",
        units="Percent",
        scale_factor=None,
    )
    shunt_a_enabled = Field(
        start=15,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Enabled, 1=Disabled",
        units="Enumerated",
        scale_factor=None,
    )
    shunt_b_enabled = Field(
        start=16,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Enabled, 1=Disabled",
        units="Enumerated",
        scale_factor=None,
    )
    shunt_c_enabled = Field(
        start=17,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Enabled, 1=Disabled",
        units="Enumerated",
        scale_factor=None,
    )
    relay_control = Field(
        start=18,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0 = Off; 1 = Auto; 2 = On",
        units="Enumerated",
        scale_factor=None,
    )
    relay_invert_logic = Field(
        start=19,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="0=Invert Logic,1=Normal",
        units="Enumerated",
        scale_factor=None,
    )
    relay_high_voltage = Field(
        start=20,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Relay high voltage enable",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    relay_low_voltage = Field(
        start=21,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Relay low voltage enable",
        units="DCVolts",
        scale_factor="dc_voltage_scale_factor",
    )
    relay_soc_high = Field(
        start=22,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Relay high SOC enable",
        units="Percent",
        scale_factor=None,
    )
    relay_soc_low = Field(
        start=23,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Relay low SOC enable",
        units="Percent",
        scale_factor=None,
    )
    relay_high_enable_delay = Field(
        start=24,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Relay High Enable Delay",
        units="Minutes",
        scale_factor=None,
    )
    relay_low_enable_delay = Field(
        start=25,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Relay Low Enable Delay",
        units="Minutes",
        scale_factor=None,
    )
    set_data_log_day_offset = Field(
        start=26,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Day offset 0-400, 0 =Today, 1 = -1 day …",
        units="Days",
        scale_factor=None,
    )
    get_current_data_log_day_offset = Field(
        start=27,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Current Data Log Day Offset",
        units="Days",
        scale_factor=None,
    )
    datalog_minimum_soc = Field(
        start=28,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Datalog minimum SOC",
        units="Percent",
        scale_factor=None,
    )
    datalog_input_ah = Field(
        start=29,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Datalog input AH",
        units="AH",
        scale_factor=None,
    )
    datalog_input_kwh = Field(
        start=30,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Datalog input kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    datalog_output_ah = Field(
        start=31,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Datalog output AH",
        units="AH",
        scale_factor=None,
    )
    datalog_output_kwh = Field(
        start=32,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Datalog output kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    datalog_net_ah = Field(
        start=33,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Datalog NET AH",
        units="AH",
        scale_factor=None,
    )
    datalog_net_kwh = Field(
        start=34,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Datalog NET kWh",
        units="kWh",
        scale_factor="kwh_scale_factor",
    )
    clear_data_log_read = Field(
        start=35,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Read value needed to clear data log",
        units=None,
        scale_factor=None,
    )
    clear_data_log_write_complement = Field(
        start=36,
        size=1,
        type=uint16,
        mode=Mode.W,
        description="Write value's complement to clear data log",
        units=None,
        scale_factor=None,
    )
    serial_number = Field(
        start=37,
        size=9,
        type=str,
        mode=Mode.R,
        description="Device serial number",
        units=None,
        scale_factor=None,
    )
    model_number = Field(
        start=46,
        size=9,
        type=str,
        mode=Mode.R,
        description="Device model",
        units=None,
        scale_factor=None,
    )

    structure = FlexnetDcConfigurationBlock
    device = Device.flexnet_dc_configuration


# This file is auto generated, do not edit. The generation code can be found in code_generator.py
class OutbackSystemControlDefinition(BaseDefinition):
    did = Field(
        start=1,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Vendor Extension for OutBack System  Control Block",
        units=None,
        scale_factor=None,
    )
    length = Field(
        start=2,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Length of block in 16-bit registers",
        units="Registers",
        scale_factor=None,
    )
    dc_voltage_scale_factor = Field(
        start=3,
        size=1,
        type=int16,
        mode=Mode.R,
        description="DC Voltage Scale Factor",
        units=None,
        scale_factor=None,
    )
    ac_current_scale_factor = Field(
        start=4,
        size=1,
        type=int16,
        mode=Mode.R,
        description="AC Current Scale Factor",
        units=None,
        scale_factor=None,
    )
    time_scale_factor = Field(
        start=5,
        size=1,
        type=int16,
        mode=Mode.R,
        description="Charge Time Scale Factor",
        units=None,
        scale_factor=None,
    )
    bulk_charge_enable_disable = Field(
        start=6,
        size=1,
        type=uint16,
        mode=Mode.W,
        description="1=Start Bulk, 2=Stop Bulk, 3=Start EQ  Charge, 4= Stop EQ Charge",
        units="Enumerated",
        scale_factor=None,
    )
    inverter_ac_drop_use = Field(
        start=7,
        size=1,
        type=uint16,
        mode=Mode.W,
        description="1=Use, 2=Drop",
        units="Enumerated",
        scale_factor=None,
    )
    set_inverter_mode = Field(
        start=8,
        size=1,
        type=uint16,
        mode=Mode.W,
        description="1=Off, 2=Search, 3=On",
        units="Enumerated",
        scale_factor=None,
    )
    grid_tie_mode = Field(
        start=9,
        size=1,
        type=uint16,
        mode=Mode.W,
        description="1=Enable, 2=Disable",
        units="Enumerated",
        scale_factor=None,
    )
    set_inverter_charger_mode = Field(
        start=10,
        size=1,
        type=uint16,
        mode=Mode.W,
        description="1=Off, 2=Auto, 3=On",
        units="Enumerated",
        scale_factor=None,
    )
    control_status = Field(
        start=11,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Bit field for status  (See OB_Control_Status Table)",
        units="Bitfield",
        scale_factor=None,
    )
    set_sell_voltage = Field(
        start=12,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Global Sell Voltage",
        units="Volts",
        scale_factor="dc_voltage_scale_factor",
    )
    set_radian_inverter_sell_current_limit = Field(
        start=13,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Radian Inverter Sell Current Limit",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    set_absorb_voltage = Field(
        start=14,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Global Absorb Voltage",
        units="Volts",
        scale_factor="dc_voltage_scale_factor",
    )
    set_absorb_time = Field(
        start=15,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Time in tenths of hour",
        units="Hours",
        scale_factor="time_scale_factor",
    )
    set_float_voltage = Field(
        start=16,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Global Float Voltage",
        units="Volts",
        scale_factor="dc_voltage_scale_factor",
    )
    set_float_time = Field(
        start=17,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Time in tenths of hour",
        units="Hours",
        scale_factor="time_scale_factor",
    )
    set_inverter_charger_current_limit = Field(
        start=18,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Inverter Charger Current Limit",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    set_inverter_ac1_current_limit = Field(
        start=19,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Inverter AC1 input Current Limit",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    set_inverter_ac2_current_limit = Field(
        start=20,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Inverter AC2 input Current Limit",
        units="Amps",
        scale_factor="ac_current_scale_factor",
    )
    set_ags_op_mode = Field(
        start=21,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="AGS Operating Mode: 0=Off, 1=On, 2=Auto",
        units="Enumerated",
        scale_factor=None,
    )
    ags_operational_state = Field(
        start=22,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="GEN_STOP=0, GEN_STARTING=1,  GEN_RUNNING=2, GEN_WARMUP=3,  GEN_COOLDOWN=4, GEN_AWAITING_AC=5",
        units="Enumerated",
        scale_factor=None,
    )
    ags_operational_state_timer = Field(
        start=23,
        size=1,
        type=uint16,
        mode=Mode.R,
        description="Number of seconds OB_AGS_Operational_State  has been in current state; if Operational State is  0 then timer=0",
        units="Seconds",
        scale_factor=None,
    )
    gen_last_run_start_time_gmt = Field(
        start=24,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Generator last start time in GMT seconds",
        units="Seconds",
        scale_factor=None,
    )
    gen_last_start_run_duration = Field(
        start=26,
        size=2,
        type=uint32,
        mode=Mode.R,
        description="Last Generator Start Run Duration Seconds",
        units="Seconds",
        scale_factor=None,
    )
    set_ac_output_freq_offline_mode = Field(
        start=28,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Not implemented",
        units="NA",
        scale_factor=None,
    )
    set_ac_output_offline_freq = Field(
        start=29,
        size=1,
        type=uint16,
        mode=Mode.RW,
        description="Set AC Output Frequency when AC Input is  disconnected: Range 60 Hz: 55.8 … 64.9 Hz,  50 Hz: 46.5 … 54.1 Hz",
        units="Hz",
        scale_factor="dc_voltage_scale_factor",
    )

    structure = OutbackSystemControlBlock
    device = Device.outback_system_control
