"""This file is auto generated, do not edit. The generation code can be found in code_generator.py"""


from enum import Enum, IntFlag, unique
from mate3.sunspec.fields import (
    Mode,
    StringField,
    Int16Field,
    Uint16Field,
    Uint32Field,
    EnumUint16Field,
    EnumInt16Field,
    Bit16Field,
    Bit32Field,
    BitfieldDescriptionMixin,
    AddressField
)
from mate3.sunspec.model_base import Model


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


class SunSpecHeaderModel(Model):
    did: Uint32Field = Uint32Field("did", 1, 2, Mode.R)
    model_id: Uint16Field = Uint16Field("model_id", 3, 1, Mode.R)
    length: Uint16Field = Uint16Field("length", 4, 1, Mode.R)
    manufacturer: StringField = StringField("manufacturer", 5, 16, Mode.R)
    model: StringField = StringField("model", 21, 16, Mode.R)
    options: StringField = StringField("options", 37, 8, Mode.R)
    version: StringField = StringField("version", 45, 8, Mode.R)
    serial_number: StringField = StringField("serial_number", 53, 16, Mode.R)


SunSpecHeaderModel.__model_fields__ = [SunSpecHeaderModel.did, SunSpecHeaderModel.model_id, SunSpecHeaderModel.length, SunSpecHeaderModel.manufacturer, SunSpecHeaderModel.model, SunSpecHeaderModel.options, SunSpecHeaderModel.version, SunSpecHeaderModel.serial_number]


class SunSpecEndModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Should be 65535")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Should be 0")


SunSpecEndModel.__model_fields__ = [SunSpecEndModel.did, SunSpecEndModel.length]


class SunSpecCommonModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Common Model block")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    manufacturer: StringField = StringField("manufacturer", 3, 16, Mode.R)
    model: StringField = StringField("model", 19, 16, Mode.R)
    options: StringField = StringField("options", 35, 8, Mode.R)
    version: StringField = StringField("version", 43, 8, Mode.R)
    serial_number: StringField = StringField("serial_number", 51, 16, Mode.R)
    device_address: Uint16Field = Uint16Field("device_address", 67, 1, Mode.RW)


SunSpecCommonModel.__model_fields__ = [SunSpecCommonModel.did, SunSpecCommonModel.length, SunSpecCommonModel.manufacturer, SunSpecCommonModel.model, SunSpecCommonModel.options, SunSpecCommonModel.version, SunSpecCommonModel.serial_number, SunSpecCommonModel.device_address]

class SunSpecInverterSinglePhaseModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Single Phase Inverter")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of model block", units="Registers")
    ac_current: Uint16Field = Uint16Field("ac_current", 3, 1, Mode.R, description="AC Total Current value", units="Amps")
    ac_current_a: Uint16Field = Uint16Field("ac_current_a", 4, 1, Mode.R, description="AC Phase-A Current value", units="Amps")
    ac_current_b: Uint16Field = Uint16Field("ac_current_b", 5, 1, Mode.R, description="AC Phase-B Current value", units="Amps")
    ac_current_c: Uint16Field = Uint16Field("ac_current_c", 6, 1, Mode.R, description="AC Phase-C Current value", units="Amps")
    ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 7, 1, Mode.R, description="AC Current Scale factor", units="SF")
    ac_voltage_ab: Uint16Field = Uint16Field("ac_voltage_ab", 8, 1, Mode.R, description="AC Voltage Phase-AB value", units="Volts")
    ac_voltage_bc: Uint16Field = Uint16Field("ac_voltage_bc", 9, 1, Mode.R, description="AC Voltage Phase BC value", units="Volts")
    ac_voltage_ca: Uint16Field = Uint16Field("ac_voltage_ca", 10, 1, Mode.R, description="AC Voltage Phase CA value", units="Volts")
    ac_voltage_an: Uint16Field = Uint16Field("ac_voltage_an", 11, 1, Mode.R, description="AC Voltage Phase-A-to-neutral value", units="Volts")
    ac_voltage_bn: Uint16Field = Uint16Field("ac_voltage_bn", 12, 1, Mode.R, description="AC Voltage Phase B-to-neutral value", units="Volts")
    ac_voltage_cn: Uint16Field = Uint16Field("ac_voltage_cn", 13, 1, Mode.R, description="AC Voltage Phase C-to-neutral value", units="Volts")
    ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 14, 1, Mode.R, description="AC Voltage Scale factor", units="SF")
    ac_power: Int16Field = Int16Field("ac_power", 15, 1, Mode.R, description="AC Power value", units="Watts")
    ac_power_scale_factor: Int16Field = Int16Field("ac_power_scale_factor", 16, 1, Mode.R, description="AC Power Scale factor", units="SF")
    ac_frequency: Uint16Field = Uint16Field("ac_frequency", 17, 1, Mode.R, description="AC Frequency value", units="Hertz")
    ac_frequency_scale_factor: Int16Field = Int16Field("ac_frequency_scale_factor", 18, 1, Mode.R, description="Scale factor", units="SF")
    ac_va: Int16Field = Int16Field("ac_va", 19, 1, Mode.R, description="Apparent Power", units="VA")
    ac_va_scale_factor: Int16Field = Int16Field("ac_va_scale_factor", 20, 1, Mode.R, description="Scale factor", units="SF")
    ac_var: Int16Field = Int16Field("ac_var", 21, 1, Mode.R, description="Reactive Power", units="VAR")
    ac_var_scale_factor: Int16Field = Int16Field("ac_var_scale_factor", 22, 1, Mode.R, description="Scale factor", units="SF")
    ac_pf: Int16Field = Int16Field("ac_pf", 23, 1, Mode.R, description="Power Factor")
    ac_pf_scale_factor: Int16Field = Int16Field("ac_pf_scale_factor", 24, 1, Mode.R, description="Scale factor", units="SF")
    ac_energy_wh: Uint32Field = Uint32Field("ac_energy_wh", 25, 2, Mode.R, description="AC Lifetime Energy production", units="WattHours")
    ac_energy_wh_scale_factor: Uint16Field = Uint16Field("ac_energy_wh_scale_factor", 27, 1, Mode.R, description="AC Lifetime Energy production scale factor", units="SF")
    dc_current: Uint16Field = Uint16Field("dc_current", 28, 1, Mode.R, description="DC Current value", units="Amps")
    dc_current_scale_factor: Int16Field = Int16Field("dc_current_scale_factor", 29, 1, Mode.R, description="Scale factor", units="SF")
    dc_voltage: Uint16Field = Uint16Field("dc_voltage", 30, 1, Mode.R, description="DC Voltage value", units="Volts")
    dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 31, 1, Mode.R, description="Scale factor", units="SF")
    dc_power: Int16Field = Int16Field("dc_power", 32, 1, Mode.R, description="DC Power value", units="Watts")
    dc_power_scale_factor: Int16Field = Int16Field("dc_power_scale_factor", 33, 1, Mode.R, description="Scale factor", units="SF")
    temp_cab: Int16Field = Int16Field("temp_cab", 34, 1, Mode.R, description="Cabinet Temperature", units="Degrees C")
    temp_sink: Int16Field = Int16Field("temp_sink", 35, 1, Mode.R, description="Coolant or Heat Sink Temperature", units="Degrees C")
    temp_trans: Int16Field = Int16Field("temp_trans", 36, 1, Mode.R, description="Transformer Temperature", units="Degrees C")
    temp_other: Int16Field = Int16Field("temp_other", 37, 1, Mode.R, description="Other Temperature", units="Degrees C")
    temp_scale_factor: Int16Field = Int16Field("temp_scale_factor", 38, 1, Mode.R, description="Scale factor", units="SF")
    status: Uint16Field = Uint16Field("status", 39, 1, Mode.R, description="Operating State", units="Enumerated")
    status_vendor: Uint16Field = Uint16Field("status_vendor", 40, 1, Mode.R, description="Vendor Defined Operating State", units="Enumerated")
    event_1: Bit32Field = Bit32Field("event_1", 41, 2, Mode.R, description="Event Flags (bits 0-31)", flags=IEvent1Flags)


SunSpecInverterSinglePhaseModel.ac_current.scale_factor = SunSpecInverterSinglePhaseModel.ac_current_scale_factor
SunSpecInverterSinglePhaseModel.ac_current_a.scale_factor = SunSpecInverterSinglePhaseModel.ac_current_scale_factor
SunSpecInverterSinglePhaseModel.ac_current_b.scale_factor = SunSpecInverterSinglePhaseModel.ac_current_scale_factor
SunSpecInverterSinglePhaseModel.ac_current_c.scale_factor = SunSpecInverterSinglePhaseModel.ac_current_scale_factor
SunSpecInverterSinglePhaseModel.ac_voltage_ab.scale_factor = SunSpecInverterSinglePhaseModel.ac_voltage_scale_factor
SunSpecInverterSinglePhaseModel.ac_voltage_bc.scale_factor = SunSpecInverterSinglePhaseModel.ac_voltage_scale_factor
SunSpecInverterSinglePhaseModel.ac_voltage_ca.scale_factor = SunSpecInverterSinglePhaseModel.ac_voltage_scale_factor
SunSpecInverterSinglePhaseModel.ac_voltage_an.scale_factor = SunSpecInverterSinglePhaseModel.ac_voltage_scale_factor
SunSpecInverterSinglePhaseModel.ac_voltage_bn.scale_factor = SunSpecInverterSinglePhaseModel.ac_voltage_scale_factor
SunSpecInverterSinglePhaseModel.ac_voltage_cn.scale_factor = SunSpecInverterSinglePhaseModel.ac_voltage_scale_factor
SunSpecInverterSinglePhaseModel.ac_power.scale_factor = SunSpecInverterSinglePhaseModel.ac_power_scale_factor
SunSpecInverterSinglePhaseModel.ac_frequency.scale_factor = SunSpecInverterSinglePhaseModel.ac_frequency_scale_factor
SunSpecInverterSinglePhaseModel.ac_va.scale_factor = SunSpecInverterSinglePhaseModel.ac_va_scale_factor
SunSpecInverterSinglePhaseModel.ac_var.scale_factor = SunSpecInverterSinglePhaseModel.ac_var_scale_factor
SunSpecInverterSinglePhaseModel.ac_pf.scale_factor = SunSpecInverterSinglePhaseModel.ac_pf_scale_factor
SunSpecInverterSinglePhaseModel.ac_energy_wh.scale_factor = SunSpecInverterSinglePhaseModel.ac_energy_wh_scale_factor
SunSpecInverterSinglePhaseModel.dc_current.scale_factor = SunSpecInverterSinglePhaseModel.dc_current_scale_factor
SunSpecInverterSinglePhaseModel.dc_voltage.scale_factor = SunSpecInverterSinglePhaseModel.dc_voltage_scale_factor
SunSpecInverterSinglePhaseModel.dc_power.scale_factor = SunSpecInverterSinglePhaseModel.dc_power_scale_factor
SunSpecInverterSinglePhaseModel.temp_cab.scale_factor = SunSpecInverterSinglePhaseModel.temp_scale_factor
SunSpecInverterSinglePhaseModel.temp_sink.scale_factor = SunSpecInverterSinglePhaseModel.temp_scale_factor
SunSpecInverterSinglePhaseModel.temp_trans.scale_factor = SunSpecInverterSinglePhaseModel.temp_scale_factor
SunSpecInverterSinglePhaseModel.temp_other.scale_factor = SunSpecInverterSinglePhaseModel.temp_scale_factor
SunSpecInverterSinglePhaseModel.__model_fields__ = [SunSpecInverterSinglePhaseModel.did, SunSpecInverterSinglePhaseModel.length, SunSpecInverterSinglePhaseModel.ac_current, SunSpecInverterSinglePhaseModel.ac_current_a, SunSpecInverterSinglePhaseModel.ac_current_b, SunSpecInverterSinglePhaseModel.ac_current_c, SunSpecInverterSinglePhaseModel.ac_current_scale_factor, SunSpecInverterSinglePhaseModel.ac_voltage_ab, SunSpecInverterSinglePhaseModel.ac_voltage_bc, SunSpecInverterSinglePhaseModel.ac_voltage_ca, SunSpecInverterSinglePhaseModel.ac_voltage_an, SunSpecInverterSinglePhaseModel.ac_voltage_bn, SunSpecInverterSinglePhaseModel.ac_voltage_cn, SunSpecInverterSinglePhaseModel.ac_voltage_scale_factor, SunSpecInverterSinglePhaseModel.ac_power, SunSpecInverterSinglePhaseModel.ac_power_scale_factor, SunSpecInverterSinglePhaseModel.ac_frequency, SunSpecInverterSinglePhaseModel.ac_frequency_scale_factor, SunSpecInverterSinglePhaseModel.ac_va, SunSpecInverterSinglePhaseModel.ac_va_scale_factor, SunSpecInverterSinglePhaseModel.ac_var, SunSpecInverterSinglePhaseModel.ac_var_scale_factor, SunSpecInverterSinglePhaseModel.ac_pf, SunSpecInverterSinglePhaseModel.ac_pf_scale_factor, SunSpecInverterSinglePhaseModel.ac_energy_wh, SunSpecInverterSinglePhaseModel.ac_energy_wh_scale_factor, SunSpecInverterSinglePhaseModel.dc_current, SunSpecInverterSinglePhaseModel.dc_current_scale_factor, SunSpecInverterSinglePhaseModel.dc_voltage, SunSpecInverterSinglePhaseModel.dc_voltage_scale_factor, SunSpecInverterSinglePhaseModel.dc_power, SunSpecInverterSinglePhaseModel.dc_power_scale_factor, SunSpecInverterSinglePhaseModel.temp_cab, SunSpecInverterSinglePhaseModel.temp_sink, SunSpecInverterSinglePhaseModel.temp_trans, SunSpecInverterSinglePhaseModel.temp_other, SunSpecInverterSinglePhaseModel.temp_scale_factor, SunSpecInverterSinglePhaseModel.status, SunSpecInverterSinglePhaseModel.status_vendor, SunSpecInverterSinglePhaseModel.event_1]

class SunSpecInverterSplitPhaseModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Split Phase Inverter")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of model block", units="Registers")
    ac_current: Uint16Field = Uint16Field("ac_current", 3, 1, Mode.R, description="AC Total Current value", units="Amps")
    ac_current_a: Uint16Field = Uint16Field("ac_current_a", 4, 1, Mode.R, description="AC Phase-A Current value", units="Amps")
    ac_current_b: Uint16Field = Uint16Field("ac_current_b", 5, 1, Mode.R, description="AC Phase-B Current value", units="Amps")
    ac_current_c: Uint16Field = Uint16Field("ac_current_c", 6, 1, Mode.R, description="AC Phase-C Current value", units="Amps")
    ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 7, 1, Mode.R, description="AC Current Scale factor", units="SF")
    ac_voltage_ab: Uint16Field = Uint16Field("ac_voltage_ab", 8, 1, Mode.R, description="AC Voltage Phase-AB value", units="Volts")
    ac_voltage_bc: Uint16Field = Uint16Field("ac_voltage_bc", 9, 1, Mode.R, description="AC Voltage Phase BC value", units="Volts")
    ac_voltage_ca: Uint16Field = Uint16Field("ac_voltage_ca", 10, 1, Mode.R, description="AC Voltage Phase CA value", units="Volts")
    ac_voltage_an: Uint16Field = Uint16Field("ac_voltage_an", 11, 1, Mode.R, description="AC Voltage Phase-A-to-neutral value", units="Volts")
    ac_voltage_bn: Uint16Field = Uint16Field("ac_voltage_bn", 12, 1, Mode.R, description="AC Voltage Phase B-to-neutral value", units="Volts")
    ac_voltage_cn: Uint16Field = Uint16Field("ac_voltage_cn", 13, 1, Mode.R, description="AC Voltage Phase C-to-neutral value", units="Volts")
    ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 14, 1, Mode.R, description="AC Voltage Scale factor", units="SF")
    ac_power: Int16Field = Int16Field("ac_power", 15, 1, Mode.R, description="AC Power value", units="Watts")
    ac_power_scale_factor: Int16Field = Int16Field("ac_power_scale_factor", 16, 1, Mode.R, description="AC Power Scale factor", units="SF")
    ac_frequency: Uint16Field = Uint16Field("ac_frequency", 17, 1, Mode.R, description="AC Frequency value", units="Hertz")
    ac_frequency_scale_factor: Int16Field = Int16Field("ac_frequency_scale_factor", 18, 1, Mode.R, description="Scale factor", units="SF")
    ac_va: Int16Field = Int16Field("ac_va", 19, 1, Mode.R, description="Apparent Power", units="VA")
    ac_va_scale_factor: Int16Field = Int16Field("ac_va_scale_factor", 20, 1, Mode.R, description="Scale factor", units="SF")
    ac_var: Int16Field = Int16Field("ac_var", 21, 1, Mode.R, description="Reactive Power", units="VAR")
    ac_var_scale_factor: Int16Field = Int16Field("ac_var_scale_factor", 22, 1, Mode.R, description="Scale factor", units="SF")
    ac_pf: Int16Field = Int16Field("ac_pf", 23, 1, Mode.R, description="Power Factor")
    ac_pf_scale_factor: Int16Field = Int16Field("ac_pf_scale_factor", 24, 1, Mode.R, description="Scale factor", units="SF")
    ac_energy_wh: Uint32Field = Uint32Field("ac_energy_wh", 25, 2, Mode.R, description="AC Lifetime Energy production", units="WattHours")
    ac_energy_wh_scale_factor: Uint16Field = Uint16Field("ac_energy_wh_scale_factor", 27, 1, Mode.R, description="AC Lifetime Energy production scale factor", units="SF")
    dc_current: Uint16Field = Uint16Field("dc_current", 28, 1, Mode.R, description="DC Current value", units="Amps")
    dc_current_scale_factor: Int16Field = Int16Field("dc_current_scale_factor", 29, 1, Mode.R, description="Scale factor", units="SF")
    dc_voltage: Uint16Field = Uint16Field("dc_voltage", 30, 1, Mode.R, description="DC Voltage value", units="Volts")
    dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 31, 1, Mode.R, description="Scale factor", units="SF")
    dc_power: Int16Field = Int16Field("dc_power", 32, 1, Mode.R, description="DC Power value", units="Watts")
    dc_power_scale_factor: Int16Field = Int16Field("dc_power_scale_factor", 33, 1, Mode.R, description="Scale factor", units="SF")
    temp_cab: Int16Field = Int16Field("temp_cab", 34, 1, Mode.R, description="Cabinet Temperature", units="Degrees C")
    temp_sink: Int16Field = Int16Field("temp_sink", 35, 1, Mode.R, description="Coolant or Heat Sink Temperature", units="Degrees C")
    temp_trans: Int16Field = Int16Field("temp_trans", 36, 1, Mode.R, description="Transformer Temperature", units="Degrees C")
    temp_other: Int16Field = Int16Field("temp_other", 37, 1, Mode.R, description="Other Temperature", units="Degrees C")
    temp_scale_factor: Int16Field = Int16Field("temp_scale_factor", 38, 1, Mode.R, description="Scale factor", units="SF")
    status: Uint16Field = Uint16Field("status", 39, 1, Mode.R, description="Operating State", units="Enumerated")
    status_vendor: Uint16Field = Uint16Field("status_vendor", 40, 1, Mode.R, description="Vendor Defined Operating State", units="Enumerated")
    event_1: Bit32Field = Bit32Field("event_1", 41, 2, Mode.R, description="Event Flags (bits 0-31)", flags=IEvent1Flags)


SunSpecInverterSplitPhaseModel.ac_current.scale_factor = SunSpecInverterSplitPhaseModel.ac_current_scale_factor
SunSpecInverterSplitPhaseModel.ac_current_a.scale_factor = SunSpecInverterSplitPhaseModel.ac_current_scale_factor
SunSpecInverterSplitPhaseModel.ac_current_b.scale_factor = SunSpecInverterSplitPhaseModel.ac_current_scale_factor
SunSpecInverterSplitPhaseModel.ac_current_c.scale_factor = SunSpecInverterSplitPhaseModel.ac_current_scale_factor
SunSpecInverterSplitPhaseModel.ac_voltage_ab.scale_factor = SunSpecInverterSplitPhaseModel.ac_voltage_scale_factor
SunSpecInverterSplitPhaseModel.ac_voltage_bc.scale_factor = SunSpecInverterSplitPhaseModel.ac_voltage_scale_factor
SunSpecInverterSplitPhaseModel.ac_voltage_ca.scale_factor = SunSpecInverterSplitPhaseModel.ac_voltage_scale_factor
SunSpecInverterSplitPhaseModel.ac_voltage_an.scale_factor = SunSpecInverterSplitPhaseModel.ac_voltage_scale_factor
SunSpecInverterSplitPhaseModel.ac_voltage_bn.scale_factor = SunSpecInverterSplitPhaseModel.ac_voltage_scale_factor
SunSpecInverterSplitPhaseModel.ac_voltage_cn.scale_factor = SunSpecInverterSplitPhaseModel.ac_voltage_scale_factor
SunSpecInverterSplitPhaseModel.ac_power.scale_factor = SunSpecInverterSplitPhaseModel.ac_power_scale_factor
SunSpecInverterSplitPhaseModel.ac_frequency.scale_factor = SunSpecInverterSplitPhaseModel.ac_frequency_scale_factor
SunSpecInverterSplitPhaseModel.ac_va.scale_factor = SunSpecInverterSplitPhaseModel.ac_va_scale_factor
SunSpecInverterSplitPhaseModel.ac_var.scale_factor = SunSpecInverterSplitPhaseModel.ac_var_scale_factor
SunSpecInverterSplitPhaseModel.ac_pf.scale_factor = SunSpecInverterSplitPhaseModel.ac_pf_scale_factor
SunSpecInverterSplitPhaseModel.ac_energy_wh.scale_factor = SunSpecInverterSplitPhaseModel.ac_energy_wh_scale_factor
SunSpecInverterSplitPhaseModel.dc_current.scale_factor = SunSpecInverterSplitPhaseModel.dc_current_scale_factor
SunSpecInverterSplitPhaseModel.dc_voltage.scale_factor = SunSpecInverterSplitPhaseModel.dc_voltage_scale_factor
SunSpecInverterSplitPhaseModel.dc_power.scale_factor = SunSpecInverterSplitPhaseModel.dc_power_scale_factor
SunSpecInverterSplitPhaseModel.temp_cab.scale_factor = SunSpecInverterSplitPhaseModel.temp_scale_factor
SunSpecInverterSplitPhaseModel.temp_sink.scale_factor = SunSpecInverterSplitPhaseModel.temp_scale_factor
SunSpecInverterSplitPhaseModel.temp_trans.scale_factor = SunSpecInverterSplitPhaseModel.temp_scale_factor
SunSpecInverterSplitPhaseModel.temp_other.scale_factor = SunSpecInverterSplitPhaseModel.temp_scale_factor
SunSpecInverterSplitPhaseModel.__model_fields__ = [SunSpecInverterSplitPhaseModel.did, SunSpecInverterSplitPhaseModel.length, SunSpecInverterSplitPhaseModel.ac_current, SunSpecInverterSplitPhaseModel.ac_current_a, SunSpecInverterSplitPhaseModel.ac_current_b, SunSpecInverterSplitPhaseModel.ac_current_c, SunSpecInverterSplitPhaseModel.ac_current_scale_factor, SunSpecInverterSplitPhaseModel.ac_voltage_ab, SunSpecInverterSplitPhaseModel.ac_voltage_bc, SunSpecInverterSplitPhaseModel.ac_voltage_ca, SunSpecInverterSplitPhaseModel.ac_voltage_an, SunSpecInverterSplitPhaseModel.ac_voltage_bn, SunSpecInverterSplitPhaseModel.ac_voltage_cn, SunSpecInverterSplitPhaseModel.ac_voltage_scale_factor, SunSpecInverterSplitPhaseModel.ac_power, SunSpecInverterSplitPhaseModel.ac_power_scale_factor, SunSpecInverterSplitPhaseModel.ac_frequency, SunSpecInverterSplitPhaseModel.ac_frequency_scale_factor, SunSpecInverterSplitPhaseModel.ac_va, SunSpecInverterSplitPhaseModel.ac_va_scale_factor, SunSpecInverterSplitPhaseModel.ac_var, SunSpecInverterSplitPhaseModel.ac_var_scale_factor, SunSpecInverterSplitPhaseModel.ac_pf, SunSpecInverterSplitPhaseModel.ac_pf_scale_factor, SunSpecInverterSplitPhaseModel.ac_energy_wh, SunSpecInverterSplitPhaseModel.ac_energy_wh_scale_factor, SunSpecInverterSplitPhaseModel.dc_current, SunSpecInverterSplitPhaseModel.dc_current_scale_factor, SunSpecInverterSplitPhaseModel.dc_voltage, SunSpecInverterSplitPhaseModel.dc_voltage_scale_factor, SunSpecInverterSplitPhaseModel.dc_power, SunSpecInverterSplitPhaseModel.dc_power_scale_factor, SunSpecInverterSplitPhaseModel.temp_cab, SunSpecInverterSplitPhaseModel.temp_sink, SunSpecInverterSplitPhaseModel.temp_trans, SunSpecInverterSplitPhaseModel.temp_other, SunSpecInverterSplitPhaseModel.temp_scale_factor, SunSpecInverterSplitPhaseModel.status, SunSpecInverterSplitPhaseModel.status_vendor, SunSpecInverterSplitPhaseModel.event_1]

class SunSpecInverterThreePhaseModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Three Phase Inverter")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of model block", units="Registers")
    ac_current: Uint16Field = Uint16Field("ac_current", 3, 1, Mode.R, description="AC Total Current value", units="Amps")
    ac_current_a: Uint16Field = Uint16Field("ac_current_a", 4, 1, Mode.R, description="AC Phase-A Current value", units="Amps")
    ac_current_b: Uint16Field = Uint16Field("ac_current_b", 5, 1, Mode.R, description="AC Phase-B Current value", units="Amps")
    ac_current_c: Uint16Field = Uint16Field("ac_current_c", 6, 1, Mode.R, description="AC Phase-C Current value", units="Amps")
    ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 7, 1, Mode.R, description="AC Current Scale factor", units="SF")
    ac_voltage_ab: Uint16Field = Uint16Field("ac_voltage_ab", 8, 1, Mode.R, description="AC Voltage Phase-AB value", units="Volts")
    ac_voltage_bc: Uint16Field = Uint16Field("ac_voltage_bc", 9, 1, Mode.R, description="AC Voltage Phase BC value", units="Volts")
    ac_voltage_ca: Uint16Field = Uint16Field("ac_voltage_ca", 10, 1, Mode.R, description="AC Voltage Phase CA value", units="Volts")
    ac_voltage_an: Uint16Field = Uint16Field("ac_voltage_an", 11, 1, Mode.R, description="AC Voltage Phase-A-to-neutral value", units="Volts")
    ac_voltage_bn: Uint16Field = Uint16Field("ac_voltage_bn", 12, 1, Mode.R, description="AC Voltage Phase B-to-neutral value", units="Volts")
    ac_voltage_cn: Uint16Field = Uint16Field("ac_voltage_cn", 13, 1, Mode.R, description="AC Voltage Phase C-to-neutral value", units="Volts")
    ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 14, 1, Mode.R, description="AC Voltage Scale factor", units="SF")
    ac_power: Int16Field = Int16Field("ac_power", 15, 1, Mode.R, description="AC Power value", units="Watts")
    ac_power_scale_factor: Int16Field = Int16Field("ac_power_scale_factor", 16, 1, Mode.R, description="AC Power Scale factor", units="SF")
    ac_frequency: Uint16Field = Uint16Field("ac_frequency", 17, 1, Mode.R, description="AC Frequency value", units="Hertz")
    ac_frequency_scale_factor: Int16Field = Int16Field("ac_frequency_scale_factor", 18, 1, Mode.R, description="Scale factor", units="SF")
    ac_va: Int16Field = Int16Field("ac_va", 19, 1, Mode.R, description="Apparent Power", units="VA")
    ac_va_scale_factor: Int16Field = Int16Field("ac_va_scale_factor", 20, 1, Mode.R, description="Scale factor", units="SF")
    ac_var: Int16Field = Int16Field("ac_var", 21, 1, Mode.R, description="Reactive Power", units="VAR")
    ac_var_scale_factor: Int16Field = Int16Field("ac_var_scale_factor", 22, 1, Mode.R, description="Scale factor", units="SF")
    ac_pf: Int16Field = Int16Field("ac_pf", 23, 1, Mode.R, description="Power Factor")
    ac_pf_scale_factor: Int16Field = Int16Field("ac_pf_scale_factor", 24, 1, Mode.R, description="Scale factor", units="SF")
    ac_energy_wh: Uint32Field = Uint32Field("ac_energy_wh", 25, 2, Mode.R, description="AC Lifetime Energy production", units="WattHours")
    ac_energy_wh_scale_factor: Uint16Field = Uint16Field("ac_energy_wh_scale_factor", 27, 1, Mode.R, description="AC Lifetime Energy production scale factor", units="SF")
    dc_current: Uint16Field = Uint16Field("dc_current", 28, 1, Mode.R, description="DC Current value", units="Amps")
    dc_current_scale_factor: Int16Field = Int16Field("dc_current_scale_factor", 29, 1, Mode.R, description="Scale factor", units="SF")
    dc_voltage: Uint16Field = Uint16Field("dc_voltage", 30, 1, Mode.R, description="DC Voltage value", units="Volts")
    dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 31, 1, Mode.R, description="Scale factor", units="SF")
    dc_power: Int16Field = Int16Field("dc_power", 32, 1, Mode.R, description="DC Power value", units="Watts")
    dc_power_scale_factor: Int16Field = Int16Field("dc_power_scale_factor", 33, 1, Mode.R, description="Scale factor", units="SF")
    temp_cab: Int16Field = Int16Field("temp_cab", 34, 1, Mode.R, description="Cabinet Temperature", units="Degrees C")
    temp_sink: Int16Field = Int16Field("temp_sink", 35, 1, Mode.R, description="Coolant or Heat Sink Temperature", units="Degrees C")
    temp_trans: Int16Field = Int16Field("temp_trans", 36, 1, Mode.R, description="Transformer Temperature", units="Degrees C")
    temp_other: Int16Field = Int16Field("temp_other", 37, 1, Mode.R, description="Other Temperature", units="Degrees C")
    temp_scale_factor: Int16Field = Int16Field("temp_scale_factor", 38, 1, Mode.R, description="Scale factor", units="SF")
    status: Uint16Field = Uint16Field("status", 39, 1, Mode.R, description="Operating State", units="Enumerated")
    status_vendor: Uint16Field = Uint16Field("status_vendor", 40, 1, Mode.R, description="Vendor Defined Operating State", units="Enumerated")
    event_1: Bit32Field = Bit32Field("event_1", 41, 2, Mode.R, description="Event Flags (bits 0-31)", flags=IEvent1Flags)


SunSpecInverterThreePhaseModel.ac_current.scale_factor = SunSpecInverterThreePhaseModel.ac_current_scale_factor
SunSpecInverterThreePhaseModel.ac_current_a.scale_factor = SunSpecInverterThreePhaseModel.ac_current_scale_factor
SunSpecInverterThreePhaseModel.ac_current_b.scale_factor = SunSpecInverterThreePhaseModel.ac_current_scale_factor
SunSpecInverterThreePhaseModel.ac_current_c.scale_factor = SunSpecInverterThreePhaseModel.ac_current_scale_factor
SunSpecInverterThreePhaseModel.ac_voltage_ab.scale_factor = SunSpecInverterThreePhaseModel.ac_voltage_scale_factor
SunSpecInverterThreePhaseModel.ac_voltage_bc.scale_factor = SunSpecInverterThreePhaseModel.ac_voltage_scale_factor
SunSpecInverterThreePhaseModel.ac_voltage_ca.scale_factor = SunSpecInverterThreePhaseModel.ac_voltage_scale_factor
SunSpecInverterThreePhaseModel.ac_voltage_an.scale_factor = SunSpecInverterThreePhaseModel.ac_voltage_scale_factor
SunSpecInverterThreePhaseModel.ac_voltage_bn.scale_factor = SunSpecInverterThreePhaseModel.ac_voltage_scale_factor
SunSpecInverterThreePhaseModel.ac_voltage_cn.scale_factor = SunSpecInverterThreePhaseModel.ac_voltage_scale_factor
SunSpecInverterThreePhaseModel.ac_power.scale_factor = SunSpecInverterThreePhaseModel.ac_power_scale_factor
SunSpecInverterThreePhaseModel.ac_frequency.scale_factor = SunSpecInverterThreePhaseModel.ac_frequency_scale_factor
SunSpecInverterThreePhaseModel.ac_va.scale_factor = SunSpecInverterThreePhaseModel.ac_va_scale_factor
SunSpecInverterThreePhaseModel.ac_var.scale_factor = SunSpecInverterThreePhaseModel.ac_var_scale_factor
SunSpecInverterThreePhaseModel.ac_pf.scale_factor = SunSpecInverterThreePhaseModel.ac_pf_scale_factor
SunSpecInverterThreePhaseModel.ac_energy_wh.scale_factor = SunSpecInverterThreePhaseModel.ac_energy_wh_scale_factor
SunSpecInverterThreePhaseModel.dc_current.scale_factor = SunSpecInverterThreePhaseModel.dc_current_scale_factor
SunSpecInverterThreePhaseModel.dc_voltage.scale_factor = SunSpecInverterThreePhaseModel.dc_voltage_scale_factor
SunSpecInverterThreePhaseModel.dc_power.scale_factor = SunSpecInverterThreePhaseModel.dc_power_scale_factor
SunSpecInverterThreePhaseModel.temp_cab.scale_factor = SunSpecInverterThreePhaseModel.temp_scale_factor
SunSpecInverterThreePhaseModel.temp_sink.scale_factor = SunSpecInverterThreePhaseModel.temp_scale_factor
SunSpecInverterThreePhaseModel.temp_trans.scale_factor = SunSpecInverterThreePhaseModel.temp_scale_factor
SunSpecInverterThreePhaseModel.temp_other.scale_factor = SunSpecInverterThreePhaseModel.temp_scale_factor
SunSpecInverterThreePhaseModel.__model_fields__ = [SunSpecInverterThreePhaseModel.did, SunSpecInverterThreePhaseModel.length, SunSpecInverterThreePhaseModel.ac_current, SunSpecInverterThreePhaseModel.ac_current_a, SunSpecInverterThreePhaseModel.ac_current_b, SunSpecInverterThreePhaseModel.ac_current_c, SunSpecInverterThreePhaseModel.ac_current_scale_factor, SunSpecInverterThreePhaseModel.ac_voltage_ab, SunSpecInverterThreePhaseModel.ac_voltage_bc, SunSpecInverterThreePhaseModel.ac_voltage_ca, SunSpecInverterThreePhaseModel.ac_voltage_an, SunSpecInverterThreePhaseModel.ac_voltage_bn, SunSpecInverterThreePhaseModel.ac_voltage_cn, SunSpecInverterThreePhaseModel.ac_voltage_scale_factor, SunSpecInverterThreePhaseModel.ac_power, SunSpecInverterThreePhaseModel.ac_power_scale_factor, SunSpecInverterThreePhaseModel.ac_frequency, SunSpecInverterThreePhaseModel.ac_frequency_scale_factor, SunSpecInverterThreePhaseModel.ac_va, SunSpecInverterThreePhaseModel.ac_va_scale_factor, SunSpecInverterThreePhaseModel.ac_var, SunSpecInverterThreePhaseModel.ac_var_scale_factor, SunSpecInverterThreePhaseModel.ac_pf, SunSpecInverterThreePhaseModel.ac_pf_scale_factor, SunSpecInverterThreePhaseModel.ac_energy_wh, SunSpecInverterThreePhaseModel.ac_energy_wh_scale_factor, SunSpecInverterThreePhaseModel.dc_current, SunSpecInverterThreePhaseModel.dc_current_scale_factor, SunSpecInverterThreePhaseModel.dc_voltage, SunSpecInverterThreePhaseModel.dc_voltage_scale_factor, SunSpecInverterThreePhaseModel.dc_power, SunSpecInverterThreePhaseModel.dc_power_scale_factor, SunSpecInverterThreePhaseModel.temp_cab, SunSpecInverterThreePhaseModel.temp_sink, SunSpecInverterThreePhaseModel.temp_trans, SunSpecInverterThreePhaseModel.temp_other, SunSpecInverterThreePhaseModel.temp_scale_factor, SunSpecInverterThreePhaseModel.status, SunSpecInverterThreePhaseModel.status_vendor, SunSpecInverterThreePhaseModel.event_1]

class OutBackModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Outback Interface")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    major_firmware_number: Uint16Field = Uint16Field("major_firmware_number", 3, 1, Mode.R, description="OutBack Major firmware revision")
    mid_firmware_number: Uint16Field = Uint16Field("mid_firmware_number", 4, 1, Mode.R, description="OutBack Mid firmware revision")
    minor_firmware_number: Uint16Field = Uint16Field("minor_firmware_number", 5, 1, Mode.R, description="OutBack Minor firmware revision")
    encryption_key: Uint16Field = Uint16Field("encryption_key", 6, 1, Mode.R, description="Encryption key for current session (0 = Encryption not enabled)")
    mac_address: StringField = StringField("mac_address", 7, 7, Mode.R, description="Ethernet MAC address")
    write_password: StringField = StringField("write_password", 14, 8, Mode.W, description="Password required to write to any register")
    enable_dhcp: EnumUint16Field = EnumUint16Field("enable_dhcp", 22, 1, Mode.RW, description="0 = DHCP Disabled, use configured network parameter; 1 = DHCP Enabled", options=Enum("enable_dhcp", [('DHCP Disabled, use configured network parameter', 0), ('DHCP Enabled', 1)]))
    tcpip_address: AddressField = AddressField("tcpip_address", 23, 2, Mode.RW, description="TCP/IP Address xxx.xxx.xxx.xxx")
    tcpip_gateway_msw: AddressField = AddressField("tcpip_gateway_msw", 25, 2, Mode.RW, description="TCP/IP Gateway xxx.xxx.xxx.xxx")
    tcpip_netmask_msw: AddressField = AddressField("tcpip_netmask_msw", 27, 2, Mode.RW, description="TCP/IP Netmask xxx.xxx.xxx.xxx")
    tcpip_dns_1_msw: AddressField = AddressField("tcpip_dns_1_msw", 29, 2, Mode.RW, description="TCP/IP DNS 1 xxx.xxx.xxx.xxx")
    tcpip_dns_2_msw: AddressField = AddressField("tcpip_dns_2_msw", 31, 2, Mode.RW, description="TCP/IP DNS 2 xxx.xxx.xxx.xxx")
    modbus_port: Uint16Field = Uint16Field("modbus_port", 33, 1, Mode.RW, description="Outback MODBUS IP port, default 502")
    smtp_server_name: StringField = StringField("smtp_server_name", 34, 20, Mode.RW, description="Email server name")
    smtp_account_name: StringField = StringField("smtp_account_name", 54, 16, Mode.RW, description="Email account name")
    smtp_ssl_enable: EnumUint16Field = EnumUint16Field("smtp_ssl_enable", 70, 1, Mode.RW, description="0 = SSL Disabled; 1 = SSL Enabled (not implemented)", options=Enum("smtp_ssl_enable", [('SSL Disabled', 0), ('SSL Enabled (not implemented)', 1)]))
    smtp_email_password: StringField = StringField("smtp_email_password", 71, 8, Mode.W, description="Email account password")
    smtp_email_user_name: StringField = StringField("smtp_email_user_name", 79, 20, Mode.RW, description="Email account User Name")
    status_email_interval: Uint16Field = Uint16Field("status_email_interval", 99, 1, Mode.RW, description="0 = Status Email Disabled, 1-23 Status Email every n hours")
    status_email_status_time: Uint16Field = Uint16Field("status_email_status_time", 100, 1, Mode.RW, description="Hour  of first status email of the day")
    status_email_subject_line: StringField = StringField("status_email_subject_line", 101, 25, Mode.RW, description="Status Email Subject Line")
    status_email_to_address_1: StringField = StringField("status_email_to_address_1", 126, 20, Mode.RW, description="Status Email to Address 1")
    status_email_to_address_2: StringField = StringField("status_email_to_address_2", 146, 20, Mode.RW, description="Status Email to Address 2")
    alarm_email_enable: EnumUint16Field = EnumUint16Field("alarm_email_enable", 166, 1, Mode.RW, description="0 = Disabled; 1 = Enabled", options=Enum("alarm_email_enable", [('Disabled', 0), ('Enabled', 1)]))
    system_name: StringField = StringField("system_name", 167, 30, Mode.RW, description="OutBack System Name")
    alarm_email_to_address_1: StringField = StringField("alarm_email_to_address_1", 197, 15, Mode.RW, description="Status Alarm to Address 1")
    alarm_email_to_address_2: StringField = StringField("alarm_email_to_address_2", 212, 20, Mode.RW, description="Status Alarm to Address 2")
    ftp_password: StringField = StringField("ftp_password", 232, 8, Mode.W, description="FTP password")
    telnet_password: StringField = StringField("telnet_password", 240, 8, Mode.W, description="Telnet password (not implemented)")
    sd_card_data_log_write_interval: Uint16Field = Uint16Field("sd_card_data_log_write_interval", 248, 1, Mode.RW, description="0 = SD-Card Data Logging disabled, 1-60 seconds")
    sd_card_data_log_retain_days: Uint16Field = Uint16Field("sd_card_data_log_retain_days", 249, 1, Mode.RW, description="0 = Log until SD-Card is full then erase oldest, 1-731 Number of days to retain data logs")
    sd_card_data_logging_mode: EnumUint16Field = EnumUint16Field("sd_card_data_logging_mode", 250, 1, Mode.RW, description="0 = Disabled; 1 = Excel Format; 2 = Compact Format", options=Enum("sd_card_data_logging_mode", [('Compact Format', 2), ('Disabled', 0), ('Excel Format', 1)]))
    time_server_name: StringField = StringField("time_server_name", 251, 20, Mode.RW, description="Timeserver domain name")
    enable_time_server: EnumUint16Field = EnumUint16Field("enable_time_server", 271, 1, Mode.RW, description="0 = Time Server Disabled, use configured time parameters; 1 = Time  Server Enabled", options=Enum("enable_time_server", [('Time  Server Enabled', 1), ('Time Server Disabled, use configured time parameters', 0)]))
    set_time_zone: Int16Field = Int16Field("set_time_zone", 272, 1, Mode.RW, description="Time Zone -12.0 \u2026 +14.0", units="Hours")
    enable_float_coordination: EnumUint16Field = EnumUint16Field("enable_float_coordination", 273, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("enable_float_coordination", [('Disabled', 0), ('Enabled', 1)]))
    enable_fndc_charge_termination: EnumUint16Field = EnumUint16Field("enable_fndc_charge_termination", 274, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("enable_fndc_charge_termination", [('Disabled', 0), ('Enabled', 1)]))
    enable_fndc_grid_tie_control: EnumUint16Field = EnumUint16Field("enable_fndc_grid_tie_control", 275, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("enable_fndc_grid_tie_control", [('Disabled', 0), ('Enabled', 1)]))
    voltage_scale_factor: Int16Field = Int16Field("voltage_scale_factor", 276, 1, Mode.R, description="DC Voltage Scale Factor")
    hour_scale_factor: Int16Field = Int16Field("hour_scale_factor", 277, 1, Mode.R, description="Hours Scale Factor")
    ags_mode: EnumUint16Field = EnumUint16Field("ags_mode", 278, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_port: Uint16Field = Uint16Field("ags_port", 279, 1, Mode.RW, description="AGS device port number 0-10")
    ags_port_type: EnumUint16Field = EnumUint16Field("ags_port_type", 280, 1, Mode.RW, description="0=Radian AUX Relay, 1=Radian AUX Output", options=Enum("ags_port_type", [('Radian AUX Output', 1), ('Radian AUX Relay', 0)]))
    ags_generator_type: EnumUint16Field = EnumUint16Field("ags_generator_type", 281, 1, Mode.RW, description="0=AC Gen, 1=DC Gen, 2=No Gen", options=Enum("ags_generator_type", [('AC Gen', 0), ('DC Gen', 1), ('No Gen', 2)]))
    ags_dc_gen_absorb_voltage: Uint16Field = Uint16Field("ags_dc_gen_absorb_voltage", 282, 1, Mode.RW, description="DC Generator Absorb Voltage", units="Volts")
    ags_dc_gen_absorb_time: Uint16Field = Uint16Field("ags_dc_gen_absorb_time", 283, 1, Mode.RW, description="DC Generator Absorb Time", units="Hour")
    ags_fault_time: Uint16Field = Uint16Field("ags_fault_time", 284, 1, Mode.RW, description="AGS Generator fault time delay", units="Minutes")
    ags_gen_cool_down_time: Uint16Field = Uint16Field("ags_gen_cool_down_time", 285, 1, Mode.RW, description="AGS Generator Cool Down Time", units="Minutes")
    ags_gen_warm_up_time: Uint16Field = Uint16Field("ags_gen_warm_up_time", 286, 1, Mode.RW, description="AGS Generator Warm Up Time", units="Minutes")
    ags_generator_exercise_mode: EnumUint16Field = EnumUint16Field("ags_generator_exercise_mode", 287, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_generator_exercise_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_exercise_start_hour: Uint16Field = Uint16Field("ags_exercise_start_hour", 288, 1, Mode.RW, description="Exercise Start Hour 0-23", units="Hour")
    ags_exercise_start_minute: Uint16Field = Uint16Field("ags_exercise_start_minute", 289, 1, Mode.RW, description="Exercise Start Minute 0-59", units="Minutes")
    ags_exercise_day: EnumUint16Field = EnumUint16Field("ags_exercise_day", 290, 1, Mode.RW, description="0=Sun, 1=Mon, 2=Tue, 3=Wed, 4=Thr, 5=Fri, 6=Sat", options=Enum("ags_exercise_day", [('Fri', 5), ('Mon', 1), ('Sat', 6), ('Sun', 0), ('Thr', 4), ('Tue', 2), ('Wed', 3)]))
    ags_exercise_period: Uint16Field = Uint16Field("ags_exercise_period", 291, 1, Mode.RW, description="Exercise Period 1-240 minutes", units="Minutes")
    ags_exercise_interval: Uint16Field = Uint16Field("ags_exercise_interval", 292, 1, Mode.RW, description="Exercise interval 1-8 Weeks", units="Weeks")
    ags_sell_mode: EnumUint16Field = EnumUint16Field("ags_sell_mode", 293, 1, Mode.RW, description="Sell During Generator Exercise Period, 0=Selling Enabled, 1=Selling Disabled", options=Enum("ags_sell_mode", [('Selling Disabled', 1), ('Selling Enabled', 0)]))
    ags_2_min_start_mode: EnumUint16Field = EnumUint16Field("ags_2_min_start_mode", 294, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_2_min_start_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_2_min_start_voltage: Uint16Field = Uint16Field("ags_2_min_start_voltage", 295, 1, Mode.RW, description="Two Minute AGS Start Voltage", units="Volts")
    ags_2_hour_start_mode: EnumUint16Field = EnumUint16Field("ags_2_hour_start_mode", 296, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_2_hour_start_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_2_hour_start_voltage: Uint16Field = Uint16Field("ags_2_hour_start_voltage", 297, 1, Mode.RW, description="Two Hour AGS Start Voltage", units="Volts")
    ags_24_hour_start_mode: EnumUint16Field = EnumUint16Field("ags_24_hour_start_mode", 298, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_24_hour_start_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_24_hour_start_voltage: Uint16Field = Uint16Field("ags_24_hour_start_voltage", 299, 1, Mode.RW, description="Twenty Four Hour AGS Start Voltage", units="Volts")
    ags_load_start_mode: EnumUint16Field = EnumUint16Field("ags_load_start_mode", 300, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_load_start_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_load_start_kw: Uint16Field = Uint16Field("ags_load_start_kw", 301, 1, Mode.RW, description="Load Start kWatts", units="kWatts")
    ags_load_start_delay: Uint16Field = Uint16Field("ags_load_start_delay", 302, 1, Mode.RW, description="Load Start Delay", units="Minutes")
    ags_load_stop_kw: Uint16Field = Uint16Field("ags_load_stop_kw", 303, 1, Mode.RW, description="Load Stop kWatts", units="kWatts")
    ags_load_stop_delay: Uint16Field = Uint16Field("ags_load_stop_delay", 304, 1, Mode.RW, description="Load Stop Delay", units="Minutes")
    ags_soc_start_mode: EnumUint16Field = EnumUint16Field("ags_soc_start_mode", 305, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_soc_start_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_soc_start_percentage: Uint16Field = Uint16Field("ags_soc_start_percentage", 306, 1, Mode.RW, description="AGS SOC Start Percentage", units="Percent")
    ags_soc_stop_percentage: Uint16Field = Uint16Field("ags_soc_stop_percentage", 307, 1, Mode.RW, description="AGS SOC Stop Percentage", units="Percent")
    ags_enable_full_charge_mode: EnumUint16Field = EnumUint16Field("ags_enable_full_charge_mode", 308, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_enable_full_charge_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_full_charge_interval: Uint16Field = Uint16Field("ags_full_charge_interval", 309, 1, Mode.RW, description="AGS SOC Full Charge Interval", units="Days")
    ags_must_run_mode: EnumUint16Field = EnumUint16Field("ags_must_run_mode", 310, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_must_run_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_must_run_weekday_start_hour: Uint16Field = Uint16Field("ags_must_run_weekday_start_hour", 311, 1, Mode.RW, description="AGS Must Run Weekday Start Hour 0-23", units="Hour")
    ags_must_run_weekday_start_minute: Uint16Field = Uint16Field("ags_must_run_weekday_start_minute", 312, 1, Mode.RW, description="AGS Must Run Weekday Start Minute 0-59", units="Minute")
    ags_must_run_weekday_stop_hour: Uint16Field = Uint16Field("ags_must_run_weekday_stop_hour", 313, 1, Mode.RW, description="AGS Must Run Weekday Stop Hour 0-23", units="Hour")
    ags_must_run_weekday_stop_minute: Uint16Field = Uint16Field("ags_must_run_weekday_stop_minute", 314, 1, Mode.RW, description="AGS Must Run Weekday Stop Minute 0-59", units="Minute")
    ags_must_run_weekend_start_hour: Uint16Field = Uint16Field("ags_must_run_weekend_start_hour", 315, 1, Mode.RW, description="AGS Must Run Weekend Start Hour 0-23", units="Hour")
    ags_must_run_weekend_start_minute: Uint16Field = Uint16Field("ags_must_run_weekend_start_minute", 316, 1, Mode.RW, description="AGS Must Run Weekend Start Minute 0-59", units="Minute")
    ags_must_run_weekend_stop_hour: Uint16Field = Uint16Field("ags_must_run_weekend_stop_hour", 317, 1, Mode.RW, description="AGS Must Run Weekend Stop Hour 0-23", units="Hour")
    ags_must_run_weekend_stop_minute: Uint16Field = Uint16Field("ags_must_run_weekend_stop_minute", 318, 1, Mode.RW, description="AGS Must Run Weekend Stop Minute 0-59", units="Minute")
    ags_quiet_time_mode: EnumUint16Field = EnumUint16Field("ags_quiet_time_mode", 319, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("ags_quiet_time_mode", [('Disabled', 0), ('Enabled', 1)]))
    ags_quiet_time_weekday_start_hour: Uint16Field = Uint16Field("ags_quiet_time_weekday_start_hour", 320, 1, Mode.RW, description="AGS Quiet Time Weekday Start Hour 0-23", units="Hour")
    ags_quiet_time_weekday_start_minute: Uint16Field = Uint16Field("ags_quiet_time_weekday_start_minute", 321, 1, Mode.RW, description="AGS Quiet Time Weekday Start Minute 0-59", units="Minute")
    ags_quiet_time_weekday_stop_hour: Uint16Field = Uint16Field("ags_quiet_time_weekday_stop_hour", 322, 1, Mode.RW, description="AGS Quiet Time Weekday Stop Hour 0-23", units="Hour")
    ags_quiet_time_weekday_stop_minute: Uint16Field = Uint16Field("ags_quiet_time_weekday_stop_minute", 323, 1, Mode.RW, description="AGS Quiet Time Weekday Stop Minute 0-59", units="Minute")
    ags_quiet_time_weekend_start_hour: Uint16Field = Uint16Field("ags_quiet_time_weekend_start_hour", 324, 1, Mode.RW, description="AGS Quiet Time Weekend Start Hour 0-23", units="Hour")
    ags_quiet_time_weekend_start_minute: Uint16Field = Uint16Field("ags_quiet_time_weekend_start_minute", 325, 1, Mode.RW, description="AGS Quiet Time Weekend Start Minute 0-59", units="Minute")
    ags_quiet_time_weekend_stop_hour: Uint16Field = Uint16Field("ags_quiet_time_weekend_stop_hour", 326, 1, Mode.RW, description="AGS Quiet Time Weekend Stop Hour 0-23", units="Hour")
    ags_quiet_time_weekend_stop_minute: Uint16Field = Uint16Field("ags_quiet_time_weekend_stop_minute", 327, 1, Mode.RW, description="AGS Quiet Time Weekend Stop Minute 0-59", units="Minute")
    ags_total_generator_run_time: Uint32Field = Uint32Field("ags_total_generator_run_time", 328, 2, Mode.RW, description="AGS Generator Total Run Time in Seconds", units="Hours")
    hbx_mode: EnumUint16Field = EnumUint16Field("hbx_mode", 330, 1, Mode.RW, description="0=Disabled, 1=Voltage Only, 2=SOC Only, 3=Both", options=Enum("hbx_mode", [('Both', 3), ('Disabled', 0), ('SOC Only', 2), ('Voltage Only', 1)]))
    hbx_grid_connect_voltage: Uint16Field = Uint16Field("hbx_grid_connect_voltage", 331, 1, Mode.RW, description="HBX Grid Connect Voltage", units="Volts")
    hbx_grid_connect_delay: Uint16Field = Uint16Field("hbx_grid_connect_delay", 332, 1, Mode.RW, description="HBX Grid Connect Delay", units="Hours")
    hbx_grid_disconnect_voltage: Uint16Field = Uint16Field("hbx_grid_disconnect_voltage", 333, 1, Mode.RW, description="HBX Grid Disconnect Voltage", units="Volts")
    hbx_grid_disconnect_delay: Uint16Field = Uint16Field("hbx_grid_disconnect_delay", 334, 1, Mode.RW, description="HBX Grid Disconnect Delay", units="Hours")
    hbx_grid_connect_soc: Uint16Field = Uint16Field("hbx_grid_connect_soc", 335, 1, Mode.RW, description="HBX Grid Connect SOC Percentage", units="Percent")
    hbx_grid_disconnect_soc: Uint16Field = Uint16Field("hbx_grid_disconnect_soc", 336, 1, Mode.RW, description="HBX Grid Disconnect SOC Percentage", units="Percent")
    grid_use_interval_1_mode: EnumUint16Field = EnumUint16Field("grid_use_interval_1_mode", 337, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("grid_use_interval_1_mode", [('Disabled', 0), ('Enabled', 1)]))
    grid_use_interval_1_weekday_start_hour: Uint16Field = Uint16Field("grid_use_interval_1_weekday_start_hour", 338, 1, Mode.RW, description="Grid Use Interval 1 Weekday Start Hour 0-23", units="Hour")
    grid_use_interval_1_weekday_start_minute: Uint16Field = Uint16Field("grid_use_interval_1_weekday_start_minute", 339, 1, Mode.RW, description="Grid Use Interval 1 Weekday Start Minute 0-59", units="Hour")
    grid_use_interval_1_weekday_stop_hour: Uint16Field = Uint16Field("grid_use_interval_1_weekday_stop_hour", 340, 1, Mode.RW, description="Grid Use Interval 1 Weekday Stop Hour 0-23", units="Hour")
    grid_use_interval_1_weekday_stop_minute: Uint16Field = Uint16Field("grid_use_interval_1_weekday_stop_minute", 341, 1, Mode.RW, description="Grid Use Interval 1 Weekday Stop Minute 0-59", units="Hour")
    grid_use_interval_1_weekend_start_hour: Uint16Field = Uint16Field("grid_use_interval_1_weekend_start_hour", 342, 1, Mode.RW, description="Grid Use Interval 1 Weekend Start Hour 0-23", units="Hour")
    grid_use_interval_1_weekend_start_minute: Uint16Field = Uint16Field("grid_use_interval_1_weekend_start_minute", 343, 1, Mode.RW, description="Grid Use Interval 1 Weekend Start Minute 0-59", units="Hour")
    grid_use_interval_1_weekend_stop_hour: Uint16Field = Uint16Field("grid_use_interval_1_weekend_stop_hour", 344, 1, Mode.RW, description="Grid Use Interval 1 Weekend Stop Hour 0-23", units="Hour")
    grid_use_interval_1_weekend_stop_minute: Uint16Field = Uint16Field("grid_use_interval_1_weekend_stop_minute", 345, 1, Mode.RW, description="Grid Use Interval 1 Weekend Stop Minute 0-59", units="Hour")
    grid_use_interval_2_mode: EnumUint16Field = EnumUint16Field("grid_use_interval_2_mode", 346, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("grid_use_interval_2_mode", [('Disabled', 0), ('Enabled', 1)]))
    grid_use_interval_2_weekday_start_hour: Uint16Field = Uint16Field("grid_use_interval_2_weekday_start_hour", 347, 1, Mode.RW, description="Grid Use Interval 2 Weekday Start Hour 0-23", units="Hour")
    grid_use_interval_2_weekday_start_minute: Uint16Field = Uint16Field("grid_use_interval_2_weekday_start_minute", 348, 1, Mode.RW, description="Grid Use Interval 2 Weekday Start Minute 0-59", units="Hour")
    grid_use_interval_2_weekday_stop_hour: Uint16Field = Uint16Field("grid_use_interval_2_weekday_stop_hour", 349, 1, Mode.RW, description="Grid Use Interval 2 Weekday Stop Hour 0-23", units="Hour")
    grid_use_interval_2_weekday_stop_minute: Uint16Field = Uint16Field("grid_use_interval_2_weekday_stop_minute", 350, 1, Mode.RW, description="Grid Use Interval 2 Weekday Stop Minute 0-59", units="Hour")
    grid_use_interval_3_mode: EnumUint16Field = EnumUint16Field("grid_use_interval_3_mode", 351, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("grid_use_interval_3_mode", [('Disabled', 0), ('Enabled', 1)]))
    grid_use_interval_3_weekday_start_hour: Uint16Field = Uint16Field("grid_use_interval_3_weekday_start_hour", 352, 1, Mode.RW, description="Grid Use Interval 3 Weekday Start Hour 0-23", units="Hour")
    grid_use_interval_3_weekday_start_minute: Uint16Field = Uint16Field("grid_use_interval_3_weekday_start_minute", 353, 1, Mode.RW, description="Grid Use Interval 3 Weekday Start Minute 0-59", units="Hour")
    grid_use_interval_3_weekday_stop_hour: Uint16Field = Uint16Field("grid_use_interval_3_weekday_stop_hour", 354, 1, Mode.RW, description="Grid Use Interval 3 Weekday Stop Hour 0-23", units="Hour")
    grid_use_interval_3_weekday_stop_minute: Uint16Field = Uint16Field("grid_use_interval_3_weekday_stop_minute", 355, 1, Mode.RW, description="Grid Use Interval 3 Weekday Stop Minute 0-59", units="Hour")
    load_grid_transfer_mode: EnumUint16Field = EnumUint16Field("load_grid_transfer_mode", 356, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("load_grid_transfer_mode", [('Disabled', 0), ('Enabled', 1)]))
    load_grid_transfer_threshold: Uint16Field = Uint16Field("load_grid_transfer_threshold", 357, 1, Mode.RW, description="Load Grid Transfer Threshold kW", units="kWatts")
    load_grid_transfer_connect_delay: Uint16Field = Uint16Field("load_grid_transfer_connect_delay", 358, 1, Mode.RW, description="Load Grid Transfer Connect Delay Seconds", units="Seconds")
    load_grid_transfer_disconnect_delay: Uint16Field = Uint16Field("load_grid_transfer_disconnect_delay", 359, 1, Mode.RW, description="Load Grid Transfer Disconnect Delay Seconds", units="Seconds")
    load_grid_transfer_connect_battery_voltage: Uint16Field = Uint16Field("load_grid_transfer_connect_battery_voltage", 360, 1, Mode.RW, description="Load Grid Transfer Low Battery Connect Voltage", units="Volts")
    load_grid_transfer_re_connect_battery_voltage: Uint16Field = Uint16Field("load_grid_transfer_re_connect_battery_voltage", 361, 1, Mode.RW, description="Load Grid Transfer Low Battery Re-Connect Voltage", units="Volts")
    global_charger_control_mode: EnumUint16Field = EnumUint16Field("global_charger_control_mode", 362, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("global_charger_control_mode", [('Disabled', 0), ('Enabled', 1)]))
    global_charger_control_output_limit: Uint16Field = Uint16Field("global_charger_control_output_limit", 363, 1, Mode.RW, description="Global Charger Output Limit Amps", units="Amps")
    radian_ac_coupled_control_mode: EnumUint16Field = EnumUint16Field("radian_ac_coupled_control_mode", 364, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("radian_ac_coupled_control_mode", [('Disabled', 0), ('Enabled', 1)]))
    radian_ac_coupled_aux_port: Uint16Field = Uint16Field("radian_ac_coupled_aux_port", 365, 1, Mode.RW, description="Radian Inverter Port Number for AUX Control 0-10", units="Port")
    url_update_lock: Uint32Field = Uint32Field("url_update_lock", 366, 2, Mode.W, description="Unlock Key", units="key")
    web_reporting_base_url: StringField = StringField("web_reporting_base_url", 368, 20, Mode.RW, description="WEB Reporting Base URL")
    web_user_logged_in_status: EnumUint16Field = EnumUint16Field("web_user_logged_in_status", 388, 1, Mode.RW, description="0=WEB User NOT logged in, 1=WEB user logged in", options=Enum("web_user_logged_in_status", [('WEB User NOT logged in', 0), ('WEB user logged in', 1)]))
    hub_type: EnumUint16Field = EnumUint16Field("hub_type", 389, 1, Mode.R, description="0=Legecy HUB, 4= HUB4, 10=HUB10.3, 11=HUB3PH", options=Enum("hub_type", [('HUB10.3', 10), ('HUB3PH', 11), ('HUB4', 4), ('Legecy HUB', 0)]))
    hub_major_firmware_number: Uint16Field = Uint16Field("hub_major_firmware_number", 390, 1, Mode.R, description="HUB Major firmware revision")
    hub_mid_firmware_number: Uint16Field = Uint16Field("hub_mid_firmware_number", 391, 1, Mode.R, description="HUB Mid firmware revision")
    hub_minor_firmware_number: Uint16Field = Uint16Field("hub_minor_firmware_number", 392, 1, Mode.R, description="HUB Minor firmware revision")
    year: Uint16Field = Uint16Field("year", 393, 1, Mode.RW, description="Clock year (4 digit)")
    month: Uint16Field = Uint16Field("month", 394, 1, Mode.RW, description="Clock Month (1 - 12)")
    day: Uint16Field = Uint16Field("day", 395, 1, Mode.RW, description="Clock Day (1 - 31)")
    hour: Uint16Field = Uint16Field("hour", 396, 1, Mode.RW, description="Clock Hour (0 - 23)")
    minute: Uint16Field = Uint16Field("minute", 397, 1, Mode.RW, description="Clock Minute (0 - 59)")
    second: Uint16Field = Uint16Field("second", 398, 1, Mode.RW, description="Clock Second (0 - 59)")
    temp_battery: Int16Field = Int16Field("temp_battery", 399, 1, Mode.R, description="Battery temp in degrees C", units="Degrees C")
    temp_ambient: Int16Field = Int16Field("temp_ambient", 400, 1, Mode.R, description="Ambient temp from temp sensor connected to device, in degrees C", units="Degrees C")
    temp_scale_factor: Int16Field = Int16Field("temp_scale_factor", 401, 1, Mode.R, description="Temperature Scale Factor")
    error: Bit16Field = Bit16Field("error", 402, 1, Mode.R, description="Bit field for errors. See Outback_Error Table", flags=OutBackErrorFlags)
    status: Bit16Field = Bit16Field("status", 403, 1, Mode.R, description="Bit field for status.See Outback_Status Table", flags=OutBackStatusFlags)
    update_device_firmware_port: Bit16Field = Bit16Field("update_device_firmware_port", 404, 1, Mode.RW, description="Device Firmware update See Device_FW_Update", flags=OutBackUpdateDeviceFirmwarePortFlags)
    gateway_type: EnumUint16Field = EnumUint16Field("gateway_type", 405, 1, Mode.R, description="1=AXS Port, 2= MATE3", options=Enum("gateway_type", [('AXS Port', 1), ('MATE3', 2)]))
    system_voltage: Uint16Field = Uint16Field("system_voltage", 406, 1, Mode.R, description="12, 24, 26, 48 or 60 VDC", units="Volts")
    measured_system_voltage: Uint16Field = Uint16Field("measured_system_voltage", 407, 1, Mode.R, description="Current system battery voltage computed by gateway", units="Volts")
    ags_ac_reconnect_delay: Uint16Field = Uint16Field("ags_ac_reconnect_delay", 408, 1, Mode.RW, description="AGS AC Reconnect Delay", units="Minute")
    multi_phase_coordination: EnumUint16Field = EnumUint16Field("multi_phase_coordination", 409, 1, Mode.RW, description="0=Disabled, 1=Enabled", options=Enum("multi_phase_coordination", [('Disabled', 0), ('Enabled', 1)]))
    sched_1_ac_mode: EnumInt16Field = EnumInt16Field("sched_1_ac_mode", 410, 1, Mode.RW, description="Scheduled Input Mode: -1=Disable, 0=Generator, 1=Support, 2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero", options=Enum("sched_1_ac_mode", [('Backup', 4), ('Disable', -1), ('Generator', 0), ('Grid Tied', 2), ('Grid Zero', 6), ('Mini Grid', 5), ('Support', 1), ('UPS', 3)]))
    sched_1_ac_mode_hour: Uint16Field = Uint16Field("sched_1_ac_mode_hour", 411, 1, Mode.RW, description="Start Hour for AC Input Mode schedule 1", units="Hour")
    sched_1_ac_mode_minute: Uint16Field = Uint16Field("sched_1_ac_mode_minute", 412, 1, Mode.RW, description="Start Minute for AC Input Mode schedule 1", units="Minute")
    sched_2_ac_mode: EnumInt16Field = EnumInt16Field("sched_2_ac_mode", 413, 1, Mode.RW, description="Scheduled Input Mode: -1=Disable, 0=Generator, 1=Support, 2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero", options=Enum("sched_2_ac_mode", [('Backup', 4), ('Disable', -1), ('Generator', 0), ('Grid Tied', 2), ('Grid Zero', 6), ('Mini Grid', 5), ('Support', 1), ('UPS', 3)]))
    sched_2_ac_mode_hour: Uint16Field = Uint16Field("sched_2_ac_mode_hour", 414, 1, Mode.RW, description="Start Hour for AC Input Mode schedule 2", units="Hour")
    sched_2_ac_mode_minute: Uint16Field = Uint16Field("sched_2_ac_mode_minute", 415, 1, Mode.RW, description="Start Minute for AC Input Mode schedule 2", units="Minute")
    sched_3_ac_mode: EnumInt16Field = EnumInt16Field("sched_3_ac_mode", 416, 1, Mode.RW, description="Scheduled Input Mode: -1=Disable, 0=Generator, 1=Support, 2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero", options=Enum("sched_3_ac_mode", [('Backup', 4), ('Disable', -1), ('Generator', 0), ('Grid Tied', 2), ('Grid Zero', 6), ('Mini Grid', 5), ('Support', 1), ('UPS', 3)]))
    sched_3_ac_mode_hour: Uint16Field = Uint16Field("sched_3_ac_mode_hour", 417, 1, Mode.RW, description="Start Hour for AC Input Mode schedule 3", units="Hour")
    sched_3_ac_mode_minute: Uint16Field = Uint16Field("sched_3_ac_mode_minute", 418, 1, Mode.RW, description="Start Minute for AC Input Mode schedule 3", units="Minute")
    auto_reboot: EnumUint16Field = EnumUint16Field("auto_reboot", 419, 1, Mode.RW, description="OPTICS auto reboot every 24 hours 0=Disable, 1=Enable", options=Enum("auto_reboot", [('Disable', 0), ('Enable', 1)]))
    time_zone_scale_factor: Int16Field = Int16Field("time_zone_scale_factor", 420, 1, Mode.R, description="Time Zone scale factor")
    spare_reg_3: Uint16Field = Uint16Field("spare_reg_3", 421, 1, Mode.RW, description="Spare Register 3")
    spare_reg_4: Uint16Field = Uint16Field("spare_reg_4", 422, 1, Mode.RW, description="Spare Register 4")


OutBackModel.set_time_zone.scale_factor = OutBackModel.time_zone_scale_factor
OutBackModel.ags_dc_gen_absorb_voltage.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.ags_dc_gen_absorb_time.scale_factor = OutBackModel.hour_scale_factor
OutBackModel.ags_2_min_start_voltage.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.ags_2_hour_start_voltage.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.ags_24_hour_start_voltage.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.hbx_grid_connect_voltage.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.hbx_grid_connect_delay.scale_factor = OutBackModel.hour_scale_factor
OutBackModel.hbx_grid_disconnect_voltage.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.hbx_grid_disconnect_delay.scale_factor = OutBackModel.hour_scale_factor
OutBackModel.load_grid_transfer_threshold.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.load_grid_transfer_connect_battery_voltage.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.load_grid_transfer_re_connect_battery_voltage.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.measured_system_voltage.scale_factor = OutBackModel.voltage_scale_factor
OutBackModel.__model_fields__ = [OutBackModel.did, OutBackModel.length, OutBackModel.major_firmware_number, OutBackModel.mid_firmware_number, OutBackModel.minor_firmware_number, OutBackModel.encryption_key, OutBackModel.mac_address, OutBackModel.write_password, OutBackModel.enable_dhcp, OutBackModel.tcpip_address, OutBackModel.tcpip_gateway_msw, OutBackModel.tcpip_netmask_msw, OutBackModel.tcpip_dns_1_msw, OutBackModel.tcpip_dns_2_msw, OutBackModel.modbus_port, OutBackModel.smtp_server_name, OutBackModel.smtp_account_name, OutBackModel.smtp_ssl_enable, OutBackModel.smtp_email_password, OutBackModel.smtp_email_user_name, OutBackModel.status_email_interval, OutBackModel.status_email_status_time, OutBackModel.status_email_subject_line, OutBackModel.status_email_to_address_1, OutBackModel.status_email_to_address_2, OutBackModel.alarm_email_enable, OutBackModel.system_name, OutBackModel.alarm_email_to_address_1, OutBackModel.alarm_email_to_address_2, OutBackModel.ftp_password, OutBackModel.telnet_password, OutBackModel.sd_card_data_log_write_interval, OutBackModel.sd_card_data_log_retain_days, OutBackModel.sd_card_data_logging_mode, OutBackModel.time_server_name, OutBackModel.enable_time_server, OutBackModel.set_time_zone, OutBackModel.enable_float_coordination, OutBackModel.enable_fndc_charge_termination, OutBackModel.enable_fndc_grid_tie_control, OutBackModel.voltage_scale_factor, OutBackModel.hour_scale_factor, OutBackModel.ags_mode, OutBackModel.ags_port, OutBackModel.ags_port_type, OutBackModel.ags_generator_type, OutBackModel.ags_dc_gen_absorb_voltage, OutBackModel.ags_dc_gen_absorb_time, OutBackModel.ags_fault_time, OutBackModel.ags_gen_cool_down_time, OutBackModel.ags_gen_warm_up_time, OutBackModel.ags_generator_exercise_mode, OutBackModel.ags_exercise_start_hour, OutBackModel.ags_exercise_start_minute, OutBackModel.ags_exercise_day, OutBackModel.ags_exercise_period, OutBackModel.ags_exercise_interval, OutBackModel.ags_sell_mode, OutBackModel.ags_2_min_start_mode, OutBackModel.ags_2_min_start_voltage, OutBackModel.ags_2_hour_start_mode, OutBackModel.ags_2_hour_start_voltage, OutBackModel.ags_24_hour_start_mode, OutBackModel.ags_24_hour_start_voltage, OutBackModel.ags_load_start_mode, OutBackModel.ags_load_start_kw, OutBackModel.ags_load_start_delay, OutBackModel.ags_load_stop_kw, OutBackModel.ags_load_stop_delay, OutBackModel.ags_soc_start_mode, OutBackModel.ags_soc_start_percentage, OutBackModel.ags_soc_stop_percentage, OutBackModel.ags_enable_full_charge_mode, OutBackModel.ags_full_charge_interval, OutBackModel.ags_must_run_mode, OutBackModel.ags_must_run_weekday_start_hour, OutBackModel.ags_must_run_weekday_start_minute, OutBackModel.ags_must_run_weekday_stop_hour, OutBackModel.ags_must_run_weekday_stop_minute, OutBackModel.ags_must_run_weekend_start_hour, OutBackModel.ags_must_run_weekend_start_minute, OutBackModel.ags_must_run_weekend_stop_hour, OutBackModel.ags_must_run_weekend_stop_minute, OutBackModel.ags_quiet_time_mode, OutBackModel.ags_quiet_time_weekday_start_hour, OutBackModel.ags_quiet_time_weekday_start_minute, OutBackModel.ags_quiet_time_weekday_stop_hour, OutBackModel.ags_quiet_time_weekday_stop_minute, OutBackModel.ags_quiet_time_weekend_start_hour, OutBackModel.ags_quiet_time_weekend_start_minute, OutBackModel.ags_quiet_time_weekend_stop_hour, OutBackModel.ags_quiet_time_weekend_stop_minute, OutBackModel.ags_total_generator_run_time, OutBackModel.hbx_mode, OutBackModel.hbx_grid_connect_voltage, OutBackModel.hbx_grid_connect_delay, OutBackModel.hbx_grid_disconnect_voltage, OutBackModel.hbx_grid_disconnect_delay, OutBackModel.hbx_grid_connect_soc, OutBackModel.hbx_grid_disconnect_soc, OutBackModel.grid_use_interval_1_mode, OutBackModel.grid_use_interval_1_weekday_start_hour, OutBackModel.grid_use_interval_1_weekday_start_minute, OutBackModel.grid_use_interval_1_weekday_stop_hour, OutBackModel.grid_use_interval_1_weekday_stop_minute, OutBackModel.grid_use_interval_1_weekend_start_hour, OutBackModel.grid_use_interval_1_weekend_start_minute, OutBackModel.grid_use_interval_1_weekend_stop_hour, OutBackModel.grid_use_interval_1_weekend_stop_minute, OutBackModel.grid_use_interval_2_mode, OutBackModel.grid_use_interval_2_weekday_start_hour, OutBackModel.grid_use_interval_2_weekday_start_minute, OutBackModel.grid_use_interval_2_weekday_stop_hour, OutBackModel.grid_use_interval_2_weekday_stop_minute, OutBackModel.grid_use_interval_3_mode, OutBackModel.grid_use_interval_3_weekday_start_hour, OutBackModel.grid_use_interval_3_weekday_start_minute, OutBackModel.grid_use_interval_3_weekday_stop_hour, OutBackModel.grid_use_interval_3_weekday_stop_minute, OutBackModel.load_grid_transfer_mode, OutBackModel.load_grid_transfer_threshold, OutBackModel.load_grid_transfer_connect_delay, OutBackModel.load_grid_transfer_disconnect_delay, OutBackModel.load_grid_transfer_connect_battery_voltage, OutBackModel.load_grid_transfer_re_connect_battery_voltage, OutBackModel.global_charger_control_mode, OutBackModel.global_charger_control_output_limit, OutBackModel.radian_ac_coupled_control_mode, OutBackModel.radian_ac_coupled_aux_port, OutBackModel.url_update_lock, OutBackModel.web_reporting_base_url, OutBackModel.web_user_logged_in_status, OutBackModel.hub_type, OutBackModel.hub_major_firmware_number, OutBackModel.hub_mid_firmware_number, OutBackModel.hub_minor_firmware_number, OutBackModel.year, OutBackModel.month, OutBackModel.day, OutBackModel.hour, OutBackModel.minute, OutBackModel.second, OutBackModel.temp_battery, OutBackModel.temp_ambient, OutBackModel.temp_scale_factor, OutBackModel.error, OutBackModel.status, OutBackModel.update_device_firmware_port, OutBackModel.gateway_type, OutBackModel.system_voltage, OutBackModel.measured_system_voltage, OutBackModel.ags_ac_reconnect_delay, OutBackModel.multi_phase_coordination, OutBackModel.sched_1_ac_mode, OutBackModel.sched_1_ac_mode_hour, OutBackModel.sched_1_ac_mode_minute, OutBackModel.sched_2_ac_mode, OutBackModel.sched_2_ac_mode_hour, OutBackModel.sched_2_ac_mode_minute, OutBackModel.sched_3_ac_mode, OutBackModel.sched_3_ac_mode_hour, OutBackModel.sched_3_ac_mode_minute, OutBackModel.auto_reboot, OutBackModel.time_zone_scale_factor, OutBackModel.spare_reg_3, OutBackModel.spare_reg_4]

class ChargeControllerModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Basic Charge Controller")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
    voltage_scale_factor: Int16Field = Int16Field("voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
    current_scale_factor: Int16Field = Int16Field("current_scale_factor", 5, 1, Mode.R, description="DC Current Scale Factor")
    power_scale_factor: Int16Field = Int16Field("power_scale_factor", 6, 1, Mode.R, description="DC Power Scale Factor")
    ah_scale_factor: Int16Field = Int16Field("ah_scale_factor", 7, 1, Mode.R, description="DC Amp Hours Scale Factor")
    kwh_scale_factor: Int16Field = Int16Field("kwh_scale_factor", 8, 1, Mode.R, description="DC kWH Scale Factor")
    battery_voltage: Uint16Field = Uint16Field("battery_voltage", 9, 1, Mode.R, description="Battery Voltage", units="Volts")
    array_voltage: Uint16Field = Uint16Field("array_voltage", 10, 1, Mode.R, description="DC Source Voltage", units="Volts")
    battery_current: Uint16Field = Uint16Field("battery_current", 11, 1, Mode.R, description="Battery Current", units="Amps")
    array_current: Uint16Field = Uint16Field("array_current", 12, 1, Mode.R, description="DC Source Current", units="Amps")
    charger_state: EnumUint16Field = EnumUint16Field("charger_state", 13, 1, Mode.R, description="0 = Silent; 1 = Float; 2 = Bulk; 3 = Absorb; 4 = EQ", options=Enum("charger_state", [('Absorb', 3), ('Bulk', 2), ('EQ', 4), ('Float', 1), ('Silent', 0)]))
    watts: Uint16Field = Uint16Field("watts", 14, 1, Mode.R, description="CC Wattage Output", units="Watts")
    todays_min_battery_volts: Uint16Field = Uint16Field("todays_min_battery_volts", 15, 1, Mode.R, description="Minimum Voltage for battery today", units="Volts")
    todays_max_battery_volts: Uint16Field = Uint16Field("todays_max_battery_volts", 16, 1, Mode.R, description="Maximum Voltage for battery today", units="Volts")
    voc: Uint16Field = Uint16Field("voc", 17, 1, Mode.R, description="Last Open Circuit Voltage (array)", units="Volts")
    todays_peak_voc: Uint16Field = Uint16Field("todays_peak_voc", 18, 1, Mode.R, description="Highest VOC today", units="Volts")
    todays_kwh: Uint16Field = Uint16Field("todays_kwh", 19, 1, Mode.R, description="Daily accumulated Kwatt hours output", units="KWH")
    todays_ah: Uint16Field = Uint16Field("todays_ah", 20, 1, Mode.R, description="Daily accumulated amp hours output", units="AH")
    lifetime_kwh_hours: Uint16Field = Uint16Field("lifetime_kwh_hours", 21, 1, Mode.R, description="Lifetime Total Kwatt Hours", units="KWH")
    lifetime_k_amp_hours: Uint16Field = Uint16Field("lifetime_k_amp_hours", 22, 1, Mode.R, description="Lifetime Total K-Amp Hours", units="Amps")
    lifetime_max_watts: Uint16Field = Uint16Field("lifetime_max_watts", 23, 1, Mode.R, description="Lifetime Maximum Wattage", units="Watts")
    lifetime_max_battery_volts: Uint16Field = Uint16Field("lifetime_max_battery_volts", 24, 1, Mode.R, description="Lifetime Maximum Battery Voltage", units="Volts")
    lifetime_max_voc: Uint16Field = Uint16Field("lifetime_max_voc", 25, 1, Mode.R, description="Lifetime Maximum VOC", units="Volts")
    temp_scale_factor: Uint16Field = Uint16Field("temp_scale_factor", 26, 1, Mode.R, description="FM80 Extreme Temperature scale factor")
    temp_output_fets: Int16Field = Int16Field("temp_output_fets", 27, 1, Mode.R, description="FM80 Extreme Output FET Temperature", units="Degrees C")
    temp_enclosure: Int16Field = Int16Field("temp_enclosure", 28, 1, Mode.R, description="FM80 Extreme Enclosure Temperature", units="Degrees C")


ChargeControllerModel.battery_voltage.scale_factor = ChargeControllerModel.voltage_scale_factor
ChargeControllerModel.array_voltage.scale_factor = ChargeControllerModel.voltage_scale_factor
ChargeControllerModel.battery_current.scale_factor = ChargeControllerModel.current_scale_factor
ChargeControllerModel.array_current.scale_factor = ChargeControllerModel.power_scale_factor
ChargeControllerModel.watts.scale_factor = ChargeControllerModel.power_scale_factor
ChargeControllerModel.todays_min_battery_volts.scale_factor = ChargeControllerModel.voltage_scale_factor
ChargeControllerModel.todays_max_battery_volts.scale_factor = ChargeControllerModel.voltage_scale_factor
ChargeControllerModel.voc.scale_factor = ChargeControllerModel.voltage_scale_factor
ChargeControllerModel.todays_kwh.scale_factor = ChargeControllerModel.kwh_scale_factor
ChargeControllerModel.todays_ah.scale_factor = ChargeControllerModel.ah_scale_factor
ChargeControllerModel.lifetime_k_amp_hours.scale_factor = ChargeControllerModel.kwh_scale_factor
ChargeControllerModel.lifetime_max_watts.scale_factor = ChargeControllerModel.power_scale_factor
ChargeControllerModel.lifetime_max_battery_volts.scale_factor = ChargeControllerModel.voltage_scale_factor
ChargeControllerModel.lifetime_max_voc.scale_factor = ChargeControllerModel.voltage_scale_factor
ChargeControllerModel.temp_output_fets.scale_factor = ChargeControllerModel.power_scale_factor
ChargeControllerModel.temp_enclosure.scale_factor = ChargeControllerModel.power_scale_factor
ChargeControllerModel.__model_fields__ = [ChargeControllerModel.did, ChargeControllerModel.length, ChargeControllerModel.port_number, ChargeControllerModel.voltage_scale_factor, ChargeControllerModel.current_scale_factor, ChargeControllerModel.power_scale_factor, ChargeControllerModel.ah_scale_factor, ChargeControllerModel.kwh_scale_factor, ChargeControllerModel.battery_voltage, ChargeControllerModel.array_voltage, ChargeControllerModel.battery_current, ChargeControllerModel.array_current, ChargeControllerModel.charger_state, ChargeControllerModel.watts, ChargeControllerModel.todays_min_battery_volts, ChargeControllerModel.todays_max_battery_volts, ChargeControllerModel.voc, ChargeControllerModel.todays_peak_voc, ChargeControllerModel.todays_kwh, ChargeControllerModel.todays_ah, ChargeControllerModel.lifetime_kwh_hours, ChargeControllerModel.lifetime_k_amp_hours, ChargeControllerModel.lifetime_max_watts, ChargeControllerModel.lifetime_max_battery_volts, ChargeControllerModel.lifetime_max_voc, ChargeControllerModel.temp_scale_factor, ChargeControllerModel.temp_output_fets, ChargeControllerModel.temp_enclosure]

class ChargeControllerConfigurationModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack FM Series Charge Controllers")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
    voltage_scale_factor: Int16Field = Int16Field("voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
    current_scale_factor: Int16Field = Int16Field("current_scale_factor", 5, 1, Mode.R, description="DC Current Scale Factor")
    hours_scale_factor: Int16Field = Int16Field("hours_scale_factor", 6, 1, Mode.R, description="Time in Hours Scale Factor")
    power_scale_factor: Int16Field = Int16Field("power_scale_factor", 7, 1, Mode.R, description="Power Scale Factor")
    ah_scale_factor: Int16Field = Int16Field("ah_scale_factor", 8, 1, Mode.R, description="Amp Hours Scale Factor")
    kwh_scale_factor: Int16Field = Int16Field("kwh_scale_factor", 9, 1, Mode.R, description="DC kWH Scale Factor")
    faults: Bit16Field = Bit16Field("faults", 10, 1, Mode.R, description="CC Error Flags: 0x0080=High VOC, 0x0040=Over Temp,  0x0020=Shorted Battery Temp Sensor, 0x0010=Fault Input Active", flags=CCconfigFaultsFlags)
    absorb_volts: Uint16Field = Uint16Field("absorb_volts", 11, 1, Mode.RW, description="Absorb Voltage Target", units="Volts")
    absorb_time_hours: Uint16Field = Uint16Field("absorb_time_hours", 12, 1, Mode.RW, description="Absorb Time Hours", units="Hours")
    absorb_end_amps: Uint16Field = Uint16Field("absorb_end_amps", 13, 1, Mode.RW, description="Amperage to end Absorbing", units="Amps")
    rebulk_volts: Uint16Field = Uint16Field("rebulk_volts", 14, 1, Mode.RW, description="Voltage to re-initiate Bulk charge", units="Volts")
    float_volts: Uint16Field = Uint16Field("float_volts", 15, 1, Mode.RW, description="Float Voltage Target", units="Volts")
    bulk_current: Uint16Field = Uint16Field("bulk_current", 16, 1, Mode.RW, description="Max Output Current Limit", units="Amps")
    eq_volts: Uint16Field = Uint16Field("eq_volts", 17, 1, Mode.RW, description="Target Voltage for Equalize", units="Volts")
    eq_time_hours: Uint16Field = Uint16Field("eq_time_hours", 18, 1, Mode.RW, description="EQ Time Hours", units="Hours")
    auto_eq_days: Uint16Field = Uint16Field("auto_eq_days", 19, 1, Mode.RW, description="Auto EQ Interval Days", units="Days")
    mppt_mode: EnumUint16Field = EnumUint16Field("mppt_mode", 20, 1, Mode.RW, description="0 = Auto; 1 = U-Pick", options=Enum("mppt_mode", [('Auto', 0), ('U-Pick', 1)]))
    sweep_width: EnumUint16Field = EnumUint16Field("sweep_width", 21, 1, Mode.RW, description="0 = Full; 1 = Half", options=Enum("sweep_width", [('Full', 0), ('Half', 1)]))
    sweep_max_percentage: EnumUint16Field = EnumUint16Field("sweep_max_percentage", 22, 1, Mode.RW, description="0 = 80; 1 = 85; 2 = 90; 3 = 99", options=Enum("sweep_max_percentage", [('80', 0), ('85', 1), ('90', 2), ('99', 3)]))
    u_pick_pwm_duty_cycle: Uint16Field = Uint16Field("u_pick_pwm_duty_cycle", 23, 1, Mode.RW, description="Park Duty Cycle (%) (40% - 90%)", units="Percentage")
    grid_tie_mode: EnumUint16Field = EnumUint16Field("grid_tie_mode", 24, 1, Mode.RW, description="0 = Grid Tie Mode disabled; 1 = Grid Tie Mode enabled", options=Enum("grid_tie_mode", [('Grid Tie Mode disabled', 0), ('Grid Tie Mode enabled', 1)]))
    temp_comp_mode: EnumUint16Field = EnumUint16Field("temp_comp_mode", 25, 1, Mode.RW, description="0 = Wide; 1 = User Limited", options=Enum("temp_comp_mode", [('User Limited', 1), ('Wide', 0)]))
    temp_comp_lower_limit_volts: Uint16Field = Uint16Field("temp_comp_lower_limit_volts", 26, 1, Mode.RW, description="RTS compensation lower voltage limit", units="Volts")
    temp_comp_upper_limit_volts: Uint16Field = Uint16Field("temp_comp_upper_limit_volts", 27, 1, Mode.RW, description="RTS compensation upper voltage limit", units="Volts")
    temp_comp_slope: Uint16Field = Uint16Field("temp_comp_slope", 28, 1, Mode.RW, description="RTS temp compensation Slope 2-6 mV per Degree C", units="Milli Volts")
    auto_restart_mode: EnumUint16Field = EnumUint16Field("auto_restart_mode", 29, 1, Mode.RW, description="0 = Off; 1 = Restart every 90 minutes; 2 = Restart every 90 minutes if absorb charging or float charging", options=Enum("auto_restart_mode", [('Off', 0), ('Restart every 90 minutes', 1), ('Restart every 90 minutes if absorb charging or float charging', 2)]))
    wakeup_voc: Uint16Field = Uint16Field("wakeup_voc", 30, 1, Mode.RW, description="VOC change which causes Wakeup occurs", units="Volts")
    snooze_mode_amps: Uint16Field = Uint16Field("snooze_mode_amps", 31, 1, Mode.RW, description="Snooze Mode Amps", units="Amps")
    wakeup_interval: Uint16Field = Uint16Field("wakeup_interval", 32, 1, Mode.RW, description="How often to check for Wakeup condition", units="Mins")
    aux_mode: EnumUint16Field = EnumUint16Field("aux_mode", 33, 1, Mode.RW, description="0 = Float; 1 = Diversion: Relay; 2 = Diversion: Solid St; 3 = Low Batt Disconnect; 4 = Remote; 5 = Vent Fan; 6 = PV Trigger; 7 = Error Output; 8 = Night Light", options=Enum("aux_mode", [('Diversion: Relay', 1), ('Diversion: Solid St', 2), ('Error Output', 7), ('Float', 0), ('Low Batt Disconnect', 3), ('Night Light', 8), ('PV Trigger', 6), ('Remote', 4), ('Vent Fan', 5)]))
    aux_control: EnumUint16Field = EnumUint16Field("aux_control", 34, 1, Mode.RW, description="0 = Off; 1 = Auto; 2 = On", options=Enum("aux_control", [('Auto', 1), ('Off', 0), ('On', 2)]))
    aux_state: EnumUint16Field = EnumUint16Field("aux_state", 35, 1, Mode.R, description="0 = Disabled; 1 = Enabled", options=Enum("aux_state", [('Disabled', 0), ('Enabled', 1)]))
    aux_polarity: EnumUint16Field = EnumUint16Field("aux_polarity", 36, 1, Mode.RW, description="0 = Low; 1 = High", options=Enum("aux_polarity", [('High', 1), ('Low', 0)]))
    aux_low_battery_disconnect: Uint16Field = Uint16Field("aux_low_battery_disconnect", 37, 1, Mode.RW, description="Low Battery Disconnect Voltage", units="Volts")
    aux_low_battery_reconnect: Uint16Field = Uint16Field("aux_low_battery_reconnect", 38, 1, Mode.RW, description="Low Battery Reconnect Volts", units="Volts")
    aux_low_battery_disconnect_delay: Uint16Field = Uint16Field("aux_low_battery_disconnect_delay", 39, 1, Mode.RW, description="Low Battery Disconnect Delay (secs)", units="Secs")
    aux_vent_fan_volts: Uint16Field = Uint16Field("aux_vent_fan_volts", 40, 1, Mode.RW, description="Vent Fan Voltage", units="Volts")
    aux_pv_limit_volts: Uint16Field = Uint16Field("aux_pv_limit_volts", 41, 1, Mode.RW, description="Voltage at which PV disconnect occurs", units="Volts")
    aux_pv_limit_hold_time: Uint16Field = Uint16Field("aux_pv_limit_hold_time", 42, 1, Mode.RW, description="AUX PV Trigger Hold Time", units="Secs")
    aux_night_light_thres_volts: Uint16Field = Uint16Field("aux_night_light_thres_volts", 43, 1, Mode.RW, description="Voltage Threshold for AUX Night Light", units="Volts")
    night_light_on_hours: Uint16Field = Uint16Field("night_light_on_hours", 44, 1, Mode.RW, description="Night Light ON Time", units="Hours")
    night_light_on_hyst_time: Uint16Field = Uint16Field("night_light_on_hyst_time", 45, 1, Mode.RW, description="Night Light ON Hyst Time", units="Mins")
    night_light_off_hyst_time: Uint16Field = Uint16Field("night_light_off_hyst_time", 46, 1, Mode.RW, description="Night Light OFF Hyst Time", units="Mins")
    aux_error_battery_volts: Uint16Field = Uint16Field("aux_error_battery_volts", 47, 1, Mode.RW, description="Battery voltage at which Aux Error occurs", units="Volts")
    aux_divert_hold_time: Uint16Field = Uint16Field("aux_divert_hold_time", 48, 1, Mode.RW, description="AUX Diver Hold Time", units="Seconds")
    aux_divert_delay_time: Uint16Field = Uint16Field("aux_divert_delay_time", 49, 1, Mode.RW, description="AUX Divert Delay", units="Secs")
    aux_divert_relative_volts: Int16Field = Int16Field("aux_divert_relative_volts", 50, 1, Mode.RW, description="AUX Divert Relative Volts", units="Volts")
    aux_divert_hyst_volts: Uint16Field = Uint16Field("aux_divert_hyst_volts", 51, 1, Mode.RW, description="AUX Divert Hyst Volts", units="Volts")
    major_firmware_number: Uint16Field = Uint16Field("major_firmware_number", 52, 1, Mode.R, description="Charge Controller Major firmware revision")
    mid_firmware_number: Uint16Field = Uint16Field("mid_firmware_number", 53, 1, Mode.R, description="Charge Controller Mid firmware revision")
    minor_firmware_number: Uint16Field = Uint16Field("minor_firmware_number", 54, 1, Mode.R, description="Charge Controller Minor firmware revision")
    set_data_log_day_offset: Uint16Field = Uint16Field("set_data_log_day_offset", 55, 1, Mode.RW, description="Day offset 0-128, 0 =Today, 1 = -1 day \u2026", units="Days")
    get_current_data_log_day_offset: Uint16Field = Uint16Field("get_current_data_log_day_offset", 56, 1, Mode.R, description="Current Data Log Day Offset", units="Days")
    data_log_daily_ah: Uint16Field = Uint16Field("data_log_daily_ah", 57, 1, Mode.R, description="Data Log AH", units="AH")
    data_log_daily_kwh: Uint16Field = Uint16Field("data_log_daily_kwh", 58, 1, Mode.R, description="Data Log kWH", units="KWH")
    data_log_daily_max_output_amps: Uint16Field = Uint16Field("data_log_daily_max_output_amps", 59, 1, Mode.R, description="Data Log maximum Output Amps", units="Amps")
    data_log_daily_max_output_watts: Uint16Field = Uint16Field("data_log_daily_max_output_watts", 60, 1, Mode.R, description="Data Log maximum Output Wattage", units="Watts")
    data_log_daily_absorb_time: Uint16Field = Uint16Field("data_log_daily_absorb_time", 61, 1, Mode.R, description="Data Log Absorb Time Minutes", units="Mins")
    data_log_daily_float_time: Uint16Field = Uint16Field("data_log_daily_float_time", 62, 1, Mode.R, description="Data Log Float Time Minutes", units="Mins")
    data_log_daily_min_battery_volts: Uint16Field = Uint16Field("data_log_daily_min_battery_volts", 63, 1, Mode.R, description="Data Log minimum daily battery voltage", units="Volts")
    data_log_daily_max_battery_volts: Uint16Field = Uint16Field("data_log_daily_max_battery_volts", 64, 1, Mode.R, description="Data Log maximum daily battery voltage", units="Volts")
    data_log_daily_max_input_volts: Uint16Field = Uint16Field("data_log_daily_max_input_volts", 65, 1, Mode.R, description="Data Log maximum daily input voltage", units="Volts")
    clear_data_log_read: Uint16Field = Uint16Field("clear_data_log_read", 66, 1, Mode.R, description="Read value needed to clear data log")
    clear_data_log_write_complement: Uint16Field = Uint16Field("clear_data_log_write_complement", 67, 1, Mode.W, description="Write value's complement to clear data log")
    stats_maximum_reset_read: Uint16Field = Uint16Field("stats_maximum_reset_read", 68, 1, Mode.R, description="Read value needed to clear Stats Maximums")
    stats_maximum_write_complement: Uint16Field = Uint16Field("stats_maximum_write_complement", 69, 1, Mode.W, description="Write value's complement to clear Stats Maximums")
    stats_totals_reset_read: Uint16Field = Uint16Field("stats_totals_reset_read", 70, 1, Mode.R, description="Read value nneded to clear Stats Totals")
    stats_totals_write_complement: Uint16Field = Uint16Field("stats_totals_write_complement", 71, 1, Mode.W, description="Write value's complement to clear Stats Totals")
    battery_voltage_calibrate_offset: Int16Field = Int16Field("battery_voltage_calibrate_offset", 72, 1, Mode.RW, description="Battery voltage calibration offset", units="DC Volts")
    serial_number: StringField = StringField("serial_number", 73, 9, Mode.R, description="Device serial number")
    model_number: StringField = StringField("model_number", 82, 9, Mode.R, description="Device model")


ChargeControllerConfigurationModel.absorb_volts.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.absorb_time_hours.scale_factor = ChargeControllerConfigurationModel.hours_scale_factor
ChargeControllerConfigurationModel.rebulk_volts.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.float_volts.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.bulk_current.scale_factor = ChargeControllerConfigurationModel.current_scale_factor
ChargeControllerConfigurationModel.eq_volts.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.u_pick_pwm_duty_cycle.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.temp_comp_lower_limit_volts.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.temp_comp_upper_limit_volts.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.wakeup_voc.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.snooze_mode_amps.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_low_battery_disconnect.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_low_battery_reconnect.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_vent_fan_volts.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_pv_limit_volts.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_pv_limit_hold_time.scale_factor = ChargeControllerConfigurationModel.hours_scale_factor
ChargeControllerConfigurationModel.aux_night_light_thres_volts.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_error_battery_volts.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_divert_hold_time.scale_factor = ChargeControllerConfigurationModel.hours_scale_factor
ChargeControllerConfigurationModel.aux_divert_relative_volts.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.aux_divert_hyst_volts.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.data_log_daily_ah.scale_factor = ChargeControllerConfigurationModel.ah_scale_factor
ChargeControllerConfigurationModel.data_log_daily_kwh.scale_factor = ChargeControllerConfigurationModel.kwh_scale_factor
ChargeControllerConfigurationModel.data_log_daily_max_output_amps.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.data_log_daily_max_output_watts.scale_factor = ChargeControllerConfigurationModel.power_scale_factor
ChargeControllerConfigurationModel.data_log_daily_min_battery_volts.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.data_log_daily_max_battery_volts.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.battery_voltage_calibrate_offset.scale_factor = ChargeControllerConfigurationModel.voltage_scale_factor
ChargeControllerConfigurationModel.__model_fields__ = [ChargeControllerConfigurationModel.did, ChargeControllerConfigurationModel.length, ChargeControllerConfigurationModel.port_number, ChargeControllerConfigurationModel.voltage_scale_factor, ChargeControllerConfigurationModel.current_scale_factor, ChargeControllerConfigurationModel.hours_scale_factor, ChargeControllerConfigurationModel.power_scale_factor, ChargeControllerConfigurationModel.ah_scale_factor, ChargeControllerConfigurationModel.kwh_scale_factor, ChargeControllerConfigurationModel.faults, ChargeControllerConfigurationModel.absorb_volts, ChargeControllerConfigurationModel.absorb_time_hours, ChargeControllerConfigurationModel.absorb_end_amps, ChargeControllerConfigurationModel.rebulk_volts, ChargeControllerConfigurationModel.float_volts, ChargeControllerConfigurationModel.bulk_current, ChargeControllerConfigurationModel.eq_volts, ChargeControllerConfigurationModel.eq_time_hours, ChargeControllerConfigurationModel.auto_eq_days, ChargeControllerConfigurationModel.mppt_mode, ChargeControllerConfigurationModel.sweep_width, ChargeControllerConfigurationModel.sweep_max_percentage, ChargeControllerConfigurationModel.u_pick_pwm_duty_cycle, ChargeControllerConfigurationModel.grid_tie_mode, ChargeControllerConfigurationModel.temp_comp_mode, ChargeControllerConfigurationModel.temp_comp_lower_limit_volts, ChargeControllerConfigurationModel.temp_comp_upper_limit_volts, ChargeControllerConfigurationModel.temp_comp_slope, ChargeControllerConfigurationModel.auto_restart_mode, ChargeControllerConfigurationModel.wakeup_voc, ChargeControllerConfigurationModel.snooze_mode_amps, ChargeControllerConfigurationModel.wakeup_interval, ChargeControllerConfigurationModel.aux_mode, ChargeControllerConfigurationModel.aux_control, ChargeControllerConfigurationModel.aux_state, ChargeControllerConfigurationModel.aux_polarity, ChargeControllerConfigurationModel.aux_low_battery_disconnect, ChargeControllerConfigurationModel.aux_low_battery_reconnect, ChargeControllerConfigurationModel.aux_low_battery_disconnect_delay, ChargeControllerConfigurationModel.aux_vent_fan_volts, ChargeControllerConfigurationModel.aux_pv_limit_volts, ChargeControllerConfigurationModel.aux_pv_limit_hold_time, ChargeControllerConfigurationModel.aux_night_light_thres_volts, ChargeControllerConfigurationModel.night_light_on_hours, ChargeControllerConfigurationModel.night_light_on_hyst_time, ChargeControllerConfigurationModel.night_light_off_hyst_time, ChargeControllerConfigurationModel.aux_error_battery_volts, ChargeControllerConfigurationModel.aux_divert_hold_time, ChargeControllerConfigurationModel.aux_divert_delay_time, ChargeControllerConfigurationModel.aux_divert_relative_volts, ChargeControllerConfigurationModel.aux_divert_hyst_volts, ChargeControllerConfigurationModel.major_firmware_number, ChargeControllerConfigurationModel.mid_firmware_number, ChargeControllerConfigurationModel.minor_firmware_number, ChargeControllerConfigurationModel.set_data_log_day_offset, ChargeControllerConfigurationModel.get_current_data_log_day_offset, ChargeControllerConfigurationModel.data_log_daily_ah, ChargeControllerConfigurationModel.data_log_daily_kwh, ChargeControllerConfigurationModel.data_log_daily_max_output_amps, ChargeControllerConfigurationModel.data_log_daily_max_output_watts, ChargeControllerConfigurationModel.data_log_daily_absorb_time, ChargeControllerConfigurationModel.data_log_daily_float_time, ChargeControllerConfigurationModel.data_log_daily_min_battery_volts, ChargeControllerConfigurationModel.data_log_daily_max_battery_volts, ChargeControllerConfigurationModel.data_log_daily_max_input_volts, ChargeControllerConfigurationModel.clear_data_log_read, ChargeControllerConfigurationModel.clear_data_log_write_complement, ChargeControllerConfigurationModel.stats_maximum_reset_read, ChargeControllerConfigurationModel.stats_maximum_write_complement, ChargeControllerConfigurationModel.stats_totals_reset_read, ChargeControllerConfigurationModel.stats_totals_write_complement, ChargeControllerConfigurationModel.battery_voltage_calibrate_offset, ChargeControllerConfigurationModel.serial_number, ChargeControllerConfigurationModel.model_number]

class FXInverterRealTimeModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack FX Series Inverter Status Block")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
    dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
    ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 5, 1, Mode.R, description="AC Current Scale Factor")
    ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 6, 1, Mode.R, description="AC Voltage Scale Factor")
    ac_frequency_scale_factor: Int16Field = Int16Field("ac_frequency_scale_factor", 7, 1, Mode.R, description="AC Frequency Scale Factor")
    inverter_output_current: Uint16Field = Uint16Field("inverter_output_current", 8, 1, Mode.R, description="Inverter output current", units="Amps")
    inverter_charge_current: Uint16Field = Uint16Field("inverter_charge_current", 9, 1, Mode.R, description="Inverter charger current", units="Amps")
    inverter_buy_current: Uint16Field = Uint16Field("inverter_buy_current", 10, 1, Mode.R, description="Inverter buy current", units="Amps")
    inverter_sell_current: Uint16Field = Uint16Field("inverter_sell_current", 11, 1, Mode.R, description="Inverter sell current", units="Amps")
    output_ac_voltage: Uint16Field = Uint16Field("output_ac_voltage", 12, 1, Mode.R, description="Output AC Voltage", units="Volts AC")
    inverter_operating_mode: EnumUint16Field = EnumUint16Field("inverter_operating_mode", 13, 1, Mode.R, description="0=Off, 1=Searching, 2=Inverting, 3=Charging, 4=Silent, 5=Float, 6=EQ, 7=Charger Off, 8=Support, 9=Selling, 10=Pass through, 14=Offsetting", options=Enum("inverter_operating_mode", [('Charger Off', 7), ('Charging', 3), ('EQ', 6), ('Float', 5), ('Inverting', 2), ('Off', 0), ('Offsetting', 14), ('Pass through', 10), ('Searching', 1), ('Selling', 9), ('Silent', 4), ('Support', 8)]))
    error_flags: Bit16Field = Bit16Field("error_flags", 14, 1, Mode.R, description="Bit field for errors. See FX_Error Table", flags=FXErrorFlags)
    warning_flags: Bit16Field = Bit16Field("warning_flags", 15, 1, Mode.R, description="Bit field for warnings See FX_Warning Table", flags=FXWarningFlags)
    battery_voltage: Uint16Field = Uint16Field("battery_voltage", 16, 1, Mode.R, description="Battery Voltage", units="Volts DC")
    temp_compensated_target_voltage: Uint16Field = Uint16Field("temp_compensated_target_voltage", 17, 1, Mode.R, description="Temperature compensated target battery voltage", units="Volts DC")
    aux_output_state: EnumUint16Field = EnumUint16Field("aux_output_state", 18, 1, Mode.R, description="0 = Disabled; 1 = Enabled", options=Enum("aux_output_state", [('Disabled', 0), ('Enabled', 1)]))
    transformer_temperature: Int16Field = Int16Field("transformer_temperature", 19, 1, Mode.R, description="Transformer temp in degrees C", units="Degrees C")
    capacitor_temperature: Int16Field = Int16Field("capacitor_temperature", 20, 1, Mode.R, description="Capacitor temp in degrees C", units="Degrees C")
    fet_temperature: Int16Field = Int16Field("fet_temperature", 21, 1, Mode.R, description="FET temp in degrees C", units="Degrees C")
    ac_input_frequency: Uint16Field = Uint16Field("ac_input_frequency", 22, 1, Mode.R, description="Selected AC Input frequency HZ", units="Hz")
    ac_input_voltage: Uint16Field = Uint16Field("ac_input_voltage", 23, 1, Mode.R, description="Selected Input AC Voltage", units="Volts AC")
    ac_input_state: EnumUint16Field = EnumUint16Field("ac_input_state", 24, 1, Mode.R, description="1=AC Use, 0=AC_Drop", options=Enum("ac_input_state", [('AC Use', 1), ('AC_Drop', 0)]))
    minimum_ac_input_voltage: Uint16Field = Uint16Field("minimum_ac_input_voltage", 25, 1, Mode.R, description="Minimum Input AC Voltage (Write to clear value)", units="Volts AC")
    maximum_ac_input_voltage: Uint16Field = Uint16Field("maximum_ac_input_voltage", 26, 1, Mode.R, description="Maximum Input AC Voltage (Write to clear value)", units="Volts AC")
    sell_status: Bit16Field = Bit16Field("sell_status", 27, 1, Mode.R, description="Bit field for sell status See FX_Sell_Status Table", flags=FXSellStatusFlags)
    kwh_scale_factor: Int16Field = Int16Field("kwh_scale_factor", 28, 1, Mode.R, description="AC kWh scale factor")
    buy_kwh: Uint16Field = Uint16Field("buy_kwh", 29, 1, Mode.R, description="Daily Buy kWh", units="kWh")
    sell_kwh: Uint16Field = Uint16Field("sell_kwh", 30, 1, Mode.R, description="Daily Sell kWh", units="kWh")
    output_kwh: Uint16Field = Uint16Field("output_kwh", 31, 1, Mode.R, description="Daily Output kWh", units="kWh")
    charger_kwh: Uint16Field = Uint16Field("charger_kwh", 32, 1, Mode.R, description="Daily Charger kWh", units="kWh")
    output_kw: Uint16Field = Uint16Field("output_kw", 33, 1, Mode.R, description="Output kW", units="kW")
    buy_kw: Uint16Field = Uint16Field("buy_kw", 34, 1, Mode.R, description="Buy kW", units="kW")
    sell_kw: Uint16Field = Uint16Field("sell_kw", 35, 1, Mode.R, description="Sell kW", units="kW")
    charge_kw: Uint16Field = Uint16Field("charge_kw", 36, 1, Mode.R, description="Charge kW", units="kW")
    load_kw: Uint16Field = Uint16Field("load_kw", 37, 1, Mode.R, description="Load kW", units="kW")
    ac_couple_kw: Uint16Field = Uint16Field("ac_couple_kw", 38, 1, Mode.R, description="AC Coupled kW", units="kW")


FXInverterRealTimeModel.inverter_output_current.scale_factor = FXInverterRealTimeModel.ac_current_scale_factor
FXInverterRealTimeModel.inverter_charge_current.scale_factor = FXInverterRealTimeModel.ac_current_scale_factor
FXInverterRealTimeModel.inverter_buy_current.scale_factor = FXInverterRealTimeModel.ac_current_scale_factor
FXInverterRealTimeModel.inverter_sell_current.scale_factor = FXInverterRealTimeModel.ac_current_scale_factor
FXInverterRealTimeModel.output_ac_voltage.scale_factor = FXInverterRealTimeModel.ac_voltage_scale_factor
FXInverterRealTimeModel.battery_voltage.scale_factor = FXInverterRealTimeModel.dc_voltage_scale_factor
FXInverterRealTimeModel.temp_compensated_target_voltage.scale_factor = FXInverterRealTimeModel.dc_voltage_scale_factor
FXInverterRealTimeModel.ac_input_frequency.scale_factor = FXInverterRealTimeModel.ac_frequency_scale_factor
FXInverterRealTimeModel.ac_input_voltage.scale_factor = FXInverterRealTimeModel.ac_voltage_scale_factor
FXInverterRealTimeModel.minimum_ac_input_voltage.scale_factor = FXInverterRealTimeModel.ac_voltage_scale_factor
FXInverterRealTimeModel.maximum_ac_input_voltage.scale_factor = FXInverterRealTimeModel.ac_voltage_scale_factor
FXInverterRealTimeModel.buy_kwh.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.sell_kwh.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.output_kwh.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.charger_kwh.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.output_kw.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.buy_kw.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.sell_kw.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.charge_kw.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.load_kw.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.ac_couple_kw.scale_factor = FXInverterRealTimeModel.kwh_scale_factor
FXInverterRealTimeModel.__model_fields__ = [FXInverterRealTimeModel.did, FXInverterRealTimeModel.length, FXInverterRealTimeModel.port_number, FXInverterRealTimeModel.dc_voltage_scale_factor, FXInverterRealTimeModel.ac_current_scale_factor, FXInverterRealTimeModel.ac_voltage_scale_factor, FXInverterRealTimeModel.ac_frequency_scale_factor, FXInverterRealTimeModel.inverter_output_current, FXInverterRealTimeModel.inverter_charge_current, FXInverterRealTimeModel.inverter_buy_current, FXInverterRealTimeModel.inverter_sell_current, FXInverterRealTimeModel.output_ac_voltage, FXInverterRealTimeModel.inverter_operating_mode, FXInverterRealTimeModel.error_flags, FXInverterRealTimeModel.warning_flags, FXInverterRealTimeModel.battery_voltage, FXInverterRealTimeModel.temp_compensated_target_voltage, FXInverterRealTimeModel.aux_output_state, FXInverterRealTimeModel.transformer_temperature, FXInverterRealTimeModel.capacitor_temperature, FXInverterRealTimeModel.fet_temperature, FXInverterRealTimeModel.ac_input_frequency, FXInverterRealTimeModel.ac_input_voltage, FXInverterRealTimeModel.ac_input_state, FXInverterRealTimeModel.minimum_ac_input_voltage, FXInverterRealTimeModel.maximum_ac_input_voltage, FXInverterRealTimeModel.sell_status, FXInverterRealTimeModel.kwh_scale_factor, FXInverterRealTimeModel.buy_kwh, FXInverterRealTimeModel.sell_kwh, FXInverterRealTimeModel.output_kwh, FXInverterRealTimeModel.charger_kwh, FXInverterRealTimeModel.output_kw, FXInverterRealTimeModel.buy_kw, FXInverterRealTimeModel.sell_kw, FXInverterRealTimeModel.charge_kw, FXInverterRealTimeModel.load_kw, FXInverterRealTimeModel.ac_couple_kw]

class FXInverterConfigurationModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack FX Series Inverter  Configuration Block")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
    dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
    ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 5, 1, Mode.R, description="AC Current Scale Factor")
    ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 6, 1, Mode.R, description="AC Voltage Scale Factor")
    time_scale_factor: Int16Field = Int16Field("time_scale_factor", 7, 1, Mode.R, description="Time Scale Factor")
    major_firmware_number: Uint16Field = Uint16Field("major_firmware_number", 8, 1, Mode.R, description="Inverter Major firmware revision")
    mid_firmware_number: Uint16Field = Uint16Field("mid_firmware_number", 9, 1, Mode.R, description="Inverter Mid firmware revision")
    minor_firmware_number: Uint16Field = Uint16Field("minor_firmware_number", 10, 1, Mode.R, description="Inverter Minor firmware revision")
    absorb_volts: Uint16Field = Uint16Field("absorb_volts", 11, 1, Mode.RW, description="Absorb Voltage Target", units="DC Volts")
    absorb_time_hours: Uint16Field = Uint16Field("absorb_time_hours", 12, 1, Mode.RW, description="Absorb Time Hours", units="Hours")
    float_volts: Uint16Field = Uint16Field("float_volts", 13, 1, Mode.RW, description="Float Voltage Target", units="DC Volts")
    float_time_hours: Uint16Field = Uint16Field("float_time_hours", 14, 1, Mode.RW, description="Float Time Hours", units="Hours")
    re_float_volts: Uint16Field = Uint16Field("re_float_volts", 15, 1, Mode.RW, description="ReFloat Voltage Target", units="DC Volts")
    eq_volts: Uint16Field = Uint16Field("eq_volts", 16, 1, Mode.RW, description="EQ Voltage Target", units="DC Volts")
    eq_time_hours: Uint16Field = Uint16Field("eq_time_hours", 17, 1, Mode.RW, description="EQ Time Hours", units="Hours")
    search_sensitivity: Uint16Field = Uint16Field("search_sensitivity", 18, 1, Mode.RW, description="Search sensitivity")
    search_pulse_length: Uint16Field = Uint16Field("search_pulse_length", 19, 1, Mode.RW, description="Search pulse length", units="Cycles")
    search_pulse_spacing: Uint16Field = Uint16Field("search_pulse_spacing", 20, 1, Mode.RW, description="Search pulse spacing", units="Cycles")
    ac_input_type: EnumUint16Field = EnumUint16Field("ac_input_type", 21, 1, Mode.RW, description="0=Grid, 1=Gen, 2=Grid Zero", options=Enum("ac_input_type", [('Gen', 1), ('Grid', 0), ('Grid Zero', 2)]))
    input_support: EnumUint16Field = EnumUint16Field("input_support", 22, 1, Mode.RW, description="1=Yes, 0=No (only valid if AC Input Type is Gen)", options=Enum("input_support", [('No (only valid if AC Input Type is Gen)', 0), ('Yes', 1)]))
    grid_ac_input_current_limit: Uint16Field = Uint16Field("grid_ac_input_current_limit", 23, 1, Mode.RW, description="Grid AC input current limit", units="Amps")
    gen_ac_input_current_limit: Uint16Field = Uint16Field("gen_ac_input_current_limit", 24, 1, Mode.RW, description="Gen AC input current limit", units="Amps")
    charger_ac_input_current_limit: Uint16Field = Uint16Field("charger_ac_input_current_limit", 25, 1, Mode.RW, description="Charger AC input current limit", units="Amps")
    charger_operating_mode: EnumUint16Field = EnumUint16Field("charger_operating_mode", 26, 1, Mode.RW, description="0=Charger Off, 1=Charger Auto, 2=Charger On", options=Enum("charger_operating_mode", [('Charger Auto', 1), ('Charger Off', 0), ('Charger On', 2)]))
    grid_lower_input_voltage_limit: Uint16Field = Uint16Field("grid_lower_input_voltage_limit", 27, 1, Mode.RW, description="Grid Input AC voltage lower limit", units="Volts AC")
    grid_upper_input_voltage_limit: Uint16Field = Uint16Field("grid_upper_input_voltage_limit", 28, 1, Mode.RW, description="Grid Input AC voltage upper limit", units="Volts AC")
    grid_transfer_delay: Uint16Field = Uint16Field("grid_transfer_delay", 29, 1, Mode.RW, description="Grid Input AC connect delay", units="Minutes")
    gen_lower_input_voltage_limit: Uint16Field = Uint16Field("gen_lower_input_voltage_limit", 30, 1, Mode.RW, description="Gen Input AC voltage lower limit", units="Volts AC")
    gen_upper_input_voltage_limit: Uint16Field = Uint16Field("gen_upper_input_voltage_limit", 31, 1, Mode.RW, description="Gen Input AC voltage upper limit", units="Volts AC")
    gen_transfer_delay: Uint16Field = Uint16Field("gen_transfer_delay", 32, 1, Mode.RW, description="Gen Input AC transfer delay", units="Cycles")
    gen_connect_delay: Uint16Field = Uint16Field("gen_connect_delay", 33, 1, Mode.RW, description="Gen Input AC connect delay", units="Minutes")
    ac_output_voltage: Uint16Field = Uint16Field("ac_output_voltage", 34, 1, Mode.RW, description="AC output Voltage", units="Volts AC")
    low_battery_cut_out_voltage: Uint16Field = Uint16Field("low_battery_cut_out_voltage", 35, 1, Mode.RW, description="Battery cut-out voltage", units="DC Volts")
    low_battery_cut_in_voltage: Uint16Field = Uint16Field("low_battery_cut_in_voltage", 36, 1, Mode.RW, description="Battery cut-in voltage", units="DC Volts")
    aux_mode: EnumUint16Field = EnumUint16Field("aux_mode", 37, 1, Mode.RW, description="0=Remote, 1=Load Shed, 2=Gen Alert, 3=Fault, 4=Vent Fan, 5=Cool Fan, 6=Divert DC, 7=Divert AC, 8=AC Drop", options=Enum("aux_mode", [('AC Drop', 8), ('Cool Fan', 5), ('Divert AC', 7), ('Divert DC', 6), ('Fault', 3), ('Gen Alert', 2), ('Load Shed', 1), ('Remote', 0), ('Vent Fan', 4)]))
    aux_control: EnumUint16Field = EnumUint16Field("aux_control", 38, 1, Mode.RW, description="0 = Off; 1 = Auto; 2 = On", options=Enum("aux_control", [('Auto', 1), ('Off', 0), ('On', 2)]))
    aux_load_shed_enable_voltage: Uint16Field = Uint16Field("aux_load_shed_enable_voltage", 39, 1, Mode.RW, description="Load Shed enable voltage", units="DC Volts")
    aux_gen_alert_on_voltage: Uint16Field = Uint16Field("aux_gen_alert_on_voltage", 40, 1, Mode.RW, description="Gen Alert On voltage", units="DC Volts")
    aux_gen_alert_on_delay: Uint16Field = Uint16Field("aux_gen_alert_on_delay", 41, 1, Mode.RW, description="Gen Alert On delay minutes", units="Minutes")
    aux_gen_alert_off_voltage: Uint16Field = Uint16Field("aux_gen_alert_off_voltage", 42, 1, Mode.RW, description="Gen Alert Off voltage", units="DC Volts")
    aux_gen_alert_off_delay: Uint16Field = Uint16Field("aux_gen_alert_off_delay", 43, 1, Mode.RW, description="Gen Alert Off delay minutes", units="Minutes")
    aux_vent_fan_enable_voltage: Uint16Field = Uint16Field("aux_vent_fan_enable_voltage", 44, 1, Mode.RW, description="Vent Fan enable voltage", units="DC Volts")
    aux_vent_fan_off_period: Uint16Field = Uint16Field("aux_vent_fan_off_period", 45, 1, Mode.RW, description="Van Fan Off delay minutes", units="Minutes")
    aux_divert_enable_voltage: Uint16Field = Uint16Field("aux_divert_enable_voltage", 46, 1, Mode.RW, description="DC Divert enable voltage", units="DC Volts")
    aux_divert_off_delay: Uint16Field = Uint16Field("aux_divert_off_delay", 47, 1, Mode.RW, description="Divert Off delay minutes", units="Minutes")
    stacking_mode: EnumUint16Field = EnumUint16Field("stacking_mode", 48, 1, Mode.RW, description="0=1-2phase Master, 1=Classic Slave, 2=OB Slave L1, 3=OB Slave L2, 4=3phase Master, 5=3phase Slave,10=Master, 11=Classic Slave, 12=OB Slave L1, 13=OB Slave L2, 14=3phase OB Slave A, 15=3phase OB Slave B, 16=3phase OB Slave C, 17=3phase Classic B, 18=3phase Classic C, 19=Independent", options=Enum("stacking_mode", [('1-2phase Master', 0), ('3phase Classic B', 17), ('3phase Classic C', 18), ('3phase Master', 4), ('3phase OB Slave A', 14), ('3phase OB Slave B', 15), ('3phase OB Slave C', 16), ('3phase Slave', 5), ('CLASSIC_SLAVE_11', 11), ('Classic Slave', 1), ('Independent', 19), ('Master', 10), ('OB Slave L1', 2), ('OB Slave L2', 3), ('OB_SLAVE_L1_12', 12), ('OB_SLAVE_L2_13', 13)]))
    master_power_save_level: Uint16Field = Uint16Field("master_power_save_level", 49, 1, Mode.RW, description="Master inverter power save level")
    slave_power_save_level: Uint16Field = Uint16Field("slave_power_save_level", 50, 1, Mode.RW, description="Slave inverter power save level")
    sell_volts: Uint16Field = Uint16Field("sell_volts", 51, 1, Mode.RW, description="Sell Voltage Target", units="DC Volts")
    grid_tie_window: EnumUint16Field = EnumUint16Field("grid_tie_window", 52, 1, Mode.RW, description="0=IEEE, 1=User", options=Enum("grid_tie_window", [('IEEE', 0), ('User', 1)]))
    grid_tie_enable: EnumUint16Field = EnumUint16Field("grid_tie_enable", 53, 1, Mode.RW, description="1=Yes, 0=No", options=Enum("grid_tie_enable", [('No', 0), ('Yes', 1)]))
    ac_input_voltage_calibrate_factor: Int16Field = Int16Field("ac_input_voltage_calibrate_factor", 54, 1, Mode.RW, description="AC input voltage calibration factor", units="Volts AC")
    ac_output_voltage_calibrate_factor: Int16Field = Int16Field("ac_output_voltage_calibrate_factor", 55, 1, Mode.RW, description="AC output voltage calibration factor", units="Volts AC")
    battery_voltage_calibrate_factor: Int16Field = Int16Field("battery_voltage_calibrate_factor", 56, 1, Mode.RW, description="Battery voltage calibration factor", units="DC Volts")
    serial_number: StringField = StringField("serial_number", 57, 9, Mode.R, description="Device serial number")
    model_number: StringField = StringField("model_number", 66, 9, Mode.R, description="Device model")


FXInverterConfigurationModel.absorb_volts.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.absorb_time_hours.scale_factor = FXInverterConfigurationModel.time_scale_factor
FXInverterConfigurationModel.float_volts.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.float_time_hours.scale_factor = FXInverterConfigurationModel.time_scale_factor
FXInverterConfigurationModel.re_float_volts.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.eq_volts.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.eq_time_hours.scale_factor = FXInverterConfigurationModel.time_scale_factor
FXInverterConfigurationModel.grid_ac_input_current_limit.scale_factor = FXInverterConfigurationModel.ac_current_scale_factor
FXInverterConfigurationModel.gen_ac_input_current_limit.scale_factor = FXInverterConfigurationModel.ac_current_scale_factor
FXInverterConfigurationModel.charger_ac_input_current_limit.scale_factor = FXInverterConfigurationModel.ac_current_scale_factor
FXInverterConfigurationModel.grid_lower_input_voltage_limit.scale_factor = FXInverterConfigurationModel.ac_voltage_scale_factor
FXInverterConfigurationModel.grid_upper_input_voltage_limit.scale_factor = FXInverterConfigurationModel.ac_voltage_scale_factor
FXInverterConfigurationModel.gen_lower_input_voltage_limit.scale_factor = FXInverterConfigurationModel.ac_voltage_scale_factor
FXInverterConfigurationModel.gen_upper_input_voltage_limit.scale_factor = FXInverterConfigurationModel.ac_voltage_scale_factor
FXInverterConfigurationModel.gen_connect_delay.scale_factor = FXInverterConfigurationModel.time_scale_factor
FXInverterConfigurationModel.ac_output_voltage.scale_factor = FXInverterConfigurationModel.ac_voltage_scale_factor
FXInverterConfigurationModel.low_battery_cut_out_voltage.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.low_battery_cut_in_voltage.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.aux_load_shed_enable_voltage.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.aux_gen_alert_on_voltage.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.aux_gen_alert_off_voltage.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.aux_vent_fan_enable_voltage.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.aux_divert_enable_voltage.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.sell_volts.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.battery_voltage_calibrate_factor.scale_factor = FXInverterConfigurationModel.dc_voltage_scale_factor
FXInverterConfigurationModel.__model_fields__ = [FXInverterConfigurationModel.did, FXInverterConfigurationModel.length, FXInverterConfigurationModel.port_number, FXInverterConfigurationModel.dc_voltage_scale_factor, FXInverterConfigurationModel.ac_current_scale_factor, FXInverterConfigurationModel.ac_voltage_scale_factor, FXInverterConfigurationModel.time_scale_factor, FXInverterConfigurationModel.major_firmware_number, FXInverterConfigurationModel.mid_firmware_number, FXInverterConfigurationModel.minor_firmware_number, FXInverterConfigurationModel.absorb_volts, FXInverterConfigurationModel.absorb_time_hours, FXInverterConfigurationModel.float_volts, FXInverterConfigurationModel.float_time_hours, FXInverterConfigurationModel.re_float_volts, FXInverterConfigurationModel.eq_volts, FXInverterConfigurationModel.eq_time_hours, FXInverterConfigurationModel.search_sensitivity, FXInverterConfigurationModel.search_pulse_length, FXInverterConfigurationModel.search_pulse_spacing, FXInverterConfigurationModel.ac_input_type, FXInverterConfigurationModel.input_support, FXInverterConfigurationModel.grid_ac_input_current_limit, FXInverterConfigurationModel.gen_ac_input_current_limit, FXInverterConfigurationModel.charger_ac_input_current_limit, FXInverterConfigurationModel.charger_operating_mode, FXInverterConfigurationModel.grid_lower_input_voltage_limit, FXInverterConfigurationModel.grid_upper_input_voltage_limit, FXInverterConfigurationModel.grid_transfer_delay, FXInverterConfigurationModel.gen_lower_input_voltage_limit, FXInverterConfigurationModel.gen_upper_input_voltage_limit, FXInverterConfigurationModel.gen_transfer_delay, FXInverterConfigurationModel.gen_connect_delay, FXInverterConfigurationModel.ac_output_voltage, FXInverterConfigurationModel.low_battery_cut_out_voltage, FXInverterConfigurationModel.low_battery_cut_in_voltage, FXInverterConfigurationModel.aux_mode, FXInverterConfigurationModel.aux_control, FXInverterConfigurationModel.aux_load_shed_enable_voltage, FXInverterConfigurationModel.aux_gen_alert_on_voltage, FXInverterConfigurationModel.aux_gen_alert_on_delay, FXInverterConfigurationModel.aux_gen_alert_off_voltage, FXInverterConfigurationModel.aux_gen_alert_off_delay, FXInverterConfigurationModel.aux_vent_fan_enable_voltage, FXInverterConfigurationModel.aux_vent_fan_off_period, FXInverterConfigurationModel.aux_divert_enable_voltage, FXInverterConfigurationModel.aux_divert_off_delay, FXInverterConfigurationModel.stacking_mode, FXInverterConfigurationModel.master_power_save_level, FXInverterConfigurationModel.slave_power_save_level, FXInverterConfigurationModel.sell_volts, FXInverterConfigurationModel.grid_tie_window, FXInverterConfigurationModel.grid_tie_enable, FXInverterConfigurationModel.ac_input_voltage_calibrate_factor, FXInverterConfigurationModel.ac_output_voltage_calibrate_factor, FXInverterConfigurationModel.battery_voltage_calibrate_factor, FXInverterConfigurationModel.serial_number, FXInverterConfigurationModel.model_number]

class SplitPhaseRadianInverterRealTimeModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack Radian Series Split Phase Inverter Status Block")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
    dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
    ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 5, 1, Mode.R, description="AC Current Scale Factor")
    ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 6, 1, Mode.R, description="AC Voltage Scale Factor")
    ac_frequency_scale_factor: Int16Field = Int16Field("ac_frequency_scale_factor", 7, 1, Mode.R, description="AC Frequency Scale Factor")
    l1_inverter_output_current: Int16Field = Int16Field("l1_inverter_output_current", 8, 1, Mode.R, description="L1 inverter output current", units="Amps")
    l1_inverter_charge_current: Int16Field = Int16Field("l1_inverter_charge_current", 9, 1, Mode.R, description="L1 inverter charger current", units="Amps")
    l1_inverter_buy_current: Int16Field = Int16Field("l1_inverter_buy_current", 10, 1, Mode.R, description="L1 inverter buy current", units="Amps")
    l1_inverter_sell_current: Int16Field = Int16Field("l1_inverter_sell_current", 11, 1, Mode.R, description="L1 inverter sell current", units="Amps")
    l1_grid_input_ac_voltage: Int16Field = Int16Field("l1_grid_input_ac_voltage", 12, 1, Mode.R, description="L1 Grid Input AC Voltage", units="Volts AC")
    l1_gen_input_ac_voltage: Int16Field = Int16Field("l1_gen_input_ac_voltage", 13, 1, Mode.R, description="L1 Gen Input AC Voltage", units="Volts AC")
    l1_output_ac_voltage: Int16Field = Int16Field("l1_output_ac_voltage", 14, 1, Mode.R, description="L1 Output AC Voltage", units="Volts AC")
    l2_inverter_output_current: Int16Field = Int16Field("l2_inverter_output_current", 15, 1, Mode.R, description="L2 inverter output current", units="Amps")
    l2_inverter_charge_current: Int16Field = Int16Field("l2_inverter_charge_current", 16, 1, Mode.R, description="L2 inverter charger current", units="Amps")
    l2_inverter_buy_current: Int16Field = Int16Field("l2_inverter_buy_current", 17, 1, Mode.R, description="L2 inverter buy current", units="Amps")
    l2_inverter_sell_current: Int16Field = Int16Field("l2_inverter_sell_current", 18, 1, Mode.R, description="L2 inverter sell current", units="Amps")
    l2_grid_input_ac_voltage: Int16Field = Int16Field("l2_grid_input_ac_voltage", 19, 1, Mode.R, description="L2 Grid Input AC Voltage", units="Volts AC")
    l2_gen_input_ac_voltage: Int16Field = Int16Field("l2_gen_input_ac_voltage", 20, 1, Mode.R, description="L2 Gen Input AC Voltage", units="Volts AC")
    l2_output_ac_voltage: Int16Field = Int16Field("l2_output_ac_voltage", 21, 1, Mode.R, description="L2 Output AC Voltage", units="Volts AC")
    inverter_operating_mode: EnumInt16Field = EnumInt16Field("inverter_operating_mode", 22, 1, Mode.R, description="0=Off, 1=Searching, 2=Inverting, 3=Charging, 4=Silent, 5=Float, 6=EQ, 7=Charger Off, 8=Support, 9=Selling, 10=Pass through, 14=Offsetting", options=Enum("inverter_operating_mode", [('Charger Off', 7), ('Charging', 3), ('EQ', 6), ('Float', 5), ('Inverting', 2), ('Off', 0), ('Offsetting', 14), ('Pass through', 10), ('Searching', 1), ('Selling', 9), ('Silent', 4), ('Support', 8)]))
    error_flags: Bit16Field = Bit16Field("error_flags", 23, 1, Mode.R, description="Bit field for errors. See GS_Error table", flags=GSSplitErrorFlags)
    warning_flags: Bit16Field = Bit16Field("warning_flags", 24, 1, Mode.R, description="Bit field for warnings See GS_Warning table", flags=GSSplitWarningFlags)
    battery_voltage: Int16Field = Int16Field("battery_voltage", 25, 1, Mode.R, description="Battery Voltage", units="Volts DC")
    temp_compensated_target_voltage: Int16Field = Int16Field("temp_compensated_target_voltage", 26, 1, Mode.R, description="Temperature compensated target battery voltage", units="Volts DC")
    aux_output_state: EnumInt16Field = EnumInt16Field("aux_output_state", 27, 1, Mode.R, description="0 = Disabled; 1 = Enabled", options=Enum("aux_output_state", [('Disabled', 0), ('Enabled', 1)]))
    aux_relay_output_state: EnumInt16Field = EnumInt16Field("aux_relay_output_state", 28, 1, Mode.R, description="0 = Disabled; 1 = Enabled", options=Enum("aux_relay_output_state", [('Disabled', 0), ('Enabled', 1)]))
    l_module_transformer_temperature: Int16Field = Int16Field("l_module_transformer_temperature", 29, 1, Mode.R, description="Left module transformer temp in degrees C", units="Degrees C")
    l_module_capacitor_temperature: Int16Field = Int16Field("l_module_capacitor_temperature", 30, 1, Mode.R, description="Left module capacitor temp in degrees C", units="Degrees C")
    l_module_fet_temperature: Int16Field = Int16Field("l_module_fet_temperature", 31, 1, Mode.R, description="Left module FET temp in degrees C", units="Degrees C")
    r_module_transformer_temperature: Int16Field = Int16Field("r_module_transformer_temperature", 32, 1, Mode.R, description="Right module transformer temp in degrees C", units="Degrees C")
    r_module_capacitor_temperature: Int16Field = Int16Field("r_module_capacitor_temperature", 33, 1, Mode.R, description="Right module capacitor temp in degrees C", units="Degrees C")
    r_module_fet_temperature: Int16Field = Int16Field("r_module_fet_temperature", 34, 1, Mode.R, description="Right module FET temp in degrees C", units="Degrees C")
    battery_temperature: Int16Field = Int16Field("battery_temperature", 35, 1, Mode.R, description="Battery temp in degrees C", units="Degrees C")
    ac_input_selection: EnumInt16Field = EnumInt16Field("ac_input_selection", 36, 1, Mode.R, description="0=Grid, 1=Gen", options=Enum("ac_input_selection", [('Gen', 1), ('Grid', 0)]))
    ac_input_frequency: Int16Field = Int16Field("ac_input_frequency", 37, 1, Mode.R, description="Selected AC Input frequency HZ", units="Hz")
    ac_input_voltage: Int16Field = Int16Field("ac_input_voltage", 38, 1, Mode.R, description="Selected Input AC Voltage", units="Volts AC")
    ac_input_state: EnumInt16Field = EnumInt16Field("ac_input_state", 39, 1, Mode.R, description="1=AC Use, 0=AC_Drop", options=Enum("ac_input_state", [('AC Use', 1), ('AC_Drop', 0)]))
    minimum_ac_input_voltage: Int16Field = Int16Field("minimum_ac_input_voltage", 40, 1, Mode.R, description="Minimum Input AC Voltage (Write to clear stored value)", units="Volts AC")
    maximum_ac_input_voltage: Int16Field = Int16Field("maximum_ac_input_voltage", 41, 1, Mode.R, description="Maximum Input AC Voltage (Write to clear stored value)", units="Volts AC")
    sell_status: Bit16Field = Bit16Field("sell_status", 42, 1, Mode.R, description="Bit field for sell status See GS_Sell_Status table", flags=GSSplitSellStatusFlags)
    kwh_scale_factor: Int16Field = Int16Field("kwh_scale_factor", 43, 1, Mode.R, description="AC kWh scale factor")
    ac1_l1_buy_kwh: Uint16Field = Uint16Field("ac1_l1_buy_kwh", 44, 1, Mode.R, description="Daily AC1 Buy L1 kWh", units="kWh")
    ac2_l1_buy_kwh: Uint16Field = Uint16Field("ac2_l1_buy_kwh", 45, 1, Mode.R, description="Daily AC2 Buy L1 kWh", units="kWh")
    ac1_l1_sell_kwh: Uint16Field = Uint16Field("ac1_l1_sell_kwh", 46, 1, Mode.R, description="Daily AC1 Sell L1 kWh", units="kWh")
    ac2_l1_sell_kwh: Uint16Field = Uint16Field("ac2_l1_sell_kwh", 47, 1, Mode.R, description="Daily AC2 Sell L1 kWh", units="kWh")
    l1_output_kwh: Uint16Field = Uint16Field("l1_output_kwh", 48, 1, Mode.R, description="Daily Output L1 kWh", units="kWh")
    ac1_l2_buy_kwh: Uint16Field = Uint16Field("ac1_l2_buy_kwh", 49, 1, Mode.R, description="Daily AC1 Buy L2 kWh", units="kWh")
    ac2_l2_buy_kwh: Uint16Field = Uint16Field("ac2_l2_buy_kwh", 50, 1, Mode.R, description="Daily AC1 Sell L2 kWh", units="kWh")
    ac1_l2_sell_kwh: Uint16Field = Uint16Field("ac1_l2_sell_kwh", 51, 1, Mode.R, description="Daily AC1 Sell L2 kWh", units="kWh")
    ac2_l2_sell_kwh: Uint16Field = Uint16Field("ac2_l2_sell_kwh", 52, 1, Mode.R, description="Daily AC2 Sell L2 kWh", units="kWh")
    l2_output_kwh: Uint16Field = Uint16Field("l2_output_kwh", 53, 1, Mode.R, description="Daily Output L2 kWh", units="kWh")
    charger_kwh: Uint16Field = Uint16Field("charger_kwh", 54, 1, Mode.R, description="Daily Charger kWh", units="kWh")
    output_kw: Uint16Field = Uint16Field("output_kw", 55, 1, Mode.R, description="Output kW", units="kW")
    buy_kw: Uint16Field = Uint16Field("buy_kw", 56, 1, Mode.R, description="Buy kW", units="kW")
    sell_kw: Uint16Field = Uint16Field("sell_kw", 57, 1, Mode.R, description="Sell kW", units="kW")
    charge_kw: Uint16Field = Uint16Field("charge_kw", 58, 1, Mode.R, description="Charge kW", units="kW")
    load_kw: Uint16Field = Uint16Field("load_kw", 59, 1, Mode.R, description="Load kW", units="kW")
    ac_couple_kw: Uint16Field = Uint16Field("ac_couple_kw", 60, 1, Mode.R, description="AC Coupled kW", units="kW")
    gt_number: Uint16Field = Uint16Field("gt_number", 61, 1, Mode.R, description="GT Number sent from Inverter to Charge Controller")


SplitPhaseRadianInverterRealTimeModel.l1_inverter_output_current.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l1_inverter_charge_current.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l1_inverter_buy_current.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l1_inverter_sell_current.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l1_grid_input_ac_voltage.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.l1_gen_input_ac_voltage.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.l1_output_ac_voltage.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_inverter_output_current.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_inverter_charge_current.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_inverter_buy_current.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_inverter_sell_current.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_grid_input_ac_voltage.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_gen_input_ac_voltage.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_output_ac_voltage.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.battery_voltage.scale_factor = SplitPhaseRadianInverterRealTimeModel.dc_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.temp_compensated_target_voltage.scale_factor = SplitPhaseRadianInverterRealTimeModel.dc_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac_input_frequency.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_frequency_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac_input_voltage.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.minimum_ac_input_voltage.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.maximum_ac_input_voltage.scale_factor = SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac1_l1_buy_kwh.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac2_l1_buy_kwh.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac1_l1_sell_kwh.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac2_l1_sell_kwh.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.l1_output_kwh.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac1_l2_buy_kwh.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac2_l2_buy_kwh.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac1_l2_sell_kwh.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac2_l2_sell_kwh.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.l2_output_kwh.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.charger_kwh.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.output_kw.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.buy_kw.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.sell_kw.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.charge_kw.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.load_kw.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.ac_couple_kw.scale_factor = SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor
SplitPhaseRadianInverterRealTimeModel.__model_fields__ = [SplitPhaseRadianInverterRealTimeModel.did, SplitPhaseRadianInverterRealTimeModel.length, SplitPhaseRadianInverterRealTimeModel.port_number, SplitPhaseRadianInverterRealTimeModel.dc_voltage_scale_factor, SplitPhaseRadianInverterRealTimeModel.ac_current_scale_factor, SplitPhaseRadianInverterRealTimeModel.ac_voltage_scale_factor, SplitPhaseRadianInverterRealTimeModel.ac_frequency_scale_factor, SplitPhaseRadianInverterRealTimeModel.l1_inverter_output_current, SplitPhaseRadianInverterRealTimeModel.l1_inverter_charge_current, SplitPhaseRadianInverterRealTimeModel.l1_inverter_buy_current, SplitPhaseRadianInverterRealTimeModel.l1_inverter_sell_current, SplitPhaseRadianInverterRealTimeModel.l1_grid_input_ac_voltage, SplitPhaseRadianInverterRealTimeModel.l1_gen_input_ac_voltage, SplitPhaseRadianInverterRealTimeModel.l1_output_ac_voltage, SplitPhaseRadianInverterRealTimeModel.l2_inverter_output_current, SplitPhaseRadianInverterRealTimeModel.l2_inverter_charge_current, SplitPhaseRadianInverterRealTimeModel.l2_inverter_buy_current, SplitPhaseRadianInverterRealTimeModel.l2_inverter_sell_current, SplitPhaseRadianInverterRealTimeModel.l2_grid_input_ac_voltage, SplitPhaseRadianInverterRealTimeModel.l2_gen_input_ac_voltage, SplitPhaseRadianInverterRealTimeModel.l2_output_ac_voltage, SplitPhaseRadianInverterRealTimeModel.inverter_operating_mode, SplitPhaseRadianInverterRealTimeModel.error_flags, SplitPhaseRadianInverterRealTimeModel.warning_flags, SplitPhaseRadianInverterRealTimeModel.battery_voltage, SplitPhaseRadianInverterRealTimeModel.temp_compensated_target_voltage, SplitPhaseRadianInverterRealTimeModel.aux_output_state, SplitPhaseRadianInverterRealTimeModel.aux_relay_output_state, SplitPhaseRadianInverterRealTimeModel.l_module_transformer_temperature, SplitPhaseRadianInverterRealTimeModel.l_module_capacitor_temperature, SplitPhaseRadianInverterRealTimeModel.l_module_fet_temperature, SplitPhaseRadianInverterRealTimeModel.r_module_transformer_temperature, SplitPhaseRadianInverterRealTimeModel.r_module_capacitor_temperature, SplitPhaseRadianInverterRealTimeModel.r_module_fet_temperature, SplitPhaseRadianInverterRealTimeModel.battery_temperature, SplitPhaseRadianInverterRealTimeModel.ac_input_selection, SplitPhaseRadianInverterRealTimeModel.ac_input_frequency, SplitPhaseRadianInverterRealTimeModel.ac_input_voltage, SplitPhaseRadianInverterRealTimeModel.ac_input_state, SplitPhaseRadianInverterRealTimeModel.minimum_ac_input_voltage, SplitPhaseRadianInverterRealTimeModel.maximum_ac_input_voltage, SplitPhaseRadianInverterRealTimeModel.sell_status, SplitPhaseRadianInverterRealTimeModel.kwh_scale_factor, SplitPhaseRadianInverterRealTimeModel.ac1_l1_buy_kwh, SplitPhaseRadianInverterRealTimeModel.ac2_l1_buy_kwh, SplitPhaseRadianInverterRealTimeModel.ac1_l1_sell_kwh, SplitPhaseRadianInverterRealTimeModel.ac2_l1_sell_kwh, SplitPhaseRadianInverterRealTimeModel.l1_output_kwh, SplitPhaseRadianInverterRealTimeModel.ac1_l2_buy_kwh, SplitPhaseRadianInverterRealTimeModel.ac2_l2_buy_kwh, SplitPhaseRadianInverterRealTimeModel.ac1_l2_sell_kwh, SplitPhaseRadianInverterRealTimeModel.ac2_l2_sell_kwh, SplitPhaseRadianInverterRealTimeModel.l2_output_kwh, SplitPhaseRadianInverterRealTimeModel.charger_kwh, SplitPhaseRadianInverterRealTimeModel.output_kw, SplitPhaseRadianInverterRealTimeModel.buy_kw, SplitPhaseRadianInverterRealTimeModel.sell_kw, SplitPhaseRadianInverterRealTimeModel.charge_kw, SplitPhaseRadianInverterRealTimeModel.load_kw, SplitPhaseRadianInverterRealTimeModel.ac_couple_kw, SplitPhaseRadianInverterRealTimeModel.gt_number]

class RadianInverterConfigurationModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack Radian Series Split Phase Inverter  Configuration Block")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
    dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
    ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 5, 1, Mode.R, description="AC Current Scale Factor")
    ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 6, 1, Mode.R, description="AC Voltage Scale Factor")
    time_scale_factor: Int16Field = Int16Field("time_scale_factor", 7, 1, Mode.R, description="Time Scale Factor")
    major_firmware_number: Uint16Field = Uint16Field("major_firmware_number", 8, 1, Mode.R, description="Inverter Major firmware revision")
    mid_firmware_number: Uint16Field = Uint16Field("mid_firmware_number", 9, 1, Mode.R, description="Inverter Mid firmware revision")
    minor_firmware_number: Uint16Field = Uint16Field("minor_firmware_number", 10, 1, Mode.R, description="Inverter Minor firmware revision")
    absorb_volts: Uint16Field = Uint16Field("absorb_volts", 11, 1, Mode.RW, description="Absorb Voltage Target", units="DC Volts")
    absorb_time_hours: Uint16Field = Uint16Field("absorb_time_hours", 12, 1, Mode.RW, description="Absorb Time Hours", units="Hours")
    float_volts: Uint16Field = Uint16Field("float_volts", 13, 1, Mode.RW, description="Float Voltage Target", units="DC Volts")
    float_time_hours: Uint16Field = Uint16Field("float_time_hours", 14, 1, Mode.RW, description="Float Time Hours", units="Hours")
    re_float_volts: Uint16Field = Uint16Field("re_float_volts", 15, 1, Mode.RW, description="ReFloat Voltage Target", units="DC Volts")
    eq_volts: Uint16Field = Uint16Field("eq_volts", 16, 1, Mode.RW, description="EQ Voltage Target", units="DC Volts")
    eq_time_hours: Uint16Field = Uint16Field("eq_time_hours", 17, 1, Mode.RW, description="EQ Time Hours", units="Hours")
    search_sensitivity: Uint16Field = Uint16Field("search_sensitivity", 18, 1, Mode.RW, description="Search sensitivity")
    search_pulse_length: Uint16Field = Uint16Field("search_pulse_length", 19, 1, Mode.RW, description="Search pulse length", units="Cycles")
    search_pulse_spacing: Uint16Field = Uint16Field("search_pulse_spacing", 20, 1, Mode.RW, description="Search pulse spacing", units="Cycles")
    ac_input_select_priority: EnumUint16Field = EnumUint16Field("ac_input_select_priority", 21, 1, Mode.RW, description="0=Grid, 1=Gen", options=Enum("ac_input_select_priority", [('Gen', 1), ('Grid', 0)]))
    grid_ac_input_current_limit: Uint16Field = Uint16Field("grid_ac_input_current_limit", 22, 1, Mode.RW, description="Grid AC input current limit", units="Amps")
    gen_ac_input_current_limit: Uint16Field = Uint16Field("gen_ac_input_current_limit", 23, 1, Mode.RW, description="Gen AC input current limit", units="Amps")
    charger_ac_input_current_limit: Uint16Field = Uint16Field("charger_ac_input_current_limit", 24, 1, Mode.RW, description="Charger AC input current limit", units="Amps")
    charger_operating_mode: EnumUint16Field = EnumUint16Field("charger_operating_mode", 25, 1, Mode.RW, description="0=All Inverter Charging Disabled, 1=Bulk and Float Charging Enabled", options=Enum("charger_operating_mode", [('All Inverter Charging Disabled', 0), ('Bulk and Float Charging Enabled', 1)]))
    ac_coupled: EnumUint16Field = EnumUint16Field("ac_coupled", 26, 1, Mode.R, description="0=No, 1=Yes", options=Enum("ac_coupled", [('No', 0), ('Yes', 1)]))
    grid_input_mode: EnumUint16Field = EnumUint16Field("grid_input_mode", 27, 1, Mode.RW, description="Grid Input Mode: 0=Generator, 1=Support, 2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero", options=Enum("grid_input_mode", [('Backup', 4), ('Generator', 0), ('Grid Tied', 2), ('Grid Zero', 6), ('Mini Grid', 5), ('Support', 1), ('UPS', 3)]))
    grid_lower_input_voltage_limit: Uint16Field = Uint16Field("grid_lower_input_voltage_limit", 28, 1, Mode.RW, description="Grid Input AC voltage lower limit", units="Volts AC")
    grid_upper_input_voltage_limit: Uint16Field = Uint16Field("grid_upper_input_voltage_limit", 29, 1, Mode.RW, description="Grid Input AC voltage upper limit", units="Volts AC")
    grid_transfer_delay: Uint16Field = Uint16Field("grid_transfer_delay", 30, 1, Mode.RW, description="Grid Input AC transfer delay", units="msecs")
    grid_connect_delay: Uint16Field = Uint16Field("grid_connect_delay", 31, 1, Mode.RW, description="Grid Input AC connect delay", units="Minutes")
    gen_input_mode: EnumUint16Field = EnumUint16Field("gen_input_mode", 32, 1, Mode.RW, description="Grid Input Mode: 0=Generator, 1=Support, 2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero", options=Enum("gen_input_mode", [('Backup', 4), ('Generator', 0), ('Grid Tied', 2), ('Grid Zero', 6), ('Mini Grid', 5), ('Support', 1), ('UPS', 3)]))
    gen_lower_input_voltage_limit: Uint16Field = Uint16Field("gen_lower_input_voltage_limit", 33, 1, Mode.RW, description="Gen Input AC voltage lower limit", units="Volts AC")
    gen_upper_input_voltage_limit: Uint16Field = Uint16Field("gen_upper_input_voltage_limit", 34, 1, Mode.RW, description="Gen Input AC voltage upper limit", units="Volts AC")
    gen_transfer_delay: Uint16Field = Uint16Field("gen_transfer_delay", 35, 1, Mode.RW, description="Gen Input AC transfer delay", units="msecs")
    gen_connect_delay: Uint16Field = Uint16Field("gen_connect_delay", 36, 1, Mode.RW, description="Gen Input AC connect delay", units="Minutes")
    ac_output_voltage: Uint16Field = Uint16Field("ac_output_voltage", 37, 1, Mode.RW, description="AC output Voltage", units="Volts AC")
    low_battery_cut_out_voltage: Uint16Field = Uint16Field("low_battery_cut_out_voltage", 38, 1, Mode.RW, description="Battery cut-out voltage", units="DC Volts")
    low_battery_cut_in_voltage: Uint16Field = Uint16Field("low_battery_cut_in_voltage", 39, 1, Mode.RW, description="Battery cut-in voltage", units="DC Volts")
    aux_mode: EnumUint16Field = EnumUint16Field("aux_mode", 40, 1, Mode.RW, description="1=Load Shed, 2=Gen Alert, 3=Fault, 4=Vent Fan, 5=Cool Fan, 6=DC Divert, 7=Grid Limit/IEEE ,8=AC Source Status,9=AC Divert", options=Enum("aux_mode", [('AC Divert', 9), ('AC Source Status', 8), ('Cool Fan', 5), ('DC Divert', 6), ('Fault', 3), ('Gen Alert', 2), ('Grid Limit/IEEE', 7), ('Load Shed', 1), ('Vent Fan', 4)]))
    aux_control: EnumUint16Field = EnumUint16Field("aux_control", 41, 1, Mode.RW, description="0 = Off; 1 = Auto; 2 = On", options=Enum("aux_control", [('Auto', 1), ('Off', 0), ('On', 2)]))
    aux_on_battery_voltage: Uint16Field = Uint16Field("aux_on_battery_voltage", 42, 1, Mode.RW, description="AUX ON battery voltage", units="DC Volts")
    aux_on_delay_time: Uint16Field = Uint16Field("aux_on_delay_time", 43, 1, Mode.RW, description="AUX ON Delay", units="Minutes")
    aux_off_battery_voltage: Uint16Field = Uint16Field("aux_off_battery_voltage", 44, 1, Mode.RW, description="AUX OFF battery voltage", units="DC Volts")
    aux_off_delay_time: Uint16Field = Uint16Field("aux_off_delay_time", 45, 1, Mode.RW, description="AUX OFF Delay", units="Minutes")
    aux_relay_mode: EnumUint16Field = EnumUint16Field("aux_relay_mode", 46, 1, Mode.RW, description="1=Load Shed, 2=Gen Alert, 3=Fault, 4=Vent Fan, 5=Cool Fan, 6=DC Divert, 7=Grid Limit/IEEE ,8=AC Source Status,9=AC Divert", options=Enum("aux_relay_mode", [('AC Divert', 9), ('AC Source Status', 8), ('Cool Fan', 5), ('DC Divert', 6), ('Fault', 3), ('Gen Alert', 2), ('Grid Limit/IEEE', 7), ('Load Shed', 1), ('Vent Fan', 4)]))
    aux_relay_control: EnumUint16Field = EnumUint16Field("aux_relay_control", 47, 1, Mode.RW, description="0 = Off; 1 = On; 2 = Auto", options=Enum("aux_relay_control", [('Auto', 2), ('Off', 0), ('On', 1)]))
    aux_relay_on_battery_voltage: Uint16Field = Uint16Field("aux_relay_on_battery_voltage", 48, 1, Mode.RW, description="AUX Relay ON battery voltage", units="DC Volts")
    aux_relay_on_delay_time: Uint16Field = Uint16Field("aux_relay_on_delay_time", 49, 1, Mode.RW, description="AUX Relay ON Delay", units="Minutes")
    aux_relay_off_battery_voltage: Uint16Field = Uint16Field("aux_relay_off_battery_voltage", 50, 1, Mode.RW, description="AUX Relay OFF battery voltage", units="DC Volts")
    aux_relay_off_delay_time: Uint16Field = Uint16Field("aux_relay_off_delay_time", 51, 1, Mode.RW, description="AUX Relay OFF Delay", units="Minutes")
    stacking_mode: EnumUint16Field = EnumUint16Field("stacking_mode", 52, 1, Mode.RW, description="10=Master, 12=Slave, 17=B Phase Master, 18=C Phase Master", options=Enum("stacking_mode", [('B Phase Master', 17), ('C Phase Master', 18), ('Master', 10), ('Slave', 12)]))
    master_power_save_level: Uint16Field = Uint16Field("master_power_save_level", 53, 1, Mode.RW, description="Master inverter power save level")
    slave_power_save_level: Uint16Field = Uint16Field("slave_power_save_level", 54, 1, Mode.RW, description="Slave inverter power save level")
    sell_volts: Uint16Field = Uint16Field("sell_volts", 55, 1, Mode.RW, description="Sell Voltage Target", units="DC Volts")
    grid_tie_window: EnumUint16Field = EnumUint16Field("grid_tie_window", 56, 1, Mode.RW, description="0=IEEE, 1=User (GS8048 Only)", options=Enum("grid_tie_window", [('IEEE', 0), ('User (GS8048 Only)', 1)]))
    grid_tie_enable: EnumUint16Field = EnumUint16Field("grid_tie_enable", 57, 1, Mode.RW, description="1=Yes, 0=No", options=Enum("grid_tie_enable", [('No', 0), ('Yes', 1)]))
    grid_ac_input_voltage_calibrate_factor: Int16Field = Int16Field("grid_ac_input_voltage_calibrate_factor", 58, 1, Mode.RW, description="Grid AC input voltage calibration factor", units="Volts AC")
    gen_ac_input_voltage_calibrate_factor: Int16Field = Int16Field("gen_ac_input_voltage_calibrate_factor", 59, 1, Mode.RW, description="Gen AC input voltage calibration factor", units="Volts AC")
    ac_output_voltage_calibrate_factor: Int16Field = Int16Field("ac_output_voltage_calibrate_factor", 60, 1, Mode.RW, description="AC output voltage calibration factor", units="Volts AC")
    battery_voltage_calibrate_factor: Int16Field = Int16Field("battery_voltage_calibrate_factor", 61, 1, Mode.RW, description="Battery voltage calibration factor", units="DC Volts")
    re_bulk_volts: Uint16Field = Uint16Field("re_bulk_volts", 62, 1, Mode.RW, description="ReBulk Voltage Target", units="DC Volts")
    mini_grid_lbx_volts: Uint16Field = Uint16Field("mini_grid_lbx_volts", 63, 1, Mode.RW, description="Mini Grid LBX reconnect to Grid Battery Voltage", units="DC Volts")
    mini_grid_lbx_delay: Uint16Field = Uint16Field("mini_grid_lbx_delay", 64, 1, Mode.RW, description="Mini Grid LBX reconnect to Grid Delay Time", units="Hours")
    grid_zero_do_d_volts: Uint16Field = Uint16Field("grid_zero_do_d_volts", 65, 1, Mode.RW, description="Grid Zero DoD Voltage", units="DC Volts")
    grid_zero_do_d_max_offset_ac_amps: Uint16Field = Uint16Field("grid_zero_do_d_max_offset_ac_amps", 66, 1, Mode.RW, description="Grid Zero Maximum Offset AC Amps", units="Amps")
    serial_number: StringField = StringField("serial_number", 67, 9, Mode.R, description="Device serial number")
    model_number: StringField = StringField("model_number", 76, 9, Mode.R, description="Device model")
    module_control: EnumUint16Field = EnumUint16Field("module_control", 85, 1, Mode.RW, description="0=Auto, 1=Left, 2=Right, 3=Both", options=Enum("module_control", [('Auto', 0), ('Both', 3), ('Left', 1), ('Right', 2)]))
    model_select: EnumUint16Field = EnumUint16Field("model_select", 86, 1, Mode.RW, description="0=Full, 1=Half", options=Enum("model_select", [('Full', 0), ('Half', 1)]))
    low_battery_cut_out_delay: Uint16Field = Uint16Field("low_battery_cut_out_delay", 87, 1, Mode.RW, description="Low Battery Cut Out Delay", units="Seconds xx.x")
    high_battery_cut_out_voltage: Uint16Field = Uint16Field("high_battery_cut_out_voltage", 88, 1, Mode.RW, description="High Battery Cut Out Voltage", units="DC Volts")
    high_battery_cut_in_voltage: Uint16Field = Uint16Field("high_battery_cut_in_voltage", 89, 1, Mode.RW, description="High Battery Cut In Voltage", units="DC Volts")
    high_battery_cut_out_delay: Uint16Field = Uint16Field("high_battery_cut_out_delay", 90, 1, Mode.RW, description="High Battery Cut Out Delay", units="Seconds xx.x")
    ee_write_enable: EnumUint16Field = EnumUint16Field("ee_write_enable", 91, 1, Mode.RW, description="EEPROM Write Enable 1= Enable, 0= Disable", options=Enum("ee_write_enable", [('Disable', 0), ('Enable', 1)]))


RadianInverterConfigurationModel.absorb_volts.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.absorb_time_hours.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.float_volts.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.float_time_hours.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.re_float_volts.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.eq_volts.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.eq_time_hours.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.grid_ac_input_current_limit.scale_factor = RadianInverterConfigurationModel.ac_current_scale_factor
RadianInverterConfigurationModel.gen_ac_input_current_limit.scale_factor = RadianInverterConfigurationModel.ac_current_scale_factor
RadianInverterConfigurationModel.charger_ac_input_current_limit.scale_factor = RadianInverterConfigurationModel.ac_current_scale_factor
RadianInverterConfigurationModel.grid_lower_input_voltage_limit.scale_factor = RadianInverterConfigurationModel.ac_voltage_scale_factor
RadianInverterConfigurationModel.grid_upper_input_voltage_limit.scale_factor = RadianInverterConfigurationModel.ac_voltage_scale_factor
RadianInverterConfigurationModel.grid_connect_delay.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.gen_lower_input_voltage_limit.scale_factor = RadianInverterConfigurationModel.ac_voltage_scale_factor
RadianInverterConfigurationModel.gen_upper_input_voltage_limit.scale_factor = RadianInverterConfigurationModel.ac_voltage_scale_factor
RadianInverterConfigurationModel.gen_connect_delay.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.ac_output_voltage.scale_factor = RadianInverterConfigurationModel.ac_voltage_scale_factor
RadianInverterConfigurationModel.low_battery_cut_out_voltage.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.low_battery_cut_in_voltage.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.aux_on_battery_voltage.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.aux_on_delay_time.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.aux_off_battery_voltage.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.aux_off_delay_time.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.aux_relay_on_battery_voltage.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.aux_relay_on_delay_time.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.aux_relay_off_battery_voltage.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.aux_relay_off_delay_time.scale_factor = RadianInverterConfigurationModel.time_scale_factor
RadianInverterConfigurationModel.sell_volts.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.battery_voltage_calibrate_factor.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.re_bulk_volts.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.mini_grid_lbx_volts.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.grid_zero_do_d_volts.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.grid_zero_do_d_max_offset_ac_amps.scale_factor = RadianInverterConfigurationModel.ac_current_scale_factor
RadianInverterConfigurationModel.low_battery_cut_out_delay.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.high_battery_cut_out_voltage.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.high_battery_cut_in_voltage.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.high_battery_cut_out_delay.scale_factor = RadianInverterConfigurationModel.dc_voltage_scale_factor
RadianInverterConfigurationModel.__model_fields__ = [RadianInverterConfigurationModel.did, RadianInverterConfigurationModel.length, RadianInverterConfigurationModel.port_number, RadianInverterConfigurationModel.dc_voltage_scale_factor, RadianInverterConfigurationModel.ac_current_scale_factor, RadianInverterConfigurationModel.ac_voltage_scale_factor, RadianInverterConfigurationModel.time_scale_factor, RadianInverterConfigurationModel.major_firmware_number, RadianInverterConfigurationModel.mid_firmware_number, RadianInverterConfigurationModel.minor_firmware_number, RadianInverterConfigurationModel.absorb_volts, RadianInverterConfigurationModel.absorb_time_hours, RadianInverterConfigurationModel.float_volts, RadianInverterConfigurationModel.float_time_hours, RadianInverterConfigurationModel.re_float_volts, RadianInverterConfigurationModel.eq_volts, RadianInverterConfigurationModel.eq_time_hours, RadianInverterConfigurationModel.search_sensitivity, RadianInverterConfigurationModel.search_pulse_length, RadianInverterConfigurationModel.search_pulse_spacing, RadianInverterConfigurationModel.ac_input_select_priority, RadianInverterConfigurationModel.grid_ac_input_current_limit, RadianInverterConfigurationModel.gen_ac_input_current_limit, RadianInverterConfigurationModel.charger_ac_input_current_limit, RadianInverterConfigurationModel.charger_operating_mode, RadianInverterConfigurationModel.ac_coupled, RadianInverterConfigurationModel.grid_input_mode, RadianInverterConfigurationModel.grid_lower_input_voltage_limit, RadianInverterConfigurationModel.grid_upper_input_voltage_limit, RadianInverterConfigurationModel.grid_transfer_delay, RadianInverterConfigurationModel.grid_connect_delay, RadianInverterConfigurationModel.gen_input_mode, RadianInverterConfigurationModel.gen_lower_input_voltage_limit, RadianInverterConfigurationModel.gen_upper_input_voltage_limit, RadianInverterConfigurationModel.gen_transfer_delay, RadianInverterConfigurationModel.gen_connect_delay, RadianInverterConfigurationModel.ac_output_voltage, RadianInverterConfigurationModel.low_battery_cut_out_voltage, RadianInverterConfigurationModel.low_battery_cut_in_voltage, RadianInverterConfigurationModel.aux_mode, RadianInverterConfigurationModel.aux_control, RadianInverterConfigurationModel.aux_on_battery_voltage, RadianInverterConfigurationModel.aux_on_delay_time, RadianInverterConfigurationModel.aux_off_battery_voltage, RadianInverterConfigurationModel.aux_off_delay_time, RadianInverterConfigurationModel.aux_relay_mode, RadianInverterConfigurationModel.aux_relay_control, RadianInverterConfigurationModel.aux_relay_on_battery_voltage, RadianInverterConfigurationModel.aux_relay_on_delay_time, RadianInverterConfigurationModel.aux_relay_off_battery_voltage, RadianInverterConfigurationModel.aux_relay_off_delay_time, RadianInverterConfigurationModel.stacking_mode, RadianInverterConfigurationModel.master_power_save_level, RadianInverterConfigurationModel.slave_power_save_level, RadianInverterConfigurationModel.sell_volts, RadianInverterConfigurationModel.grid_tie_window, RadianInverterConfigurationModel.grid_tie_enable, RadianInverterConfigurationModel.grid_ac_input_voltage_calibrate_factor, RadianInverterConfigurationModel.gen_ac_input_voltage_calibrate_factor, RadianInverterConfigurationModel.ac_output_voltage_calibrate_factor, RadianInverterConfigurationModel.battery_voltage_calibrate_factor, RadianInverterConfigurationModel.re_bulk_volts, RadianInverterConfigurationModel.mini_grid_lbx_volts, RadianInverterConfigurationModel.mini_grid_lbx_delay, RadianInverterConfigurationModel.grid_zero_do_d_volts, RadianInverterConfigurationModel.grid_zero_do_d_max_offset_ac_amps, RadianInverterConfigurationModel.serial_number, RadianInverterConfigurationModel.model_number, RadianInverterConfigurationModel.module_control, RadianInverterConfigurationModel.model_select, RadianInverterConfigurationModel.low_battery_cut_out_delay, RadianInverterConfigurationModel.high_battery_cut_out_voltage, RadianInverterConfigurationModel.high_battery_cut_in_voltage, RadianInverterConfigurationModel.high_battery_cut_out_delay, RadianInverterConfigurationModel.ee_write_enable]

class SinglePhaseRadianInverterRealTimeModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack Radian Series Split Phase Inverter Status Block")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
    dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
    ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 5, 1, Mode.R, description="AC Current Scale Factor")
    ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 6, 1, Mode.R, description="AC Voltage Scale Factor")
    ac_frequency_scale_factor: Int16Field = Int16Field("ac_frequency_scale_factor", 7, 1, Mode.R, description="AC Frequency Scale Factor")
    inverter_output_current: Uint16Field = Uint16Field("inverter_output_current", 8, 1, Mode.R, description="Inverter output current", units="Amps")
    inverter_charge_current: Uint16Field = Uint16Field("inverter_charge_current", 9, 1, Mode.R, description="Inverter charger current", units="Amps")
    inverter_buy_current: Uint16Field = Uint16Field("inverter_buy_current", 10, 1, Mode.R, description="Inverter buy current", units="Amps")
    inverter_sell_current: Uint16Field = Uint16Field("inverter_sell_current", 11, 1, Mode.R, description="Inverter sell current", units="Amps")
    grid_input_ac_voltage: Uint16Field = Uint16Field("grid_input_ac_voltage", 12, 1, Mode.R, description="Grid Input AC Voltage", units="Volts AC")
    gen_input_ac_voltage: Uint16Field = Uint16Field("gen_input_ac_voltage", 13, 1, Mode.R, description="Gen Input AC Voltage", units="Volts AC")
    output_ac_voltage: Uint16Field = Uint16Field("output_ac_voltage", 14, 1, Mode.R, description="Output AC Voltage", units="Volts AC")
    inverter_operating_mode: EnumUint16Field = EnumUint16Field("inverter_operating_mode", 15, 1, Mode.R, description="0=Off, 1=Searching, 2=Inverting, 3=Charging, 4=Silent, 5=Float, 6=EQ, 7=Charger Off, 8=Support, 9=Selling, 10=Pass through, 14=Offsetting", options=Enum("inverter_operating_mode", [('Charger Off', 7), ('Charging', 3), ('EQ', 6), ('Float', 5), ('Inverting', 2), ('Off', 0), ('Offsetting', 14), ('Pass through', 10), ('Searching', 1), ('Selling', 9), ('Silent', 4), ('Support', 8)]))
    error_flags: Bit16Field = Bit16Field("error_flags", 16, 1, Mode.R, description="Bit field for errors. See GS_Error Table", flags=GSSingleErrorFlags)
    warning_flags: Bit16Field = Bit16Field("warning_flags", 17, 1, Mode.R, description="Bit field for warnings See GS_Warning Table", flags=GSSingleWarningFlags)
    battery_voltage: Uint16Field = Uint16Field("battery_voltage", 18, 1, Mode.R, description="Battery Voltage", units="Volts DC")
    temp_compensated_target_voltage: Uint16Field = Uint16Field("temp_compensated_target_voltage", 19, 1, Mode.R, description="Temperature compensated target battery voltage", units="Volts DC")
    aux_output_state: EnumUint16Field = EnumUint16Field("aux_output_state", 20, 1, Mode.R, description="0 = Disabled; 1 = Enabled", options=Enum("aux_output_state", [('Disabled', 0), ('Enabled', 1)]))
    aux_relay_output_state: EnumUint16Field = EnumUint16Field("aux_relay_output_state", 21, 1, Mode.R, description="0 = Disabled; 1 = Enabled", options=Enum("aux_relay_output_state", [('Disabled', 0), ('Enabled', 1)]))
    l_module_transformer_temperature: Int16Field = Int16Field("l_module_transformer_temperature", 22, 1, Mode.R, description="Left module transformer temp in degrees C", units="Degrees C")
    l_module_capacitor_temperature: Int16Field = Int16Field("l_module_capacitor_temperature", 23, 1, Mode.R, description="Left module capacitor temp in degrees C", units="Degrees C")
    l_module_fet_temperature: Int16Field = Int16Field("l_module_fet_temperature", 24, 1, Mode.R, description="Left module FET temp in degrees C", units="Degrees C")
    r_module_transformer_temperature: Int16Field = Int16Field("r_module_transformer_temperature", 25, 1, Mode.R, description="Right module transformer temp in degrees C", units="Degrees C")
    r_module_capacitor_temperature: Int16Field = Int16Field("r_module_capacitor_temperature", 26, 1, Mode.R, description="Right module capacitor temp in degrees C", units="Degrees C")
    r_module_fet_temperature: Int16Field = Int16Field("r_module_fet_temperature", 27, 1, Mode.R, description="Right module FET temp in degrees C", units="Degrees C")
    battery_temperature: Int16Field = Int16Field("battery_temperature", 28, 1, Mode.R, description="Battery temp in degrees C", units="Degrees C")
    ac_input_selection: EnumUint16Field = EnumUint16Field("ac_input_selection", 29, 1, Mode.R, description="0=Grid, 1=Gen", options=Enum("ac_input_selection", [('Gen', 1), ('Grid', 0)]))
    ac_input_frequency: Uint16Field = Uint16Field("ac_input_frequency", 30, 1, Mode.R, description="Selected AC Input frequency HZ", units="Hz")
    ac_input_voltage: Uint16Field = Uint16Field("ac_input_voltage", 31, 1, Mode.R, description="Selected Input AC Voltage", units="Volts AC")
    ac_input_state: EnumUint16Field = EnumUint16Field("ac_input_state", 32, 1, Mode.R, description="1=AC Use, 0=AC_Drop", options=Enum("ac_input_state", [('AC Use', 1), ('AC_Drop', 0)]))
    minimum_ac_input_voltage: Uint16Field = Uint16Field("minimum_ac_input_voltage", 33, 1, Mode.R, description="Minimum Input AC Voltage (Write to clear value)", units="Volts AC")
    maximum_ac_input_voltage: Uint16Field = Uint16Field("maximum_ac_input_voltage", 34, 1, Mode.R, description="Maximum Input AC Voltage (Write to clear value)", units="Volts AC")
    sell_status: Bit16Field = Bit16Field("sell_status", 35, 1, Mode.R, description="Bit field for sell status See GS_Sell_Status Table", flags=GSSingleSellStatusFlags)
    kwh_scale_factor: Int16Field = Int16Field("kwh_scale_factor", 36, 1, Mode.R, description="AC kWh scale factor")
    ac1_buy_kwh: Uint16Field = Uint16Field("ac1_buy_kwh", 37, 1, Mode.R, description="Daily AC1 Buy kWh", units="kWh")
    ac2_buy_kwh: Uint16Field = Uint16Field("ac2_buy_kwh", 38, 1, Mode.R, description="Daily AC2 Buy kWh", units="kWh")
    ac1_sell_kwh: Uint16Field = Uint16Field("ac1_sell_kwh", 39, 1, Mode.R, description="Daily AC1 Sell kWh", units="kWh")
    ac2_sell_kwh: Uint16Field = Uint16Field("ac2_sell_kwh", 40, 1, Mode.R, description="Daily AC2 Sell kWh", units="kWh")
    output_kwh: Uint16Field = Uint16Field("output_kwh", 41, 1, Mode.R, description="Daily Output kWh", units="kWh")
    charger_kwh: Uint16Field = Uint16Field("charger_kwh", 42, 1, Mode.R, description="Daily Charger kWh", units="kWh")
    output_kw: Uint16Field = Uint16Field("output_kw", 43, 1, Mode.R, description="Output kW", units="kW")
    buy_kw: Uint16Field = Uint16Field("buy_kw", 44, 1, Mode.R, description="Buy kW", units="kW")
    sell_kw: Uint16Field = Uint16Field("sell_kw", 45, 1, Mode.R, description="Sell kW", units="kW")
    charge_kw: Uint16Field = Uint16Field("charge_kw", 46, 1, Mode.R, description="Charger kW", units="kW")
    load_kw: Uint16Field = Uint16Field("load_kw", 47, 1, Mode.R, description="Load kW", units="kW")
    ac_couple_kw: Uint16Field = Uint16Field("ac_couple_kw", 48, 1, Mode.R, description="AC Coupled kW", units="kW")
    gt_number: Uint16Field = Uint16Field("gt_number", 49, 1, Mode.R, description="GT Number sent from Inverter to Charge Controller")


SinglePhaseRadianInverterRealTimeModel.inverter_output_current.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_current_scale_factor
SinglePhaseRadianInverterRealTimeModel.inverter_charge_current.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_current_scale_factor
SinglePhaseRadianInverterRealTimeModel.inverter_buy_current.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_current_scale_factor
SinglePhaseRadianInverterRealTimeModel.inverter_sell_current.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_current_scale_factor
SinglePhaseRadianInverterRealTimeModel.grid_input_ac_voltage.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.gen_input_ac_voltage.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.output_ac_voltage.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.battery_voltage.scale_factor = SinglePhaseRadianInverterRealTimeModel.dc_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.temp_compensated_target_voltage.scale_factor = SinglePhaseRadianInverterRealTimeModel.dc_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.ac_input_frequency.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_frequency_scale_factor
SinglePhaseRadianInverterRealTimeModel.ac_input_voltage.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.minimum_ac_input_voltage.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.maximum_ac_input_voltage.scale_factor = SinglePhaseRadianInverterRealTimeModel.ac_voltage_scale_factor
SinglePhaseRadianInverterRealTimeModel.ac1_buy_kwh.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.ac2_buy_kwh.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.ac1_sell_kwh.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.ac2_sell_kwh.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.output_kwh.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.charger_kwh.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.output_kw.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.buy_kw.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.sell_kw.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.charge_kw.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.load_kw.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.ac_couple_kw.scale_factor = SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor
SinglePhaseRadianInverterRealTimeModel.__model_fields__ = [SinglePhaseRadianInverterRealTimeModel.did, SinglePhaseRadianInverterRealTimeModel.length, SinglePhaseRadianInverterRealTimeModel.port_number, SinglePhaseRadianInverterRealTimeModel.dc_voltage_scale_factor, SinglePhaseRadianInverterRealTimeModel.ac_current_scale_factor, SinglePhaseRadianInverterRealTimeModel.ac_voltage_scale_factor, SinglePhaseRadianInverterRealTimeModel.ac_frequency_scale_factor, SinglePhaseRadianInverterRealTimeModel.inverter_output_current, SinglePhaseRadianInverterRealTimeModel.inverter_charge_current, SinglePhaseRadianInverterRealTimeModel.inverter_buy_current, SinglePhaseRadianInverterRealTimeModel.inverter_sell_current, SinglePhaseRadianInverterRealTimeModel.grid_input_ac_voltage, SinglePhaseRadianInverterRealTimeModel.gen_input_ac_voltage, SinglePhaseRadianInverterRealTimeModel.output_ac_voltage, SinglePhaseRadianInverterRealTimeModel.inverter_operating_mode, SinglePhaseRadianInverterRealTimeModel.error_flags, SinglePhaseRadianInverterRealTimeModel.warning_flags, SinglePhaseRadianInverterRealTimeModel.battery_voltage, SinglePhaseRadianInverterRealTimeModel.temp_compensated_target_voltage, SinglePhaseRadianInverterRealTimeModel.aux_output_state, SinglePhaseRadianInverterRealTimeModel.aux_relay_output_state, SinglePhaseRadianInverterRealTimeModel.l_module_transformer_temperature, SinglePhaseRadianInverterRealTimeModel.l_module_capacitor_temperature, SinglePhaseRadianInverterRealTimeModel.l_module_fet_temperature, SinglePhaseRadianInverterRealTimeModel.r_module_transformer_temperature, SinglePhaseRadianInverterRealTimeModel.r_module_capacitor_temperature, SinglePhaseRadianInverterRealTimeModel.r_module_fet_temperature, SinglePhaseRadianInverterRealTimeModel.battery_temperature, SinglePhaseRadianInverterRealTimeModel.ac_input_selection, SinglePhaseRadianInverterRealTimeModel.ac_input_frequency, SinglePhaseRadianInverterRealTimeModel.ac_input_voltage, SinglePhaseRadianInverterRealTimeModel.ac_input_state, SinglePhaseRadianInverterRealTimeModel.minimum_ac_input_voltage, SinglePhaseRadianInverterRealTimeModel.maximum_ac_input_voltage, SinglePhaseRadianInverterRealTimeModel.sell_status, SinglePhaseRadianInverterRealTimeModel.kwh_scale_factor, SinglePhaseRadianInverterRealTimeModel.ac1_buy_kwh, SinglePhaseRadianInverterRealTimeModel.ac2_buy_kwh, SinglePhaseRadianInverterRealTimeModel.ac1_sell_kwh, SinglePhaseRadianInverterRealTimeModel.ac2_sell_kwh, SinglePhaseRadianInverterRealTimeModel.output_kwh, SinglePhaseRadianInverterRealTimeModel.charger_kwh, SinglePhaseRadianInverterRealTimeModel.output_kw, SinglePhaseRadianInverterRealTimeModel.buy_kw, SinglePhaseRadianInverterRealTimeModel.sell_kw, SinglePhaseRadianInverterRealTimeModel.charge_kw, SinglePhaseRadianInverterRealTimeModel.load_kw, SinglePhaseRadianInverterRealTimeModel.ac_couple_kw, SinglePhaseRadianInverterRealTimeModel.gt_number]

class FLEXnetDCRealTimeModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack FLEXnet DC Battery Monitor Status Block")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
    dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
    dc_current_scale_factor: Int16Field = Int16Field("dc_current_scale_factor", 5, 1, Mode.R, description="DC Current Scale Factor")
    time_scale_factor: Int16Field = Int16Field("time_scale_factor", 6, 1, Mode.R, description="Time Scale Factor")
    kwh_scale_factor: Int16Field = Int16Field("kwh_scale_factor", 7, 1, Mode.R, description="Kilo Watt Hours Scale Factor")
    kw_scale_factor: Int16Field = Int16Field("kw_scale_factor", 8, 1, Mode.R, description="Kilo Watt Scale Factor")
    shunt_a_current: Int16Field = Int16Field("shunt_a_current", 9, 1, Mode.R, description="Shunt A current", units="Amps")
    shunt_b_current: Int16Field = Int16Field("shunt_b_current", 10, 1, Mode.R, description="Shunt B current", units="Amps")
    shunt_c_current: Int16Field = Int16Field("shunt_c_current", 11, 1, Mode.R, description="Shunt C current", units="Amps")
    battery_voltage: Uint16Field = Uint16Field("battery_voltage", 12, 1, Mode.R, description="Battery Voltage", units="Volts")
    battery_current: Int16Field = Int16Field("battery_current", 13, 1, Mode.R, description="Battery Current", units="Amps")
    battery_temperature: Int16Field = Int16Field("battery_temperature", 14, 1, Mode.R, description="Battery Temperature C", units="Degrees C")
    status_flags: Bit16Field = Bit16Field("status_flags", 15, 1, Mode.R, description="See FN Status Table", flags=FNStatusFlags)
    shunt_a_accumulated_ah: Int16Field = Int16Field("shunt_a_accumulated_ah", 16, 1, Mode.R, description="Shunt A Accumulated_AH", units="AH")
    shunt_a_accumulated_kwh: Int16Field = Int16Field("shunt_a_accumulated_kwh", 17, 1, Mode.R, description="Shunt A Accumulated_kWh", units="kWh")
    shunt_b_accumulated_ah: Int16Field = Int16Field("shunt_b_accumulated_ah", 18, 1, Mode.R, description="Shunt B Accumulated_AH", units="AH")
    shunt_b_accumulated_kwh: Int16Field = Int16Field("shunt_b_accumulated_kwh", 19, 1, Mode.R, description="Shunt B Accumulated_kWh", units="kWh")
    shunt_c_accumulated_ah: Int16Field = Int16Field("shunt_c_accumulated_ah", 20, 1, Mode.R, description="Shunt C Accumulated_AH", units="AH")
    shunt_c_accumulated_kwh: Int16Field = Int16Field("shunt_c_accumulated_kwh", 21, 1, Mode.R, description="Shunt C Accumulated_kWh", units="kWh")
    input_current: Uint16Field = Uint16Field("input_current", 22, 1, Mode.R, description="Total_input_current", units="Amps")
    output_current: Uint16Field = Uint16Field("output_current", 23, 1, Mode.R, description="Total_output_current", units="Amps")
    input_kw: Uint16Field = Uint16Field("input_kw", 24, 1, Mode.R, description="Total_input_kWatts", units="kW")
    output_kw: Uint16Field = Uint16Field("output_kw", 25, 1, Mode.R, description="Total_output_kWatts", units="kW")
    net_kw: Int16Field = Int16Field("net_kw", 26, 1, Mode.R, description="Total_net_kWatts", units="kW")
    days_since_charge_parameters_met: Uint16Field = Uint16Field("days_since_charge_parameters_met", 27, 1, Mode.R, description="Days Since Charge Parameters Met", units="Days")
    state_of_charge: Uint16Field = Uint16Field("state_of_charge", 28, 1, Mode.R, description="Current Battery State of Charge", units="Percent")
    todays_minimum_soc: Uint16Field = Uint16Field("todays_minimum_soc", 29, 1, Mode.R, description="Todays minimum SOC", units="Percent")
    todays_maximum_soc: Uint16Field = Uint16Field("todays_maximum_soc", 30, 1, Mode.R, description="Todays maximum SOC", units="Percent")
    todays_net_input_ah: Uint16Field = Uint16Field("todays_net_input_ah", 31, 1, Mode.R, description="Todays NET input AH", units="AH")
    todays_net_input_kwh: Uint16Field = Uint16Field("todays_net_input_kwh", 32, 1, Mode.R, description="Todays NET input kWh", units="kWh")
    todays_net_output_ah: Uint16Field = Uint16Field("todays_net_output_ah", 33, 1, Mode.R, description="Todays NET output AH", units="AH")
    todays_net_output_kwh: Uint16Field = Uint16Field("todays_net_output_kwh", 34, 1, Mode.R, description="Todays NET output kWh", units="kWh")
    todays_net_battery_ah: Int16Field = Int16Field("todays_net_battery_ah", 35, 1, Mode.R, description="Todays NET battery AH", units="AH")
    todays_net_battery_kwh: Int16Field = Int16Field("todays_net_battery_kwh", 36, 1, Mode.R, description="Todays NET battery kWh", units="kWh")
    charge_factor_corrected_net_battery_ah: Int16Field = Int16Field("charge_factor_corrected_net_battery_ah", 37, 1, Mode.R, description="Charge factor corrected NET battery AH", units="AH")
    charge_factor_corrected_net_battery_kwh: Int16Field = Int16Field("charge_factor_corrected_net_battery_kwh", 38, 1, Mode.R, description="Charge factor corrected NET battery kWh", units="kWh")
    todays_minimum_battery_voltage: Uint16Field = Uint16Field("todays_minimum_battery_voltage", 39, 1, Mode.R, description="Todays minimum battery voltage", units="Volts")
    todays_minimum_battery_time: Uint32Field = Uint32Field("todays_minimum_battery_time", 40, 2, Mode.R, description="Todays minimum battery voltage time UTC", units="Seconds")
    todays_maximum_battery_voltage: Uint16Field = Uint16Field("todays_maximum_battery_voltage", 42, 1, Mode.R, description="Todays maximum battery voltage", units="Volts")
    todays_maximum_battery_time: Uint32Field = Uint32Field("todays_maximum_battery_time", 43, 2, Mode.R, description="Todays maximum battery voltage time UTC", units="Seconds")
    cycle_charge_factor: Uint16Field = Uint16Field("cycle_charge_factor", 45, 1, Mode.R, description="Cycle Charge Factor", units="Percent")
    cycle_kwh_charge_efficiency: Uint16Field = Uint16Field("cycle_kwh_charge_efficiency", 46, 1, Mode.R, description="Cycle kWh Charge Efficiency", units="Percent")
    total_days_at_100_percent: Uint16Field = Uint16Field("total_days_at_100_percent", 47, 1, Mode.R, description="Total days at 100% charged", units="Days")
    lifetime_k_ah_removed: Uint16Field = Uint16Field("lifetime_k_ah_removed", 48, 1, Mode.R, description="Lifetime kAH removed from battery", units="AH")
    shunt_a_historical_returned_to_battery_ah: Uint16Field = Uint16Field("shunt_a_historical_returned_to_battery_ah", 49, 1, Mode.R, description="Shunt A historical returned to battery AH", units="AH")
    shunt_a_historical_returned_to_battery_kwh: Uint16Field = Uint16Field("shunt_a_historical_returned_to_battery_kwh", 50, 1, Mode.R, description="Shunt A historical returned to battery kWh", units="kWh")
    shunt_a_historical_removed_from_battery_ah: Uint16Field = Uint16Field("shunt_a_historical_removed_from_battery_ah", 51, 1, Mode.R, description="Shunt A historical removed from battery AH", units="AH")
    shunt_a_historical_removed_from_battery_kwh: Uint16Field = Uint16Field("shunt_a_historical_removed_from_battery_kwh", 52, 1, Mode.R, description="Shunt A historical removed from battery kWh", units="kWh")
    shunt_a_maximum_charge_rate: Uint16Field = Uint16Field("shunt_a_maximum_charge_rate", 53, 1, Mode.R, description="Shunt A historical maximum charge rate Amps", units="Amps")
    shunt_a_maximum_charge_rate_kw: Uint16Field = Uint16Field("shunt_a_maximum_charge_rate_kw", 54, 1, Mode.R, description="Shunt A historical maximum charge rate kW", units="kW")
    shunt_a_maximum_discharge_rate: Int16Field = Int16Field("shunt_a_maximum_discharge_rate", 55, 1, Mode.R, description="Shunt A historical maximum discharge rate Amps", units="Amps")
    shunt_a_maximum_discharge_rate_kw: Int16Field = Int16Field("shunt_a_maximum_discharge_rate_kw", 56, 1, Mode.R, description="Shunt A historical maximum discharge rate kW", units="kW")
    shunt_b_historical_returned_to_battery_ah: Uint16Field = Uint16Field("shunt_b_historical_returned_to_battery_ah", 57, 1, Mode.R, description="Shunt B historical returned to battery AH", units="AH")
    shunt_b_historical_returned_to_battery_kwh: Uint16Field = Uint16Field("shunt_b_historical_returned_to_battery_kwh", 58, 1, Mode.R, description="Shunt B historical returned to battery kWh", units="kWh")
    shunt_b_historical_removed_from_battery_ah: Uint16Field = Uint16Field("shunt_b_historical_removed_from_battery_ah", 59, 1, Mode.R, description="Shunt B historical removed from battery AH", units="AH")
    shunt_b_historical_removed_from_battery_kwh: Uint16Field = Uint16Field("shunt_b_historical_removed_from_battery_kwh", 60, 1, Mode.R, description="Shunt B historical removed from battery kWh", units="kWh")
    shunt_b_maximum_charge_rate: Uint16Field = Uint16Field("shunt_b_maximum_charge_rate", 61, 1, Mode.R, description="Shunt B historical maximum charge rate Amps", units="Amps")
    shunt_b_maximum_charge_rate_kw: Uint16Field = Uint16Field("shunt_b_maximum_charge_rate_kw", 62, 1, Mode.R, description="Shunt B historical maximum charge rate kW", units="kW")
    shunt_b_maximum_discharge_rate: Int16Field = Int16Field("shunt_b_maximum_discharge_rate", 63, 1, Mode.R, description="Shunt B historical maximum discharge rate Amps", units="Amps")
    shunt_b_maximum_discharge_rate_kw: Int16Field = Int16Field("shunt_b_maximum_discharge_rate_kw", 64, 1, Mode.R, description="Shunt B historical maximum discharge rate kW", units="kW")
    shunt_c_historical_returned_to_battery_ah: Uint16Field = Uint16Field("shunt_c_historical_returned_to_battery_ah", 65, 1, Mode.R, description="Shunt C historical returned to battery AH", units="AH")
    shunt_c_historical_returned_to_battery_kwh: Uint16Field = Uint16Field("shunt_c_historical_returned_to_battery_kwh", 66, 1, Mode.R, description="Shunt C historical returned to battery kWh", units="kWh")
    shunt_c_historical_removed_from_battery_ah: Uint16Field = Uint16Field("shunt_c_historical_removed_from_battery_ah", 67, 1, Mode.R, description="Shunt C historical removed from battery AH", units="AH")
    shunt_c_historical_removed_from_battery_kwh: Uint16Field = Uint16Field("shunt_c_historical_removed_from_battery_kwh", 68, 1, Mode.R, description="Shunt C historical removed from battery kWh", units="kWh")
    shunt_c_maximum_charge_rate: Uint16Field = Uint16Field("shunt_c_maximum_charge_rate", 69, 1, Mode.R, description="Shunt C historical maximum charge rate Amps", units="Amps")
    shunt_c_maximum_charge_rate_kw: Uint16Field = Uint16Field("shunt_c_maximum_charge_rate_kw", 70, 1, Mode.R, description="Shunt C historical maximum charge rate kW", units="kW")
    shunt_c_maximum_discharge_rate: Int16Field = Int16Field("shunt_c_maximum_discharge_rate", 71, 1, Mode.R, description="Shunt C historical maximum discharge rate Amps", units="Amps")
    shunt_c_maximum_discharge_rate_kw: Int16Field = Int16Field("shunt_c_maximum_discharge_rate_kw", 72, 1, Mode.R, description="Shunt C historical maximum discharge rate kW", units="kW")
    shunt_a_reset_maximum_data: Uint16Field = Uint16Field("shunt_a_reset_maximum_data", 73, 1, Mode.R, description="Read value needed to reset shunt A maximum data")
    shunt_a_reset_maximum_data_write_complement: Uint16Field = Uint16Field("shunt_a_reset_maximum_data_write_complement", 74, 1, Mode.W, description="Write value's complement to reset shunt A maximum data")
    shunt_b_reset_maximum_data: Uint16Field = Uint16Field("shunt_b_reset_maximum_data", 75, 1, Mode.R, description="Read value needed to reset shunt B maximum data")
    shunt_b_reset_maximum_data_write_complement: Uint16Field = Uint16Field("shunt_b_reset_maximum_data_write_complement", 76, 1, Mode.W, description="Write value's complement to reset shunt B maximum data")
    shunt_c_reset_maximum_data: Uint16Field = Uint16Field("shunt_c_reset_maximum_data", 77, 1, Mode.R, description="Read value needed to reset shunt C maximum data")
    shunt_c_reset_maximum_data_write_complement: Uint16Field = Uint16Field("shunt_c_reset_maximum_data_write_complement", 78, 1, Mode.W, description="Write value's complement to reset shunt C maximum data")


FLEXnetDCRealTimeModel.shunt_a_current.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_b_current.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_c_current.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.battery_voltage.scale_factor = FLEXnetDCRealTimeModel.dc_voltage_scale_factor
FLEXnetDCRealTimeModel.battery_current.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_a_accumulated_kwh.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_b_accumulated_kwh.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_c_accumulated_kwh.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.input_current.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.output_current.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.input_kw.scale_factor = FLEXnetDCRealTimeModel.kw_scale_factor
FLEXnetDCRealTimeModel.output_kw.scale_factor = FLEXnetDCRealTimeModel.kw_scale_factor
FLEXnetDCRealTimeModel.net_kw.scale_factor = FLEXnetDCRealTimeModel.kw_scale_factor
FLEXnetDCRealTimeModel.days_since_charge_parameters_met.scale_factor = FLEXnetDCRealTimeModel.time_scale_factor
FLEXnetDCRealTimeModel.todays_net_input_kwh.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.todays_net_output_kwh.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.todays_net_battery_kwh.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.charge_factor_corrected_net_battery_kwh.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.todays_minimum_battery_voltage.scale_factor = FLEXnetDCRealTimeModel.dc_voltage_scale_factor
FLEXnetDCRealTimeModel.todays_maximum_battery_voltage.scale_factor = FLEXnetDCRealTimeModel.dc_voltage_scale_factor
FLEXnetDCRealTimeModel.total_days_at_100_percent.scale_factor = FLEXnetDCRealTimeModel.time_scale_factor
FLEXnetDCRealTimeModel.shunt_a_historical_returned_to_battery_kwh.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_a_historical_removed_from_battery_kwh.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_a_maximum_charge_rate.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_a_maximum_charge_rate_kw.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_a_maximum_discharge_rate.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_a_maximum_discharge_rate_kw.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_b_historical_returned_to_battery_kwh.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_b_historical_removed_from_battery_kwh.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_b_maximum_charge_rate.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_b_maximum_charge_rate_kw.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_b_maximum_discharge_rate.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_b_maximum_discharge_rate_kw.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_c_historical_returned_to_battery_kwh.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_c_historical_removed_from_battery_kwh.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_c_maximum_charge_rate.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_c_maximum_charge_rate_kw.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.shunt_c_maximum_discharge_rate.scale_factor = FLEXnetDCRealTimeModel.dc_current_scale_factor
FLEXnetDCRealTimeModel.shunt_c_maximum_discharge_rate_kw.scale_factor = FLEXnetDCRealTimeModel.kwh_scale_factor
FLEXnetDCRealTimeModel.__model_fields__ = [FLEXnetDCRealTimeModel.did, FLEXnetDCRealTimeModel.length, FLEXnetDCRealTimeModel.port_number, FLEXnetDCRealTimeModel.dc_voltage_scale_factor, FLEXnetDCRealTimeModel.dc_current_scale_factor, FLEXnetDCRealTimeModel.time_scale_factor, FLEXnetDCRealTimeModel.kwh_scale_factor, FLEXnetDCRealTimeModel.kw_scale_factor, FLEXnetDCRealTimeModel.shunt_a_current, FLEXnetDCRealTimeModel.shunt_b_current, FLEXnetDCRealTimeModel.shunt_c_current, FLEXnetDCRealTimeModel.battery_voltage, FLEXnetDCRealTimeModel.battery_current, FLEXnetDCRealTimeModel.battery_temperature, FLEXnetDCRealTimeModel.status_flags, FLEXnetDCRealTimeModel.shunt_a_accumulated_ah, FLEXnetDCRealTimeModel.shunt_a_accumulated_kwh, FLEXnetDCRealTimeModel.shunt_b_accumulated_ah, FLEXnetDCRealTimeModel.shunt_b_accumulated_kwh, FLEXnetDCRealTimeModel.shunt_c_accumulated_ah, FLEXnetDCRealTimeModel.shunt_c_accumulated_kwh, FLEXnetDCRealTimeModel.input_current, FLEXnetDCRealTimeModel.output_current, FLEXnetDCRealTimeModel.input_kw, FLEXnetDCRealTimeModel.output_kw, FLEXnetDCRealTimeModel.net_kw, FLEXnetDCRealTimeModel.days_since_charge_parameters_met, FLEXnetDCRealTimeModel.state_of_charge, FLEXnetDCRealTimeModel.todays_minimum_soc, FLEXnetDCRealTimeModel.todays_maximum_soc, FLEXnetDCRealTimeModel.todays_net_input_ah, FLEXnetDCRealTimeModel.todays_net_input_kwh, FLEXnetDCRealTimeModel.todays_net_output_ah, FLEXnetDCRealTimeModel.todays_net_output_kwh, FLEXnetDCRealTimeModel.todays_net_battery_ah, FLEXnetDCRealTimeModel.todays_net_battery_kwh, FLEXnetDCRealTimeModel.charge_factor_corrected_net_battery_ah, FLEXnetDCRealTimeModel.charge_factor_corrected_net_battery_kwh, FLEXnetDCRealTimeModel.todays_minimum_battery_voltage, FLEXnetDCRealTimeModel.todays_minimum_battery_time, FLEXnetDCRealTimeModel.todays_maximum_battery_voltage, FLEXnetDCRealTimeModel.todays_maximum_battery_time, FLEXnetDCRealTimeModel.cycle_charge_factor, FLEXnetDCRealTimeModel.cycle_kwh_charge_efficiency, FLEXnetDCRealTimeModel.total_days_at_100_percent, FLEXnetDCRealTimeModel.lifetime_k_ah_removed, FLEXnetDCRealTimeModel.shunt_a_historical_returned_to_battery_ah, FLEXnetDCRealTimeModel.shunt_a_historical_returned_to_battery_kwh, FLEXnetDCRealTimeModel.shunt_a_historical_removed_from_battery_ah, FLEXnetDCRealTimeModel.shunt_a_historical_removed_from_battery_kwh, FLEXnetDCRealTimeModel.shunt_a_maximum_charge_rate, FLEXnetDCRealTimeModel.shunt_a_maximum_charge_rate_kw, FLEXnetDCRealTimeModel.shunt_a_maximum_discharge_rate, FLEXnetDCRealTimeModel.shunt_a_maximum_discharge_rate_kw, FLEXnetDCRealTimeModel.shunt_b_historical_returned_to_battery_ah, FLEXnetDCRealTimeModel.shunt_b_historical_returned_to_battery_kwh, FLEXnetDCRealTimeModel.shunt_b_historical_removed_from_battery_ah, FLEXnetDCRealTimeModel.shunt_b_historical_removed_from_battery_kwh, FLEXnetDCRealTimeModel.shunt_b_maximum_charge_rate, FLEXnetDCRealTimeModel.shunt_b_maximum_charge_rate_kw, FLEXnetDCRealTimeModel.shunt_b_maximum_discharge_rate, FLEXnetDCRealTimeModel.shunt_b_maximum_discharge_rate_kw, FLEXnetDCRealTimeModel.shunt_c_historical_returned_to_battery_ah, FLEXnetDCRealTimeModel.shunt_c_historical_returned_to_battery_kwh, FLEXnetDCRealTimeModel.shunt_c_historical_removed_from_battery_ah, FLEXnetDCRealTimeModel.shunt_c_historical_removed_from_battery_kwh, FLEXnetDCRealTimeModel.shunt_c_maximum_charge_rate, FLEXnetDCRealTimeModel.shunt_c_maximum_charge_rate_kw, FLEXnetDCRealTimeModel.shunt_c_maximum_discharge_rate, FLEXnetDCRealTimeModel.shunt_c_maximum_discharge_rate_kw, FLEXnetDCRealTimeModel.shunt_a_reset_maximum_data, FLEXnetDCRealTimeModel.shunt_a_reset_maximum_data_write_complement, FLEXnetDCRealTimeModel.shunt_b_reset_maximum_data, FLEXnetDCRealTimeModel.shunt_b_reset_maximum_data_write_complement, FLEXnetDCRealTimeModel.shunt_c_reset_maximum_data, FLEXnetDCRealTimeModel.shunt_c_reset_maximum_data_write_complement]

class FLEXnetDCConfigurationModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack FLEXnet-DC Battery Monitor Configuration Block")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on OutBack network")
    dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
    dc_current_scale_factor: Int16Field = Int16Field("dc_current_scale_factor", 5, 1, Mode.R, description="DC Current Scale Factor")
    kwh_scale_factor: Int16Field = Int16Field("kwh_scale_factor", 6, 1, Mode.R, description="Kilo Watt Hours Scale Factor")
    major_firmware_number: Uint16Field = Uint16Field("major_firmware_number", 7, 1, Mode.R, description="FLEXnet-DC Major firmware revision")
    mid_firmware_number: Uint16Field = Uint16Field("mid_firmware_number", 8, 1, Mode.R, description="FLEXnet-DC Mid firmware revision")
    minor_firmware_number: Uint16Field = Uint16Field("minor_firmware_number", 9, 1, Mode.R, description="FLEXnet-DC Minor firmware revision")
    battery_capacity: Uint16Field = Uint16Field("battery_capacity", 10, 1, Mode.RW, description="Battery AH capacity", units="AH")
    charged_volts: Uint16Field = Uint16Field("charged_volts", 11, 1, Mode.RW, description="Battery Charged Voltage", units="DC Volts")
    charged_time: Uint16Field = Uint16Field("charged_time", 12, 1, Mode.RW, description="Battery Charged Time Minutes", units="Minutes")
    battery_charged_amps: Uint16Field = Uint16Field("battery_charged_amps", 13, 1, Mode.RW, description="Battery Charged Return Amps", units="Amps")
    charge_factor: Uint16Field = Uint16Field("charge_factor", 14, 1, Mode.RW, description="Battery Charge Factor", units="Percent")
    shunt_a_enabled: EnumUint16Field = EnumUint16Field("shunt_a_enabled", 15, 1, Mode.RW, description="0=Enabled, 1=Disabled", options=Enum("shunt_a_enabled", [('Disabled', 1), ('Enabled', 0)]))
    shunt_b_enabled: EnumUint16Field = EnumUint16Field("shunt_b_enabled", 16, 1, Mode.RW, description="0=Enabled, 1=Disabled", options=Enum("shunt_b_enabled", [('Disabled', 1), ('Enabled', 0)]))
    shunt_c_enabled: EnumUint16Field = EnumUint16Field("shunt_c_enabled", 17, 1, Mode.RW, description="0=Enabled, 1=Disabled", options=Enum("shunt_c_enabled", [('Disabled', 1), ('Enabled', 0)]))
    relay_control: EnumUint16Field = EnumUint16Field("relay_control", 18, 1, Mode.RW, description="0 = Off; 1 = Auto; 2 = On", options=Enum("relay_control", [('Auto', 1), ('Off', 0), ('On', 2)]))
    relay_invert_logic: EnumUint16Field = EnumUint16Field("relay_invert_logic", 19, 1, Mode.RW, description="0=Invert Logic,1=Normal", options=Enum("relay_invert_logic", [('Invert Logic', 0), ('Normal', 1)]))
    relay_high_voltage: Uint16Field = Uint16Field("relay_high_voltage", 20, 1, Mode.RW, description="Relay high voltage enable", units="DC Volts")
    relay_low_voltage: Uint16Field = Uint16Field("relay_low_voltage", 21, 1, Mode.RW, description="Relay low voltage enable", units="DC Volts")
    relay_soc_high: Uint16Field = Uint16Field("relay_soc_high", 22, 1, Mode.RW, description="Relay high SOC enable", units="Percent")
    relay_soc_low: Uint16Field = Uint16Field("relay_soc_low", 23, 1, Mode.RW, description="Relay low SOC enable", units="Percent")
    relay_high_enable_delay: Uint16Field = Uint16Field("relay_high_enable_delay", 24, 1, Mode.RW, description="Relay High Enable Delay", units="Minutes")
    relay_low_enable_delay: Uint16Field = Uint16Field("relay_low_enable_delay", 25, 1, Mode.RW, description="Relay Low Enable Delay", units="Minutes")
    set_data_log_day_offset: Uint16Field = Uint16Field("set_data_log_day_offset", 26, 1, Mode.RW, description="Day offset 0-400, 0 =Today, 1 = -1 day \u2026", units="Days")
    get_current_data_log_day_offset: Uint16Field = Uint16Field("get_current_data_log_day_offset", 27, 1, Mode.R, description="Current Data Log Day Offset", units="Days")
    datalog_minimum_soc: Uint16Field = Uint16Field("datalog_minimum_soc", 28, 1, Mode.R, description="Datalog minimum SOC", units="Percent")
    datalog_input_ah: Uint16Field = Uint16Field("datalog_input_ah", 29, 1, Mode.R, description="Datalog input AH", units="AH")
    datalog_input_kwh: Uint16Field = Uint16Field("datalog_input_kwh", 30, 1, Mode.R, description="Datalog input kWh", units="kWh")
    datalog_output_ah: Uint16Field = Uint16Field("datalog_output_ah", 31, 1, Mode.R, description="Datalog output AH", units="AH")
    datalog_output_kwh: Uint16Field = Uint16Field("datalog_output_kwh", 32, 1, Mode.R, description="Datalog output kWh", units="kWh")
    datalog_net_ah: Uint16Field = Uint16Field("datalog_net_ah", 33, 1, Mode.R, description="Datalog NET AH", units="AH")
    datalog_net_kwh: Uint16Field = Uint16Field("datalog_net_kwh", 34, 1, Mode.R, description="Datalog NET kWh", units="kWh")
    clear_data_log_read: Uint16Field = Uint16Field("clear_data_log_read", 35, 1, Mode.R, description="Read value needed to clear data log")
    clear_data_log_write_complement: Uint16Field = Uint16Field("clear_data_log_write_complement", 36, 1, Mode.W, description="Write value's complement to clear data log")
    serial_number: StringField = StringField("serial_number", 37, 9, Mode.R, description="Device serial number")
    model_number: StringField = StringField("model_number", 46, 9, Mode.R, description="Device model")


FLEXnetDCConfigurationModel.charged_volts.scale_factor = FLEXnetDCConfigurationModel.dc_voltage_scale_factor
FLEXnetDCConfigurationModel.battery_charged_amps.scale_factor = FLEXnetDCConfigurationModel.dc_current_scale_factor
FLEXnetDCConfigurationModel.relay_high_voltage.scale_factor = FLEXnetDCConfigurationModel.dc_voltage_scale_factor
FLEXnetDCConfigurationModel.relay_low_voltage.scale_factor = FLEXnetDCConfigurationModel.dc_voltage_scale_factor
FLEXnetDCConfigurationModel.datalog_input_kwh.scale_factor = FLEXnetDCConfigurationModel.kwh_scale_factor
FLEXnetDCConfigurationModel.datalog_output_kwh.scale_factor = FLEXnetDCConfigurationModel.kwh_scale_factor
FLEXnetDCConfigurationModel.datalog_net_kwh.scale_factor = FLEXnetDCConfigurationModel.kwh_scale_factor
FLEXnetDCConfigurationModel.__model_fields__ = [FLEXnetDCConfigurationModel.did, FLEXnetDCConfigurationModel.length, FLEXnetDCConfigurationModel.port_number, FLEXnetDCConfigurationModel.dc_voltage_scale_factor, FLEXnetDCConfigurationModel.dc_current_scale_factor, FLEXnetDCConfigurationModel.kwh_scale_factor, FLEXnetDCConfigurationModel.major_firmware_number, FLEXnetDCConfigurationModel.mid_firmware_number, FLEXnetDCConfigurationModel.minor_firmware_number, FLEXnetDCConfigurationModel.battery_capacity, FLEXnetDCConfigurationModel.charged_volts, FLEXnetDCConfigurationModel.charged_time, FLEXnetDCConfigurationModel.battery_charged_amps, FLEXnetDCConfigurationModel.charge_factor, FLEXnetDCConfigurationModel.shunt_a_enabled, FLEXnetDCConfigurationModel.shunt_b_enabled, FLEXnetDCConfigurationModel.shunt_c_enabled, FLEXnetDCConfigurationModel.relay_control, FLEXnetDCConfigurationModel.relay_invert_logic, FLEXnetDCConfigurationModel.relay_high_voltage, FLEXnetDCConfigurationModel.relay_low_voltage, FLEXnetDCConfigurationModel.relay_soc_high, FLEXnetDCConfigurationModel.relay_soc_low, FLEXnetDCConfigurationModel.relay_high_enable_delay, FLEXnetDCConfigurationModel.relay_low_enable_delay, FLEXnetDCConfigurationModel.set_data_log_day_offset, FLEXnetDCConfigurationModel.get_current_data_log_day_offset, FLEXnetDCConfigurationModel.datalog_minimum_soc, FLEXnetDCConfigurationModel.datalog_input_ah, FLEXnetDCConfigurationModel.datalog_input_kwh, FLEXnetDCConfigurationModel.datalog_output_ah, FLEXnetDCConfigurationModel.datalog_output_kwh, FLEXnetDCConfigurationModel.datalog_net_ah, FLEXnetDCConfigurationModel.datalog_net_kwh, FLEXnetDCConfigurationModel.clear_data_log_read, FLEXnetDCConfigurationModel.clear_data_log_write_complement, FLEXnetDCConfigurationModel.serial_number, FLEXnetDCConfigurationModel.model_number]

class OutBackSystemControlModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack System Control Block")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of block in 16-bit registers", units="Registers")
    dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 3, 1, Mode.R, description="DC Voltage Scale Factor")
    ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 4, 1, Mode.R, description="AC Current Scale Factor")
    time_scale_factor: Int16Field = Int16Field("time_scale_factor", 5, 1, Mode.R, description="Charge Time Scale Factor")
    bulk_charge_enable_disable: EnumUint16Field = EnumUint16Field("bulk_charge_enable_disable", 6, 1, Mode.W, description="1=Start Bulk, 2=Stop Bulk, 3=Start EQ Charge, 4= Stop EQ Charge", options=Enum("bulk_charge_enable_disable", [('Start Bulk', 1), ('Start EQ Charge', 3), ('Stop Bulk', 2), ('Stop EQ Charge', 4)]))
    inverter_ac_drop_use: EnumUint16Field = EnumUint16Field("inverter_ac_drop_use", 7, 1, Mode.W, description="1=Use, 2=Drop", options=Enum("inverter_ac_drop_use", [('Drop', 2), ('Use', 1)]))
    set_inverter_mode: EnumUint16Field = EnumUint16Field("set_inverter_mode", 8, 1, Mode.W, description="1=Off, 2=Search, 3=On", options=Enum("set_inverter_mode", [('Off', 1), ('On', 3), ('Search', 2)]))
    grid_tie_mode: EnumUint16Field = EnumUint16Field("grid_tie_mode", 9, 1, Mode.W, description="1=Enable, 2=Disable", options=Enum("grid_tie_mode", [('Disable', 2), ('Enable', 1)]))
    set_inverter_charger_mode: EnumUint16Field = EnumUint16Field("set_inverter_charger_mode", 10, 1, Mode.W, description="1=Off, 2=Auto, 3=On", options=Enum("set_inverter_charger_mode", [('Auto', 2), ('Off', 1), ('On', 3)]))
    control_status: Bit16Field = Bit16Field("control_status", 11, 1, Mode.R, description="Bit field for status. See OB_Control_Status Table", flags=OBControlStatusFlags)
    set_sell_voltage: Uint16Field = Uint16Field("set_sell_voltage", 12, 1, Mode.RW, description="Global Sell Voltage", units="Volts")
    set_radian_inverter_sell_current_limit: Uint16Field = Uint16Field("set_radian_inverter_sell_current_limit", 13, 1, Mode.RW, description="Radian Inverter Sell Current Limit", units="Amps")
    set_absorb_voltage: Uint16Field = Uint16Field("set_absorb_voltage", 14, 1, Mode.RW, description="Global Absorb Voltage", units="Volts")
    set_absorb_time: Uint16Field = Uint16Field("set_absorb_time", 15, 1, Mode.RW, description="Time in tenths of hour", units="Hours")
    set_float_voltage: Uint16Field = Uint16Field("set_float_voltage", 16, 1, Mode.RW, description="Global Float Voltage", units="Volts")
    set_float_time: Uint16Field = Uint16Field("set_float_time", 17, 1, Mode.RW, description="Time in tenths of hour", units="Hours")
    set_inverter_charger_current_limit: Uint16Field = Uint16Field("set_inverter_charger_current_limit", 18, 1, Mode.RW, description="Inverter Charger Current Limit", units="Amps")
    set_inverter_ac1_current_limit: Uint16Field = Uint16Field("set_inverter_ac1_current_limit", 19, 1, Mode.RW, description="Inverter AC1 input Current Limit", units="Amps")
    set_inverter_ac2_current_limit: Uint16Field = Uint16Field("set_inverter_ac2_current_limit", 20, 1, Mode.RW, description="Inverter AC2 input Current Limit", units="Amps")
    set_ags_op_mode: EnumUint16Field = EnumUint16Field("set_ags_op_mode", 21, 1, Mode.RW, description="AGS Operating Mode: 0=Off, 1=On, 2=Auto", options=Enum("set_ags_op_mode", [('Auto', 2), ('Off', 0), ('On', 1)]))
    ags_operational_state: EnumUint16Field = EnumUint16Field("ags_operational_state", 22, 1, Mode.R, description="GEN_STOP=0, GEN_STARTING=1, GEN_RUNNING=2, GEN_WARMUP=3, GEN_COOLDOWN=4, GEN_AWAITING_AC=5", options=Enum("ags_operational_state", [(' GEN_AWAITING_AC', 5), (' GEN_COOLDOWN', 4), (' GEN_RUNNING', 2), (' GEN_STARTING', 1), (' GEN_WARMUP', 3), ('GEN_STOP', 0)]))
    ags_operational_state_timer: Uint16Field = Uint16Field("ags_operational_state_timer", 23, 1, Mode.R, description="Number of seconds that OB_AGS_Operational_State has been in current state. If Operational State is 0 then timer=0", units="Seconds")
    gen_last_run_start_time_gmt: Uint32Field = Uint32Field("gen_last_run_start_time_gmt", 24, 2, Mode.R, description="Generator last start time in GMT seconds", units="Seconds")
    gen_last_start_run_duration: Uint32Field = Uint32Field("gen_last_start_run_duration", 26, 2, Mode.R, description="Last Generator Start Run Duration Seconds", units="Seconds")


OutBackSystemControlModel.set_sell_voltage.scale_factor = OutBackSystemControlModel.dc_voltage_scale_factor
OutBackSystemControlModel.set_radian_inverter_sell_current_limit.scale_factor = OutBackSystemControlModel.ac_current_scale_factor
OutBackSystemControlModel.set_absorb_voltage.scale_factor = OutBackSystemControlModel.dc_voltage_scale_factor
OutBackSystemControlModel.set_absorb_time.scale_factor = OutBackSystemControlModel.time_scale_factor
OutBackSystemControlModel.set_float_voltage.scale_factor = OutBackSystemControlModel.dc_voltage_scale_factor
OutBackSystemControlModel.set_float_time.scale_factor = OutBackSystemControlModel.time_scale_factor
OutBackSystemControlModel.set_inverter_charger_current_limit.scale_factor = OutBackSystemControlModel.ac_current_scale_factor
OutBackSystemControlModel.set_inverter_ac1_current_limit.scale_factor = OutBackSystemControlModel.ac_current_scale_factor
OutBackSystemControlModel.set_inverter_ac2_current_limit.scale_factor = OutBackSystemControlModel.ac_current_scale_factor
OutBackSystemControlModel.__model_fields__ = [OutBackSystemControlModel.did, OutBackSystemControlModel.length, OutBackSystemControlModel.dc_voltage_scale_factor, OutBackSystemControlModel.ac_current_scale_factor, OutBackSystemControlModel.time_scale_factor, OutBackSystemControlModel.bulk_charge_enable_disable, OutBackSystemControlModel.inverter_ac_drop_use, OutBackSystemControlModel.set_inverter_mode, OutBackSystemControlModel.grid_tie_mode, OutBackSystemControlModel.set_inverter_charger_mode, OutBackSystemControlModel.control_status, OutBackSystemControlModel.set_sell_voltage, OutBackSystemControlModel.set_radian_inverter_sell_current_limit, OutBackSystemControlModel.set_absorb_voltage, OutBackSystemControlModel.set_absorb_time, OutBackSystemControlModel.set_float_voltage, OutBackSystemControlModel.set_float_time, OutBackSystemControlModel.set_inverter_charger_current_limit, OutBackSystemControlModel.set_inverter_ac1_current_limit, OutBackSystemControlModel.set_inverter_ac2_current_limit, OutBackSystemControlModel.set_ags_op_mode, OutBackSystemControlModel.ags_operational_state, OutBackSystemControlModel.ags_operational_state_timer, OutBackSystemControlModel.gen_last_run_start_time_gmt, OutBackSystemControlModel.gen_last_start_run_duration]

class OPTICSPacketStatisticsModel(Model):
    did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="OPTICS Packet Stats DID")
    length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Length of OPTICS Packet Status Block", units="Registers")
    bt_min: Uint16Field = Uint16Field("bt_min", 3, 1, Mode.R, description="Boot packet minimum time", units="msecs")
    bt_max: Uint16Field = Uint16Field("bt_max", 4, 1, Mode.R, description="Boot packet maximum time", units="msecs")
    bt_ave: Uint16Field = Uint16Field("bt_ave", 5, 1, Mode.R, description="Boot packet average time", units="msecs")
    bt_attempts: Uint16Field = Uint16Field("bt_attempts", 6, 1, Mode.R, description="Boot packet number of attempts")
    bt_errors: Uint16Field = Uint16Field("bt_errors", 7, 1, Mode.R, description="Boot packet error returned from server count")
    bt_timeouts: Uint16Field = Uint16Field("bt_timeouts", 8, 1, Mode.R, description="Boot packet timeout from server count")
    bt_packet_timeout: Uint16Field = Uint16Field("bt_packet_timeout", 9, 1, Mode.R, description="Boot packet current gateway timeout", units="secs")
    mp_min: Uint16Field = Uint16Field("mp_min", 10, 1, Mode.R, description="Map packet minimum time", units="msecs")
    mp_max: Uint16Field = Uint16Field("mp_max", 11, 1, Mode.R, description="Map packet maximum time", units="msecs")
    mp_ave: Uint16Field = Uint16Field("mp_ave", 12, 1, Mode.R, description="Map packet average time", units="msecs")
    mp_attempts: Uint16Field = Uint16Field("mp_attempts", 13, 1, Mode.R, description="Map packet number of attempts")
    mp_errors: Uint16Field = Uint16Field("mp_errors", 14, 1, Mode.R, description="Map packet error returned from server count")
    mp_timeouts: Uint16Field = Uint16Field("mp_timeouts", 15, 1, Mode.R, description="Map packet timeout from server count")
    mp_packet_timeout: Uint16Field = Uint16Field("mp_packet_timeout", 16, 1, Mode.R, description="Map packet current gateway timeout", units="secs")
    cu_min: Uint16Field = Uint16Field("cu_min", 17, 1, Mode.R, description="Config packet minimum time", units="msecs")
    cu_max: Uint16Field = Uint16Field("cu_max", 18, 1, Mode.R, description="Config packet maximum time", units="msecs")
    cu_ave: Uint16Field = Uint16Field("cu_ave", 19, 1, Mode.R, description="Config packet average time", units="msecs")
    cu_attempts: Uint16Field = Uint16Field("cu_attempts", 20, 1, Mode.R, description="Config packet number of attempts")
    cu_errors: Uint16Field = Uint16Field("cu_errors", 21, 1, Mode.R, description="Config packet error returned from server count")
    cu_timeouts: Uint16Field = Uint16Field("cu_timeouts", 22, 1, Mode.R, description="Config packet timeout from server count")
    cu_packet_timeout: Uint16Field = Uint16Field("cu_packet_timeout", 23, 1, Mode.R, description="Config packet current gateway timeout", units="secs")
    su_min: Uint16Field = Uint16Field("su_min", 24, 1, Mode.R, description="Status packet minimum time", units="msecs")
    su_max: Uint16Field = Uint16Field("su_max", 25, 1, Mode.R, description="Status packet maximum time", units="msecs")
    su_ave: Uint16Field = Uint16Field("su_ave", 26, 1, Mode.R, description="Status packet average time", units="msecs")
    su_attempts: Uint16Field = Uint16Field("su_attempts", 27, 1, Mode.R, description="Status packet number of attempts")
    su_errors: Uint16Field = Uint16Field("su_errors", 28, 1, Mode.R, description="Status packet error returned from server count")
    su_timeouts: Uint16Field = Uint16Field("su_timeouts", 29, 1, Mode.R, description="Status packet timeout from server count")
    su_packet_timeout: Uint16Field = Uint16Field("su_packet_timeout", 30, 1, Mode.R, description="Status packet current gateway timeout", units="secs")
    pg_min: Uint16Field = Uint16Field("pg_min", 31, 1, Mode.R, description="Ping packet minimum time", units="msecs")
    pg_max: Uint16Field = Uint16Field("pg_max", 32, 1, Mode.R, description="Ping packet maximum time", units="msecs")
    pg_ave: Uint16Field = Uint16Field("pg_ave", 33, 1, Mode.R, description="Ping packet average time", units="msecs")
    pg_attempts: Uint16Field = Uint16Field("pg_attempts", 34, 1, Mode.R, description="Ping packet number of attempts")
    pg_errors: Uint16Field = Uint16Field("pg_errors", 35, 1, Mode.R, description="Ping packet error returned from server count")
    pg_timeouts: Uint16Field = Uint16Field("pg_timeouts", 36, 1, Mode.R, description="Ping packet timeout from server count")
    pg_packet_timeout: Uint16Field = Uint16Field("pg_packet_timeout", 37, 1, Mode.R, description="Ping packet current gateway timeout", units="secs")
    mb_min: Uint16Field = Uint16Field("mb_min", 38, 1, Mode.R, description="Modbus packet minimum time", units="msecs")
    mb_max: Uint16Field = Uint16Field("mb_max", 39, 1, Mode.R, description="Modbus packet maximum time", units="msecs")
    mb_ave: Uint16Field = Uint16Field("mb_ave", 40, 1, Mode.R, description="Modbus packet average time", units="msecs")
    mb_attempts: Uint16Field = Uint16Field("mb_attempts", 41, 1, Mode.R, description="Modbus packet number of attempts")
    mb_errors: Uint16Field = Uint16Field("mb_errors", 42, 1, Mode.R, description="Modbus packet error returned from server count")
    mb_timeouts: Uint16Field = Uint16Field("mb_timeouts", 43, 1, Mode.R, description="Modbus packet timeout from server count")
    mb_packet_timeout: Uint16Field = Uint16Field("mb_packet_timeout", 44, 1, Mode.R, description="Modbus packet current gateway timeout", units="secs")
    fu_min: Uint16Field = Uint16Field("fu_min", 45, 1, Mode.R, description="File IO packet minimum time", units="msecs")
    fu_max: Uint16Field = Uint16Field("fu_max", 46, 1, Mode.R, description="File IO packet maximum time", units="msecs")
    fu_ave: Uint16Field = Uint16Field("fu_ave", 47, 1, Mode.R, description="File IO packet average time", units="msecs")
    fu_attempts: Uint16Field = Uint16Field("fu_attempts", 48, 1, Mode.R, description="File IO packet number of attempts")
    fu_errors: Uint16Field = Uint16Field("fu_errors", 49, 1, Mode.R, description="File IO packet error returned from server count")
    fu_timeouts: Uint16Field = Uint16Field("fu_timeouts", 50, 1, Mode.R, description="File IO packet timeout from server count")
    fu_packet_timeout: Uint16Field = Uint16Field("fu_packet_timeout", 51, 1, Mode.R, description="File IO packet current gateway timeout", units="secs")
    ev_min: Uint16Field = Uint16Field("ev_min", 52, 1, Mode.R, description="Event packet minimum time", units="msecs")
    ev_max: Uint16Field = Uint16Field("ev_max", 53, 1, Mode.R, description="Event packet maximum time", units="msecs")
    ev_ave: Uint16Field = Uint16Field("ev_ave", 54, 1, Mode.R, description="Event packet average time", units="msecs")
    ev_attempts: Uint16Field = Uint16Field("ev_attempts", 55, 1, Mode.R, description="Event packet number of attempts")
    ev_errors: Uint16Field = Uint16Field("ev_errors", 56, 1, Mode.R, description="Event packet error returned from server count")
    ev_timeouts: Uint16Field = Uint16Field("ev_timeouts", 57, 1, Mode.R, description="Event packet timeout from server count")
    ev_packet_timeout: Uint16Field = Uint16Field("ev_packet_timeout", 58, 1, Mode.R, description="Event packet current gateway timeout", units="secs")


OPTICSPacketStatisticsModel.__model_fields__ = [OPTICSPacketStatisticsModel.did, OPTICSPacketStatisticsModel.length, OPTICSPacketStatisticsModel.bt_min, OPTICSPacketStatisticsModel.bt_max, OPTICSPacketStatisticsModel.bt_ave, OPTICSPacketStatisticsModel.bt_attempts, OPTICSPacketStatisticsModel.bt_errors, OPTICSPacketStatisticsModel.bt_timeouts, OPTICSPacketStatisticsModel.bt_packet_timeout, OPTICSPacketStatisticsModel.mp_min, OPTICSPacketStatisticsModel.mp_max, OPTICSPacketStatisticsModel.mp_ave, OPTICSPacketStatisticsModel.mp_attempts, OPTICSPacketStatisticsModel.mp_errors, OPTICSPacketStatisticsModel.mp_timeouts, OPTICSPacketStatisticsModel.mp_packet_timeout, OPTICSPacketStatisticsModel.cu_min, OPTICSPacketStatisticsModel.cu_max, OPTICSPacketStatisticsModel.cu_ave, OPTICSPacketStatisticsModel.cu_attempts, OPTICSPacketStatisticsModel.cu_errors, OPTICSPacketStatisticsModel.cu_timeouts, OPTICSPacketStatisticsModel.cu_packet_timeout, OPTICSPacketStatisticsModel.su_min, OPTICSPacketStatisticsModel.su_max, OPTICSPacketStatisticsModel.su_ave, OPTICSPacketStatisticsModel.su_attempts, OPTICSPacketStatisticsModel.su_errors, OPTICSPacketStatisticsModel.su_timeouts, OPTICSPacketStatisticsModel.su_packet_timeout, OPTICSPacketStatisticsModel.pg_min, OPTICSPacketStatisticsModel.pg_max, OPTICSPacketStatisticsModel.pg_ave, OPTICSPacketStatisticsModel.pg_attempts, OPTICSPacketStatisticsModel.pg_errors, OPTICSPacketStatisticsModel.pg_timeouts, OPTICSPacketStatisticsModel.pg_packet_timeout, OPTICSPacketStatisticsModel.mb_min, OPTICSPacketStatisticsModel.mb_max, OPTICSPacketStatisticsModel.mb_ave, OPTICSPacketStatisticsModel.mb_attempts, OPTICSPacketStatisticsModel.mb_errors, OPTICSPacketStatisticsModel.mb_timeouts, OPTICSPacketStatisticsModel.mb_packet_timeout, OPTICSPacketStatisticsModel.fu_min, OPTICSPacketStatisticsModel.fu_max, OPTICSPacketStatisticsModel.fu_ave, OPTICSPacketStatisticsModel.fu_attempts, OPTICSPacketStatisticsModel.fu_errors, OPTICSPacketStatisticsModel.fu_timeouts, OPTICSPacketStatisticsModel.fu_packet_timeout, OPTICSPacketStatisticsModel.ev_min, OPTICSPacketStatisticsModel.ev_max, OPTICSPacketStatisticsModel.ev_ave, OPTICSPacketStatisticsModel.ev_attempts, OPTICSPacketStatisticsModel.ev_errors, OPTICSPacketStatisticsModel.ev_timeouts, OPTICSPacketStatisticsModel.ev_packet_timeout]

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
