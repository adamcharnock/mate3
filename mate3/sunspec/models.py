"""This file is auto generated, do not edit. The generation code can be found in code_generator.py"""


from enum import Enum, IntFlag, unique
from mate3.sunspec.fields import (
    Mode,
    StringField,
    Int16Field,
    Uint16Field,
    Int32Field,
    Uint32Field,
    EnumUint16Field,
    EnumUint32Field,
    EnumInt16Field,
    EnumInt32Field,
    Bit16Field,
    Bit32Field,
    BitfieldDescriptionMixin,
    AddressField
)


@unique
class CCconfigFaultsFlags(BitfieldDescriptionMixin, IntFlag):
    fault_input_active = 16, "EX80 Fault Input Active"
    shorted_battery_temperature_sensor = 32, "Shorted Battery Temp sensor"
    over_temperature = 64, "Over Tempurature Fault"
    voc_too_high = 128, "PV Input voltage too high"

@unique
class FNStatusFlags(BitfieldDescriptionMixin, IntFlag):
    relay_status = 1, "AUX Relay Enabled (Unset means 'AUX Relay Disabled')"
    charged_parms = 2, "Charged Parms Met (Unset means 'Charged Parms Not Met')"

@unique
class FXErrorFlags(BitfieldDescriptionMixin, IntFlag):
    low_vac = 1, "Low AC output voltage"
    stacking_error = 2, "Stacking error"
    over_temperature = 4, "Over temperature error"
    low_vdc = 8, "Low battery voltage"
    phase_loss = 16, "Phase loss"
    high_vdc = 32, "High battery voltage"
    ac_shorted = 64, "AC output shorted"
    ac_backfeed = 128, "AC backfeed"

@unique
class FXSellStatusFlags(BitfieldDescriptionMixin, IntFlag):
    ac_input_frequency_too_high = 1, "AC input frequency too high"
    ac_input_frequency_too_low = 2, "AC input frequency too low"
    ac_input_voltage_too_low = 4, "AC input voltage too low"
    ac_input_voltage_too_high = 8, "AC input voltage too high"
    awaiting_sell_delay = 16, "Awaiting sell delay"
    disabled = 32, "Sell disabled"
    battery_voltage_less_than_target = 64, "Battery voltage less than target"
    ac2_selected = 128, "AC2 Selected"

@unique
class FXWarningFlags(BitfieldDescriptionMixin, IntFlag):
    ac_input_frequency_too_high = 1, "AC input frequency too high"
    ac_input_frequency_too_low = 2, "AC input frequency too low"
    ac_input_voltage_too_low = 4, "AC input voltage too low"
    ac_input_voltage_too_high = 8, "AC input voltage too high"
    ac_input_current_exceeds_max = 16, "AC input current exceeds max"
    temperature_sensor_bad = 32, "Temperature sensor bad"
    communications_error = 64, "Communications error"
    cooling_fan_fault = 128, "Cooling fan fault"

@unique
class GSSingleErrorFlags(BitfieldDescriptionMixin, IntFlag):
    low_vac = 1, "Low AC output voltage"
    stacking_error = 2, "Stacking error"
    over_temperature = 4, "Over temperature error"
    low_vdc = 8, "Low battery voltage"
    phase_loss = 16, "Phase loss"
    high_vdc = 32, "High battery voltage"
    ac_shorted = 64, "AC output shorted"
    ac_backfeed = 128, "AC backfeed"

@unique
class GSSingleSellStatusFlags(BitfieldDescriptionMixin, IntFlag):
    ac_input_frequency_too_high = 1, "AC input frequency too high"
    ac_input_frequency_too_low = 2, "AC input frequency too low"
    ac_input_voltage_too_low = 4, "AC input voltage too low"
    ac_input_voltage_too_high = 8, "AC input voltage too high"
    awaiting_sell_delay = 16, "Awaiting sell delay"
    disabled = 32, "Sell disabled"
    battery_voltage_less_than_target = 64, "Battery voltage less than target"

@unique
class GSSingleWarningFlags(BitfieldDescriptionMixin, IntFlag):
    ac_input_frequency_too_high = 1, "AC input frequency too high"
    ac_input_frequency_too_low = 2, "AC input frequency too low"
    ac_input_voltage_too_low = 4, "AC input voltage too low"
    ac_input_voltage_too_high = 8, "AC input voltage too high"
    ac_input_current_exceeds_max = 16, "AC input current exceeds max"
    temperature_sensor_bad = 32, "Temperature sensor bad"
    communications_error = 64, "Communications error"
    cooling_fan_fault = 128, "Cooling fan fault"

@unique
class GSSplitErrorFlags(BitfieldDescriptionMixin, IntFlag):
    low_vac = 1, "Low AC output voltage"
    stacking_error = 2, "Stacking error"
    over_temperature = 4, "Over temperature error"
    low_vdc = 8, "Low battery voltage"
    phase_loss = 16, "Phase loss"
    high_vdc = 32, "High battery voltage"
    ac_shorted = 64, "AC output shorted"
    ac_backfeed = 128, "AC backfeed"

@unique
class GSSplitSellStatusFlags(BitfieldDescriptionMixin, IntFlag):
    ac_input_frequency_too_high = 1, "AC input frequency too high"
    ac_input_frequency_too_low = 2, "AC input frequency too low"
    ac_input_voltage_too_low = 4, "AC input voltage too low"
    ac_input_voltage_too_high = 8, "AC input voltage too high"
    awaiting_sell_delay = 16, "Awaiting sell delay"
    disabled = 32, "Sell disabled"
    battery_voltage_less_than_target = 64, "Battery voltage less than target"

@unique
class GSSplitWarningFlags(BitfieldDescriptionMixin, IntFlag):
    ac_input_frequency_too_high = 1, "AC input frequency too high"
    ac_input_frequency_too_low = 2, "AC input frequency too low"
    ac_input_voltage_too_low = 4, "AC input voltage too low"
    ac_input_voltage_too_high = 8, "AC input voltage too high"
    ac_input_current_exceeds_max = 16, "AC input current exceeds max"
    temperature_sensor_bad = 32, "Temperature sensor bad"
    communications_error = 64, "Communications error"
    cooling_fan_fault = 128, "Cooling fan fault"

@unique
class IEvent1Flags(BitfieldDescriptionMixin, IntFlag):
    battery_voltage = 2, "High Battery Voltage (Unset means 'Normal Battery Voltage')"
    ac_input = 4, "AC Input Disconnected (Unset means 'AC Input Connected')"
    inverter = 64, "Inverter Off (Unset means 'Inverter On')"
    inverter_temperature = 128, "Inverter Over Temp (Unset means 'Inverter Temp Normal')"
    inverter_ac_input_freq_high = 256, "AC Input Over Frequency (Unset means 'AC Input Below High Frequency Limit')"
    inverter_ac_input_freq_low = 512, "AC Input Under Frequency (Unset means 'AC Input Above Lower Frequency Limit')"
    inverter_ac_input_voltage_high = 1024, "AC Input Over Voltage (Unset means 'AC Input Below High Voltage Limit')"
    inverter_ac_input_voltage_low = 2048, "AC Input Under Voltage (Unset means 'AC Input Above Lower Voltage Limit')"
    inverter_hardware_failure = 32768, "Inverter Fan or Temp Sensor Failure (Unset means 'Inverter Hardware No Faults Detected')"

@unique
class OBControlStatusFlags(BitfieldDescriptionMixin, IntFlag):
    charging_absorb = 1, "Absorb Charging"
    float_charging = 2, "Float Charging"
    inverter_ac_input = 4, "Inverter AC Input Use (Unset means 'Inverter AC Input Drop')"
    inverter_off = 8, "Inverter Off"
    inverter_search_mode = 16, "Inverter Search Mode"
    inverter_on = 32, "Inverter On"
    inverter_gridtie = 64, "Inverter Grid-Tie Enabled (Unset means 'Inverter Grid-Tie Disabled')"
    inverter_charger_disabled = 128, "Inverter Charger Off"
    inverter_charger_auto_mode = 256, "Inverter Charger Auto Mode"
    inverter_charger_bulk_and_float_mode = 512, "Inverter Charger On"
    eq_charging = 1024, "EQ Charging"
    charging_bulk = 2048, "Bulk Charging"
    sd_card_present = 4096, "SD Card Present"
    replay_file_present = 8192, "Replay File Present"
    sd_card_error = 16384, "SD Card Error"

@unique
class OutBackErrorFlags(BitfieldDescriptionMixin, IntFlag):
    write_high_limit = 1, "High limit last write"
    write_low_limit = 2, "Low limit last write"
    write_invalid = 4, "Last write invalid"
    dhcp_failed = 8, "DHCP failed"
    dns_resolve_failed = 16, "DNS resolve failure"
    smtp_authorization_failed = 32, "SMTP authorization failed"
    smtp_send_failed = 64, "SMTP send failed"
    ftp_error = 128, "FTP Error"
    sd_card_error = 256, "SD-Card Error"
    sntp_failure = 512, "SNTP failure"
    write_while_locked = 1024, "Write while locked"
    firmware_update_not_supported = 2048, "Device firmware updating not supported"
    firmware_update_file_not_found = 4096, "Device firmware update file not found"
    firmware_update_file_invalid = 8192, "Device firmware update file invalid"
    firmware_update_failure = 16384, "Device firmware update failure"

@unique
class OutBackStatusFlags(BitfieldDescriptionMixin, IntFlag):
    out_back_status_firmware_update_complete = 1, "Firmware Update Complete"

@unique
class OutBackUpdateDeviceFirmwarePortFlags(BitfieldDescriptionMixin, IntFlag):
    portnumber = 255, "Port Number"
    update_percentage = 65280, "Firmware Update Percentage"


@unique
class SunSpecHeaderModel(Enum):
    did = Uint32Field(1, 2, Mode.R)
    model_id = Uint16Field(3, 1, Mode.R)
    length = Uint16Field(4, 1, Mode.R)
    manufacturer = StringField(5, 16, Mode.R)
    model = StringField(21, 16, Mode.R)
    options = StringField(37, 8, Mode.R)
    version = StringField(45, 8, Mode.R)
    serial_number = StringField(53, 16, Mode.R)


@unique
class SunSpecEndModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Should be 65535")
    length = Uint16Field(2, 1, Mode.R, description="Should be 0")


@unique
class SunSpecCommonModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Common Model block")
    length = Uint16Field(2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    manufacturer = StringField(3, 16, Mode.R)
    model = StringField(19, 16, Mode.R)
    options = StringField(35, 8, Mode.R)
    version = StringField(43, 8, Mode.R)
    serial_number = StringField(51, 16, Mode.R)
    device_address = Uint16Field(67, 1, Mode.RW)


@unique
class SunSpecInverterSinglePhaseModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Single Phase Inverter")
    length = Uint16Field(2, 1, Mode.R, description="Length of model block", units="Registers")
    ac_current = Uint16Field(3, 1, Mode.R, description="AC Total Current value", units="Amps")
    ac_current_a = Uint16Field(4, 1, Mode.R, description="AC Phase-A Current value", units="Amps")
    ac_current_b = Uint16Field(5, 1, Mode.R, description="AC Phase-B Current value", units="Amps")
    ac_current_c = Uint16Field(6, 1, Mode.R, description="AC Phase-C Current value", units="Amps")
    ac_current_scale_factor = Int16Field(7, 1, Mode.R, description="AC Current Scale factor", units="SF")
    ac_voltage_ab = Uint16Field(8, 1, Mode.R, description="AC Voltage Phase-AB value", units="Volts")
    ac_voltage_bc = Uint16Field(9, 1, Mode.R, description="AC Voltage Phase BC value", units="Volts")
    ac_voltage_ca = Uint16Field(10, 1, Mode.R, description="AC Voltage Phase CA value", units="Volts")
    ac_voltage_an = Uint16Field(11, 1, Mode.R, description="AC Voltage Phase-A-to-neutral value", units="Volts")
    ac_voltage_bn = Uint16Field(12, 1, Mode.R, description="AC Voltage Phase B-to-neutral value", units="Volts")
    ac_voltage_cn = Uint16Field(13, 1, Mode.R, description="AC Voltage Phase C-to-neutral value", units="Volts")
    ac_voltage_scale_factor = Int16Field(14, 1, Mode.R, description="AC Voltage Scale factor", units="SF")
    ac_power = Int16Field(15, 1, Mode.R, description="AC Power value", units="Watts")
    ac_power_scale_factor = Int16Field(16, 1, Mode.R, description="AC Power Scale factor", units="SF")
    ac_frequency = Uint16Field(17, 1, Mode.R, description="AC Frequency value", units="Hertz")
    ac_frequency_scale_factor = Int16Field(18, 1, Mode.R, description="Scale factor", units="SF")
    ac_va = Int16Field(19, 1, Mode.R, description="Apparent Power", units="VA")
    ac_va_scale_factor = Int16Field(20, 1, Mode.R, description="Scale factor", units="SF")
    ac_var = Int16Field(21, 1, Mode.R, description="Reactive Power", units="VAR")
    ac_var_scale_factor = Int16Field(22, 1, Mode.R, description="Scale factor", units="SF")
    ac_pf = Int16Field(23, 1, Mode.R, description="Power Factor")
    ac_pf_scale_factor = Int16Field(24, 1, Mode.R, description="Scale factor", units="SF")
    ac_energy_wh = Uint32Field(25, 2, Mode.R, description="AC Lifetime Energy production", units="WattHours")
    ac_energy_wh_scale_factor = Uint16Field(27, 1, Mode.R, description="AC Lifetime Energy production scale factor", units="SF")
    dc_current = Uint16Field(28, 1, Mode.R, description="DC Current value", units="Amps")
    dc_current_scale_factor = Int16Field(29, 1, Mode.R, description="Scale factor", units="SF")
    dc_voltage = Uint16Field(30, 1, Mode.R, description="DC Voltage value", units="Volts")
    dc_voltage_scale_factor = Int16Field(31, 1, Mode.R, description="Scale factor", units="SF")
    dc_power = Int16Field(32, 1, Mode.R, description="DC Power value", units="Watts")
    dc_power_scale_factor = Int16Field(33, 1, Mode.R, description="Scale factor", units="SF")
    temp_cab = Int16Field(34, 1, Mode.R, description="Cabinet Temperature", units="Degrees C")
    temp_sink = Int16Field(35, 1, Mode.R, description="Coolant or Heat Sink Temperature", units="Degrees C")
    temp_trans = Int16Field(36, 1, Mode.R, description="Transformer Temperature", units="Degrees C")
    temp_other = Int16Field(37, 1, Mode.R, description="Other Temperature", units="Degrees C")
    temp_scale_factor = Int16Field(38, 1, Mode.R, description="Scale factor", units="SF")
    status = Uint16Field(39, 1, Mode.R, description="Operating State", units="Enumerated")
    status_vendor = Uint16Field(40, 1, Mode.R, description="Vendor Defined Operating State", units="Enumerated")
    event_1 = Bit32Field(41, 2, Mode.R, description="Event Flags (bits 0-31)", flags=IEvent1Flags)


SunSpecInverterSinglePhaseModel.ac_current.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_current_scale_factor
SunSpecInverterSinglePhaseModel.ac_current_a.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_current_scale_factor
SunSpecInverterSinglePhaseModel.ac_current_b.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_current_scale_factor
SunSpecInverterSinglePhaseModel.ac_current_c.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_current_scale_factor
SunSpecInverterSinglePhaseModel.ac_voltage_ab.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_voltage_scale_factor
SunSpecInverterSinglePhaseModel.ac_voltage_bc.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_voltage_scale_factor
SunSpecInverterSinglePhaseModel.ac_voltage_ca.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_voltage_scale_factor
SunSpecInverterSinglePhaseModel.ac_voltage_an.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_voltage_scale_factor
SunSpecInverterSinglePhaseModel.ac_voltage_bn.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_voltage_scale_factor
SunSpecInverterSinglePhaseModel.ac_voltage_cn.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_voltage_scale_factor
SunSpecInverterSinglePhaseModel.ac_power.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_power_scale_factor
SunSpecInverterSinglePhaseModel.ac_frequency.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_frequency_scale_factor
SunSpecInverterSinglePhaseModel.ac_va.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_va_scale_factor
SunSpecInverterSinglePhaseModel.ac_var.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_var_scale_factor
SunSpecInverterSinglePhaseModel.ac_pf.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_pf_scale_factor
SunSpecInverterSinglePhaseModel.ac_energy_wh.value.scale_factor = SunSpecInverterSinglePhaseModel.ac_energy_wh_scale_factor
SunSpecInverterSinglePhaseModel.dc_current.value.scale_factor = SunSpecInverterSinglePhaseModel.dc_current_scale_factor
SunSpecInverterSinglePhaseModel.dc_voltage.value.scale_factor = SunSpecInverterSinglePhaseModel.dc_voltage_scale_factor
SunSpecInverterSinglePhaseModel.dc_power.value.scale_factor = SunSpecInverterSinglePhaseModel.dc_power_scale_factor
SunSpecInverterSinglePhaseModel.temp_cab.value.scale_factor = SunSpecInverterSinglePhaseModel.temp_scale_factor
SunSpecInverterSinglePhaseModel.temp_sink.value.scale_factor = SunSpecInverterSinglePhaseModel.temp_scale_factor
SunSpecInverterSinglePhaseModel.temp_trans.value.scale_factor = SunSpecInverterSinglePhaseModel.temp_scale_factor
SunSpecInverterSinglePhaseModel.temp_other.value.scale_factor = SunSpecInverterSinglePhaseModel.temp_scale_factor


@unique
class SunSpecInverterSplitPhaseModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Split Phase Inverter")
    length = Uint16Field(2, 1, Mode.R, description="Length of model block", units="Registers")
    ac_current = Uint16Field(3, 1, Mode.R, description="AC Total Current value", units="Amps")
    ac_current_a = Uint16Field(4, 1, Mode.R, description="AC Phase-A Current value", units="Amps")
    ac_current_b = Uint16Field(5, 1, Mode.R, description="AC Phase-B Current value", units="Amps")
    ac_current_c = Uint16Field(6, 1, Mode.R, description="AC Phase-C Current value", units="Amps")
    ac_current_scale_factor = Int16Field(7, 1, Mode.R, description="AC Current Scale factor", units="SF")
    ac_voltage_ab = Uint16Field(8, 1, Mode.R, description="AC Voltage Phase-AB value", units="Volts")
    ac_voltage_bc = Uint16Field(9, 1, Mode.R, description="AC Voltage Phase BC value", units="Volts")
    ac_voltage_ca = Uint16Field(10, 1, Mode.R, description="AC Voltage Phase CA value", units="Volts")
    ac_voltage_an = Uint16Field(11, 1, Mode.R, description="AC Voltage Phase-A-to-neutral value", units="Volts")
    ac_voltage_bn = Uint16Field(12, 1, Mode.R, description="AC Voltage Phase B-to-neutral value", units="Volts")
    ac_voltage_cn = Uint16Field(13, 1, Mode.R, description="AC Voltage Phase C-to-neutral value", units="Volts")
    ac_voltage_scale_factor = Int16Field(14, 1, Mode.R, description="AC Voltage Scale factor", units="SF")
    ac_power = Int16Field(15, 1, Mode.R, description="AC Power value", units="Watts")
    ac_power_scale_factor = Int16Field(16, 1, Mode.R, description="AC Power Scale factor", units="SF")
    ac_frequency = Uint16Field(17, 1, Mode.R, description="AC Frequency value", units="Hertz")
    ac_frequency_scale_factor = Int16Field(18, 1, Mode.R, description="Scale factor", units="SF")
    ac_va = Int16Field(19, 1, Mode.R, description="Apparent Power", units="VA")
    ac_va_scale_factor = Int16Field(20, 1, Mode.R, description="Scale factor", units="SF")
    ac_var = Int16Field(21, 1, Mode.R, description="Reactive Power", units="VAR")
    ac_var_scale_factor = Int16Field(22, 1, Mode.R, description="Scale factor", units="SF")
    ac_pf = Int16Field(23, 1, Mode.R, description="Power Factor")
    ac_pf_scale_factor = Int16Field(24, 1, Mode.R, description="Scale factor", units="SF")
    ac_energy_wh = Uint32Field(25, 2, Mode.R, description="AC Lifetime Energy production", units="WattHours")
    ac_energy_wh_scale_factor = Uint16Field(27, 1, Mode.R, description="AC Lifetime Energy production scale factor", units="SF")
    dc_current = Uint16Field(28, 1, Mode.R, description="DC Current value", units="Amps")
    dc_current_scale_factor = Int16Field(29, 1, Mode.R, description="Scale factor", units="SF")
    dc_voltage = Uint16Field(30, 1, Mode.R, description="DC Voltage value", units="Volts")
    dc_voltage_scale_factor = Int16Field(31, 1, Mode.R, description="Scale factor", units="SF")
    dc_power = Int16Field(32, 1, Mode.R, description="DC Power value", units="Watts")
    dc_power_scale_factor = Int16Field(33, 1, Mode.R, description="Scale factor", units="SF")
    temp_cab = Int16Field(34, 1, Mode.R, description="Cabinet Temperature", units="Degrees C")
    temp_sink = Int16Field(35, 1, Mode.R, description="Coolant or Heat Sink Temperature", units="Degrees C")
    temp_trans = Int16Field(36, 1, Mode.R, description="Transformer Temperature", units="Degrees C")
    temp_other = Int16Field(37, 1, Mode.R, description="Other Temperature", units="Degrees C")
    temp_scale_factor = Int16Field(38, 1, Mode.R, description="Scale factor", units="SF")
    status = Uint16Field(39, 1, Mode.R, description="Operating State", units="Enumerated")
    status_vendor = Uint16Field(40, 1, Mode.R, description="Vendor Defined Operating State", units="Enumerated")
    event_1 = Bit32Field(41, 2, Mode.R, description="Event Flags (bits 0-31)", flags=IEvent1Flags)


SunSpecInverterSplitPhaseModel.ac_current.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_current_scale_factor
SunSpecInverterSplitPhaseModel.ac_current_a.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_current_scale_factor
SunSpecInverterSplitPhaseModel.ac_current_b.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_current_scale_factor
SunSpecInverterSplitPhaseModel.ac_current_c.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_current_scale_factor
SunSpecInverterSplitPhaseModel.ac_voltage_ab.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_voltage_scale_factor
SunSpecInverterSplitPhaseModel.ac_voltage_bc.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_voltage_scale_factor
SunSpecInverterSplitPhaseModel.ac_voltage_ca.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_voltage_scale_factor
SunSpecInverterSplitPhaseModel.ac_voltage_an.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_voltage_scale_factor
SunSpecInverterSplitPhaseModel.ac_voltage_bn.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_voltage_scale_factor
SunSpecInverterSplitPhaseModel.ac_voltage_cn.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_voltage_scale_factor
SunSpecInverterSplitPhaseModel.ac_power.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_power_scale_factor
SunSpecInverterSplitPhaseModel.ac_frequency.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_frequency_scale_factor
SunSpecInverterSplitPhaseModel.ac_va.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_va_scale_factor
SunSpecInverterSplitPhaseModel.ac_var.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_var_scale_factor
SunSpecInverterSplitPhaseModel.ac_pf.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_pf_scale_factor
SunSpecInverterSplitPhaseModel.ac_energy_wh.value.scale_factor = SunSpecInverterSplitPhaseModel.ac_energy_wh_scale_factor
SunSpecInverterSplitPhaseModel.dc_current.value.scale_factor = SunSpecInverterSplitPhaseModel.dc_current_scale_factor
SunSpecInverterSplitPhaseModel.dc_voltage.value.scale_factor = SunSpecInverterSplitPhaseModel.dc_voltage_scale_factor
SunSpecInverterSplitPhaseModel.dc_power.value.scale_factor = SunSpecInverterSplitPhaseModel.dc_power_scale_factor
SunSpecInverterSplitPhaseModel.temp_cab.value.scale_factor = SunSpecInverterSplitPhaseModel.temp_scale_factor
SunSpecInverterSplitPhaseModel.temp_sink.value.scale_factor = SunSpecInverterSplitPhaseModel.temp_scale_factor
SunSpecInverterSplitPhaseModel.temp_trans.value.scale_factor = SunSpecInverterSplitPhaseModel.temp_scale_factor
SunSpecInverterSplitPhaseModel.temp_other.value.scale_factor = SunSpecInverterSplitPhaseModel.temp_scale_factor


@unique
class SunSpecInverterThreePhaseModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Three Phase Inverter")
    length = Uint16Field(2, 1, Mode.R, description="Length of model block", units="Registers")
    ac_current = Uint16Field(3, 1, Mode.R, description="AC Total Current value", units="Amps")
    ac_current_a = Uint16Field(4, 1, Mode.R, description="AC Phase-A Current value", units="Amps")
    ac_current_b = Uint16Field(5, 1, Mode.R, description="AC Phase-B Current value", units="Amps")
    ac_current_c = Uint16Field(6, 1, Mode.R, description="AC Phase-C Current value", units="Amps")
    ac_current_scale_factor = Int16Field(7, 1, Mode.R, description="AC Current Scale factor", units="SF")
    ac_voltage_ab = Uint16Field(8, 1, Mode.R, description="AC Voltage Phase-AB value", units="Volts")
    ac_voltage_bc = Uint16Field(9, 1, Mode.R, description="AC Voltage Phase BC value", units="Volts")
    ac_voltage_ca = Uint16Field(10, 1, Mode.R, description="AC Voltage Phase CA value", units="Volts")
    ac_voltage_an = Uint16Field(11, 1, Mode.R, description="AC Voltage Phase-A-to-neutral value", units="Volts")
    ac_voltage_bn = Uint16Field(12, 1, Mode.R, description="AC Voltage Phase B-to-neutral value", units="Volts")
    ac_voltage_cn = Uint16Field(13, 1, Mode.R, description="AC Voltage Phase C-to-neutral value", units="Volts")
    ac_voltage_scale_factor = Int16Field(14, 1, Mode.R, description="AC Voltage Scale factor", units="SF")
    ac_power = Int16Field(15, 1, Mode.R, description="AC Power value", units="Watts")
    ac_power_scale_factor = Int16Field(16, 1, Mode.R, description="AC Power Scale factor", units="SF")
    ac_frequency = Uint16Field(17, 1, Mode.R, description="AC Frequency value", units="Hertz")
    ac_frequency_scale_factor = Int16Field(18, 1, Mode.R, description="Scale factor", units="SF")
    ac_va = Int16Field(19, 1, Mode.R, description="Apparent Power", units="VA")
    ac_va_scale_factor = Int16Field(20, 1, Mode.R, description="Scale factor", units="SF")
    ac_var = Int16Field(21, 1, Mode.R, description="Reactive Power", units="VAR")
    ac_var_scale_factor = Int16Field(22, 1, Mode.R, description="Scale factor", units="SF")
    ac_pf = Int16Field(23, 1, Mode.R, description="Power Factor")
    ac_pf_scale_factor = Int16Field(24, 1, Mode.R, description="Scale factor", units="SF")
    ac_energy_wh = Uint32Field(25, 2, Mode.R, description="AC Lifetime Energy production", units="WattHours")
    ac_energy_wh_scale_factor = Uint16Field(27, 1, Mode.R, description="AC Lifetime Energy production scale factor", units="SF")
    dc_current = Uint16Field(28, 1, Mode.R, description="DC Current value", units="Amps")
    dc_current_scale_factor = Int16Field(29, 1, Mode.R, description="Scale factor", units="SF")
    dc_voltage = Uint16Field(30, 1, Mode.R, description="DC Voltage value", units="Volts")
    dc_voltage_scale_factor = Int16Field(31, 1, Mode.R, description="Scale factor", units="SF")
    dc_power = Int16Field(32, 1, Mode.R, description="DC Power value", units="Watts")
    dc_power_scale_factor = Int16Field(33, 1, Mode.R, description="Scale factor", units="SF")
    temp_cab = Int16Field(34, 1, Mode.R, description="Cabinet Temperature", units="Degrees C")
    temp_sink = Int16Field(35, 1, Mode.R, description="Coolant or Heat Sink Temperature", units="Degrees C")
    temp_trans = Int16Field(36, 1, Mode.R, description="Transformer Temperature", units="Degrees C")
    temp_other = Int16Field(37, 1, Mode.R, description="Other Temperature", units="Degrees C")
    temp_scale_factor = Int16Field(38, 1, Mode.R, description="Scale factor", units="SF")
    status = Uint16Field(39, 1, Mode.R, description="Operating State", units="Enumerated")
    status_vendor = Uint16Field(40, 1, Mode.R, description="Vendor Defined Operating State", units="Enumerated")
    event_1 = Bit32Field(41, 2, Mode.R, description="Event Flags (bits 0-31)", flags=IEvent1Flags)


SunSpecInverterThreePhaseModel.ac_current.value.scale_factor = SunSpecInverterThreePhaseModel.ac_current_scale_factor
SunSpecInverterThreePhaseModel.ac_current_a.value.scale_factor = SunSpecInverterThreePhaseModel.ac_current_scale_factor
SunSpecInverterThreePhaseModel.ac_current_b.value.scale_factor = SunSpecInverterThreePhaseModel.ac_current_scale_factor
SunSpecInverterThreePhaseModel.ac_current_c.value.scale_factor = SunSpecInverterThreePhaseModel.ac_current_scale_factor
SunSpecInverterThreePhaseModel.ac_voltage_ab.value.scale_factor = SunSpecInverterThreePhaseModel.ac_voltage_scale_factor
SunSpecInverterThreePhaseModel.ac_voltage_bc.value.scale_factor = SunSpecInverterThreePhaseModel.ac_voltage_scale_factor
SunSpecInverterThreePhaseModel.ac_voltage_ca.value.scale_factor = SunSpecInverterThreePhaseModel.ac_voltage_scale_factor
SunSpecInverterThreePhaseModel.ac_voltage_an.value.scale_factor = SunSpecInverterThreePhaseModel.ac_voltage_scale_factor
SunSpecInverterThreePhaseModel.ac_voltage_bn.value.scale_factor = SunSpecInverterThreePhaseModel.ac_voltage_scale_factor
SunSpecInverterThreePhaseModel.ac_voltage_cn.value.scale_factor = SunSpecInverterThreePhaseModel.ac_voltage_scale_factor
SunSpecInverterThreePhaseModel.ac_power.value.scale_factor = SunSpecInverterThreePhaseModel.ac_power_scale_factor
SunSpecInverterThreePhaseModel.ac_frequency.value.scale_factor = SunSpecInverterThreePhaseModel.ac_frequency_scale_factor
SunSpecInverterThreePhaseModel.ac_va.value.scale_factor = SunSpecInverterThreePhaseModel.ac_va_scale_factor
SunSpecInverterThreePhaseModel.ac_var.value.scale_factor = SunSpecInverterThreePhaseModel.ac_var_scale_factor
SunSpecInverterThreePhaseModel.ac_pf.value.scale_factor = SunSpecInverterThreePhaseModel.ac_pf_scale_factor
SunSpecInverterThreePhaseModel.ac_energy_wh.value.scale_factor = SunSpecInverterThreePhaseModel.ac_energy_wh_scale_factor
SunSpecInverterThreePhaseModel.dc_current.value.scale_factor = SunSpecInverterThreePhaseModel.dc_current_scale_factor
SunSpecInverterThreePhaseModel.dc_voltage.value.scale_factor = SunSpecInverterThreePhaseModel.dc_voltage_scale_factor
SunSpecInverterThreePhaseModel.dc_power.value.scale_factor = SunSpecInverterThreePhaseModel.dc_power_scale_factor
SunSpecInverterThreePhaseModel.temp_cab.value.scale_factor = SunSpecInverterThreePhaseModel.temp_scale_factor
SunSpecInverterThreePhaseModel.temp_sink.value.scale_factor = SunSpecInverterThreePhaseModel.temp_scale_factor
SunSpecInverterThreePhaseModel.temp_trans.value.scale_factor = SunSpecInverterThreePhaseModel.temp_scale_factor
SunSpecInverterThreePhaseModel.temp_other.value.scale_factor = SunSpecInverterThreePhaseModel.temp_scale_factor


@unique
class OutBackModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Outback Interface")
    length = Uint16Field(2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    major_firmware_number = Uint16Field(3, 1, Mode.R, description="OutBack Major firmware revision")
    mid_firmware_number = Uint16Field(4, 1, Mode.R, description="OutBack Mid firmware revision")
    minor_firmware_number = Uint16Field(5, 1, Mode.R, description="OutBack Minor firmware revision")
    encryption_key = Uint16Field(6, 1, Mode.R, description="Encryption key for current session (0 = Encryption not enabled)")
    mac_address = StringField(7, 7, Mode.R, description="Ethernet MAC address")
    write_password = StringField(14, 8, Mode.W, description="Password required to write to any register")
    enable_dhcp = EnumUint16Field(22, 1, Mode.RW, description="0 = DHCP Disabled, use configured network parameter; 1 = DHCP Enabled", options=Enum("enable_dhcp", [('DHCP Disabled, use configured network parameter;', 0), ('DHCP Enabled', 1)]))
    tcpip_address = AddressField(23, 2, Mode.RW, description="TCP/IP Address xxx.xxx.xxx.xxx")
    tcpip_gateway_msw = AddressField(25, 2, Mode.RW, description="TCP/IP Gateway xxx.xxx.xxx.xxx")
    tcpip_netmask_msw = AddressField(27, 2, Mode.RW, description="TCP/IP Netmask xxx.xxx.xxx.xxx")
    tcpip_dns_1_msw = AddressField(29, 2, Mode.RW, description="TCP/IP DNS 1 xxx.xxx.xxx.xxx")
    tcpip_dns_2_msw = AddressField(31, 2, Mode.RW, description="TCP/IP DNS 2 xxx.xxx.xxx.xxx")
    modbus_port = Uint16Field(33, 1, Mode.RW, description="Outback MODBUS IP port, default 502")
    smtp_server_name = StringField(34, 20, Mode.RW, description="Email server name")
    smtp_account_name = StringField(54, 16, Mode.RW, description="Email account name")
    smtp_ssl_enable = EnumUint16Field(70, 1, Mode.RW, description="0 = SSL Disabled; 1 = SSL Enabled (not implemented)", options=Enum("smtp_ssl_enable", [('SSL Disabled;', 0), ('SSL Enabled (not implemented)', 1)]))
    smtp_email_password = StringField(71, 8, Mode.W, description="Email account password")
    smtp_email_user_name = StringField(79, 20, Mode.RW, description="Email account User Name")
    status_email_interval = Uint16Field(99, 1, Mode.RW, description="0 = Status Email Disabled, 1-23 Status Email every n hours")
    status_email_status_time = Uint16Field(100, 1, Mode.RW, description="Hour  of first status email of the day")
    status_email_subject_line = StringField(101, 25, Mode.RW, description="Status Email Subject Line")
    status_email_to_address_1 = StringField(126, 20, Mode.RW, description="Status Email to Address 1")
    status_email_to_address_2 = StringField(146, 20, Mode.RW, description="Status Email to Address 2")
    alarm_email_enable = EnumUint16Field(166, 1, Mode.RW, description="0 = Disabled; 1 = Enabled", options=Enum("alarm_email_enable", [('Disabled;', 0), ('Enabled', 1)]))
    system_name = StringField(167, 30, Mode.RW, description="OutBack System Name")
    alarm_email_to_address_1 = StringField(197, 15, Mode.RW, description="Status Alarm to Address 1")
    alarm_email_to_address_2 = StringField(212, 20, Mode.RW, description="Status Alarm to Address 2")
    ftp_password = StringField(232, 8, Mode.W, description="FTP password")
    telnet_password = StringField(240, 8, Mode.W, description="Telnet password (not implemented)")
    sd_card_data_log_write_interval = Uint16Field(248, 1, Mode.RW, description="0 = SD-Card Data Logging disabled, 1-60 seconds")
    sd_card_data_log_retain_days = Uint16Field(249, 1, Mode.RW, description="0 = Log until SD-Card is full then erase oldest, 1-731 Number of days to retain data logs")
    sd_card_data_logging_mode = EnumUint16Field(250, 1, Mode.RW, description="0 = Disabled; 1 = Excel Format; 2 = Compact Format", options=Enum("sd_card_data_logging_mode", [('Compact Format', 2), ('Disabled;', 0), ('Excel Format;', 1)]))
    time_server_name = StringField(251, 20, Mode.RW, description="Timeserver domain name")
    enable_time_server = EnumUint16Field(271, 1, Mode.RW, description="0 = Time Server Disabled, use configured time parameters; 1 = Time  Server Enabled", options=Enum("enable_time_server", [('Time  Server Enabled', 1), ('Time Server Disabled, use configured time parameters;', 0)]))
    set_time_zone = Int16Field(272, 1, Mode.RW, description="Time Zone -12.0 \u2026 +14.0", units="Hours")
    enable_float_coordination = EnumUint16Field(273, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("enable_float_coordination", [('Disabled', 0), ('Enabled', 1)]))
    enable_fndc_charge_termination = EnumUint16Field(274, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("enable_fndc_charge_termination", [('Disabled', 0), ('Enabled', 1)]))
    enable_fndc_grid_tie_control = EnumUint16Field(275, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("enable_fndc_grid_tie_control", [('Disabled', 0), ('Enabled', 1)]))
    voltage_scale_factor = Int16Field(276, 1, Mode.R, description="DC Voltage Scale Factor")
    hour_scale_factor = Int16Field(277, 1, Mode.R, description="Hours Scale Factor")
    ags_mode = EnumUint16Field(278, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_port = Uint16Field(279, 1, Mode.RW, description="AGS device port number 0-10")
    ags_port_type = EnumUint16Field(280, 1, Mode.RW, description="0=Radian AUX Relay, 1=Radian AUX Output", options=Enum("ags_port_type", [('Radian AUX Output', 1), ('Radian AUX Relay', 0)]))
    ags_generator_type = EnumUint16Field(281, 1, Mode.RW, description="0=AC Gen, 1=DC Gen, 2=No Gen", options=Enum("ags_generator_type", [('AC Gen', 0), ('DC Gen', 1), ('No Gen', 2)]))
    ags_dc_gen_absorb_voltage = Uint16Field(282, 1, Mode.RW, description="DC Generator Absorb Voltage", units="Volts")
    ags_dc_gen_absorb_time = Uint16Field(283, 1, Mode.RW, description="DC Generator Absorb Time", units="Hour")
    ags_fault_time = Uint16Field(284, 1, Mode.RW, description="AGS Generator fault time delay", units="Minutes")
    ags_gen_cool_down_time = Uint16Field(285, 1, Mode.RW, description="AGS Generator Cool Down Time", units="Minutes")
    ags_gen_warm_up_time = Uint16Field(286, 1, Mode.RW, description="AGS Generator Warm Up Time", units="Minutes")
    ags_generator_exercise_mode = EnumUint16Field(287, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_generator_exercise_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_exercise_start_hour = Uint16Field(288, 1, Mode.RW, description="Exercise Start Hour 0-23", units="Hour")
    ags_exercise_start_minute = Uint16Field(289, 1, Mode.RW, description="Exercise Start Minute 0-59", units="Minutes")
    ags_exercise_day = EnumUint16Field(290, 1, Mode.RW, description="0=Sun, 1=Mon, 2=Tue, 3=Wed, 4=Thr, 5=Fri, 6=Sat", options=Enum("ags_exercise_day", [('Fri', 5), ('Mon', 1), ('Sat', 6), ('Sun', 0), ('Thr', 4), ('Tue', 2), ('Wed', 3)]))
    ags_exercise_period = Uint16Field(291, 1, Mode.RW, description="Exercise Period 1-240 minutes", units="Minutes")
    ags_exercise_interval = Uint16Field(292, 1, Mode.RW, description="Exercise interval 1-8 Weeks", units="Weeks")
    ags_sell_mode = EnumUint16Field(293, 1, Mode.RW, description="Sell During Generator Exercise Period, 0=Selling Enabled, 1=Selling Disabled", options=Enum("ags_sell_mode", [('Selling Disabled', 1), ('Selling Enabled', 0)]))
    ags_2_min_start_mode = EnumUint16Field(294, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_2_min_start_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_2_min_start_voltage = Uint16Field(295, 1, Mode.RW, description="Two Minute AGS Start Voltage", units="Volts")
    ags_2_hour_start_mode = EnumUint16Field(296, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_2_hour_start_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_2_hour_start_voltage = Uint16Field(297, 1, Mode.RW, description="Two Hour AGS Start Voltage", units="Volts")
    ags_24_hour_start_mode = EnumUint16Field(298, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_24_hour_start_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_24_hour_start_voltage = Uint16Field(299, 1, Mode.RW, description="Twenty Four Hour AGS Start Voltage", units="Volts")
    ags_load_start_mode = EnumUint16Field(300, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_load_start_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_load_start_kw = Uint16Field(301, 1, Mode.RW, description="Load Start kWatts", units="kWatts")
    ags_load_start_delay = Uint16Field(302, 1, Mode.RW, description="Load Start Delay", units="Minutes")
    ags_load_stop_kw = Uint16Field(303, 1, Mode.RW, description="Load Stop kWatts", units="kWatts")
    ags_load_stop_delay = Uint16Field(304, 1, Mode.RW, description="Load Stop Delay", units="Minutes")
    ags_soc_start_mode = EnumUint16Field(305, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_soc_start_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_soc_start_percentage = Uint16Field(306, 1, Mode.RW, description="AGS SOC Start Percentage", units="Percent")
    ags_soc_stop_percentage = Uint16Field(307, 1, Mode.RW, description="AGS SOC Stop Percentage", units="Percent")
    ags_enable_full_charge_mode = EnumUint16Field(308, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_enable_full_charge_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_full_charge_interval = Uint16Field(309, 1, Mode.RW, description="AGS SOC Full Charge Interval", units="Days")
    ags_must_run_mode = EnumUint16Field(310, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_must_run_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_must_run_weekday_start_hour = Uint16Field(311, 1, Mode.RW, description="AGS Must Run Weekday Start Hour 0-23", units="Hour")
    ags_must_run_weekday_start_minute = Uint16Field(312, 1, Mode.RW, description="AGS Must Run Weekday Start Minute 0-59", units="Minute")
    ags_must_run_weekday_stop_hour = Uint16Field(313, 1, Mode.RW, description="AGS Must Run Weekday Stop Hour 0-23", units="Hour")
    ags_must_run_weekday_stop_minute = Uint16Field(314, 1, Mode.RW, description="AGS Must Run Weekday Stop Minute 0-59", units="Minute")
    ags_must_run_weekend_start_hour = Uint16Field(315, 1, Mode.RW, description="AGS Must Run Weekend Start Hour 0-23", units="Hour")
    ags_must_run_weekend_start_minute = Uint16Field(316, 1, Mode.RW, description="AGS Must Run Weekend Start Minute 0-59", units="Minute")
    ags_must_run_weekend_stop_hour = Uint16Field(317, 1, Mode.RW, description="AGS Must Run Weekend Stop Hour 0-23", units="Hour")
    ags_must_run_weekend_stop_minute = Uint16Field(318, 1, Mode.RW, description="AGS Must Run Weekend Stop Minute 0-59", units="Minute")
    ags_quiet_time_mode = EnumUint16Field(319, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_quiet_time_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_quiet_time_weekday_start_hour = Uint16Field(320, 1, Mode.RW, description="AGS Quiet Time Weekday Start Hour 0-23", units="Hour")
    ags_quiet_time_weekday_start_minute = Uint16Field(321, 1, Mode.RW, description="AGS Quiet Time Weekday Start Minute 0-59", units="Minute")
    ags_quiet_time_weekday_stop_hour = Uint16Field(322, 1, Mode.RW, description="AGS Quiet Time Weekday Stop Hour 0-23", units="Hour")
    ags_quiet_time_weekday_stop_minute = Uint16Field(323, 1, Mode.RW, description="AGS Quiet Time Weekday Stop Minute 0-59", units="Minute")
    ags_quiet_time_weekend_start_hour = Uint16Field(324, 1, Mode.RW, description="AGS Quiet Time Weekend Start Hour 0-23", units="Hour")
    ags_quiet_time_weekend_start_minute = Uint16Field(325, 1, Mode.RW, description="AGS Quiet Time Weekend Start Minute 0-59", units="Minute")
    ags_quiet_time_weekend_stop_hour = Uint16Field(326, 1, Mode.RW, description="AGS Quiet Time Weekend Stop Hour 0-23", units="Hour")
    ags_quiet_time_weekend_stop_minute = Uint16Field(327, 1, Mode.RW, description="AGS Quiet Time Weekend Stop Minute 0-59", units="Minute")
    ags_total_generator_run_time = Uint32Field(328, 2, Mode.RW, description="AGS Generator Total Run Time in Seconds", units="Hours")
    hbx_mode = EnumUint16Field(330, 1, Mode.RW, description="0=Disabled, 1=Voltage Only, 2=SOC Only, 3=Both", options=Enum("hbx_mode", [('Both', 3), ('Disabled', 0), ('SOC Only', 2), ('Voltage Only', 1)]))
    hbx_grid_connect_voltage = Uint16Field(331, 1, Mode.RW, description="HBX Grid Connect Voltage", units="Volts")
    hbx_grid_connect_delay = Uint16Field(332, 1, Mode.RW, description="HBX Grid Connect Delay", units="Hours")
    hbx_grid_disconnect_voltage = Uint16Field(333, 1, Mode.RW, description="HBX Grid Disconnect Voltage", units="Volts")
    hbx_grid_disconnect_delay = Uint16Field(334, 1, Mode.RW, description="HBX Grid Disconnect Delay", units="Hours")
    hbx_grid_connect_soc = Uint16Field(335, 1, Mode.RW, description="HBX Grid Connect SOC Percentage", units="Percent")
    hbx_grid_disconnect_soc = Uint16Field(336, 1, Mode.RW, description="HBX Grid Disconnect SOC Percentage", units="Percent")
    grid_use_interval_1_mode = EnumUint16Field(337, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("grid_use_interval_1_mode", [('Disabled', 0), ('Enabled', 1)]))
    grid_use_interval_1_weekday_start_hour = Uint16Field(338, 1, Mode.RW, description="Grid Use Interval 1 Weekday Start Hour 0-23", units="Hour")
    grid_use_interval_1_weekday_start_minute = Uint16Field(339, 1, Mode.RW, description="Grid Use Interval 1 Weekday Start Minute 0-59", units="Hour")
    grid_use_interval_1_weekday_stop_hour = Uint16Field(340, 1, Mode.RW, description="Grid Use Interval 1 Weekday Stop Hour 0-23", units="Hour")
    grid_use_interval_1_weekday_stop_minute = Uint16Field(341, 1, Mode.RW, description="Grid Use Interval 1 Weekday Stop Minute 0-59", units="Hour")
    grid_use_interval_1_weekend_start_hour = Uint16Field(342, 1, Mode.RW, description="Grid Use Interval 1 Weekend Start Hour 0-23", units="Hour")
    grid_use_interval_1_weekend_start_minute = Uint16Field(343, 1, Mode.RW, description="Grid Use Interval 1 Weekend Start Minute 0-59", units="Hour")
    grid_use_interval_1_weekend_stop_hour = Uint16Field(344, 1, Mode.RW, description="Grid Use Interval 1 Weekend Stop Hour 0-23", units="Hour")
    grid_use_interval_1_weekend_stop_minute = Uint16Field(345, 1, Mode.RW, description="Grid Use Interval 1 Weekend Stop Minute 0-59", units="Hour")
    grid_use_interval_2_mode = EnumUint16Field(346, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("grid_use_interval_2_mode", [('Disabled', 0), ('Enabled', 1)]))
    grid_use_interval_2_weekday_start_hour = Uint16Field(347, 1, Mode.RW, description="Grid Use Interval 2 Weekday Start Hour 0-23", units="Hour")
    grid_use_interval_2_weekday_start_minute = Uint16Field(348, 1, Mode.RW, description="Grid Use Interval 2 Weekday Start Minute 0-59", units="Hour")
    grid_use_interval_2_weekday_stop_hour = Uint16Field(349, 1, Mode.RW, description="Grid Use Interval 2 Weekday Stop Hour 0-23", units="Hour")
    grid_use_interval_2_weekday_stop_minute = Uint16Field(350, 1, Mode.RW, description="Grid Use Interval 2 Weekday Stop Minute 0-59", units="Hour")
    grid_use_interval_3_mode = EnumUint16Field(351, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("grid_use_interval_3_mode", [('Disabled', 0), ('Enabled', 1)]))
    grid_use_interval_3_weekday_start_hour = Uint16Field(352, 1, Mode.RW, description="Grid Use Interval 3 Weekday Start Hour 0-23", units="Hour")
    grid_use_interval_3_weekday_start_minute = Uint16Field(353, 1, Mode.RW, description="Grid Use Interval 3 Weekday Start Minute 0-59", units="Hour")
    grid_use_interval_3_weekday_stop_hour = Uint16Field(354, 1, Mode.RW, description="Grid Use Interval 3 Weekday Stop Hour 0-23", units="Hour")
    grid_use_interval_3_weekday_stop_minute = Uint16Field(355, 1, Mode.RW, description="Grid Use Interval 3 Weekday Stop Minute 0-59", units="Hour")
    load_grid_transfer_mode = EnumUint16Field(356, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("load_grid_transfer_mode", [('Disabled', 0), ('Enabled', 1)]))
    load_grid_transfer_threshold = Uint16Field(357, 1, Mode.RW, description="Load Grid Transfer Threshold kW", units="kWatts")
    load_grid_transfer_connect_delay = Uint16Field(358, 1, Mode.RW, description="Load Grid Transfer Connect Delay Seconds", units="Seconds")
    load_grid_transfer_disconnect_delay = Uint16Field(359, 1, Mode.RW, description="Load Grid Transfer Disconnect Delay Seconds", units="Seconds")
    load_grid_transfer_connect_battery_voltage = Uint16Field(360, 1, Mode.RW, description="Load Grid Transfer Low Battery Connect Voltage", units="Volts")
    load_grid_transfer_re_connect_battery_voltage = Uint16Field(361, 1, Mode.RW, description="Load Grid Transfer Low Battery Re-Connect Voltage", units="Volts")
    global_charger_control_mode = EnumUint16Field(362, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("global_charger_control_mode", [('Disabled', 0), ('Enabled', 1)]))
    global_charger_control_output_limit = Uint16Field(363, 1, Mode.RW, description="Global Charger Output Limit Amps", units="Amps")
    radian_ac_coupled_control_mode = EnumUint16Field(364, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("radian_ac_coupled_control_mode", [('Disabled', 0), ('Enabled', 1)]))
    radian_ac_coupled_aux_port = Uint16Field(365, 1, Mode.RW, description="Radian Inverter Port Number for AUX Control 0-10", units="Port")
    url_update_lock = Uint32Field(366, 2, Mode.W, description="Unlock Key", units="key")
    web_reporting_base_url = StringField(368, 20, Mode.RW, description="WEB Reporting Base URL")
    web_user_logged_in_status = EnumUint16Field(388, 1, Mode.RW, description="0=WEB User NOT logged in, 1=WEB user logged in", options=Enum("web_user_logged_in_status", [('WEB User NOT logged in', 0), ('WEB user logged in', 1)]))
    hub_type = EnumUint16Field(389, 1, Mode.R, description="0=Legecy HUB, 4= HUB4, 10=HUB10.3, 11=HUB3PH", options=Enum("hub_type", [('HUB10.3', 10), ('HUB3PH', 11), ('HUB4', 4), ('Legecy HUB', 0)]))
    hub_major_firmware_number = Uint16Field(390, 1, Mode.R, description="HUB Major firmware revision")
    hub_mid_firmware_number = Uint16Field(391, 1, Mode.R, description="HUB Mid firmware revision")
    hub_minor_firmware_number = Uint16Field(392, 1, Mode.R, description="HUB Minor firmware revision")
    year = Uint16Field(393, 1, Mode.RW, description="Clock year (4 digit)")
    month = Uint16Field(394, 1, Mode.RW, description="Clock Month (1 - 12)")
    day = Uint16Field(395, 1, Mode.RW, description="Clock Day (1 - 31)")
    hour = Uint16Field(396, 1, Mode.RW, description="Clock Hour (0 - 23)")
    minute = Uint16Field(397, 1, Mode.RW, description="Clock Minute (0 - 59)")
    second = Uint16Field(398, 1, Mode.RW, description="Clock Second (0 - 59)")
    temp_battery = Int16Field(399, 1, Mode.R, description="Battery temp in degrees C", units="Degrees C")
    temp_ambient = Int16Field(400, 1, Mode.R, description="Ambient temp from temp sensor connected to device, in degrees C", units="Degrees C")
    temp_scale_factor = Int16Field(401, 1, Mode.R, description="Temperature Scale Factor")
    error = Bit16Field(402, 1, Mode.R, description="Bit field for errors. See Outback_Error Table", flags=OutBackErrorFlags)
    status = Bit16Field(403, 1, Mode.R, description="Bit field for status.See Outback_Status Table", flags=OutBackStatusFlags)
    update_device_firmware_port = Bit16Field(404, 1, Mode.RW, description="Device Firmware update See Device_FW_Update", flags=OutBackUpdateDeviceFirmwarePortFlags)
    gateway_type = EnumUint16Field(405, 1, Mode.R, description="1=AXS Port, 2= MATE3", options=Enum("gateway_type", [('AXS Port', 1), ('MATE3', 2)]))
    system_voltage = Uint16Field(406, 1, Mode.R, description="12, 24, 26, 48 or 60 VDC", units="Volts")
    measured_system_voltage = Uint16Field(407, 1, Mode.R, description="Current system battery voltage computed by gateway", units="Volts")
    ags_ac_reconnect_delay = Uint16Field(408, 1, Mode.RW, description="AGS AC Reconnect Delay", units="Minute")
    multi_phase_coordination = EnumUint16Field(409, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("multi_phase_coordination", [('Disabled', 0), ('Enabled', 1)]))
    sched_1_ac_mode = EnumInt16Field(410, 1, Mode.RW, description="Scheduled Input Mode: -1=Disable, 0=Generator, 1=Support, 2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero", options=Enum("sched_1_ac_mode", [('Backup', 4), ('Disable', -1), ('Generator', 0), ('Grid Tied', 2), ('Grid Zero', 6), ('Mini Grid', 5), ('Support', 1), ('UPS', 3)]))
    sched_1_ac_mode_hour = Uint16Field(411, 1, Mode.RW, description="Start Hour for AC Input Mode schedule 1", units="Hour")
    sched_1_ac_mode_minute = Uint16Field(412, 1, Mode.RW, description="Start Minute for AC Input Mode schedule 1", units="Minute")
    sched_2_ac_mode = EnumInt16Field(413, 1, Mode.RW, description="Scheduled Input Mode: -1=Disable, 0=Generator, 1=Support, 2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero", options=Enum("sched_2_ac_mode", [('Backup', 4), ('Disable', -1), ('Generator', 0), ('Grid Tied', 2), ('Grid Zero', 6), ('Mini Grid', 5), ('Support', 1), ('UPS', 3)]))
    sched_2_ac_mode_hour = Uint16Field(414, 1, Mode.RW, description="Start Hour for AC Input Mode schedule 2", units="Hour")
    sched_2_ac_mode_minute = Uint16Field(415, 1, Mode.RW, description="Start Minute for AC Input Mode schedule 2", units="Minute")
    sched_3_ac_mode = EnumInt16Field(416, 1, Mode.RW, description="Scheduled Input Mode: -1=Disable, 0=Generator, 1=Support, 2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero", options=Enum("sched_3_ac_mode", [('Backup', 4), ('Disable', -1), ('Generator', 0), ('Grid Tied', 2), ('Grid Zero', 6), ('Mini Grid', 5), ('Support', 1), ('UPS', 3)]))
    sched_3_ac_mode_hour = Uint16Field(417, 1, Mode.RW, description="Start Hour for AC Input Mode schedule 3", units="Hour")
    sched_3_ac_mode_minute = Uint16Field(418, 1, Mode.RW, description="Start Minute for AC Input Mode schedule 3", units="Minute")
    auto_reboot = EnumUint16Field(419, 1, Mode.RW, description="OPTICS auto reboot every 24 hours 0=Disable, 1=Enable", options=Enum("auto_reboot", [('Disable', 0), ('Enable', 1)]))
    time_zone_scale_factor = Int16Field(420, 1, Mode.R, description="Time Zone scale factor")
    spare_reg_3 = Uint16Field(421, 1, Mode.RW, description="Spare Register 3")
    spare_reg_4 = Uint16Field(422, 1, Mode.RW, description="Spare Register 4")


OutBackModel.set_time_zone.value.scale_factor = OutBackModel.time_zone_scale_factor
OutBackModel.ags_dc_gen_absorb_voltage.value.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.ags_dc_gen_absorb_time.value.scale_factor = OutBackModel.hour_scale_factor
OutBackModel.ags_2_min_start_voltage.value.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.ags_2_hour_start_voltage.value.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.ags_24_hour_start_voltage.value.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.hbx_grid_connect_voltage.value.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.hbx_grid_connect_delay.value.scale_factor = OutBackModel.hour_scale_factor
OutBackModel.hbx_grid_disconnect_voltage.value.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.hbx_grid_disconnect_delay.value.scale_factor = OutBackModel.hour_scale_factor
OutBackModel.load_grid_transfer_threshold.value.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.load_grid_transfer_connect_battery_voltage.value.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.load_grid_transfer_re_connect_battery_voltage.value.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.measured_system_voltage.value.scale_factor = OutBackModel.voltage_scale_factor


@unique
class ChargeControllerModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Basic Charge Controller")
    length = Uint16Field(2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number = Uint16Field(3, 1, Mode.R, description="Port number on Outback network")
    voltage_scale_factor = Int16Field(4, 1, Mode.R, description="DC Voltage Scale Factor")
    current_scale_factor = Int16Field(5, 1, Mode.R, description="DC Current Scale Factor")
    power_scale_factor = Int16Field(6, 1, Mode.R, description="DC Power Scale Factor")
    ah_scale_factor = Int16Field(7, 1, Mode.R, description="DC Amp Hours Scale Factor")
    kwh_scale_factor = Int16Field(8, 1, Mode.R, description="DC kWH Scale Factor")
    battery_voltage = Uint16Field(9, 1, Mode.R, description="Battery Voltage", units="Volts")
    array_voltage = Uint16Field(10, 1, Mode.R, description="DC Source Voltage", units="Volts")
    battery_current = Uint16Field(11, 1, Mode.R, description="Battery Current", units="Amps")
    array_current = Uint16Field(12, 1, Mode.R, description="DC Source Current", units="Amps")
    charger_state = EnumUint16Field(13, 1, Mode.R, description="0 = Silent; 1 = Float; 2 = Bulk; 3 = Absorb; 4 = EQ", options=Enum("charger_state", [('Absorb;', 3), ('Bulk;', 2), ('EQ', 4), ('Float;', 1), ('Silent;', 0)]))
    watts = Uint16Field(14, 1, Mode.R, description="CC Wattage Output", units="Watts")
    todays_min_battery_volts = Uint16Field(15, 1, Mode.R, description="Minimum Voltage for battery today", units="Volts")
    todays_max_battery_volts = Uint16Field(16, 1, Mode.R, description="Maximum Voltage for battery today", units="Volts")
    voc = Uint16Field(17, 1, Mode.R, description="Last Open Circuit Voltage (array)", units="Volts")
    todays_peak_voc = Uint16Field(18, 1, Mode.R, description="Highest VOC today", units="Volts")
    todays_kwh = Uint16Field(19, 1, Mode.R, description="Daily accumulated Kwatt hours output", units="KWH")
    todays_ah = Uint16Field(20, 1, Mode.R, description="Daily accumulated amp hours output", units="AH")
    lifetime_kwh_hours = Uint16Field(21, 1, Mode.R, description="Lifetime Total Kwatt Hours", units="KWH")
    lifetime_k_amp_hours = Uint16Field(22, 1, Mode.R, description="Lifetime Total K-Amp Hours", units="Amps")
    lifetime_max_watts = Uint16Field(23, 1, Mode.R, description="Lifetime Maximum Wattage", units="Watts")
    lifetime_max_battery_volts = Uint16Field(24, 1, Mode.R, description="Lifetime Maximum Battery Voltage", units="Volts")
    lifetime_max_voc = Uint16Field(25, 1, Mode.R, description="Lifetime Maximum VOC", units="Volts")
    temp_scale_factor = Uint16Field(26, 1, Mode.R, description="FM80 Extreme Temperature scale factor")
    temp_output_fets = Int16Field(27, 1, Mode.R, description="FM80 Extreme Output FET Temperature", units="Degrees C")
    temp_enclosure = Int16Field(28, 1, Mode.R, description="FM80 Extreme Enclosure Temperature", units="Degrees C")


ChargeControllerModel.battery_voltage.value.scale_factor = ChargeControllerModel.voltage_scale_factor
ChargeControllerModel.array_voltage.value.scale_factor = ChargeControllerModel.voltage_scale_factor
ChargeControllerModel.battery_current.value.scale_factor = ChargeControllerModel.current_scale_factor
ChargeControllerModel.array_current.value.scale_factor = ChargeControllerModel.power_scale_factor
ChargeControllerModel.watts.value.scale_factor = ChargeControllerModel.power_scale_factor
ChargeControllerModel.todays_min_battery_volts.value.scale_factor = ChargeControllerModel.voltage_scale_factor
ChargeControllerModel.todays_max_battery_volts.value.scale_factor = ChargeControllerModel.voltage_scale_factor
ChargeControllerModel.voc.value.scale_factor = ChargeControllerModel.voltage_scale_factor
ChargeControllerModel.todays_kwh.value.scale_factor = ChargeControllerModel.kwh_scale_factor
ChargeControllerModel.todays_ah.value.scale_factor = ChargeControllerModel.ah_scale_factor
ChargeControllerModel.lifetime_k_amp_hours.value.scale_factor = ChargeControllerModel.kwh_scale_factor
ChargeControllerModel.lifetime_max_watts.value.scale_factor = ChargeControllerModel.power_scale_factor
ChargeControllerModel.lifetime_max_battery_volts.value.scale_factor = ChargeControllerModel.voltage_scale_factor
ChargeControllerModel.lifetime_max_voc.value.scale_factor = ChargeControllerModel.voltage_scale_factor
ChargeControllerModel.temp_output_fets.value.scale_factor = ChargeControllerModel.power_scale_factor
ChargeControllerModel.temp_enclosure.value.scale_factor = ChargeControllerModel.power_scale_factor


@unique
class ChargeControllerConfigurationModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Vendor Extension for OutBack FM Series Charge Controllers")
    length = Uint16Field(2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number = Uint16Field(3, 1, Mode.R, description="Port number on Outback network")
    voltage_scale_factor = Int16Field(4, 1, Mode.R, description="DC Voltage Scale Factor")
    current_scale_factor = Int16Field(5, 1, Mode.R, description="DC Current Scale Factor")
    hours_scale_factor = Int16Field(6, 1, Mode.R, description="Time in Hours Scale Factor")
    power_scale_factor = Int16Field(7, 1, Mode.R, description="Power Scale Factor")
    ah_scale_factor = Int16Field(8, 1, Mode.R, description="Amp Hours Scale Factor")
    kwh_scale_factor = Int16Field(9, 1, Mode.R, description="DC kWH Scale Factor")
    faults = Bit16Field(10, 1, Mode.R, description="CC Error Flags: 0x0080=High VOC, 0x0040=Over Temp,  0x0020=Shorted Battery Temp Sensor, 0x0010=Fault Input Active", flags=CCconfigFaultsFlags)
    absorb_volts = Uint16Field(11, 1, Mode.RW, description="Absorb Voltage Target", units="Volts")
    absorb_time_hours = Uint16Field(12, 1, Mode.RW, description="Absorb Time Hours", units="Hours")
    absorb_end_amps = Uint16Field(13, 1, Mode.RW, description="Amperage to end Absorbing", units="Amps")
    rebulk_volts = Uint16Field(14, 1, Mode.RW, description="Voltage to re-initiate Bulk charge", units="Volts")
    float_volts = Uint16Field(15, 1, Mode.RW, description="Float Voltage Target", units="Volts")
    bulk_current = Uint16Field(16, 1, Mode.RW, description="Max Output Current Limit", units="Amps")
    eq_volts = Uint16Field(17, 1, Mode.RW, description="Target Voltage for Equalize", units="Volts")
    eq_time_hours = Uint16Field(18, 1, Mode.RW, description="EQ Time Hours", units="Hours")
    auto_eq_days = Uint16Field(19, 1, Mode.RW, description="Auto EQ Interval Days", units="Days")
    mppt_mode = EnumUint16Field(20, 1, Mode.RW, description="0 = Auto; 1 = U-Pick", options=Enum("mppt_mode", [('Auto;', 0), ('U-Pick', 1)]))
    sweep_width = EnumUint16Field(21, 1, Mode.RW, description="0 = Full; 1 = Half", options=Enum("sweep_width", [('Full;', 0), ('Half', 1)]))
    sweep_max_percentage = EnumUint16Field(22, 1, Mode.RW, description="0 = 80; 1 = 85; 2 = 90; 3 = 99", options=Enum("sweep_max_percentage", [('80;', 0), ('85;', 1), ('90;', 2), ('99', 3)]))
    u_pick_pwm_duty_cycle = Uint16Field(23, 1, Mode.RW, description="Park Duty Cycle (%) (40% - 90%)", units="Percentage")
    grid_tie_mode = EnumUint16Field(24, 1, Mode.RW, description="0 = Grid Tie Mode disabled; 1 = Grid Tie Mode enabled", options=Enum("grid_tie_mode", [('Grid Tie Mode disabled;', 0), ('Grid Tie Mode enabled', 1)]))
    temp_comp_mode = EnumUint16Field(25, 1, Mode.RW, description="0 = Wide; 1 = User Limited", options=Enum("temp_comp_mode", [('User Limited', 1), ('Wide;', 0)]))
    temp_comp_lower_limit_volts = Uint16Field(26, 1, Mode.RW, description="RTS compensation lower voltage limit", units="Volts")
    temp_comp_upper_limit_volts = Uint16Field(27, 1, Mode.RW, description="RTS compensation upper voltage limit", units="Volts")
    temp_comp_slope = Uint16Field(28, 1, Mode.RW, description="RTS temp compensation Slope 2-6 mV per Degree C", units="Milli Volts")
    auto_restart_mode = EnumUint16Field(29, 1, Mode.RW, description="0 = Off; 1 = Restart every 90 minutes; 2 = Restart every 90 minutes if absorb charging or float charging", options=Enum("auto_restart_mode", [('Off;', 0), ('Restart every 90 minutes if absorb charging or float charging', 2), ('Restart every 90 minutes;', 1)]))
    wakeup_voc = Uint16Field(30, 1, Mode.RW, description="VOC change which causes Wakeup occurs", units="Volts")
    snooze_mode_amps = Uint16Field(31, 1, Mode.RW, description="Snooze Mode Amps", units="Amps")
    wakeup_interval = Uint16Field(32, 1, Mode.RW, description="How often to check for Wakeup condition", units="Mins")
    aux_mode = EnumUint16Field(33, 1, Mode.RW, description="0 = Float; 1 = Diversion: Relay; 2 = Diversion: Solid St; 3 = Low Batt Disconnect; 4 = Remote; 5 = Vent Fan; 6 = PV Trigger; 7 = Error Output; 8 = Night Light", options=Enum("aux_mode", [('Diversion: Relay;', 1), ('Diversion: Solid St;', 2), ('Error Output;', 7), ('Float;', 0), ('Low Batt Disconnect;', 3), ('Night Light', 8), ('PV Trigger;', 6), ('Remote;', 4), ('Vent Fan;', 5)]))
    aux_control = EnumUint16Field(34, 1, Mode.RW, description="0 = Off; 1 = Auto; 2 = On", options=Enum("aux_control", [('Auto;', 1), ('Off;', 0), ('On', 2)]))
    aux_state = EnumUint16Field(35, 1, Mode.R, description="0 = Disabled; 1 = Enabled", options=Enum("aux_state", [('Disabled;', 0), ('Enabled', 1)]))
    aux_polarity = EnumUint16Field(36, 1, Mode.RW, description="0 = Low; 1 = High", options=Enum("aux_polarity", [('High', 1), ('Low;', 0)]))
    aux_low_battery_disconnect = Uint16Field(37, 1, Mode.RW, description="Low Battery Disconnect Voltage", units="Volts")
    aux_low_battery_reconnect = Uint16Field(38, 1, Mode.RW, description="Low Battery Reconnect Volts", units="Volts")
    aux_low_battery_disconnect_delay = Uint16Field(39, 1, Mode.RW, description="Low Battery Disconnect Delay (secs)", units="Secs")
    aux_vent_fan_volts = Uint16Field(40, 1, Mode.RW, description="Vent Fan Voltage", units="Volts")
    aux_pv_limit_volts = Uint16Field(41, 1, Mode.RW, description="Voltage at which PV disconnect occurs", units="Volts")
    aux_pv_limit_hold_time = Uint16Field(42, 1, Mode.RW, description="AUX PV Trigger Hold Time", units="Secs")
    aux_night_light_thres_volts = Uint16Field(43, 1, Mode.RW, description="Voltage Threshold for AUX Night Light", units="Volts")
    night_light_on_hours = Uint16Field(44, 1, Mode.RW, description="Night Light ON Time", units="Hours")
    night_light_on_hyst_time = Uint16Field(45, 1, Mode.RW, description="Night Light ON Hyst Time", units="Mins")
    night_light_off_hyst_time = Uint16Field(46, 1, Mode.RW, description="Night Light OFF Hyst Time", units="Mins")
    aux_error_battery_volts = Uint16Field(47, 1, Mode.RW, description="Battery voltage at which Aux Error occurs", units="Volts")
    aux_divert_hold_time = Uint16Field(48, 1, Mode.RW, description="AUX Diver Hold Time", units="Seconds")
    aux_divert_delay_time = Uint16Field(49, 1, Mode.RW, description="AUX Divert Delay", units="Secs")
    aux_divert_relative_volts = Int16Field(50, 1, Mode.RW, description="AUX Divert Relative Volts", units="Volts")
    aux_divert_hyst_volts = Uint16Field(51, 1, Mode.RW, description="AUX Divert Hyst Volts", units="Volts")
    major_firmware_number = Uint16Field(52, 1, Mode.R, description="Charge Controller Major firmware revision")
    mid_firmware_number = Uint16Field(53, 1, Mode.R, description="Charge Controller Mid firmware revision")
    minor_firmware_number = Uint16Field(54, 1, Mode.R, description="Charge Controller Minor firmware revision")
    set_data_log_day_offset = Uint16Field(55, 1, Mode.RW, description="Day offset 0-128, 0 =Today, 1 = -1 day \u2026", units="Days")
    get_current_data_log_day_offset = Uint16Field(56, 1, Mode.R, description="Current Data Log Day Offset", units="Days")
    data_log_daily_ah = Uint16Field(57, 1, Mode.R, description="Data Log AH", units="AH")
    data_log_daily_kwh = Uint16Field(58, 1, Mode.R, description="Data Log kWH", units="KWH")
    data_log_daily_max_output_amps = Uint16Field(59, 1, Mode.R, description="Data Log maximum Output Amps", units="Amps")
    data_log_daily_max_output_watts = Uint16Field(60, 1, Mode.R, description="Data Log maximum Output Wattage", units="Watts")
    data_log_daily_absorb_time = Uint16Field(61, 1, Mode.R, description="Data Log Absorb Time Minutes", units="Mins")
    data_log_daily_float_time = Uint16Field(62, 1, Mode.R, description="Data Log Float Time Minutes", units="Mins")
    data_log_daily_min_battery_volts = Uint16Field(63, 1, Mode.R, description="Data Log minimum daily battery voltage", units="Volts")
    data_log_daily_max_battery_volts = Uint16Field(64, 1, Mode.R, description="Data Log maximum daily battery voltage", units="Volts")
    data_log_daily_max_input_volts = Uint16Field(65, 1, Mode.R, description="Data Log maximum daily input voltage", units="Volts")
    clear_data_log_read = Uint16Field(66, 1, Mode.R, description="Read value needed to clear data log")
    clear_data_log_write_complement = Uint16Field(67, 1, Mode.W, description="Write value's complement to clear data log")
    stats_maximum_reset_read = Uint16Field(68, 1, Mode.R, description="Read value needed to clear Stats Maximums")
    stats_maximum_write_complement = Uint16Field(69, 1, Mode.W, description="Write value's complement to clear Stats Maximums")
    stats_totals_reset_read = Uint16Field(70, 1, Mode.R, description="Read value nneded to clear Stats Totals")
    stats_totals_write_complement = Uint16Field(71, 1, Mode.W, description="Write value's complement to clear Stats Totals")
    battery_voltage_calibrate_offset = Int16Field(72, 1, Mode.RW, description="Battery voltage calibration offset", units="DC Volts")
    serial_number = StringField(73, 9, Mode.R, description="Device serial number")
    model_number = StringField(82, 9, Mode.R, description="Device model")


ChargeControllerConfigurationModel.absorb_volts.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.absorb_time_hours.value.scale_factor = ChargeControllerConfigurationModel.hours_scale_factor
ChargeControllerConfigurationModel.rebulk_volts.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.float_volts.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.bulk_current.value.scale_factor = ChargeControllerConfigurationModel.current_scale_factor
ChargeControllerConfigurationModel.eq_volts.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.u_pick_pwm_duty_cycle.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.temp_comp_lower_limit_volts.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.temp_comp_upper_limit_volts.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.wakeup_voc.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.snooze_mode_amps.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_low_battery_disconnect.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_low_battery_reconnect.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_vent_fan_volts.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_pv_limit_volts.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_pv_limit_hold_time.value.scale_factor = ChargeControllerConfigurationModel.hours_scale_factor
ChargeControllerConfigurationModel.aux_night_light_thres_volts.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_error_battery_volts.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_divert_hold_time.value.scale_factor = ChargeControllerConfigurationModel.hours_scale_factor
ChargeControllerConfigurationModel.aux_divert_relative_volts.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_divert_hyst_volts.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.data_log_daily_ah.value.scale_factor = ChargeControllerConfigurationModel.ah_scale_factor
ChargeControllerConfigurationModel.data_log_daily_kwh.value.scale_factor = ChargeControllerConfigurationModel.kwh_scale_factor
ChargeControllerConfigurationModel.data_log_daily_max_output_amps.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.data_log_daily_max_output_watts.value.scale_factor = ChargeControllerConfigurationModel.power_scale_factor
ChargeControllerConfigurationModel.data_log_daily_min_battery_volts.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.data_log_daily_max_battery_volts.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.battery_voltage_calibrate_offset.value.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor


@unique
class FXInverterRealTimeModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Vendor Extension for OutBack FX Series Inverter Status Block")
    length = Uint16Field(2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number = Uint16Field(3, 1, Mode.R, description="Port number on Outback network")
    dc_voltage_scale_factor = Int16Field(4, 1, Mode.R, description="DC Voltage Scale Factor")
    ac_current_scale_factor = Int16Field(5, 1, Mode.R, description="AC Current Scale Factor")
    ac_voltage_scale_factor = Int16Field(6, 1, Mode.R, description="AC Voltage Scale Factor")
    ac_frequency_scale_factor = Int16Field(7, 1, Mode.R, description="AC Frequency Scale Factor")
    inverter_output_current = Uint16Field(8, 1, Mode.R, description="Inverter output current", units="Amps")
    inverter_charge_current = Uint16Field(9, 1, Mode.R, description="Inverter charger current", units="Amps")
    inverter_buy_current = Uint16Field(10, 1, Mode.R, description="Inverter buy current", units="Amps")
    inverter_sell_current = Uint16Field(11, 1, Mode.R, description="Inverter sell current", units="Amps")
    output_ac_voltage = Uint16Field(12, 1, Mode.R, description="Output AC Voltage", units="Volts AC")
    inverter_operating_mode = EnumUint16Field(13, 1, Mode.R, description="0=Off, 1=Searching, 2=Inverting, 3=Charging, 4=Silent, 5=Float, 6=EQ, 7=Charger Off, 8=Support, 9=Selling, 10=Pass through, 14=Offsetting", options=Enum("inverter_operating_mode", [('Charger Off', 7), ('Charging', 3), ('EQ', 6), ('Float', 5), ('Inverting', 2), ('Off', 0), ('Offsetting', 14), ('Pass through', 10), ('Searching', 1), ('Selling', 9), ('Silent', 4), ('Support', 8)]))
    error_flags = Bit16Field(14, 1, Mode.R, description="Bit field for errors. See FX_Error Table", flags=FXErrorFlags)
    warning_flags = Bit16Field(15, 1, Mode.R, description="Bit field for warnings See FX_Warning Table", flags=FXWarningFlags)
    battery_voltage = Uint16Field(16, 1, Mode.R, description="Battery Voltage", units="Volts DC")
    temp_compensated_target_voltage = Uint16Field(17, 1, Mode.R, description="Temperature compensated target battery voltage", units="Volts DC")
    aux_output_state = EnumUint16Field(18, 1, Mode.R, description="0 = Disabled; 1 = Enabled", options=Enum("aux_output_state", [('Disabled;', 0), ('Enabled', 1)]))
    transformer_temperature = Int16Field(19, 1, Mode.R, description="Transformer temp in degrees C", units="Degrees C")
    capacitor_temperature = Int16Field(20, 1, Mode.R, description="Capacitor temp in degrees C", units="Degrees C")
    fet_temperature = Int16Field(21, 1, Mode.R, description="FET temp in degrees C", units="Degrees C")
    ac_input_frequency = Uint16Field(22, 1, Mode.R, description="Selected AC Input frequency HZ", units="Hz")
    ac_input_voltage = Uint16Field(23, 1, Mode.R, description="Selected Input AC Voltage", units="Volts AC")
    ac_input_state = EnumUint16Field(24, 1, Mode.R, description="1=AC Use, 0=AC_Drop", options=Enum("ac_input_state", [('AC Use', 1), ('AC_Drop', 0)]))
    minimum_ac_input_voltage = Uint16Field(25, 1, Mode.R, description="Minimum Input AC Voltage (Write to clear value)", units="Volts AC")
    maximum_ac_input_voltage = Uint16Field(26, 1, Mode.R, description="Maximum Input AC Voltage (Write to clear value)", units="Volts AC")
    sell_status = Bit16Field(27, 1, Mode.R, description="Bit field for sell status See FX_Sell_Status Table", flags=FXSellStatusFlags)
    kwh_scale_factor = Int16Field(28, 1, Mode.R, description="AC kWh scale factor")
    buy_kwh = Uint16Field(29, 1, Mode.R, description="Daily Buy kWh", units="kWh")
    sell_kwh = Uint16Field(30, 1, Mode.R, description="Daily Sell kWh", units="kWh")
    output_kwh = Uint16Field(31, 1, Mode.R, description="Daily Output kWh", units="kWh")
    charger_kwh = Uint16Field(32, 1, Mode.R, description="Daily Charger kWh", units="kWh")
    output_kw = Uint16Field(33, 1, Mode.R, description="Output kW", units="kW")
    buy_kw = Uint16Field(34, 1, Mode.R, description="Buy kW", units="kW")
    sell_kw = Uint16Field(35, 1, Mode.R, description="Sell kW", units="kW")
    charge_kw = Uint16Field(36, 1, Mode.R, description="Charge kW", units="kW")
    load_kw = Uint16Field(37, 1, Mode.R, description="Load kW", units="kW")
    ac_couple_kw = Uint16Field(38, 1, Mode.R, description="AC Coupled kW", units="kW")


FXInverterRealTimeModel.inverter_output_current.value.scale_factor = FXInverterRealTimeModel.ac_current_scale_factor
FXInverterRealTimeModel.inverter_charge_current.value.scale_factor = FXInverterRealTimeModel.ac_current_scale_factor
FXInverterRealTimeModel.inverter_buy_current.value.scale_factor = FXInverterRealTimeModel.ac_current_scale_factor
FXInverterRealTimeModel.inverter_sell_current.value.scale_factor = FXInverterRealTimeModel.ac_current_scale_factor
FXInverterRealTimeModel.output_ac_voltage.value.scale_factor = FXInverterRealTimeModel.ac_voltage_scale_factor
FXInverterRealTimeModel.battery_voltage.value.scale_factor = FXInverterRealTimeModel.dc_voltage_scale_factor
FXInverterRealTimeModel.temp_compensated_target_voltage.value.scale_factor = FXInverterRealTimeModel.dc_voltage_scale_factor
FXInverterRealTimeModel.ac_input_frequency.value.scale_factor = FXInverterRealTimeModel.ac_frequency_scale_factor
FXInverterRealTimeModel.ac_input_voltage.value.scale_factor = FXInverterRealTimeModel.ac_voltage_scale_factor
FXInverterRealTimeModel.minimum_ac_input_voltage.value.scale_factor = FXInverterRealTimeModel.ac_voltage_scale_factor
FXInverterRealTimeModel.maximum_ac_input_voltage.value.scale_factor = FXInverterRealTimeModel.ac_voltage_scale_factor
FXInverterRealTimeModel.buy_kwh.value.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.sell_kwh.value.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.output_kwh.value.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.charger_kwh.value.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.output_kw.value.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.buy_kw.value.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.sell_kw.value.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.charge_kw.value.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.load_kw.value.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.ac_couple_kw.value.scale_factor = FXInverterRealTimeModel.kwh_scale_factor


@unique
class FXInverterConfigurationModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Vendor Extension for OutBack FX Series Inverter  Configuration Block")
    length = Uint16Field(2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number = Uint16Field(3, 1, Mode.R, description="Port number on Outback network")
    dc_voltage_scale_factor = Int16Field(4, 1, Mode.R, description="DC Voltage Scale Factor")
    ac_current_scale_factor = Int16Field(5, 1, Mode.R, description="AC Current Scale Factor")
    ac_voltage_scale_factor = Int16Field(6, 1, Mode.R, description="AC Voltage Scale Factor")
    time_scale_factor = Int16Field(7, 1, Mode.R, description="Time Scale Factor")
    major_firmware_number = Uint16Field(8, 1, Mode.R, description="Inverter Major firmware revision")
    mid_firmware_number = Uint16Field(9, 1, Mode.R, description="Inverter Mid firmware revision")
    minor_firmware_number = Uint16Field(10, 1, Mode.R, description="Inverter Minor firmware revision")
    absorb_volts = Uint16Field(11, 1, Mode.RW, description="Absorb Voltage Target", units="DC Volts")
    absorb_time_hours = Uint16Field(12, 1, Mode.RW, description="Absorb Time Hours", units="Hours")
    float_volts = Uint16Field(13, 1, Mode.RW, description="Float Voltage Target", units="DC Volts")
    float_time_hours = Uint16Field(14, 1, Mode.RW, description="Float Time Hours", units="Hours")
    re_float_volts = Uint16Field(15, 1, Mode.RW, description="ReFloat Voltage Target", units="DC Volts")
    eq_volts = Uint16Field(16, 1, Mode.RW, description="EQ Voltage Target", units="DC Volts")
    eq_time_hours = Uint16Field(17, 1, Mode.RW, description="EQ Time Hours", units="Hours")
    search_sensitivity = Uint16Field(18, 1, Mode.RW, description="Search sensitivity")
    search_pulse_length = Uint16Field(19, 1, Mode.RW, description="Search pulse length", units="Cycles")
    search_pulse_spacing = Uint16Field(20, 1, Mode.RW, description="Search pulse spacing", units="Cycles")
    ac_input_type = EnumUint16Field(21, 1, Mode.RW, description="0=Grid, 1=Gen, 2=Grid Zero", options=Enum("ac_input_type", [('Gen', 1), ('Grid', 0), ('Grid Zero', 2)]))
    input_support = EnumUint16Field(22, 1, Mode.RW, description="1=Yes, 0=No (only valid if AC Input Type is Gen)", options=Enum("input_support", [('No (only valid if AC Input Type is Gen)', 0), ('Yes', 1)]))
    grid_ac_input_current_limit = Uint16Field(23, 1, Mode.RW, description="Grid AC input current limit", units="Amps")
    gen_ac_input_current_limit = Uint16Field(24, 1, Mode.RW, description="Gen AC input current limit", units="Amps")
    charger_ac_input_current_limit = Uint16Field(25, 1, Mode.RW, description="Charger AC input current limit", units="Amps")
    charger_operating_mode = EnumUint16Field(26, 1, Mode.RW, description="0=Charger Off, 1=Charger Auto, 2=Charger On", options=Enum("charger_operating_mode", [('Charger Auto', 1), ('Charger Off', 0), ('Charger On', 2)]))
    grid_lower_input_voltage_limit = Uint16Field(27, 1, Mode.RW, description="Grid Input AC voltage lower limit", units="Volts AC")
    grid_upper_input_voltage_limit = Uint16Field(28, 1, Mode.RW, description="Grid Input AC voltage upper limit", units="Volts AC")
    grid_transfer_delay = Uint16Field(29, 1, Mode.RW, description="Grid Input AC connect delay", units="Minutes")
    gen_lower_input_voltage_limit = Uint16Field(30, 1, Mode.RW, description="Gen Input AC voltage lower limit", units="Volts AC")
    gen_upper_input_voltage_limit = Uint16Field(31, 1, Mode.RW, description="Gen Input AC voltage upper limit", units="Volts AC")
    gen_transfer_delay = Uint16Field(32, 1, Mode.RW, description="Gen Input AC transfer delay", units="Cycles")
    gen_connect_delay = Uint16Field(33, 1, Mode.RW, description="Gen Input AC connect delay", units="Minutes")
    ac_output_voltage = Uint16Field(34, 1, Mode.RW, description="AC output Voltage", units="Volts AC")
    low_battery_cut_out_voltage = Uint16Field(35, 1, Mode.RW, description="Battery cut-out voltage", units="DC Volts")
    low_battery_cut_in_voltage = Uint16Field(36, 1, Mode.RW, description="Battery cut-in voltage", units="DC Volts")
    aux_mode = EnumUint16Field(37, 1, Mode.RW, description="0=Remote, 1=Load Shed, 2=Gen Alert, 3=Fault, 4=Vent Fan, 5=Cool Fan, 6=Divert DC, 7=Divert AC, 8=AC Drop", options=Enum("aux_mode", [('AC Drop', 8), ('Cool Fan', 5), ('Divert AC', 7), ('Divert DC', 6), ('Fault', 3), ('Gen Alert', 2), ('Load Shed', 1), ('Remote', 0), ('Vent Fan', 4)]))
    aux_control = EnumUint16Field(38, 1, Mode.RW, description="0 = Off; 1 = Auto; 2 = On", options=Enum("aux_control", [('Auto;', 1), ('Off;', 0), ('On', 2)]))
    aux_load_shed_enable_voltage = Uint16Field(39, 1, Mode.RW, description="Load Shed enable voltage", units="DC Volts")
    aux_gen_alert_on_voltage = Uint16Field(40, 1, Mode.RW, description="Gen Alert On voltage", units="DC Volts")
    aux_gen_alert_on_delay = Uint16Field(41, 1, Mode.RW, description="Gen Alert On delay minutes", units="Minutes")
    aux_gen_alert_off_voltage = Uint16Field(42, 1, Mode.RW, description="Gen Alert Off voltage", units="DC Volts")
    aux_gen_alert_off_delay = Uint16Field(43, 1, Mode.RW, description="Gen Alert Off delay minutes", units="Minutes")
    aux_vent_fan_enable_voltage = Uint16Field(44, 1, Mode.RW, description="Vent Fan enable voltage", units="DC Volts")
    aux_vent_fan_off_period = Uint16Field(45, 1, Mode.RW, description="Van Fan Off delay minutes", units="Minutes")
    aux_divert_enable_voltage = Uint16Field(46, 1, Mode.RW, description="DC Divert enable voltage", units="DC Volts")
    aux_divert_off_delay = Uint16Field(47, 1, Mode.RW, description="Divert Off delay minutes", units="Minutes")
    stacking_mode = EnumUint16Field(48, 1, Mode.RW, description="0=1-2phase Master, 1=Classic Slave, 2=OB Slave L1, 3=OB Slave L2, 4=3phase Master, 5=3phase Slave,10=Master, 11=Classic Slave, 12=OB Slave L1, 13=OB Slave L2, 14=3phase OB Slave A, 15=3phase OB Slave B, 16=3phase OB Slave C, 17=3phase Classic B, 18=3phase Classic C, 19=Independent", options=Enum("stacking_mode", [('1-2phase Master', 0), ('3phase Classic B', 17), ('3phase Classic C', 18), ('3phase Master', 4), ('3phase OB Slave A', 14), ('3phase OB Slave B', 15), ('3phase OB Slave C', 16), ('3phase Slave', 5), ('CLASSIC_SLAVE_11', 11), ('Classic Slave', 1), ('Independent', 19), ('Master', 10), ('OB Slave L1', 2), ('OB Slave L2', 3), ('OB_SLAVE_L1_12', 12), ('OB_SLAVE_L2_13', 13)]))
    master_power_save_level = Uint16Field(49, 1, Mode.RW, description="Master inverter power save level")
    slave_power_save_level = Uint16Field(50, 1, Mode.RW, description="Slave inverter power save level")
    sell_volts = Uint16Field(51, 1, Mode.RW, description="Sell Voltage Target", units="DC Volts")
    grid_tie_window = EnumUint16Field(52, 1, Mode.RW, description="0=IEEE, 1=User", options=Enum("grid_tie_window", [('IEEE', 0), ('User', 1)]))
    grid_tie_enable = EnumUint16Field(53, 1, Mode.RW, description="1=Yes, 0=No", options=Enum("grid_tie_enable", [('No', 0), ('Yes', 1)]))
    ac_input_voltage_calibrate_factor = Int16Field(54, 1, Mode.RW, description="AC input voltage calibration factor", units="Volts AC")
    ac_output_voltage_calibrate_factor = Int16Field(55, 1, Mode.RW, description="AC output voltage calibration factor", units="Volts AC")
    battery_voltage_calibrate_factor = Int16Field(56, 1, Mode.RW, description="Battery voltage calibration factor", units="DC Volts")
    serial_number = StringField(57, 9, Mode.R, description="Device serial number")
    model_number = StringField(66, 9, Mode.R, description="Device model")


FXInverterConfigurationModel.absorb_volts.value.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.absorb_time_hours.value.scale_factor = FXInverterConfigurationModel.time_scale_factor
FXInverterConfigurationModel.float_volts.value.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.float_time_hours.value.scale_factor = FXInverterConfigurationModel.time_scale_factor
FXInverterConfigurationModel.re_float_volts.value.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.eq_volts.value.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.eq_time_hours.value.scale_factor = FXInverterConfigurationModel.time_scale_factor
FXInverterConfigurationModel.grid_ac_input_current_limit.value.scale_factor = FXInverterConfigurationModel.ac_current_scale_factor
FXInverterConfigurationModel.gen_ac_input_current_limit.value.scale_factor = FXInverterConfigurationModel.ac_current_scale_factor
FXInverterConfigurationModel.charger_ac_input_current_limit.value.scale_factor = FXInverterConfigurationModel.ac_current_scale_factor
FXInverterConfigurationModel.grid_lower_input_voltage_limit.value.scale_factor = FXInverterConfigurationModel.ac_voltage_scale_factor
FXInverterConfigurationModel.grid_upper_input_voltage_limit.value.scale_factor = FXInverterConfigurationModel.ac_voltage_scale_factor
FXInverterConfigurationModel.gen_lower_input_voltage_limit.value.scale_factor = FXInverterConfigurationModel.ac_voltage_scale_factor
FXInverterConfigurationModel.gen_upper_input_voltage_limit.value.scale_factor = FXInverterConfigurationModel.ac_voltage_scale_factor
FXInverterConfigurationModel.gen_connect_delay.value.scale_factor = FXInverterConfigurationModel.time_scale_factor
FXInverterConfigurationModel.ac_output_voltage.value.scale_factor = FXInverterConfigurationModel.ac_voltage_scale_factor
FXInverterConfigurationModel.low_battery_cut_out_voltage.value.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.low_battery_cut_in_voltage.value.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.aux_load_shed_enable_voltage.value.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.aux_gen_alert_on_voltage.value.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.aux_gen_alert_off_voltage.value.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.aux_vent_fan_enable_voltage.value.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.aux_divert_enable_voltage.value.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.sell_volts.value.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.battery_voltage_calibrate_factor.value.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor


@unique
class SplitPhaseRadianInverterRealTimeModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Vendor Extension for OutBack Radian Series Split Phase Inverter Status Block")
    length = Uint16Field(2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number = Uint16Field(3, 1, Mode.R, description="Port number on Outback network")
    dc_voltage_scale_factor = Int16Field(4, 1, Mode.R, description="DC Voltage Scale Factor")
    ac_current_scale_factor = Int16Field(5, 1, Mode.R, description="AC Current Scale Factor")
    ac_voltage_scale_factor = Int16Field(6, 1, Mode.R, description="AC Voltage Scale Factor")
    ac_frequency_scale_factor = Int16Field(7, 1, Mode.R, description="AC Frequency Scale Factor")
    l1_inverter_output_current = Int16Field(8, 1, Mode.R, description="L1 inverter output current", units="Amps")
    l1_inverter_charge_current = Int16Field(9, 1, Mode.R, description="L1 inverter charger current", units="Amps")
    l1_inverter_buy_current = Int16Field(10, 1, Mode.R, description="L1 inverter buy current", units="Amps")
    l1_inverter_sell_current = Int16Field(11, 1, Mode.R, description="L1 inverter sell current", units="Amps")
    l1_grid_input_ac_voltage = Int16Field(12, 1, Mode.R, description="L1 Grid Input AC Voltage", units="Volts AC")
    l1_gen_input_ac_voltage = Int16Field(13, 1, Mode.R, description="L1 Gen Input AC Voltage", units="Volts AC")
    l1_output_ac_voltage = Int16Field(14, 1, Mode.R, description="L1 Output AC Voltage", units="Volts AC")
    l2_inverter_output_current = Int16Field(15, 1, Mode.R, description="L2 inverter output current", units="Amps")
    l2_inverter_charge_current = Int16Field(16, 1, Mode.R, description="L2 inverter charger current", units="Amps")
    l2_inverter_buy_current = Int16Field(17, 1, Mode.R, description="L2 inverter buy current", units="Amps")
    l2_inverter_sell_current = Int16Field(18, 1, Mode.R, description="L2 inverter sell current", units="Amps")
    l2_grid_input_ac_voltage = Int16Field(19, 1, Mode.R, description="L2 Grid Input AC Voltage", units="Volts AC")
    l2_gen_input_ac_voltage = Int16Field(20, 1, Mode.R, description="L2 Gen Input AC Voltage", units="Volts AC")
    l2_output_ac_voltage = Int16Field(21, 1, Mode.R, description="L2 Output AC Voltage", units="Volts AC")
    inverter_operating_mode = EnumInt16Field(22, 1, Mode.R, description="0=Off, 1=Searching, 2=Inverting, 3=Charging, 4=Silent, 5=Float, 6=EQ, 7=Charger Off, 8=Support, 9=Selling, 10=Pass through, 14=Offsetting", options=Enum("inverter_operating_mode", [('Charger Off', 7), ('Charging', 3), ('EQ', 6), ('Float', 5), ('Inverting', 2), ('Off', 0), ('Offsetting', 14), ('Pass through', 10), ('Searching', 1), ('Selling', 9), ('Silent', 4), ('Support', 8)]))
    error_flags = Bit16Field(23, 1, Mode.R, description="Bit field for errors. See GS_Error table", flags=GSSplitErrorFlags)
    warning_flags = Bit16Field(24, 1, Mode.R, description="Bit field for warnings See GS_Warning table", flags=GSSplitWarningFlags)
    battery_voltage = Int16Field(25, 1, Mode.R, description="Battery Voltage", units="Volts DC")
    temp_compensated_target_voltage = Int16Field(26, 1, Mode.R, description="Temperature compensated target battery voltage", units="Volts DC")
    aux_output_state = EnumInt16Field(27, 1, Mode.R, description="0 = Disabled; 1 = Enabled", options=Enum("aux_output_state", [('Disabled;', 0), ('Enabled', 1)]))
    aux_relay_output_state = EnumInt16Field(28, 1, Mode.R, description="0 = Disabled; 1 = Enabled", options=Enum("aux_relay_output_state", [('Disabled;', 0), ('Enabled', 1)]))
    l_module_transformer_temperature = Int16Field(29, 1, Mode.R, description="Left module transformer temp in degrees C", units="Degrees C")
    l_module_capacitor_temperature = Int16Field(30, 1, Mode.R, description="Left module capacitor temp in degrees C", units="Degrees C")
    l_module_fet_temperature = Int16Field(31, 1, Mode.R, description="Left module FET temp in degrees C", units="Degrees C")
    r_module_transformer_temperature = Int16Field(32, 1, Mode.R, description="Right module transformer temp in degrees C", units="Degrees C")
    r_module_capacitor_temperature = Int16Field(33, 1, Mode.R, description="Right module capacitor temp in degrees C", units="Degrees C")
    r_module_fet_temperature = Int16Field(34, 1, Mode.R, description="Right module FET temp in degrees C", units="Degrees C")
    battery_temperature = Int16Field(35, 1, Mode.R, description="Battery temp in degrees C", units="Degrees C")
    ac_input_selection = EnumInt16Field(36, 1, Mode.R, description="0=Grid, 1=Gen", options=Enum("ac_input_selection", [('Gen', 1), ('Grid', 0)]))
    ac_input_frequency = Int16Field(37, 1, Mode.R, description="Selected AC Input frequency HZ", units="Hz")
    ac_input_voltage = Int16Field(38, 1, Mode.R, description="Selected Input AC Voltage", units="Volts AC")
    ac_input_state = EnumInt16Field(39, 1, Mode.R, description="1=AC Use, 0=AC_Drop", options=Enum("ac_input_state", [('AC Use', 1), ('AC_Drop', 0)]))
    minimum_ac_input_voltage = Int16Field(40, 1, Mode.R, description="Minimum Input AC Voltage (Write to clear stored value)", units="Volts AC")
    maximum_ac_input_voltage = Int16Field(41, 1, Mode.R, description="Maximum Input AC Voltage (Write to clear stored value)", units="Volts AC")
    sell_status = Bit16Field(42, 1, Mode.R, description="Bit field for sell status See GS_Sell_Status table", flags=GSSplitSellStatusFlags)
    kwh_scale_factor = Int16Field(43, 1, Mode.R, description="AC kWh scale factor")
    ac1_l1_buy_kwh = Uint16Field(44, 1, Mode.R, description="Daily AC1 Buy L1 kWh", units="kWh")
    ac2_l1_buy_kwh = Uint16Field(45, 1, Mode.R, description="Daily AC2 Buy L1 kWh", units="kWh")
    ac1_l1_sell_kwh = Uint16Field(46, 1, Mode.R, description="Daily AC1 Sell L1 kWh", units="kWh")
    ac2_l1_sell_kwh = Uint16Field(47, 1, Mode.R, description="Daily AC2 Sell L1 kWh", units="kWh")
    l1_output_kwh = Uint16Field(48, 1, Mode.R, description="Daily Output L1 kWh", units="kWh")
    ac1_l2_buy_kwh = Uint16Field(49, 1, Mode.R, description="Daily AC1 Buy L2 kWh", units="kWh")
    ac2_l2_buy_kwh = Uint16Field(50, 1, Mode.R, description="Daily AC1 Sell L2 kWh", units="kWh")
    ac1_l2_sell_kwh = Uint16Field(51, 1, Mode.R, description="Daily AC1 Sell L2 kWh", units="kWh")
    ac2_l2_sell_kwh = Uint16Field(52, 1, Mode.R, description="Daily AC2 Sell L2 kWh", units="kWh")
    l2_output_kwh = Uint16Field(53, 1, Mode.R, description="Daily Output L2 kWh", units="kWh")
    charger_kwh = Uint16Field(54, 1, Mode.R, description="Daily Charger kWh", units="kWh")
    output_kw = Uint16Field(55, 1, Mode.R, description="Output kW", units="kW")
    buy_kw = Uint16Field(56, 1, Mode.R, description="Buy kW", units="kW")
    sell_kw = Uint16Field(57, 1, Mode.R, description="Sell kW", units="kW")
    charge_kw = Uint16Field(58, 1, Mode.R, description="Charge kW", units="kW")
    load_kw = Uint16Field(59, 1, Mode.R, description="Load kW", units="kW")
    ac_couple_kw = Uint16Field(60, 1, Mode.R, description="AC Coupled kW", units="kW")
    gt_number = Uint16Field(61, 1, Mode.R, description="GT Number sent from Inverter to Charge Controller")


SplitPhaseRadianInverterRealTimeModel.l1_inverter_output_current.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l1_inverter_charge_current.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l1_inverter_buy_current.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l1_inverter_sell_current.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l1_grid_input_ac_voltage.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.l1_gen_input_ac_voltage.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.l1_output_ac_voltage.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_inverter_output_current.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_inverter_charge_current.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_inverter_buy_current.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_inverter_sell_current.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_grid_input_ac_voltage.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_gen_input_ac_voltage.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_output_ac_voltage.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.battery_voltage.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.dc_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.temp_compensated_target_voltage.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.dc_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac_input_frequency.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_frequency_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac_input_voltage.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.minimum_ac_input_voltage.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.maximum_ac_input_voltage.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac1_l1_buy_kwh.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac2_l1_buy_kwh.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac1_l1_sell_kwh.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac2_l1_sell_kwh.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.l1_output_kwh.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac1_l2_buy_kwh.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac2_l2_buy_kwh.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac1_l2_sell_kwh.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac2_l2_sell_kwh.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_output_kwh.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.charger_kwh.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.output_kw.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.buy_kw.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.sell_kw.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.charge_kw.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.load_kw.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac_couple_kw.value.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor


@unique
class RadianInverterConfigurationModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Vendor Extension for OutBack Radian Series Split Phase Inverter  Configuration Block")
    length = Uint16Field(2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number = Uint16Field(3, 1, Mode.R, description="Port number on Outback network")
    dc_voltage_scale_factor = Int16Field(4, 1, Mode.R, description="DC Voltage Scale Factor")
    ac_current_scale_factor = Int16Field(5, 1, Mode.R, description="AC Current Scale Factor")
    ac_voltage_scale_factor = Int16Field(6, 1, Mode.R, description="AC Voltage Scale Factor")
    time_scale_factor = Int16Field(7, 1, Mode.R, description="Time Scale Factor")
    major_firmware_number = Uint16Field(8, 1, Mode.R, description="Inverter Major firmware revision")
    mid_firmware_number = Uint16Field(9, 1, Mode.R, description="Inverter Mid firmware revision")
    minor_firmware_number = Uint16Field(10, 1, Mode.R, description="Inverter Minor firmware revision")
    absorb_volts = Uint16Field(11, 1, Mode.RW, description="Absorb Voltage Target", units="DC Volts")
    absorb_time_hours = Uint16Field(12, 1, Mode.RW, description="Absorb Time Hours", units="Hours")
    float_volts = Uint16Field(13, 1, Mode.RW, description="Float Voltage Target", units="DC Volts")
    float_time_hours = Uint16Field(14, 1, Mode.RW, description="Float Time Hours", units="Hours")
    re_float_volts = Uint16Field(15, 1, Mode.RW, description="ReFloat Voltage Target", units="DC Volts")
    eq_volts = Uint16Field(16, 1, Mode.RW, description="EQ Voltage Target", units="DC Volts")
    eq_time_hours = Uint16Field(17, 1, Mode.RW, description="EQ Time Hours", units="Hours")
    search_sensitivity = Uint16Field(18, 1, Mode.RW, description="Search sensitivity")
    search_pulse_length = Uint16Field(19, 1, Mode.RW, description="Search pulse length", units="Cycles")
    search_pulse_spacing = Uint16Field(20, 1, Mode.RW, description="Search pulse spacing", units="Cycles")
    ac_input_select_priority = EnumUint16Field(21, 1, Mode.RW, description="0=Grid, 1=Gen", options=Enum("ac_input_select_priority", [('Gen', 1), ('Grid', 0)]))
    grid_ac_input_current_limit = Uint16Field(22, 1, Mode.RW, description="Grid AC input current limit", units="Amps")
    gen_ac_input_current_limit = Uint16Field(23, 1, Mode.RW, description="Gen AC input current limit", units="Amps")
    charger_ac_input_current_limit = Uint16Field(24, 1, Mode.RW, description="Charger AC input current limit", units="Amps")
    charger_operating_mode = EnumUint16Field(25, 1, Mode.RW, description="0=All Inverter Charging Disabled, 1=Bulk and Float Charging Enabled", options=Enum("charger_operating_mode", [('All Inverter Charging Disabled', 0), ('Bulk and Float Charging Enabled', 1)]))
    ac_coupled = EnumUint16Field(26, 1, Mode.R, description="0=No, 1=Yes", options=Enum("ac_coupled", [('No', 0), ('Yes', 1)]))
    grid_input_mode = EnumUint16Field(27, 1, Mode.RW, description="Grid Input Mode: 0=Generator, 1=Support, 2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero", options=Enum("grid_input_mode", [('Backup', 4), ('Generator', 0), ('Grid Tied', 2), ('Grid Zero', 6), ('Mini Grid', 5), ('Support', 1), ('UPS', 3)]))
    grid_lower_input_voltage_limit = Uint16Field(28, 1, Mode.RW, description="Grid Input AC voltage lower limit", units="Volts AC")
    grid_upper_input_voltage_limit = Uint16Field(29, 1, Mode.RW, description="Grid Input AC voltage upper limit", units="Volts AC")
    grid_transfer_delay = Uint16Field(30, 1, Mode.RW, description="Grid Input AC transfer delay", units="msecs")
    grid_connect_delay = Uint16Field(31, 1, Mode.RW, description="Grid Input AC connect delay", units="Minutes")
    gen_input_mode = EnumUint16Field(32, 1, Mode.RW, description="Grid Input Mode: 0=Generator, 1=Support, 2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero", options=Enum("gen_input_mode", [('Backup', 4), ('Generator', 0), ('Grid Tied', 2), ('Grid Zero', 6), ('Mini Grid', 5), ('Support', 1), ('UPS', 3)]))
    gen_lower_input_voltage_limit = Uint16Field(33, 1, Mode.RW, description="Gen Input AC voltage lower limit", units="Volts AC")
    gen_upper_input_voltage_limit = Uint16Field(34, 1, Mode.RW, description="Gen Input AC voltage upper limit", units="Volts AC")
    gen_transfer_delay = Uint16Field(35, 1, Mode.RW, description="Gen Input AC transfer delay", units="msecs")
    gen_connect_delay = Uint16Field(36, 1, Mode.RW, description="Gen Input AC connect delay", units="Minutes")
    ac_output_voltage = Uint16Field(37, 1, Mode.RW, description="AC output Voltage", units="Volts AC")
    low_battery_cut_out_voltage = Uint16Field(38, 1, Mode.RW, description="Battery cut-out voltage", units="DC Volts")
    low_battery_cut_in_voltage = Uint16Field(39, 1, Mode.RW, description="Battery cut-in voltage", units="DC Volts")
    aux_mode = EnumUint16Field(40, 1, Mode.RW, description="1=Load Shed, 2=Gen Alert, 3=Fault, 4=Vent Fan, 5=Cool Fan, 6=DC Divert, 7=Grid Limit/IEEE ,8=AC Source Status,9=AC Divert", options=Enum("aux_mode", [('AC Divert', 9), ('AC Source Status', 8), ('Cool Fan', 5), ('DC Divert', 6), ('Fault', 3), ('Gen Alert', 2), ('Grid Limit/IEEE ', 7), ('Load Shed', 1), ('Vent Fan', 4)]))
    aux_control = EnumUint16Field(41, 1, Mode.RW, description="0 = Off; 1 = Auto; 2 = On", options=Enum("aux_control", [('Auto;', 1), ('Off;', 0), ('On', 2)]))
    aux_on_battery_voltage = Uint16Field(42, 1, Mode.RW, description="AUX ON battery voltage", units="DC Volts")
    aux_on_delay_time = Uint16Field(43, 1, Mode.RW, description="AUX ON Delay", units="Minutes")
    aux_off_battery_voltage = Uint16Field(44, 1, Mode.RW, description="AUX OFF battery voltage", units="DC Volts")
    aux_off_delay_time = Uint16Field(45, 1, Mode.RW, description="AUX OFF Delay", units="Minutes")
    aux_relay_mode = EnumUint16Field(46, 1, Mode.RW, description="1=Load Shed, 2=Gen Alert, 3=Fault, 4=Vent Fan, 5=Cool Fan, 6=DC Divert, 7=Grid Limit/IEEE ,8=AC Source Status,9=AC Divert", options=Enum("aux_relay_mode", [('AC Divert', 9), ('AC Source Status', 8), ('Cool Fan', 5), ('DC Divert', 6), ('Fault', 3), ('Gen Alert', 2), ('Grid Limit/IEEE ', 7), ('Load Shed', 1), ('Vent Fan', 4)]))
    aux_relay_control = EnumUint16Field(47, 1, Mode.RW, description="0 = Off; 1 = On; 2 = Auto", options=Enum("aux_relay_control", [('Auto', 2), ('Off;', 0), ('On;', 1)]))
    aux_relay_on_battery_voltage = Uint16Field(48, 1, Mode.RW, description="AUX Relay ON battery voltage", units="DC Volts")
    aux_relay_on_delay_time = Uint16Field(49, 1, Mode.RW, description="AUX Relay ON Delay", units="Minutes")
    aux_relay_off_battery_voltage = Uint16Field(50, 1, Mode.RW, description="AUX Relay OFF battery voltage", units="DC Volts")
    aux_relay_off_delay_time = Uint16Field(51, 1, Mode.RW, description="AUX Relay OFF Delay", units="Minutes")
    stacking_mode = EnumUint16Field(52, 1, Mode.RW, description="10=Master, 12=Slave, 17=B Phase Master, 18=C Phase Master", options=Enum("stacking_mode", [('B Phase Master', 17), ('C Phase Master', 18), ('Master', 10), ('Slave', 12)]))
    master_power_save_level = Uint16Field(53, 1, Mode.RW, description="Master inverter power save level")
    slave_power_save_level = Uint16Field(54, 1, Mode.RW, description="Slave inverter power save level")
    sell_volts = Uint16Field(55, 1, Mode.RW, description="Sell Voltage Target", units="DC Volts")
    grid_tie_window = EnumUint16Field(56, 1, Mode.RW, description="0=IEEE, 1=User (GS8048 Only)", options=Enum("grid_tie_window", [('IEEE', 0), ('User (GS8048 Only)', 1)]))
    grid_tie_enable = EnumUint16Field(57, 1, Mode.RW, description="1=Yes, 0=No", options=Enum("grid_tie_enable", [('No', 0), ('Yes', 1)]))
    grid_ac_input_voltage_calibrate_factor = Int16Field(58, 1, Mode.RW, description="Grid AC input voltage calibration factor", units="Volts AC")
    gen_ac_input_voltage_calibrate_factor = Int16Field(59, 1, Mode.RW, description="Gen AC input voltage calibration factor", units="Volts AC")
    ac_output_voltage_calibrate_factor = Int16Field(60, 1, Mode.RW, description="AC output voltage calibration factor", units="Volts AC")
    battery_voltage_calibrate_factor = Int16Field(61, 1, Mode.RW, description="Battery voltage calibration factor", units="DC Volts")
    re_bulk_volts = Uint16Field(62, 1, Mode.RW, description="ReBulk Voltage Target", units="DC Volts")
    mini_grid_lbx_volts = Uint16Field(63, 1, Mode.RW, description="Mini Grid LBX reconnect to Grid Battery Voltage", units="DC Volts")
    mini_grid_lbx_delay = Uint16Field(64, 1, Mode.RW, description="Mini Grid LBX reconnect to Grid Delay Time", units="Hours")
    grid_zero_do_d_volts = Uint16Field(65, 1, Mode.RW, description="Grid Zero DoD Voltage", units="DC Volts")
    grid_zero_do_d_max_offset_ac_amps = Uint16Field(66, 1, Mode.RW, description="Grid Zero Maximum Offset AC Amps", units="Amps")
    serial_number = StringField(67, 9, Mode.R, description="Device serial number")
    model_number = StringField(76, 9, Mode.R, description="Device model")
    module_control = EnumUint16Field(85, 1, Mode.RW, description="0=Auto, 1=Left, 2=Right, 3=Both", options=Enum("module_control", [('Auto', 0), ('Both', 3), ('Left', 1), ('Right', 2)]))
    model_select = EnumUint16Field(86, 1, Mode.RW, description="0=Full, 1=Half", options=Enum("model_select", [('Full', 0), ('Half', 1)]))
    low_battery_cut_out_delay = Uint16Field(87, 1, Mode.RW, description="Low Battery Cut Out Delay", units="Seconds xx.x")
    high_battery_cut_out_voltage = Uint16Field(88, 1, Mode.RW, description="High Battery Cut Out Voltage", units="DC Volts")
    high_battery_cut_in_voltage = Uint16Field(89, 1, Mode.RW, description="High Battery Cut In Voltage", units="DC Volts")
    high_battery_cut_out_delay = Uint16Field(90, 1, Mode.RW, description="High Battery Cut Out Delay", units="Seconds xx.x")
    ee_write_enable = EnumUint16Field(91, 1, Mode.RW, description="EEPROM Write Enable 1= Enable, 0= Disable", options=Enum("ee_write_enable", [('Disable', 0), ('Enable', 1)]))


RadianInverterConfigurationModel.absorb_volts.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.absorb_time_hours.value.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.float_volts.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.float_time_hours.value.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.re_float_volts.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.eq_volts.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.eq_time_hours.value.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.grid_ac_input_current_limit.value.scale_factor = RadianInverterConfigurationModel.ac_current_scale_factor
RadianInverterConfigurationModel.gen_ac_input_current_limit.value.scale_factor = RadianInverterConfigurationModel.ac_current_scale_factor
RadianInverterConfigurationModel.charger_ac_input_current_limit.value.scale_factor = RadianInverterConfigurationModel.ac_current_scale_factor
RadianInverterConfigurationModel.grid_lower_input_voltage_limit.value.scale_factor = RadianInverterConfigurationModel.ac_voltage_scale_factor
RadianInverterConfigurationModel.grid_upper_input_voltage_limit.value.scale_factor = RadianInverterConfigurationModel.ac_voltage_scale_factor
RadianInverterConfigurationModel.grid_connect_delay.value.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.gen_lower_input_voltage_limit.value.scale_factor = RadianInverterConfigurationModel.ac_voltage_scale_factor
RadianInverterConfigurationModel.gen_upper_input_voltage_limit.value.scale_factor = RadianInverterConfigurationModel.ac_voltage_scale_factor
RadianInverterConfigurationModel.gen_connect_delay.value.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.ac_output_voltage.value.scale_factor = RadianInverterConfigurationModel.ac_voltage_scale_factor
RadianInverterConfigurationModel.low_battery_cut_out_voltage.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.low_battery_cut_in_voltage.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.aux_on_battery_voltage.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.aux_on_delay_time.value.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.aux_off_battery_voltage.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.aux_off_delay_time.value.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.aux_relay_on_battery_voltage.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.aux_relay_on_delay_time.value.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.aux_relay_off_battery_voltage.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.aux_relay_off_delay_time.value.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.sell_volts.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.battery_voltage_calibrate_factor.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.re_bulk_volts.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.mini_grid_lbx_volts.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.grid_zero_do_d_volts.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.grid_zero_do_d_max_offset_ac_amps.value.scale_factor = RadianInverterConfigurationModel.ac_current_scale_factor
RadianInverterConfigurationModel.low_battery_cut_out_delay.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.high_battery_cut_out_voltage.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.high_battery_cut_in_voltage.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.high_battery_cut_out_delay.value.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor


@unique
class SinglePhaseRadianInverterRealTimeModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Vendor Extension for OutBack Radian Series Split Phase Inverter Status Block")
    length = Uint16Field(2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number = Uint16Field(3, 1, Mode.R, description="Port number on Outback network")
    dc_voltage_scale_factor = Int16Field(4, 1, Mode.R, description="DC Voltage Scale Factor")
    ac_current_scale_factor = Int16Field(5, 1, Mode.R, description="AC Current Scale Factor")
    ac_voltage_scale_factor = Int16Field(6, 1, Mode.R, description="AC Voltage Scale Factor")
    ac_frequency_scale_factor = Int16Field(7, 1, Mode.R, description="AC Frequency Scale Factor")
    inverter_output_current = Uint16Field(8, 1, Mode.R, description="Inverter output current", units="Amps")
    inverter_charge_current = Uint16Field(9, 1, Mode.R, description="Inverter charger current", units="Amps")
    inverter_buy_current = Uint16Field(10, 1, Mode.R, description="Inverter buy current", units="Amps")
    inverter_sell_current = Uint16Field(11, 1, Mode.R, description="Inverter sell current", units="Amps")
    grid_input_ac_voltage = Uint16Field(12, 1, Mode.R, description="Grid Input AC Voltage", units="Volts AC")
    gen_input_ac_voltage = Uint16Field(13, 1, Mode.R, description="Gen Input AC Voltage", units="Volts AC")
    output_ac_voltage = Uint16Field(14, 1, Mode.R, description="Output AC Voltage", units="Volts AC")
    inverter_operating_mode = EnumUint16Field(15, 1, Mode.R, description="0=Off, 1=Searching, 2=Inverting, 3=Charging, 4=Silent, 5=Float, 6=EQ, 7=Charger Off, 8=Support, 9=Selling, 10=Pass through, 14=Offsetting", options=Enum("inverter_operating_mode", [('Charger Off', 7), ('Charging', 3), ('EQ', 6), ('Float', 5), ('Inverting', 2), ('Off', 0), ('Offsetting', 14), ('Pass through', 10), ('Searching', 1), ('Selling', 9), ('Silent', 4), ('Support', 8)]))
    error_flags = Bit16Field(16, 1, Mode.R, description="Bit field for errors. See GS_Error Table", flags=GSSingleErrorFlags)
    warning_flags = Bit16Field(17, 1, Mode.R, description="Bit field for warnings See GS_Warning Table", flags=GSSingleWarningFlags)
    battery_voltage = Uint16Field(18, 1, Mode.R, description="Battery Voltage", units="Volts DC")
    temp_compensated_target_voltage = Uint16Field(19, 1, Mode.R, description="Temperature compensated target battery voltage", units="Volts DC")
    aux_output_state = EnumUint16Field(20, 1, Mode.R, description="0 = Disabled; 1 = Enabled", options=Enum("aux_output_state", [('Disabled;', 0), ('Enabled', 1)]))
    aux_relay_output_state = EnumUint16Field(21, 1, Mode.R, description="0 = Disabled; 1 = Enabled", options=Enum("aux_relay_output_state", [('Disabled;', 0), ('Enabled', 1)]))
    l_module_transformer_temperature = Int16Field(22, 1, Mode.R, description="Left module transformer temp in degrees C", units="Degrees C")
    l_module_capacitor_temperature = Int16Field(23, 1, Mode.R, description="Left module capacitor temp in degrees C", units="Degrees C")
    l_module_fet_temperature = Int16Field(24, 1, Mode.R, description="Left module FET temp in degrees C", units="Degrees C")
    r_module_transformer_temperature = Int16Field(25, 1, Mode.R, description="Right module transformer temp in degrees C", units="Degrees C")
    r_module_capacitor_temperature = Int16Field(26, 1, Mode.R, description="Right module capacitor temp in degrees C", units="Degrees C")
    r_module_fet_temperature = Int16Field(27, 1, Mode.R, description="Right module FET temp in degrees C", units="Degrees C")
    battery_temperature = Int16Field(28, 1, Mode.R, description="Battery temp in degrees C", units="Degrees C")
    ac_input_selection = EnumUint16Field(29, 1, Mode.R, description="0=Grid, 1=Gen", options=Enum("ac_input_selection", [('Gen', 1), ('Grid', 0)]))
    ac_input_frequency = Uint16Field(30, 1, Mode.R, description="Selected AC Input frequency HZ", units="Hz")
    ac_input_voltage = Uint16Field(31, 1, Mode.R, description="Selected Input AC Voltage", units="Volts AC")
    ac_input_state = EnumUint16Field(32, 1, Mode.R, description="1=AC Use, 0=AC_Drop", options=Enum("ac_input_state", [('AC Use', 1), ('AC_Drop', 0)]))
    minimum_ac_input_voltage = Uint16Field(33, 1, Mode.R, description="Minimum Input AC Voltage (Write to clear value)", units="Volts AC")
    maximum_ac_input_voltage = Uint16Field(34, 1, Mode.R, description="Maximum Input AC Voltage (Write to clear value)", units="Volts AC")
    sell_status = Bit16Field(35, 1, Mode.R, description="Bit field for sell status See GS_Sell_Status Table", flags=GSSingleSellStatusFlags)
    kwh_scale_factor = Int16Field(36, 1, Mode.R, description="AC kWh scale factor")
    ac1_buy_kwh = Uint16Field(37, 1, Mode.R, description="Daily AC1 Buy kWh", units="kWh")
    ac2_buy_kwh = Uint16Field(38, 1, Mode.R, description="Daily AC2 Buy kWh", units="kWh")
    ac1_sell_kwh = Uint16Field(39, 1, Mode.R, description="Daily AC1 Sell kWh", units="kWh")
    ac2_sell_kwh = Uint16Field(40, 1, Mode.R, description="Daily AC2 Sell kWh", units="kWh")
    output_kwh = Uint16Field(41, 1, Mode.R, description="Daily Output kWh", units="kWh")
    charger_kwh = Uint16Field(42, 1, Mode.R, description="Daily Charger kWh", units="kWh")
    output_kw = Uint16Field(43, 1, Mode.R, description="Output kW", units="kW")
    buy_kw = Uint16Field(44, 1, Mode.R, description="Buy kW", units="kW")
    sell_kw = Uint16Field(45, 1, Mode.R, description="Sell kW", units="kW")
    charge_kw = Uint16Field(46, 1, Mode.R, description="Charger kW", units="kW")
    load_kw = Uint16Field(47, 1, Mode.R, description="Load kW", units="kW")
    ac_couple_kw = Uint16Field(48, 1, Mode.R, description="AC Coupled kW", units="kW")
    gt_number = Uint16Field(49, 1, Mode.R, description="GT Number sent from Inverter to Charge Controller")


SinglePhaseRadianInverterRealTimeModel.inverter_output_current.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_current_scale_factor
SinglePhaseRadianInverterRealTimeModel.inverter_charge_current.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_current_scale_factor
SinglePhaseRadianInverterRealTimeModel.inverter_buy_current.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_current_scale_factor
SinglePhaseRadianInverterRealTimeModel.inverter_sell_current.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_current_scale_factor
SinglePhaseRadianInverterRealTimeModel.grid_input_ac_voltage.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.gen_input_ac_voltage.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.output_ac_voltage.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.battery_voltage.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.dc_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.temp_compensated_target_voltage.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.dc_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.ac_input_frequency.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_frequency_scale_factor
SinglePhaseRadianInverterRealTimeModel.ac_input_voltage.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.minimum_ac_input_voltage.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.maximum_ac_input_voltage.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.ac1_buy_kwh.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.ac2_buy_kwh.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.ac1_sell_kwh.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.ac2_sell_kwh.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.output_kwh.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.charger_kwh.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.output_kw.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.buy_kw.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.sell_kw.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.charge_kw.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.load_kw.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.ac_couple_kw.value.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor


@unique
class FLEXnetDCRealTimeModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Vendor Extension for OutBack FLEXnet DC Battery Monitor Status Block")
    length = Uint16Field(2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number = Uint16Field(3, 1, Mode.R, description="Port number on Outback network")
    dc_voltage_scale_factor = Int16Field(4, 1, Mode.R, description="DC Voltage Scale Factor")
    dc_current_scale_factor = Int16Field(5, 1, Mode.R, description="DC Current Scale Factor")
    time_scale_factor = Int16Field(6, 1, Mode.R, description="Time Scale Factor")
    kwh_scale_factor = Int16Field(7, 1, Mode.R, description="Kilo Watt Hours Scale Factor")
    kw_scale_factor = Int16Field(8, 1, Mode.R, description="Kilo Watt Scale Factor")
    shunt_a_current = Int16Field(9, 1, Mode.R, description="Shunt A current", units="Amps")
    shunt_b_current = Int16Field(10, 1, Mode.R, description="Shunt B current", units="Amps")
    shunt_c_current = Int16Field(11, 1, Mode.R, description="Shunt C current", units="Amps")
    battery_voltage = Uint16Field(12, 1, Mode.R, description="Battery Voltage", units="Volts")
    battery_current = Int16Field(13, 1, Mode.R, description="Battery Current", units="Amps")
    battery_temperature = Int16Field(14, 1, Mode.R, description="Battery Temperature C", units="Degrees C")
    status_flags = Bit16Field(15, 1, Mode.R, description="See FN Status Table", flags=FNStatusFlags)
    shunt_a_accumulated_ah = Int16Field(16, 1, Mode.R, description="Shunt A Accumulated_AH", units="AH")
    shunt_a_accumulated_kwh = Int16Field(17, 1, Mode.R, description="Shunt A Accumulated_kWh", units="kWh")
    shunt_b_accumulated_ah = Int16Field(18, 1, Mode.R, description="Shunt B Accumulated_AH", units="AH")
    shunt_b_accumulated_kwh = Int16Field(19, 1, Mode.R, description="Shunt B Accumulated_kWh", units="kWh")
    shunt_c_accumulated_ah = Int16Field(20, 1, Mode.R, description="Shunt C Accumulated_AH", units="AH")
    shunt_c_accumulated_kwh = Int16Field(21, 1, Mode.R, description="Shunt C Accumulated_kWh", units="kWh")
    input_current = Uint16Field(22, 1, Mode.R, description="Total_input_current", units="Amps")
    output_current = Uint16Field(23, 1, Mode.R, description="Total_output_current", units="Amps")
    input_kw = Uint16Field(24, 1, Mode.R, description="Total_input_kWatts", units="kW")
    output_kw = Uint16Field(25, 1, Mode.R, description="Total_output_kWatts", units="kW")
    net_kw = Int16Field(26, 1, Mode.R, description="Total_net_kWatts", units="kW")
    days_since_charge_parameters_met = Uint16Field(27, 1, Mode.R, description="Days Since Charge Parameters Met", units="Days")
    state_of_charge = Uint16Field(28, 1, Mode.R, description="Current Battery State of Charge", units="Percent")
    todays_minimum_soc = Uint16Field(29, 1, Mode.R, description="Todays minimum SOC", units="Percent")
    todays_maximum_soc = Uint16Field(30, 1, Mode.R, description="Todays maximum SOC", units="Percent")
    todays_net_input_ah = Uint16Field(31, 1, Mode.R, description="Todays NET input AH", units="AH")
    todays_net_input_kwh = Uint16Field(32, 1, Mode.R, description="Todays NET input kWh", units="kWh")
    todays_net_output_ah = Uint16Field(33, 1, Mode.R, description="Todays NET output AH", units="AH")
    todays_net_output_kwh = Uint16Field(34, 1, Mode.R, description="Todays NET output kWh", units="kWh")
    todays_net_battery_ah = Int16Field(35, 1, Mode.R, description="Todays NET battery AH", units="AH")
    todays_net_battery_kwh = Int16Field(36, 1, Mode.R, description="Todays NET battery kWh", units="kWh")
    charge_factor_corrected_net_battery_ah = Int16Field(37, 1, Mode.R, description="Charge factor corrected NET battery AH", units="AH")
    charge_factor_corrected_net_battery_kwh = Int16Field(38, 1, Mode.R, description="Charge factor corrected NET battery kWh", units="kWh")
    todays_minimum_battery_voltage = Uint16Field(39, 1, Mode.R, description="Todays minimum battery voltage", units="Volts")
    todays_minimum_battery_time = Uint32Field(40, 2, Mode.R, description="Todays minimum battery voltage time UTC", units="Seconds")
    todays_maximum_battery_voltage = Uint16Field(42, 1, Mode.R, description="Todays maximum battery voltage", units="Volts")
    todays_maximum_battery_time = Uint32Field(43, 2, Mode.R, description="Todays maximum battery voltage time UTC", units="Seconds")
    cycle_charge_factor = Uint16Field(45, 1, Mode.R, description="Cycle Charge Factor", units="Percent")
    cycle_kwh_charge_efficiency = Uint16Field(46, 1, Mode.R, description="Cycle kWh Charge Efficiency", units="Percent")
    total_days_at_100_percent = Uint16Field(47, 1, Mode.R, description="Total days at 100% charged", units="Days")
    lifetime_k_ah_removed = Uint16Field(48, 1, Mode.R, description="Lifetime kAH removed from battery", units="AH")
    shunt_a_historical_returned_to_battery_ah = Uint16Field(49, 1, Mode.R, description="Shunt A historical returned to battery AH", units="AH")
    shunt_a_historical_returned_to_battery_kwh = Uint16Field(50, 1, Mode.R, description="Shunt A historical returned to battery kWh", units="kWh")
    shunt_a_historical_removed_from_battery_ah = Uint16Field(51, 1, Mode.R, description="Shunt A historical removed from battery AH", units="AH")
    shunt_a_historical_removed_from_battery_kwh = Uint16Field(52, 1, Mode.R, description="Shunt A historical removed from battery kWh", units="kWh")
    shunt_a_maximum_charge_rate = Uint16Field(53, 1, Mode.R, description="Shunt A historical maximum charge rate Amps", units="Amps")
    shunt_a_maximum_charge_rate_kw = Uint16Field(54, 1, Mode.R, description="Shunt A historical maximum charge rate kW", units="kW")
    shunt_a_maximum_discharge_rate = Int16Field(55, 1, Mode.R, description="Shunt A historical maximum discharge rate Amps", units="Amps")
    shunt_a_maximum_discharge_rate_kw = Int16Field(56, 1, Mode.R, description="Shunt A historical maximum discharge rate kW", units="kW")
    shunt_b_historical_returned_to_battery_ah = Uint16Field(57, 1, Mode.R, description="Shunt B historical returned to battery AH", units="AH")
    shunt_b_historical_returned_to_battery_kwh = Uint16Field(58, 1, Mode.R, description="Shunt B historical returned to battery kWh", units="kWh")
    shunt_b_historical_removed_from_battery_ah = Uint16Field(59, 1, Mode.R, description="Shunt B historical removed from battery AH", units="AH")
    shunt_b_historical_removed_from_battery_kwh = Uint16Field(60, 1, Mode.R, description="Shunt B historical removed from battery kWh", units="kWh")
    shunt_b_maximum_charge_rate = Uint16Field(61, 1, Mode.R, description="Shunt B historical maximum charge rate Amps", units="Amps")
    shunt_b_maximum_charge_rate_kw = Uint16Field(62, 1, Mode.R, description="Shunt B historical maximum charge rate kW", units="kW")
    shunt_b_maximum_discharge_rate = Int16Field(63, 1, Mode.R, description="Shunt B historical maximum discharge rate Amps", units="Amps")
    shunt_b_maximum_discharge_rate_kw = Int16Field(64, 1, Mode.R, description="Shunt B historical maximum discharge rate kW", units="kW")
    shunt_c_historical_returned_to_battery_ah = Uint16Field(65, 1, Mode.R, description="Shunt C historical returned to battery AH", units="AH")
    shunt_c_historical_returned_to_battery_kwh = Uint16Field(66, 1, Mode.R, description="Shunt C historical returned to battery kWh", units="kWh")
    shunt_c_historical_removed_from_battery_ah = Uint16Field(67, 1, Mode.R, description="Shunt C historical removed from battery AH", units="AH")
    shunt_c_historical_removed_from_battery_kwh = Uint16Field(68, 1, Mode.R, description="Shunt C historical removed from battery kWh", units="kWh")
    shunt_c_maximum_charge_rate = Uint16Field(69, 1, Mode.R, description="Shunt C historical maximum charge rate Amps", units="Amps")
    shunt_c_maximum_charge_rate_kw = Uint16Field(70, 1, Mode.R, description="Shunt C historical maximum charge rate kW", units="kW")
    shunt_c_maximum_discharge_rate = Int16Field(71, 1, Mode.R, description="Shunt C historical maximum discharge rate Amps", units="Amps")
    shunt_c_maximum_discharge_rate_kw = Int16Field(72, 1, Mode.R, description="Shunt C historical maximum discharge rate kW", units="kW")
    shunt_a_reset_maximum_data = Uint16Field(73, 1, Mode.R, description="Read value needed to reset shunt A maximum data")
    shunt_a_reset_maximum_data_write_complement = Uint16Field(74, 1, Mode.W, description="Write value's complement to reset shunt A maximum data")
    shunt_b_reset_maximum_data = Uint16Field(75, 1, Mode.R, description="Read value needed to reset shunt B maximum data")
    shunt_b_reset_maximum_data_write_complement = Uint16Field(76, 1, Mode.W, description="Write value's complement to reset shunt B maximum data")
    shunt_c_reset_maximum_data = Uint16Field(77, 1, Mode.R, description="Read value needed to reset shunt C maximum data")
    shunt_c_reset_maximum_data_write_complement = Uint16Field(78, 1, Mode.W, description="Write value's complement to reset shunt C maximum data")


FLEXnetDCRealTimeModel.shunt_a_current.value.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_b_current.value.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_c_current.value.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.battery_voltage.value.scale_factor = FLEXnetDCRealTimeModel.dc_voltage_scale_factor
FLEXnetDCRealTimeModel.battery_current.value.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_a_accumulated_kwh.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_b_accumulated_kwh.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_c_accumulated_kwh.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.input_current.value.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.output_current.value.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.input_kw.value.scale_factor = FLEXnetDCRealTimeModel.kw_scale_factor
FLEXnetDCRealTimeModel.output_kw.value.scale_factor = FLEXnetDCRealTimeModel.kw_scale_factor
FLEXnetDCRealTimeModel.net_kw.value.scale_factor = FLEXnetDCRealTimeModel.kw_scale_factor
FLEXnetDCRealTimeModel.days_since_charge_parameters_met.value.scale_factor = FLEXnetDCRealTimeModel.time_scale_factor
FLEXnetDCRealTimeModel.todays_net_input_kwh.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.todays_net_output_kwh.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.todays_net_battery_kwh.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.charge_factor_corrected_net_battery_kwh.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.todays_minimum_battery_voltage.value.scale_factor = FLEXnetDCRealTimeModel.dc_voltage_scale_factor
FLEXnetDCRealTimeModel.todays_maximum_battery_voltage.value.scale_factor = FLEXnetDCRealTimeModel.dc_voltage_scale_factor
FLEXnetDCRealTimeModel.total_days_at_100_percent.value.scale_factor = FLEXnetDCRealTimeModel.time_scale_factor
FLEXnetDCRealTimeModel.shunt_a_historical_returned_to_battery_kwh.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_a_historical_removed_from_battery_kwh.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_a_maximum_charge_rate.value.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_a_maximum_charge_rate_kw.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_a_maximum_discharge_rate.value.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_a_maximum_discharge_rate_kw.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_b_historical_returned_to_battery_kwh.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_b_historical_removed_from_battery_kwh.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_b_maximum_charge_rate.value.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_b_maximum_charge_rate_kw.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_b_maximum_discharge_rate.value.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_b_maximum_discharge_rate_kw.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_c_historical_returned_to_battery_kwh.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_c_historical_removed_from_battery_kwh.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_c_maximum_charge_rate.value.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_c_maximum_charge_rate_kw.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_c_maximum_discharge_rate.value.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_c_maximum_discharge_rate_kw.value.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor


@unique
class FLEXnetDCConfigurationModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Vendor Extension for OutBack FLEXnet-DC Battery Monitor Configuration Block")
    length = Uint16Field(2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number = Uint16Field(3, 1, Mode.R, description="Port number on OutBack network")
    dc_voltage_scale_factor = Int16Field(4, 1, Mode.R, description="DC Voltage Scale Factor")
    dc_current_scale_factor = Int16Field(5, 1, Mode.R, description="DC Current Scale Factor")
    kwh_scale_factor = Int16Field(6, 1, Mode.R, description="Kilo Watt Hours Scale Factor")
    major_firmware_number = Uint16Field(7, 1, Mode.R, description="FLEXnet-DC Major firmware revision")
    mid_firmware_number = Uint16Field(8, 1, Mode.R, description="FLEXnet-DC Mid firmware revision")
    minor_firmware_number = Uint16Field(9, 1, Mode.R, description="FLEXnet-DC Minor firmware revision")
    battery_capacity = Uint16Field(10, 1, Mode.RW, description="Battery AH capacity", units="AH")
    charged_volts = Uint16Field(11, 1, Mode.RW, description="Battery Charged Voltage", units="DC Volts")
    charged_time = Uint16Field(12, 1, Mode.RW, description="Battery Charged Time Minutes", units="Minutes")
    battery_charged_amps = Uint16Field(13, 1, Mode.RW, description="Battery Charged Return Amps", units="Amps")
    charge_factor = Uint16Field(14, 1, Mode.RW, description="Battery Charge Factor", units="Percent")
    shunt_a_enabled = EnumUint16Field(15, 1, Mode.RW, description="0=Enabled, 1=Disabled", options=Enum("shunt_a_enabled", [('Disabled', 1), ('Enabled', 0)]))
    shunt_b_enabled = EnumUint16Field(16, 1, Mode.RW, description="0=Enabled, 1=Disabled", options=Enum("shunt_b_enabled", [('Disabled', 1), ('Enabled', 0)]))
    shunt_c_enabled = EnumUint16Field(17, 1, Mode.RW, description="0=Enabled, 1=Disabled", options=Enum("shunt_c_enabled", [('Disabled', 1), ('Enabled', 0)]))
    relay_control = EnumUint16Field(18, 1, Mode.RW, description="0 = Off; 1 = Auto; 2 = On", options=Enum("relay_control", [('Auto;', 1), ('Off;', 0), ('On', 2)]))
    relay_invert_logic = EnumUint16Field(19, 1, Mode.RW, description="0=Invert Logic,1=Normal", options=Enum("relay_invert_logic", [('Invert Logic', 0), ('Normal', 1)]))
    relay_high_voltage = Uint16Field(20, 1, Mode.RW, description="Relay high voltage enable", units="DC Volts")
    relay_low_voltage = Uint16Field(21, 1, Mode.RW, description="Relay low voltage enable", units="DC Volts")
    relay_soc_high = Uint16Field(22, 1, Mode.RW, description="Relay high SOC enable", units="Percent")
    relay_soc_low = Uint16Field(23, 1, Mode.RW, description="Relay low SOC enable", units="Percent")
    relay_high_enable_delay = Uint16Field(24, 1, Mode.RW, description="Relay High Enable Delay", units="Minutes")
    relay_low_enable_delay = Uint16Field(25, 1, Mode.RW, description="Relay Low Enable Delay", units="Minutes")
    set_data_log_day_offset = Uint16Field(26, 1, Mode.RW, description="Day offset 0-400, 0 =Today, 1 = -1 day \u2026", units="Days")
    get_current_data_log_day_offset = Uint16Field(27, 1, Mode.R, description="Current Data Log Day Offset", units="Days")
    datalog_minimum_soc = Uint16Field(28, 1, Mode.R, description="Datalog minimum SOC", units="Percent")
    datalog_input_ah = Uint16Field(29, 1, Mode.R, description="Datalog input AH", units="AH")
    datalog_input_kwh = Uint16Field(30, 1, Mode.R, description="Datalog input kWh", units="kWh")
    datalog_output_ah = Uint16Field(31, 1, Mode.R, description="Datalog output AH", units="AH")
    datalog_output_kwh = Uint16Field(32, 1, Mode.R, description="Datalog output kWh", units="kWh")
    datalog_net_ah = Uint16Field(33, 1, Mode.R, description="Datalog NET AH", units="AH")
    datalog_net_kwh = Uint16Field(34, 1, Mode.R, description="Datalog NET kWh", units="kWh")
    clear_data_log_read = Uint16Field(35, 1, Mode.R, description="Read value needed to clear data log")
    clear_data_log_write_complement = Uint16Field(36, 1, Mode.W, description="Write value's complement to clear data log")
    serial_number = StringField(37, 9, Mode.R, description="Device serial number")
    model_number = StringField(46, 9, Mode.R, description="Device model")


FLEXnetDCConfigurationModel.charged_volts.value.scale_factor = FLEXnetDCConfigurationModel.dc_voltage_scale_factor
FLEXnetDCConfigurationModel.battery_charged_amps.value.scale_factor = FLEXnetDCConfigurationModel.dc_current_scale_factor
FLEXnetDCConfigurationModel.relay_high_voltage.value.scale_factor = FLEXnetDCConfigurationModel.dc_voltage_scale_factor
FLEXnetDCConfigurationModel.relay_low_voltage.value.scale_factor = FLEXnetDCConfigurationModel.dc_voltage_scale_factor
FLEXnetDCConfigurationModel.datalog_input_kwh.value.scale_factor = FLEXnetDCConfigurationModel.kwh_scale_factor
FLEXnetDCConfigurationModel.datalog_output_kwh.value.scale_factor = FLEXnetDCConfigurationModel.kwh_scale_factor
FLEXnetDCConfigurationModel.datalog_net_kwh.value.scale_factor = FLEXnetDCConfigurationModel.kwh_scale_factor


@unique
class OutBackSystemControlModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Vendor Extension for OutBack System Control Block")
    length = Uint16Field(2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    dc_voltage_scale_factor = Int16Field(3, 1, Mode.R, description="DC Voltage Scale Factor")
    ac_current_scale_factor = Int16Field(4, 1, Mode.R, description="AC Current Scale Factor")
    time_scale_factor = Int16Field(5, 1, Mode.R, description="Charge Time Scale Factor")
    bulk_charge_enable_disable = EnumUint16Field(6, 1, Mode.W, description="1=Start Bulk, 2=Stop Bulk, 3=Start EQ Charge, 4= Stop EQ Charge", options=Enum("bulk_charge_enable_disable", [('Start Bulk', 1), ('Start EQ Charge', 3), ('Stop Bulk', 2), ('Stop EQ Charge', 4)]))
    inverter_ac_drop_use = EnumUint16Field(7, 1, Mode.W, description="1=Use, 2=Drop", options=Enum("inverter_ac_drop_use", [('Drop', 2), ('Use', 1)]))
    set_inverter_mode = EnumUint16Field(8, 1, Mode.W, description="1=Off, 2=Search, 3=On", options=Enum("set_inverter_mode", [('Off', 1), ('On', 3), ('Search', 2)]))
    grid_tie_mode = EnumUint16Field(9, 1, Mode.W, description="1=Enable, 2=Disable", options=Enum("grid_tie_mode", [('Disable', 2), ('Enable', 1)]))
    set_inverter_charger_mode = EnumUint16Field(10, 1, Mode.W, description="1=Off, 2=Auto, 3=On", options=Enum("set_inverter_charger_mode", [('Auto', 2), ('Off', 1), ('On', 3)]))
    control_status = Bit16Field(11, 1, Mode.R, description="Bit field for status. See OB_Control_Status Table", flags=OBControlStatusFlags)
    set_sell_voltage = Uint16Field(12, 1, Mode.RW, description="Global Sell Voltage", units="Volts")
    set_radian_inverter_sell_current_limit = Uint16Field(13, 1, Mode.RW, description="Radian Inverter Sell Current Limit", units="Amps")
    set_absorb_voltage = Uint16Field(14, 1, Mode.RW, description="Global Absorb Voltage", units="Volts")
    set_absorb_time = Uint16Field(15, 1, Mode.RW, description="Time in tenths of hour", units="Hours")
    set_float_voltage = Uint16Field(16, 1, Mode.RW, description="Global Float Voltage", units="Volts")
    set_float_time = Uint16Field(17, 1, Mode.RW, description="Time in tenths of hour", units="Hours")
    set_inverter_charger_current_limit = Uint16Field(18, 1, Mode.RW, description="Inverter Charger Current Limit", units="Amps")
    set_inverter_ac1_current_limit = Uint16Field(19, 1, Mode.RW, description="Inverter AC1 input Current Limit", units="Amps")
    set_inverter_ac2_current_limit = Uint16Field(20, 1, Mode.RW, description="Inverter AC2 input Current Limit", units="Amps")
    set_ags_op_mode = EnumUint16Field(21, 1, Mode.RW, description="AGS Operating Mode: 0=Off, 1=On, 2=Auto", options=Enum("set_ags_op_mode", [('Auto', 2), ('Off', 0), ('On', 1)]))
    ags_operational_state = EnumUint16Field(22, 1, Mode.R, description="GEN_STOP=0, GEN_STARTING=1, GEN_RUNNING=2, GEN_WARMUP=3, GEN_COOLDOWN=4, GEN_AWAITING_AC=5", options=Enum("ags_operational_state", [(' GEN_AWAITING_AC', 5), (' GEN_COOLDOWN', 4), (' GEN_RUNNING', 2), (' GEN_STARTING', 1), (' GEN_WARMUP', 3), ('GEN_STOP', 0)]))
    ags_operational_state_timer = Uint16Field(23, 1, Mode.R, description="Number of seconds that OB_AGS_Operational_State has been in current state. If Operational State is 0 then timer=0", units="Seconds")
    gen_last_run_start_time_gmt = Uint32Field(24, 2, Mode.R, description="Generator last start time in GMT seconds", units="Seconds")
    gen_last_start_run_duration = Uint32Field(26, 2, Mode.R, description="Last Generator Start Run Duration Seconds", units="Seconds")


OutBackSystemControlModel.set_sell_voltage.value.scale_factor = OutBackSystemControlModel.dc_voltage_scale_factor
OutBackSystemControlModel.set_radian_inverter_sell_current_limit.value.scale_factor = OutBackSystemControlModel.ac_current_scale_factor
OutBackSystemControlModel.set_absorb_voltage.value.scale_factor = OutBackSystemControlModel.dc_voltage_scale_factor
OutBackSystemControlModel.set_absorb_time.value.scale_factor = OutBackSystemControlModel.time_scale_factor
OutBackSystemControlModel.set_float_voltage.value.scale_factor = OutBackSystemControlModel.dc_voltage_scale_factor
OutBackSystemControlModel.set_float_time.value.scale_factor = OutBackSystemControlModel.time_scale_factor
OutBackSystemControlModel.set_inverter_charger_current_limit.value.scale_factor = OutBackSystemControlModel.ac_current_scale_factor
OutBackSystemControlModel.set_inverter_ac1_current_limit.value.scale_factor = OutBackSystemControlModel.ac_current_scale_factor
OutBackSystemControlModel.set_inverter_ac2_current_limit.value.scale_factor = OutBackSystemControlModel.ac_current_scale_factor


@unique
class OPTICSPacketStatisticsModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="OPTICS Packet Stats DID")
    length = Uint16Field(2, 1, Mode.R, description="Length of OPTICS Packet Status Block", units="Registers")
    bt_min = Uint16Field(3, 1, Mode.R, description="Boot packet minimum time", units="msecs")
    bt_max = Uint16Field(4, 1, Mode.R, description="Boot packet maximum time", units="msecs")
    bt_ave = Uint16Field(5, 1, Mode.R, description="Boot packet average time", units="msecs")
    bt_attempts = Uint16Field(6, 1, Mode.R, description="Boot packet number of attempts")
    bt_errors = Uint16Field(7, 1, Mode.R, description="Boot packet error returned from server count")
    bt_timeouts = Uint16Field(8, 1, Mode.R, description="Boot packet timeout from server count")
    bt_packet_timeout = Uint16Field(9, 1, Mode.R, description="Boot packet current gateway timeout", units="secs")
    mp_min = Uint16Field(10, 1, Mode.R, description="Map packet minimum time", units="msecs")
    mp_max = Uint16Field(11, 1, Mode.R, description="Map packet maximum time", units="msecs")
    mp_ave = Uint16Field(12, 1, Mode.R, description="Map packet average time", units="msecs")
    mp_attempts = Uint16Field(13, 1, Mode.R, description="Map packet number of attempts")
    mp_errors = Uint16Field(14, 1, Mode.R, description="Map packet error returned from server count")
    mp_timeouts = Uint16Field(15, 1, Mode.R, description="Map packet timeout from server count")
    mp_packet_timeout = Uint16Field(16, 1, Mode.R, description="Map packet current gateway timeout", units="secs")
    cu_min = Uint16Field(17, 1, Mode.R, description="Config packet minimum time", units="msecs")
    cu_max = Uint16Field(18, 1, Mode.R, description="Config packet maximum time", units="msecs")
    cu_ave = Uint16Field(19, 1, Mode.R, description="Config packet average time", units="msecs")
    cu_attempts = Uint16Field(20, 1, Mode.R, description="Config packet number of attempts")
    cu_errors = Uint16Field(21, 1, Mode.R, description="Config packet error returned from server count")
    cu_timeouts = Uint16Field(22, 1, Mode.R, description="Config packet timeout from server count")
    cu_packet_timeout = Uint16Field(23, 1, Mode.R, description="Config packet current gateway timeout", units="secs")
    su_min = Uint16Field(24, 1, Mode.R, description="Status packet minimum time", units="msecs")
    su_max = Uint16Field(25, 1, Mode.R, description="Status packet maximum time", units="msecs")
    su_ave = Uint16Field(26, 1, Mode.R, description="Status packet average time", units="msecs")
    su_attempts = Uint16Field(27, 1, Mode.R, description="Status packet number of attempts")
    su_errors = Uint16Field(28, 1, Mode.R, description="Status packet error returned from server count")
    su_timeouts = Uint16Field(29, 1, Mode.R, description="Status packet timeout from server count")
    su_packet_timeout = Uint16Field(30, 1, Mode.R, description="Status packet current gateway timeout", units="secs")
    pg_min = Uint16Field(31, 1, Mode.R, description="Ping packet minimum time", units="msecs")
    pg_max = Uint16Field(32, 1, Mode.R, description="Ping packet maximum time", units="msecs")
    pg_ave = Uint16Field(33, 1, Mode.R, description="Ping packet average time", units="msecs")
    pg_attempts = Uint16Field(34, 1, Mode.R, description="Ping packet number of attempts")
    pg_errors = Uint16Field(35, 1, Mode.R, description="Ping packet error returned from server count")
    pg_timeouts = Uint16Field(36, 1, Mode.R, description="Ping packet timeout from server count")
    pg_packet_timeout = Uint16Field(37, 1, Mode.R, description="Ping packet current gateway timeout", units="secs")
    mb_min = Uint16Field(38, 1, Mode.R, description="Modbus packet minimum time", units="msecs")
    mb_max = Uint16Field(39, 1, Mode.R, description="Modbus packet maximum time", units="msecs")
    mb_ave = Uint16Field(40, 1, Mode.R, description="Modbus packet average time", units="msecs")
    mb_attempts = Uint16Field(41, 1, Mode.R, description="Modbus packet number of attempts")
    mb_errors = Uint16Field(42, 1, Mode.R, description="Modbus packet error returned from server count")
    mb_timeouts = Uint16Field(43, 1, Mode.R, description="Modbus packet timeout from server count")
    mb_packet_timeout = Uint16Field(44, 1, Mode.R, description="Modbus packet current gateway timeout", units="secs")
    fu_min = Uint16Field(45, 1, Mode.R, description="File IO packet minimum time", units="msecs")
    fu_max = Uint16Field(46, 1, Mode.R, description="File IO packet maximum time", units="msecs")
    fu_ave = Uint16Field(47, 1, Mode.R, description="File IO packet average time", units="msecs")
    fu_attempts = Uint16Field(48, 1, Mode.R, description="File IO packet number of attempts")
    fu_errors = Uint16Field(49, 1, Mode.R, description="File IO packet error returned from server count")
    fu_timeouts = Uint16Field(50, 1, Mode.R, description="File IO packet timeout from server count")
    fu_packet_timeout = Uint16Field(51, 1, Mode.R, description="File IO packet current gateway timeout", units="secs")
    ev_min = Uint16Field(52, 1, Mode.R, description="Event packet minimum time", units="msecs")
    ev_max = Uint16Field(53, 1, Mode.R, description="Event packet maximum time", units="msecs")
    ev_ave = Uint16Field(54, 1, Mode.R, description="Event packet average time", units="msecs")
    ev_attempts = Uint16Field(55, 1, Mode.R, description="Event packet number of attempts")
    ev_errors = Uint16Field(56, 1, Mode.R, description="Event packet error returned from server count")
    ev_timeouts = Uint16Field(57, 1, Mode.R, description="Event packet timeout from server count")
    ev_packet_timeout = Uint16Field(58, 1, Mode.R, description="Event packet current gateway timeout", units="secs")


MODEL_DEVICE_IDS = {
    1400204883: SunSpecHeaderModel,
    65535: SunSpecEndModel,
    1: SunSpecCommonModel,
    101: SunSpecInverterSinglePhaseModel,
    102: SunSpecInverterSplitPhaseModel,
    103: SunSpecInverterThreePhaseModel,
    64110: OutBackModel,
    64111: ChargeControllerModel,
    64112: ChargeControllerConfigurationModel,
    64113: FXInverterRealTimeModel,
    64114: FXInverterConfigurationModel,
    64115: SplitPhaseRadianInverterRealTimeModel,
    64116: RadianInverterConfigurationModel,
    64117: SinglePhaseRadianInverterRealTimeModel,
    64118: FLEXnetDCRealTimeModel,
    64119: FLEXnetDCConfigurationModel,
    64120: OutBackSystemControlModel,
    64255: OPTICSPacketStatisticsModel,
}
