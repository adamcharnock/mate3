"""This file is auto generated, do not edit. The generation code can be found in code_generator.py"""


from enum import Enum, IntFlag, unique
from mate3.sunspec.fields import (
    Mode,
    StringField,
    Int16Field,
    Uint16Field,
    Uint32Field,
    FloatInt16Field,
    FloatUint16Field,
    FloatUint32Field,
    EnumUint16Field,
    EnumInt16Field,
    Bit16Field,
    Bit32Field,
    DescribedIntFlag,
    AddressField
)
from mate3.sunspec.model_base import Model


@unique
class CCconfigFaultsFlags(DescribedIntFlag):
    fault_input_active = 16, "EX80 Fault Input Active"
    shorted_battery_temperature_sensor = 32, "Shorted Battery Temp sensor"
    over_temperature = 64, "Over Tempurature Fault"
    voc_too_high = 128, "PV Input voltage too high"


@unique
class FNStatusFlags(DescribedIntFlag):
    relay_status = 1, "AUX Relay Enabled (Unset means 'AUX Relay Disabled')"
    charged_parms = 2, "Charged Parms Met (Unset means 'Charged Parms Not Met')"


@unique
class FXErrorFlags(DescribedIntFlag):
    low_vac = 1, "Low AC output voltage"
    stacking_error = 2, "Stacking error"
    over_temperature = 4, "Over temperature error"
    low_vdc = 8, "Low battery voltage"
    phase_loss = 16, "Phase loss"
    high_vdc = 32, "High battery voltage"
    ac_shorted = 64, "AC output shorted"
    ac_backfeed = 128, "AC backfeed"


@unique
class FXSellStatusFlags(DescribedIntFlag):
    ac_input_frequency_too_high = 1, "AC input frequency too high"
    ac_input_frequency_too_low = 2, "AC input frequency too low"
    ac_input_voltage_too_low = 4, "AC input voltage too low"
    ac_input_voltage_too_high = 8, "AC input voltage too high"
    awaiting_sell_delay = 16, "Awaiting sell delay"
    disabled = 32, "Sell disabled"
    battery_voltage_less_than_target = 64, "Battery voltage less than target"
    ac2_selected = 128, "AC2 Selected"


@unique
class FXWarningFlags(DescribedIntFlag):
    ac_input_frequency_too_high = 1, "AC input frequency too high"
    ac_input_frequency_too_low = 2, "AC input frequency too low"
    ac_input_voltage_too_low = 4, "AC input voltage too low"
    ac_input_voltage_too_high = 8, "AC input voltage too high"
    ac_input_current_exceeds_max = 16, "AC input current exceeds max"
    temperature_sensor_bad = 32, "Temperature sensor bad"
    communications_error = 64, "Communications error"
    cooling_fan_fault = 128, "Cooling fan fault"


@unique
class GSSingleErrorFlags(DescribedIntFlag):
    low_vac = 1, "Low AC output voltage"
    stacking_error = 2, "Stacking error"
    over_temperature = 4, "Over temperature error"
    low_vdc = 8, "Low battery voltage"
    phase_loss = 16, "Phase loss"
    high_vdc = 32, "High battery voltage"
    ac_shorted = 64, "AC output shorted"
    ac_backfeed = 128, "AC backfeed"


@unique
class GSSingleSellStatusFlags(DescribedIntFlag):
    ac_input_frequency_too_high = 1, "AC input frequency too high"
    ac_input_frequency_too_low = 2, "AC input frequency too low"
    ac_input_voltage_too_low = 4, "AC input voltage too low"
    ac_input_voltage_too_high = 8, "AC input voltage too high"
    awaiting_sell_delay = 16, "Awaiting sell delay"
    disabled = 32, "Sell disabled"
    battery_voltage_less_than_target = 64, "Battery voltage less than target"


@unique
class GSSingleWarningFlags(DescribedIntFlag):
    ac_input_frequency_too_high = 1, "AC input frequency too high"
    ac_input_frequency_too_low = 2, "AC input frequency too low"
    ac_input_voltage_too_low = 4, "AC input voltage too low"
    ac_input_voltage_too_high = 8, "AC input voltage too high"
    ac_input_current_exceeds_max = 16, "AC input current exceeds max"
    temperature_sensor_bad = 32, "Temperature sensor bad"
    communications_error = 64, "Communications error"
    cooling_fan_fault = 128, "Cooling fan fault"


@unique
class GSSplitErrorFlags(DescribedIntFlag):
    low_vac = 1, "Low AC output voltage"
    stacking_error = 2, "Stacking error"
    over_temperature = 4, "Over temperature error"
    low_vdc = 8, "Low battery voltage"
    phase_loss = 16, "Phase loss"
    high_vdc = 32, "High battery voltage"
    ac_shorted = 64, "AC output shorted"
    ac_backfeed = 128, "AC backfeed"


@unique
class GSSplitSellStatusFlags(DescribedIntFlag):
    ac_input_frequency_too_high = 1, "AC input frequency too high"
    ac_input_frequency_too_low = 2, "AC input frequency too low"
    ac_input_voltage_too_low = 4, "AC input voltage too low"
    ac_input_voltage_too_high = 8, "AC input voltage too high"
    awaiting_sell_delay = 16, "Awaiting sell delay"
    disabled = 32, "Sell disabled"
    battery_voltage_less_than_target = 64, "Battery voltage less than target"


@unique
class GSSplitWarningFlags(DescribedIntFlag):
    ac_input_frequency_too_high = 1, "AC input frequency too high"
    ac_input_frequency_too_low = 2, "AC input frequency too low"
    ac_input_voltage_too_low = 4, "AC input voltage too low"
    ac_input_voltage_too_high = 8, "AC input voltage too high"
    ac_input_current_exceeds_max = 16, "AC input current exceeds max"
    temperature_sensor_bad = 32, "Temperature sensor bad"
    communications_error = 64, "Communications error"
    cooling_fan_fault = 128, "Cooling fan fault"


@unique
class IEvent1Flags(DescribedIntFlag):
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
class OBControlStatusFlags(DescribedIntFlag):
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
class OutBackErrorFlags(DescribedIntFlag):
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
class OutBackStatusFlags(DescribedIntFlag):
    out_back_status_firmware_update_complete = 1, "Firmware Update Complete"


@unique
class OutBackUpdateDeviceFirmwarePortFlags(DescribedIntFlag):
    portnumber = 255, "Port Number"
    update_percentage = 65280, "Firmware Update Percentage"


class SunSpecHeaderModel(Model):
    def __init__(self):
        self.did: Uint32Field = Uint32Field("did", 1, 2, Mode.R)
        self.model_id: Uint16Field = Uint16Field("model_id", 3, 1, Mode.R)
        self.length: Uint16Field = Uint16Field("length", 4, 1, Mode.R)
        self.manufacturer: StringField = StringField("manufacturer", 5, 16, Mode.R)
        self.model: StringField = StringField("model", 21, 16, Mode.R)
        self.options: StringField = StringField("options", 37, 8, Mode.R)
        self.version: StringField = StringField("version", 45, 8, Mode.R)
        self.serial_number: StringField = StringField("serial_number", 53, 16, Mode.R)


class SunSpecEndModel(Model):
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Should be 65535")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, description="Should be 0")


class SunSpecCommonModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Common Model block")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of block in 16-bit registers")
        self.manufacturer: StringField = StringField("manufacturer", 3, 16, Mode.R)
        self.model: StringField = StringField("model", 19, 16, Mode.R)
        self.options: StringField = StringField("options", 35, 8, Mode.R)
        self.version: StringField = StringField("version", 43, 8, Mode.R)
        self.serial_number: StringField = StringField("serial_number", 51, 16, Mode.R)
        self.device_address: Uint16Field = Uint16Field("device_address", 67, 1, Mode.RW)


class SunSpecInverterSinglePhaseModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Single Phase Inverter")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of model block")
        self.ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 7, 1, Mode.R, units="SF", description="AC Current Scale factor")
        self.ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 14, 1, Mode.R, units="SF", description="AC Voltage Scale factor")
        self.ac_power_scale_factor: Int16Field = Int16Field("ac_power_scale_factor", 16, 1, Mode.R, units="SF", description="AC Power Scale factor")
        self.ac_frequency_scale_factor: Int16Field = Int16Field("ac_frequency_scale_factor", 18, 1, Mode.R, units="SF", description="Scale factor")
        self.ac_va_scale_factor: Int16Field = Int16Field("ac_va_scale_factor", 20, 1, Mode.R, units="SF", description="Scale factor")
        self.ac_var_scale_factor: Int16Field = Int16Field("ac_var_scale_factor", 22, 1, Mode.R, units="SF", description="Scale factor")
        self.ac_pf_scale_factor: Int16Field = Int16Field("ac_pf_scale_factor", 24, 1, Mode.R, units="SF", description="Scale factor")
        self.ac_energy_wh_scale_factor: Uint16Field = Uint16Field("ac_energy_wh_scale_factor", 27, 1, Mode.R, units="SF", description="AC Lifetime Energy production scale factor")
        self.dc_current_scale_factor: Int16Field = Int16Field("dc_current_scale_factor", 29, 1, Mode.R, units="SF", description="Scale factor")
        self.dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 31, 1, Mode.R, units="SF", description="Scale factor")
        self.dc_power_scale_factor: Int16Field = Int16Field("dc_power_scale_factor", 33, 1, Mode.R, units="SF", description="Scale factor")
        self.temp_scale_factor: Int16Field = Int16Field("temp_scale_factor", 38, 1, Mode.R, units="SF", description="Scale factor")
        self.status: Uint16Field = Uint16Field("status", 39, 1, Mode.R, units="Enumerated", description="Operating State")
        self.status_vendor: Uint16Field = Uint16Field("status_vendor", 40, 1, Mode.R, units="Enumerated", description="Vendor Defined Operating State")
        self.event_1: Bit32Field = Bit32Field("event_1", 41, 2, Mode.R, flags=IEvent1Flags, description="Event Flags (bits 0-31)")
        self.ac_current: FloatUint16Field = FloatUint16Field("ac_current", 3, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="AC Total Current value")
        self.ac_current_a: FloatUint16Field = FloatUint16Field("ac_current_a", 4, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="AC Phase-A Current value")
        self.ac_current_b: FloatUint16Field = FloatUint16Field("ac_current_b", 5, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="AC Phase-B Current value")
        self.ac_current_c: FloatUint16Field = FloatUint16Field("ac_current_c", 6, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="AC Phase-C Current value")
        self.ac_voltage_ab: FloatUint16Field = FloatUint16Field("ac_voltage_ab", 8, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase-AB value")
        self.ac_voltage_bc: FloatUint16Field = FloatUint16Field("ac_voltage_bc", 9, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase BC value")
        self.ac_voltage_ca: FloatUint16Field = FloatUint16Field("ac_voltage_ca", 10, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase CA value")
        self.ac_voltage_an: FloatUint16Field = FloatUint16Field("ac_voltage_an", 11, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase-A-to-neutral value")
        self.ac_voltage_bn: FloatUint16Field = FloatUint16Field("ac_voltage_bn", 12, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase B-to-neutral value")
        self.ac_voltage_cn: FloatUint16Field = FloatUint16Field("ac_voltage_cn", 13, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase C-to-neutral value")
        self.ac_power: FloatInt16Field = FloatInt16Field("ac_power", 15, 1, Mode.R, units="Watts", scale_factor=self.ac_power_scale_factor, description="AC Power value")
        self.ac_frequency: FloatUint16Field = FloatUint16Field("ac_frequency", 17, 1, Mode.R, units="Hertz", scale_factor=self.ac_frequency_scale_factor, description="AC Frequency value")
        self.ac_va: FloatInt16Field = FloatInt16Field("ac_va", 19, 1, Mode.R, units="VA", scale_factor=self.ac_va_scale_factor, description="Apparent Power")
        self.ac_var: FloatInt16Field = FloatInt16Field("ac_var", 21, 1, Mode.R, units="VAR", scale_factor=self.ac_var_scale_factor, description="Reactive Power")
        self.ac_pf: FloatInt16Field = FloatInt16Field("ac_pf", 23, 1, Mode.R, scale_factor=self.ac_pf_scale_factor, description="Power Factor")
        self.ac_energy_wh: FloatUint32Field = FloatUint32Field("ac_energy_wh", 25, 2, Mode.R, units="WattHours", scale_factor=self.ac_energy_wh_scale_factor, description="AC Lifetime Energy production")
        self.dc_current: FloatUint16Field = FloatUint16Field("dc_current", 28, 1, Mode.R, units="Amps", scale_factor=self.dc_current_scale_factor, description="DC Current value")
        self.dc_voltage: FloatUint16Field = FloatUint16Field("dc_voltage", 30, 1, Mode.R, units="Volts", scale_factor=self.dc_voltage_scale_factor, description="DC Voltage value")
        self.dc_power: FloatInt16Field = FloatInt16Field("dc_power", 32, 1, Mode.R, units="Watts", scale_factor=self.dc_power_scale_factor, description="DC Power value")
        self.temp_cab: FloatInt16Field = FloatInt16Field("temp_cab", 34, 1, Mode.R, units="Degrees C", scale_factor=self.temp_scale_factor, description="Cabinet Temperature")
        self.temp_sink: FloatInt16Field = FloatInt16Field("temp_sink", 35, 1, Mode.R, units="Degrees C", scale_factor=self.temp_scale_factor, description="Coolant or Heat Sink Temperature")
        self.temp_trans: FloatInt16Field = FloatInt16Field("temp_trans", 36, 1, Mode.R, units="Degrees C", scale_factor=self.temp_scale_factor, description="Transformer Temperature")
        self.temp_other: FloatInt16Field = FloatInt16Field("temp_other", 37, 1, Mode.R, units="Degrees C", scale_factor=self.temp_scale_factor, description="Other Temperature")


class SunSpecInverterSplitPhaseModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Split Phase Inverter")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of model block")
        self.ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 7, 1, Mode.R, units="SF", description="AC Current Scale factor")
        self.ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 14, 1, Mode.R, units="SF", description="AC Voltage Scale factor")
        self.ac_power_scale_factor: Int16Field = Int16Field("ac_power_scale_factor", 16, 1, Mode.R, units="SF", description="AC Power Scale factor")
        self.ac_frequency_scale_factor: Int16Field = Int16Field("ac_frequency_scale_factor", 18, 1, Mode.R, units="SF", description="Scale factor")
        self.ac_va_scale_factor: Int16Field = Int16Field("ac_va_scale_factor", 20, 1, Mode.R, units="SF", description="Scale factor")
        self.ac_var_scale_factor: Int16Field = Int16Field("ac_var_scale_factor", 22, 1, Mode.R, units="SF", description="Scale factor")
        self.ac_pf_scale_factor: Int16Field = Int16Field("ac_pf_scale_factor", 24, 1, Mode.R, units="SF", description="Scale factor")
        self.ac_energy_wh_scale_factor: Uint16Field = Uint16Field("ac_energy_wh_scale_factor", 27, 1, Mode.R, units="SF", description="AC Lifetime Energy production scale factor")
        self.dc_current_scale_factor: Int16Field = Int16Field("dc_current_scale_factor", 29, 1, Mode.R, units="SF", description="Scale factor")
        self.dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 31, 1, Mode.R, units="SF", description="Scale factor")
        self.dc_power_scale_factor: Int16Field = Int16Field("dc_power_scale_factor", 33, 1, Mode.R, units="SF", description="Scale factor")
        self.temp_scale_factor: Int16Field = Int16Field("temp_scale_factor", 38, 1, Mode.R, units="SF", description="Scale factor")
        self.status: Uint16Field = Uint16Field("status", 39, 1, Mode.R, units="Enumerated", description="Operating State")
        self.status_vendor: Uint16Field = Uint16Field("status_vendor", 40, 1, Mode.R, units="Enumerated", description="Vendor Defined Operating State")
        self.event_1: Bit32Field = Bit32Field("event_1", 41, 2, Mode.R, flags=IEvent1Flags, description="Event Flags (bits 0-31)")
        self.ac_current: FloatUint16Field = FloatUint16Field("ac_current", 3, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="AC Total Current value")
        self.ac_current_a: FloatUint16Field = FloatUint16Field("ac_current_a", 4, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="AC Phase-A Current value")
        self.ac_current_b: FloatUint16Field = FloatUint16Field("ac_current_b", 5, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="AC Phase-B Current value")
        self.ac_current_c: FloatUint16Field = FloatUint16Field("ac_current_c", 6, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="AC Phase-C Current value")
        self.ac_voltage_ab: FloatUint16Field = FloatUint16Field("ac_voltage_ab", 8, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase-AB value")
        self.ac_voltage_bc: FloatUint16Field = FloatUint16Field("ac_voltage_bc", 9, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase BC value")
        self.ac_voltage_ca: FloatUint16Field = FloatUint16Field("ac_voltage_ca", 10, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase CA value")
        self.ac_voltage_an: FloatUint16Field = FloatUint16Field("ac_voltage_an", 11, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase-A-to-neutral value")
        self.ac_voltage_bn: FloatUint16Field = FloatUint16Field("ac_voltage_bn", 12, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase B-to-neutral value")
        self.ac_voltage_cn: FloatUint16Field = FloatUint16Field("ac_voltage_cn", 13, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase C-to-neutral value")
        self.ac_power: FloatInt16Field = FloatInt16Field("ac_power", 15, 1, Mode.R, units="Watts", scale_factor=self.ac_power_scale_factor, description="AC Power value")
        self.ac_frequency: FloatUint16Field = FloatUint16Field("ac_frequency", 17, 1, Mode.R, units="Hertz", scale_factor=self.ac_frequency_scale_factor, description="AC Frequency value")
        self.ac_va: FloatInt16Field = FloatInt16Field("ac_va", 19, 1, Mode.R, units="VA", scale_factor=self.ac_va_scale_factor, description="Apparent Power")
        self.ac_var: FloatInt16Field = FloatInt16Field("ac_var", 21, 1, Mode.R, units="VAR", scale_factor=self.ac_var_scale_factor, description="Reactive Power")
        self.ac_pf: FloatInt16Field = FloatInt16Field("ac_pf", 23, 1, Mode.R, scale_factor=self.ac_pf_scale_factor, description="Power Factor")
        self.ac_energy_wh: FloatUint32Field = FloatUint32Field("ac_energy_wh", 25, 2, Mode.R, units="WattHours", scale_factor=self.ac_energy_wh_scale_factor, description="AC Lifetime Energy production")
        self.dc_current: FloatUint16Field = FloatUint16Field("dc_current", 28, 1, Mode.R, units="Amps", scale_factor=self.dc_current_scale_factor, description="DC Current value")
        self.dc_voltage: FloatUint16Field = FloatUint16Field("dc_voltage", 30, 1, Mode.R, units="Volts", scale_factor=self.dc_voltage_scale_factor, description="DC Voltage value")
        self.dc_power: FloatInt16Field = FloatInt16Field("dc_power", 32, 1, Mode.R, units="Watts", scale_factor=self.dc_power_scale_factor, description="DC Power value")
        self.temp_cab: FloatInt16Field = FloatInt16Field("temp_cab", 34, 1, Mode.R, units="Degrees C", scale_factor=self.temp_scale_factor, description="Cabinet Temperature")
        self.temp_sink: FloatInt16Field = FloatInt16Field("temp_sink", 35, 1, Mode.R, units="Degrees C", scale_factor=self.temp_scale_factor, description="Coolant or Heat Sink Temperature")
        self.temp_trans: FloatInt16Field = FloatInt16Field("temp_trans", 36, 1, Mode.R, units="Degrees C", scale_factor=self.temp_scale_factor, description="Transformer Temperature")
        self.temp_other: FloatInt16Field = FloatInt16Field("temp_other", 37, 1, Mode.R, units="Degrees C", scale_factor=self.temp_scale_factor, description="Other Temperature")


class SunSpecInverterThreePhaseModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Three Phase Inverter")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of model block")
        self.ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 7, 1, Mode.R, units="SF", description="AC Current Scale factor")
        self.ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 14, 1, Mode.R, units="SF", description="AC Voltage Scale factor")
        self.ac_power_scale_factor: Int16Field = Int16Field("ac_power_scale_factor", 16, 1, Mode.R, units="SF", description="AC Power Scale factor")
        self.ac_frequency_scale_factor: Int16Field = Int16Field("ac_frequency_scale_factor", 18, 1, Mode.R, units="SF", description="Scale factor")
        self.ac_va_scale_factor: Int16Field = Int16Field("ac_va_scale_factor", 20, 1, Mode.R, units="SF", description="Scale factor")
        self.ac_var_scale_factor: Int16Field = Int16Field("ac_var_scale_factor", 22, 1, Mode.R, units="SF", description="Scale factor")
        self.ac_pf_scale_factor: Int16Field = Int16Field("ac_pf_scale_factor", 24, 1, Mode.R, units="SF", description="Scale factor")
        self.ac_energy_wh_scale_factor: Uint16Field = Uint16Field("ac_energy_wh_scale_factor", 27, 1, Mode.R, units="SF", description="AC Lifetime Energy production scale factor")
        self.dc_current_scale_factor: Int16Field = Int16Field("dc_current_scale_factor", 29, 1, Mode.R, units="SF", description="Scale factor")
        self.dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 31, 1, Mode.R, units="SF", description="Scale factor")
        self.dc_power_scale_factor: Int16Field = Int16Field("dc_power_scale_factor", 33, 1, Mode.R, units="SF", description="Scale factor")
        self.temp_scale_factor: Int16Field = Int16Field("temp_scale_factor", 38, 1, Mode.R, units="SF", description="Scale factor")
        self.status: Uint16Field = Uint16Field("status", 39, 1, Mode.R, units="Enumerated", description="Operating State")
        self.status_vendor: Uint16Field = Uint16Field("status_vendor", 40, 1, Mode.R, units="Enumerated", description="Vendor Defined Operating State")
        self.event_1: Bit32Field = Bit32Field("event_1", 41, 2, Mode.R, flags=IEvent1Flags, description="Event Flags (bits 0-31)")
        self.ac_current: FloatUint16Field = FloatUint16Field("ac_current", 3, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="AC Total Current value")
        self.ac_current_a: FloatUint16Field = FloatUint16Field("ac_current_a", 4, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="AC Phase-A Current value")
        self.ac_current_b: FloatUint16Field = FloatUint16Field("ac_current_b", 5, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="AC Phase-B Current value")
        self.ac_current_c: FloatUint16Field = FloatUint16Field("ac_current_c", 6, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="AC Phase-C Current value")
        self.ac_voltage_ab: FloatUint16Field = FloatUint16Field("ac_voltage_ab", 8, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase-AB value")
        self.ac_voltage_bc: FloatUint16Field = FloatUint16Field("ac_voltage_bc", 9, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase BC value")
        self.ac_voltage_ca: FloatUint16Field = FloatUint16Field("ac_voltage_ca", 10, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase CA value")
        self.ac_voltage_an: FloatUint16Field = FloatUint16Field("ac_voltage_an", 11, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase-A-to-neutral value")
        self.ac_voltage_bn: FloatUint16Field = FloatUint16Field("ac_voltage_bn", 12, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase B-to-neutral value")
        self.ac_voltage_cn: FloatUint16Field = FloatUint16Field("ac_voltage_cn", 13, 1, Mode.R, units="Volts", scale_factor=self.ac_voltage_scale_factor, description="AC Voltage Phase C-to-neutral value")
        self.ac_power: FloatInt16Field = FloatInt16Field("ac_power", 15, 1, Mode.R, units="Watts", scale_factor=self.ac_power_scale_factor, description="AC Power value")
        self.ac_frequency: FloatUint16Field = FloatUint16Field("ac_frequency", 17, 1, Mode.R, units="Hertz", scale_factor=self.ac_frequency_scale_factor, description="AC Frequency value")
        self.ac_va: FloatInt16Field = FloatInt16Field("ac_va", 19, 1, Mode.R, units="VA", scale_factor=self.ac_va_scale_factor, description="Apparent Power")
        self.ac_var: FloatInt16Field = FloatInt16Field("ac_var", 21, 1, Mode.R, units="VAR", scale_factor=self.ac_var_scale_factor, description="Reactive Power")
        self.ac_pf: FloatInt16Field = FloatInt16Field("ac_pf", 23, 1, Mode.R, scale_factor=self.ac_pf_scale_factor, description="Power Factor")
        self.ac_energy_wh: FloatUint32Field = FloatUint32Field("ac_energy_wh", 25, 2, Mode.R, units="WattHours", scale_factor=self.ac_energy_wh_scale_factor, description="AC Lifetime Energy production")
        self.dc_current: FloatUint16Field = FloatUint16Field("dc_current", 28, 1, Mode.R, units="Amps", scale_factor=self.dc_current_scale_factor, description="DC Current value")
        self.dc_voltage: FloatUint16Field = FloatUint16Field("dc_voltage", 30, 1, Mode.R, units="Volts", scale_factor=self.dc_voltage_scale_factor, description="DC Voltage value")
        self.dc_power: FloatInt16Field = FloatInt16Field("dc_power", 32, 1, Mode.R, units="Watts", scale_factor=self.dc_power_scale_factor, description="DC Power value")
        self.temp_cab: FloatInt16Field = FloatInt16Field("temp_cab", 34, 1, Mode.R, units="Degrees C", scale_factor=self.temp_scale_factor, description="Cabinet Temperature")
        self.temp_sink: FloatInt16Field = FloatInt16Field("temp_sink", 35, 1, Mode.R, units="Degrees C", scale_factor=self.temp_scale_factor, description="Coolant or Heat Sink Temperature")
        self.temp_trans: FloatInt16Field = FloatInt16Field("temp_trans", 36, 1, Mode.R, units="Degrees C", scale_factor=self.temp_scale_factor, description="Transformer Temperature")
        self.temp_other: FloatInt16Field = FloatInt16Field("temp_other", 37, 1, Mode.R, units="Degrees C", scale_factor=self.temp_scale_factor, description="Other Temperature")


class OutBackModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Outback Interface")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of block in 16-bit registers")
        self.major_firmware_number: Uint16Field = Uint16Field("major_firmware_number", 3, 1, Mode.R, description="OutBack Major firmware revision")
        self.mid_firmware_number: Uint16Field = Uint16Field("mid_firmware_number", 4, 1, Mode.R, description="OutBack Mid firmware revision")
        self.minor_firmware_number: Uint16Field = Uint16Field("minor_firmware_number", 5, 1, Mode.R, description="OutBack Minor firmware revision")
        self.encryption_key: Uint16Field = Uint16Field("encryption_key", 6, 1, Mode.R, description="Encryption key for current session (0 = Encryption not enabled)")
        self.mac_address: StringField = StringField("mac_address", 7, 7, Mode.R, description="Ethernet MAC address")
        self.write_password: StringField = StringField("write_password", 14, 8, Mode.W, description="Password required to write to any register")
        self.enable_dhcp: EnumUint16Field = EnumUint16Field("enable_dhcp", 22, 1, Mode.RW, enum=Enum("enable_dhcp", [('DHCP Disabled, use configured network parameter', 0), ('DHCP Enabled', 1)]), description="0 = DHCP Disabled, use configured network parameter; 1 = DHCP Enabled")
        self.tcpip_address: AddressField = AddressField("tcpip_address", 23, 2, Mode.RW, description="TCP/IP Address xxx.xxx.xxx.xxx")
        self.tcpip_gateway_msw: AddressField = AddressField("tcpip_gateway_msw", 25, 2, Mode.RW, description="TCP/IP Gateway xxx.xxx.xxx.xxx")
        self.tcpip_netmask_msw: AddressField = AddressField("tcpip_netmask_msw", 27, 2, Mode.RW, description="TCP/IP Netmask xxx.xxx.xxx.xxx")
        self.tcpip_dns_1_msw: AddressField = AddressField("tcpip_dns_1_msw", 29, 2, Mode.RW, description="TCP/IP DNS 1 xxx.xxx.xxx.xxx")
        self.tcpip_dns_2_msw: AddressField = AddressField("tcpip_dns_2_msw", 31, 2, Mode.RW, description="TCP/IP DNS 2 xxx.xxx.xxx.xxx")
        self.modbus_port: Uint16Field = Uint16Field("modbus_port", 33, 1, Mode.RW, description="Outback MODBUS IP port, default 502")
        self.smtp_server_name: StringField = StringField("smtp_server_name", 34, 20, Mode.RW, description="Email server name")
        self.smtp_account_name: StringField = StringField("smtp_account_name", 54, 16, Mode.RW, description="Email account name")
        self.smtp_ssl_enable: EnumUint16Field = EnumUint16Field("smtp_ssl_enable", 70, 1, Mode.RW, enum=Enum("smtp_ssl_enable", [('SSL Disabled', 0), ('SSL Enabled (not implemented)', 1)]), description="0 = SSL Disabled; 1 = SSL Enabled (not implemented)")
        self.smtp_email_password: StringField = StringField("smtp_email_password", 71, 8, Mode.W, description="Email account password")
        self.smtp_email_user_name: StringField = StringField("smtp_email_user_name", 79, 20, Mode.RW, description="Email account User Name")
        self.status_email_interval: Uint16Field = Uint16Field("status_email_interval", 99, 1, Mode.RW, description="0 = Status Email Disabled, 1-23 Status Email every n hours")
        self.status_email_status_time: Uint16Field = Uint16Field("status_email_status_time", 100, 1, Mode.RW, description="Hour  of first status email of the day")
        self.status_email_subject_line: StringField = StringField("status_email_subject_line", 101, 25, Mode.RW, description="Status Email Subject Line")
        self.status_email_to_address_1: StringField = StringField("status_email_to_address_1", 126, 20, Mode.RW, description="Status Email to Address 1")
        self.status_email_to_address_2: StringField = StringField("status_email_to_address_2", 146, 20, Mode.RW, description="Status Email to Address 2")
        self.alarm_email_enable: EnumUint16Field = EnumUint16Field("alarm_email_enable", 166, 1, Mode.RW, enum=Enum("alarm_email_enable", [('Disabled', 0), ('Enabled', 1)]), description="0 = Disabled; 1 = Enabled")
        self.system_name: StringField = StringField("system_name", 167, 30, Mode.RW, description="OutBack System Name")
        self.alarm_email_to_address_1: StringField = StringField("alarm_email_to_address_1", 197, 15, Mode.RW, description="Status Alarm to Address 1")
        self.alarm_email_to_address_2: StringField = StringField("alarm_email_to_address_2", 212, 20, Mode.RW, description="Status Alarm to Address 2")
        self.ftp_password: StringField = StringField("ftp_password", 232, 8, Mode.W, description="FTP password")
        self.telnet_password: StringField = StringField("telnet_password", 240, 8, Mode.W, description="Telnet password (not implemented)")
        self.sd_card_data_log_write_interval: Uint16Field = Uint16Field("sd_card_data_log_write_interval", 248, 1, Mode.RW, description="0 = SD-Card Data Logging disabled, 1-60 seconds")
        self.sd_card_data_log_retain_days: Uint16Field = Uint16Field("sd_card_data_log_retain_days", 249, 1, Mode.RW, description="0 = Log until SD-Card is full then erase oldest, 1-731 Number of days to retain data logs")
        self.sd_card_data_logging_mode: EnumUint16Field = EnumUint16Field("sd_card_data_logging_mode", 250, 1, Mode.RW, enum=Enum("sd_card_data_logging_mode", [('Compact Format', 2), ('Disabled', 0), ('Excel Format', 1)]), description="0 = Disabled; 1 = Excel Format; 2 = Compact Format")
        self.time_server_name: StringField = StringField("time_server_name", 251, 20, Mode.RW, description="Timeserver domain name")
        self.enable_time_server: EnumUint16Field = EnumUint16Field("enable_time_server", 271, 1, Mode.RW, enum=Enum("enable_time_server", [('Time  Server Enabled', 1), ('Time Server Disabled, use configured time parameters', 0)]), description="0 = Time Server Disabled, use configured time parameters; 1 = Time  Server Enabled")
        self.enable_float_coordination: EnumUint16Field = EnumUint16Field("enable_float_coordination", 273, 1, Mode.RW, enum=Enum("enable_float_coordination", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.enable_fndc_charge_termination: EnumUint16Field = EnumUint16Field("enable_fndc_charge_termination", 274, 1, Mode.RW, enum=Enum("enable_fndc_charge_termination", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.enable_fndc_grid_tie_control: EnumUint16Field = EnumUint16Field("enable_fndc_grid_tie_control", 275, 1, Mode.RW, enum=Enum("enable_fndc_grid_tie_control", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.voltage_scale_factor: Int16Field = Int16Field("voltage_scale_factor", 276, 1, Mode.R, description="DC Voltage Scale Factor")
        self.hour_scale_factor: Int16Field = Int16Field("hour_scale_factor", 277, 1, Mode.R, description="Hours Scale Factor")
        self.ags_mode: EnumUint16Field = EnumUint16Field("ags_mode", 278, 1, Mode.RW, enum=Enum("ags_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.ags_port: Uint16Field = Uint16Field("ags_port", 279, 1, Mode.RW, description="AGS device port number 0-10")
        self.ags_port_type: EnumUint16Field = EnumUint16Field("ags_port_type", 280, 1, Mode.RW, enum=Enum("ags_port_type", [('Radian AUX Output', 1), ('Radian AUX Relay', 0)]), description="0=Radian AUX Relay, 1=Radian AUX Output")
        self.ags_generator_type: EnumUint16Field = EnumUint16Field("ags_generator_type", 281, 1, Mode.RW, enum=Enum("ags_generator_type", [('AC Gen', 0), ('DC Gen', 1), ('No Gen', 2)]), description="0=AC Gen, 1=DC Gen, 2=No Gen")
        self.ags_fault_time: Uint16Field = Uint16Field("ags_fault_time", 284, 1, Mode.RW, units="Minutes", description="AGS Generator fault time delay")
        self.ags_gen_cool_down_time: Uint16Field = Uint16Field("ags_gen_cool_down_time", 285, 1, Mode.RW, units="Minutes", description="AGS Generator Cool Down Time")
        self.ags_gen_warm_up_time: Uint16Field = Uint16Field("ags_gen_warm_up_time", 286, 1, Mode.RW, units="Minutes", description="AGS Generator Warm Up Time")
        self.ags_generator_exercise_mode: EnumUint16Field = EnumUint16Field("ags_generator_exercise_mode", 287, 1, Mode.RW, enum=Enum("ags_generator_exercise_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.ags_exercise_start_hour: Uint16Field = Uint16Field("ags_exercise_start_hour", 288, 1, Mode.RW, units="Hour", description="Exercise Start Hour 0-23")
        self.ags_exercise_start_minute: Uint16Field = Uint16Field("ags_exercise_start_minute", 289, 1, Mode.RW, units="Minutes", description="Exercise Start Minute 0-59")
        self.ags_exercise_day: EnumUint16Field = EnumUint16Field("ags_exercise_day", 290, 1, Mode.RW, enum=Enum("ags_exercise_day", [('Fri', 5), ('Mon', 1), ('Sat', 6), ('Sun', 0), ('Thr', 4), ('Tue', 2), ('Wed', 3)]), description="0=Sun, 1=Mon, 2=Tue, 3=Wed, 4=Thr, 5=Fri, 6=Sat")
        self.ags_exercise_period: Uint16Field = Uint16Field("ags_exercise_period", 291, 1, Mode.RW, units="Minutes", description="Exercise Period 1-240 minutes")
        self.ags_exercise_interval: Uint16Field = Uint16Field("ags_exercise_interval", 292, 1, Mode.RW, units="Weeks", description="Exercise interval 1-8 Weeks")
        self.ags_sell_mode: EnumUint16Field = EnumUint16Field("ags_sell_mode", 293, 1, Mode.RW, enum=Enum("ags_sell_mode", [('Selling Disabled', 1), ('Selling Enabled', 0)]), description="Sell During Generator Exercise Period, 0=Selling Enabled, 1=Selling Disabled")
        self.ags_2_min_start_mode: EnumUint16Field = EnumUint16Field("ags_2_min_start_mode", 294, 1, Mode.RW, enum=Enum("ags_2_min_start_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.ags_2_hour_start_mode: EnumUint16Field = EnumUint16Field("ags_2_hour_start_mode", 296, 1, Mode.RW, enum=Enum("ags_2_hour_start_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.ags_24_hour_start_mode: EnumUint16Field = EnumUint16Field("ags_24_hour_start_mode", 298, 1, Mode.RW, enum=Enum("ags_24_hour_start_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.ags_load_start_mode: EnumUint16Field = EnumUint16Field("ags_load_start_mode", 300, 1, Mode.RW, enum=Enum("ags_load_start_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.ags_load_start_kw: Uint16Field = Uint16Field("ags_load_start_kw", 301, 1, Mode.RW, units="kWatts", description="Load Start kWatts")
        self.ags_load_start_delay: Uint16Field = Uint16Field("ags_load_start_delay", 302, 1, Mode.RW, units="Minutes", description="Load Start Delay")
        self.ags_load_stop_kw: Uint16Field = Uint16Field("ags_load_stop_kw", 303, 1, Mode.RW, units="kWatts", description="Load Stop kWatts")
        self.ags_load_stop_delay: Uint16Field = Uint16Field("ags_load_stop_delay", 304, 1, Mode.RW, units="Minutes", description="Load Stop Delay")
        self.ags_soc_start_mode: EnumUint16Field = EnumUint16Field("ags_soc_start_mode", 305, 1, Mode.RW, enum=Enum("ags_soc_start_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.ags_soc_start_percentage: Uint16Field = Uint16Field("ags_soc_start_percentage", 306, 1, Mode.RW, units="Percent", description="AGS SOC Start Percentage")
        self.ags_soc_stop_percentage: Uint16Field = Uint16Field("ags_soc_stop_percentage", 307, 1, Mode.RW, units="Percent", description="AGS SOC Stop Percentage")
        self.ags_enable_full_charge_mode: EnumUint16Field = EnumUint16Field("ags_enable_full_charge_mode", 308, 1, Mode.RW, enum=Enum("ags_enable_full_charge_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.ags_full_charge_interval: Uint16Field = Uint16Field("ags_full_charge_interval", 309, 1, Mode.RW, units="Days", description="AGS SOC Full Charge Interval")
        self.ags_must_run_mode: EnumUint16Field = EnumUint16Field("ags_must_run_mode", 310, 1, Mode.RW, enum=Enum("ags_must_run_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.ags_must_run_weekday_start_hour: Uint16Field = Uint16Field("ags_must_run_weekday_start_hour", 311, 1, Mode.RW, units="Hour", description="AGS Must Run Weekday Start Hour 0-23")
        self.ags_must_run_weekday_start_minute: Uint16Field = Uint16Field("ags_must_run_weekday_start_minute", 312, 1, Mode.RW, units="Minute", description="AGS Must Run Weekday Start Minute 0-59")
        self.ags_must_run_weekday_stop_hour: Uint16Field = Uint16Field("ags_must_run_weekday_stop_hour", 313, 1, Mode.RW, units="Hour", description="AGS Must Run Weekday Stop Hour 0-23")
        self.ags_must_run_weekday_stop_minute: Uint16Field = Uint16Field("ags_must_run_weekday_stop_minute", 314, 1, Mode.RW, units="Minute", description="AGS Must Run Weekday Stop Minute 0-59")
        self.ags_must_run_weekend_start_hour: Uint16Field = Uint16Field("ags_must_run_weekend_start_hour", 315, 1, Mode.RW, units="Hour", description="AGS Must Run Weekend Start Hour 0-23")
        self.ags_must_run_weekend_start_minute: Uint16Field = Uint16Field("ags_must_run_weekend_start_minute", 316, 1, Mode.RW, units="Minute", description="AGS Must Run Weekend Start Minute 0-59")
        self.ags_must_run_weekend_stop_hour: Uint16Field = Uint16Field("ags_must_run_weekend_stop_hour", 317, 1, Mode.RW, units="Hour", description="AGS Must Run Weekend Stop Hour 0-23")
        self.ags_must_run_weekend_stop_minute: Uint16Field = Uint16Field("ags_must_run_weekend_stop_minute", 318, 1, Mode.RW, units="Minute", description="AGS Must Run Weekend Stop Minute 0-59")
        self.ags_quiet_time_mode: EnumUint16Field = EnumUint16Field("ags_quiet_time_mode", 319, 1, Mode.RW, enum=Enum("ags_quiet_time_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.ags_quiet_time_weekday_start_hour: Uint16Field = Uint16Field("ags_quiet_time_weekday_start_hour", 320, 1, Mode.RW, units="Hour", description="AGS Quiet Time Weekday Start Hour 0-23")
        self.ags_quiet_time_weekday_start_minute: Uint16Field = Uint16Field("ags_quiet_time_weekday_start_minute", 321, 1, Mode.RW, units="Minute", description="AGS Quiet Time Weekday Start Minute 0-59")
        self.ags_quiet_time_weekday_stop_hour: Uint16Field = Uint16Field("ags_quiet_time_weekday_stop_hour", 322, 1, Mode.RW, units="Hour", description="AGS Quiet Time Weekday Stop Hour 0-23")
        self.ags_quiet_time_weekday_stop_minute: Uint16Field = Uint16Field("ags_quiet_time_weekday_stop_minute", 323, 1, Mode.RW, units="Minute", description="AGS Quiet Time Weekday Stop Minute 0-59")
        self.ags_quiet_time_weekend_start_hour: Uint16Field = Uint16Field("ags_quiet_time_weekend_start_hour", 324, 1, Mode.RW, units="Hour", description="AGS Quiet Time Weekend Start Hour 0-23")
        self.ags_quiet_time_weekend_start_minute: Uint16Field = Uint16Field("ags_quiet_time_weekend_start_minute", 325, 1, Mode.RW, units="Minute", description="AGS Quiet Time Weekend Start Minute 0-59")
        self.ags_quiet_time_weekend_stop_hour: Uint16Field = Uint16Field("ags_quiet_time_weekend_stop_hour", 326, 1, Mode.RW, units="Hour", description="AGS Quiet Time Weekend Stop Hour 0-23")
        self.ags_quiet_time_weekend_stop_minute: Uint16Field = Uint16Field("ags_quiet_time_weekend_stop_minute", 327, 1, Mode.RW, units="Minute", description="AGS Quiet Time Weekend Stop Minute 0-59")
        self.ags_total_generator_run_time: Uint32Field = Uint32Field("ags_total_generator_run_time", 328, 2, Mode.RW, units="Hours", description="AGS Generator Total Run Time in Seconds")
        self.hbx_mode: EnumUint16Field = EnumUint16Field("hbx_mode", 330, 1, Mode.RW, enum=Enum("hbx_mode", [('Both', 3), ('Disabled', 0), ('SOC Only', 2), ('Voltage Only', 1)]), description="0=Disabled, 1=Voltage Only, 2=SOC Only, 3=Both")
        self.hbx_grid_connect_soc: Uint16Field = Uint16Field("hbx_grid_connect_soc", 335, 1, Mode.RW, units="Percent", description="HBX Grid Connect SOC Percentage")
        self.hbx_grid_disconnect_soc: Uint16Field = Uint16Field("hbx_grid_disconnect_soc", 336, 1, Mode.RW, units="Percent", description="HBX Grid Disconnect SOC Percentage")
        self.grid_use_interval_1_mode: EnumUint16Field = EnumUint16Field("grid_use_interval_1_mode", 337, 1, Mode.RW, enum=Enum("grid_use_interval_1_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.grid_use_interval_1_weekday_start_hour: Uint16Field = Uint16Field("grid_use_interval_1_weekday_start_hour", 338, 1, Mode.RW, units="Hour", description="Grid Use Interval 1 Weekday Start Hour 0-23")
        self.grid_use_interval_1_weekday_start_minute: Uint16Field = Uint16Field("grid_use_interval_1_weekday_start_minute", 339, 1, Mode.RW, units="Hour", description="Grid Use Interval 1 Weekday Start Minute 0-59")
        self.grid_use_interval_1_weekday_stop_hour: Uint16Field = Uint16Field("grid_use_interval_1_weekday_stop_hour", 340, 1, Mode.RW, units="Hour", description="Grid Use Interval 1 Weekday Stop Hour 0-23")
        self.grid_use_interval_1_weekday_stop_minute: Uint16Field = Uint16Field("grid_use_interval_1_weekday_stop_minute", 341, 1, Mode.RW, units="Hour", description="Grid Use Interval 1 Weekday Stop Minute 0-59")
        self.grid_use_interval_1_weekend_start_hour: Uint16Field = Uint16Field("grid_use_interval_1_weekend_start_hour", 342, 1, Mode.RW, units="Hour", description="Grid Use Interval 1 Weekend Start Hour 0-23")
        self.grid_use_interval_1_weekend_start_minute: Uint16Field = Uint16Field("grid_use_interval_1_weekend_start_minute", 343, 1, Mode.RW, units="Hour", description="Grid Use Interval 1 Weekend Start Minute 0-59")
        self.grid_use_interval_1_weekend_stop_hour: Uint16Field = Uint16Field("grid_use_interval_1_weekend_stop_hour", 344, 1, Mode.RW, units="Hour", description="Grid Use Interval 1 Weekend Stop Hour 0-23")
        self.grid_use_interval_1_weekend_stop_minute: Uint16Field = Uint16Field("grid_use_interval_1_weekend_stop_minute", 345, 1, Mode.RW, units="Hour", description="Grid Use Interval 1 Weekend Stop Minute 0-59")
        self.grid_use_interval_2_mode: EnumUint16Field = EnumUint16Field("grid_use_interval_2_mode", 346, 1, Mode.RW, enum=Enum("grid_use_interval_2_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.grid_use_interval_2_weekday_start_hour: Uint16Field = Uint16Field("grid_use_interval_2_weekday_start_hour", 347, 1, Mode.RW, units="Hour", description="Grid Use Interval 2 Weekday Start Hour 0-23")
        self.grid_use_interval_2_weekday_start_minute: Uint16Field = Uint16Field("grid_use_interval_2_weekday_start_minute", 348, 1, Mode.RW, units="Hour", description="Grid Use Interval 2 Weekday Start Minute 0-59")
        self.grid_use_interval_2_weekday_stop_hour: Uint16Field = Uint16Field("grid_use_interval_2_weekday_stop_hour", 349, 1, Mode.RW, units="Hour", description="Grid Use Interval 2 Weekday Stop Hour 0-23")
        self.grid_use_interval_2_weekday_stop_minute: Uint16Field = Uint16Field("grid_use_interval_2_weekday_stop_minute", 350, 1, Mode.RW, units="Hour", description="Grid Use Interval 2 Weekday Stop Minute 0-59")
        self.grid_use_interval_3_mode: EnumUint16Field = EnumUint16Field("grid_use_interval_3_mode", 351, 1, Mode.RW, enum=Enum("grid_use_interval_3_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.grid_use_interval_3_weekday_start_hour: Uint16Field = Uint16Field("grid_use_interval_3_weekday_start_hour", 352, 1, Mode.RW, units="Hour", description="Grid Use Interval 3 Weekday Start Hour 0-23")
        self.grid_use_interval_3_weekday_start_minute: Uint16Field = Uint16Field("grid_use_interval_3_weekday_start_minute", 353, 1, Mode.RW, units="Hour", description="Grid Use Interval 3 Weekday Start Minute 0-59")
        self.grid_use_interval_3_weekday_stop_hour: Uint16Field = Uint16Field("grid_use_interval_3_weekday_stop_hour", 354, 1, Mode.RW, units="Hour", description="Grid Use Interval 3 Weekday Stop Hour 0-23")
        self.grid_use_interval_3_weekday_stop_minute: Uint16Field = Uint16Field("grid_use_interval_3_weekday_stop_minute", 355, 1, Mode.RW, units="Hour", description="Grid Use Interval 3 Weekday Stop Minute 0-59")
        self.load_grid_transfer_mode: EnumUint16Field = EnumUint16Field("load_grid_transfer_mode", 356, 1, Mode.RW, enum=Enum("load_grid_transfer_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.load_grid_transfer_connect_delay: Uint16Field = Uint16Field("load_grid_transfer_connect_delay", 358, 1, Mode.RW, units="Seconds", description="Load Grid Transfer Connect Delay Seconds")
        self.load_grid_transfer_disconnect_delay: Uint16Field = Uint16Field("load_grid_transfer_disconnect_delay", 359, 1, Mode.RW, units="Seconds", description="Load Grid Transfer Disconnect Delay Seconds")
        self.global_charger_control_mode: EnumUint16Field = EnumUint16Field("global_charger_control_mode", 362, 1, Mode.RW, enum=Enum("global_charger_control_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.global_charger_control_output_limit: Uint16Field = Uint16Field("global_charger_control_output_limit", 363, 1, Mode.RW, units="Amps", description="Global Charger Output Limit Amps")
        self.radian_ac_coupled_control_mode: EnumUint16Field = EnumUint16Field("radian_ac_coupled_control_mode", 364, 1, Mode.RW, enum=Enum("radian_ac_coupled_control_mode", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.radian_ac_coupled_aux_port: Uint16Field = Uint16Field("radian_ac_coupled_aux_port", 365, 1, Mode.RW, units="Port", description="Radian Inverter Port Number for AUX Control 0-10")
        self.url_update_lock: Uint32Field = Uint32Field("url_update_lock", 366, 2, Mode.W, units="key", description="Unlock Key")
        self.web_reporting_base_url: StringField = StringField("web_reporting_base_url", 368, 20, Mode.RW, description="WEB Reporting Base URL")
        self.web_user_logged_in_status: EnumUint16Field = EnumUint16Field("web_user_logged_in_status", 388, 1, Mode.RW, enum=Enum("web_user_logged_in_status", [('WEB User NOT logged in', 0), ('WEB user logged in', 1)]), description="0=WEB User NOT logged in, 1=WEB user logged in")
        self.hub_type: EnumUint16Field = EnumUint16Field("hub_type", 389, 1, Mode.R, enum=Enum("hub_type", [('HUB10.3', 10), ('HUB3PH', 11), ('HUB4', 4), ('Legecy HUB', 0)]), description="0=Legecy HUB, 4= HUB4, 10=HUB10.3, 11=HUB3PH")
        self.hub_major_firmware_number: Uint16Field = Uint16Field("hub_major_firmware_number", 390, 1, Mode.R, description="HUB Major firmware revision")
        self.hub_mid_firmware_number: Uint16Field = Uint16Field("hub_mid_firmware_number", 391, 1, Mode.R, description="HUB Mid firmware revision")
        self.hub_minor_firmware_number: Uint16Field = Uint16Field("hub_minor_firmware_number", 392, 1, Mode.R, description="HUB Minor firmware revision")
        self.year: Uint16Field = Uint16Field("year", 393, 1, Mode.RW, description="Clock year (4 digit)")
        self.month: Uint16Field = Uint16Field("month", 394, 1, Mode.RW, description="Clock Month (1 - 12)")
        self.day: Uint16Field = Uint16Field("day", 395, 1, Mode.RW, description="Clock Day (1 - 31)")
        self.hour: Uint16Field = Uint16Field("hour", 396, 1, Mode.RW, description="Clock Hour (0 - 23)")
        self.minute: Uint16Field = Uint16Field("minute", 397, 1, Mode.RW, description="Clock Minute (0 - 59)")
        self.second: Uint16Field = Uint16Field("second", 398, 1, Mode.RW, description="Clock Second (0 - 59)")
        self.temp_battery: Int16Field = Int16Field("temp_battery", 399, 1, Mode.R, units="Degrees C", description="Battery temp in degrees C")
        self.temp_ambient: Int16Field = Int16Field("temp_ambient", 400, 1, Mode.R, units="Degrees C", description="Ambient temp from temp sensor connected to device, in degrees C")
        self.temp_scale_factor: Int16Field = Int16Field("temp_scale_factor", 401, 1, Mode.R, description="Temperature Scale Factor")
        self.error: Bit16Field = Bit16Field("error", 402, 1, Mode.R, flags=OutBackErrorFlags, description="Bit field for errors. See Outback_Error Table")
        self.status: Bit16Field = Bit16Field("status", 403, 1, Mode.R, flags=OutBackStatusFlags, description="Bit field for status.See Outback_Status Table")
        self.update_device_firmware_port: Bit16Field = Bit16Field("update_device_firmware_port", 404, 1, Mode.RW, flags=OutBackUpdateDeviceFirmwarePortFlags, description="Device Firmware update See Device_FW_Update")
        self.gateway_type: EnumUint16Field = EnumUint16Field("gateway_type", 405, 1, Mode.R, enum=Enum("gateway_type", [('AXS Port', 1), ('MATE3', 2)]), description="1=AXS Port, 2= MATE3")
        self.system_voltage: Uint16Field = Uint16Field("system_voltage", 406, 1, Mode.R, units="Volts", description="12, 24, 26, 48 or 60 VDC")
        self.ags_ac_reconnect_delay: Uint16Field = Uint16Field("ags_ac_reconnect_delay", 408, 1, Mode.RW, units="Minute", description="AGS AC Reconnect Delay")
        self.multi_phase_coordination: EnumUint16Field = EnumUint16Field("multi_phase_coordination", 409, 1, Mode.RW, enum=Enum("multi_phase_coordination", [('Disabled', 0), ('Enabled', 1)]), description="0=Disabled, 1=Enabled")
        self.sched_1_ac_mode: EnumInt16Field = EnumInt16Field("sched_1_ac_mode", 410, 1, Mode.RW, enum=Enum("sched_1_ac_mode", [('Backup', 4), ('Disable', -1), ('Generator', 0), ('Grid Tied', 2), ('Grid Zero', 6), ('Mini Grid', 5), ('Support', 1), ('UPS', 3)]), description="Scheduled Input Mode: -1=Disable, 0=Generator, 1=Support, 2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero")
        self.sched_1_ac_mode_hour: Uint16Field = Uint16Field("sched_1_ac_mode_hour", 411, 1, Mode.RW, units="Hour", description="Start Hour for AC Input Mode schedule 1")
        self.sched_1_ac_mode_minute: Uint16Field = Uint16Field("sched_1_ac_mode_minute", 412, 1, Mode.RW, units="Minute", description="Start Minute for AC Input Mode schedule 1")
        self.sched_2_ac_mode: EnumInt16Field = EnumInt16Field("sched_2_ac_mode", 413, 1, Mode.RW, enum=Enum("sched_2_ac_mode", [('Backup', 4), ('Disable', -1), ('Generator', 0), ('Grid Tied', 2), ('Grid Zero', 6), ('Mini Grid', 5), ('Support', 1), ('UPS', 3)]), description="Scheduled Input Mode: -1=Disable, 0=Generator, 1=Support, 2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero")
        self.sched_2_ac_mode_hour: Uint16Field = Uint16Field("sched_2_ac_mode_hour", 414, 1, Mode.RW, units="Hour", description="Start Hour for AC Input Mode schedule 2")
        self.sched_2_ac_mode_minute: Uint16Field = Uint16Field("sched_2_ac_mode_minute", 415, 1, Mode.RW, units="Minute", description="Start Minute for AC Input Mode schedule 2")
        self.sched_3_ac_mode: EnumInt16Field = EnumInt16Field("sched_3_ac_mode", 416, 1, Mode.RW, enum=Enum("sched_3_ac_mode", [('Backup', 4), ('Disable', -1), ('Generator', 0), ('Grid Tied', 2), ('Grid Zero', 6), ('Mini Grid', 5), ('Support', 1), ('UPS', 3)]), description="Scheduled Input Mode: -1=Disable, 0=Generator, 1=Support, 2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero")
        self.sched_3_ac_mode_hour: Uint16Field = Uint16Field("sched_3_ac_mode_hour", 417, 1, Mode.RW, units="Hour", description="Start Hour for AC Input Mode schedule 3")
        self.sched_3_ac_mode_minute: Uint16Field = Uint16Field("sched_3_ac_mode_minute", 418, 1, Mode.RW, units="Minute", description="Start Minute for AC Input Mode schedule 3")
        self.auto_reboot: EnumUint16Field = EnumUint16Field("auto_reboot", 419, 1, Mode.RW, enum=Enum("auto_reboot", [('Disable', 0), ('Enable', 1)]), description="OPTICS auto reboot every 24 hours 0=Disable, 1=Enable")
        self.time_zone_scale_factor: Int16Field = Int16Field("time_zone_scale_factor", 420, 1, Mode.R, description="Time Zone scale factor")
        self.spare_reg_3: Uint16Field = Uint16Field("spare_reg_3", 421, 1, Mode.RW, description="Spare Register 3")
        self.spare_reg_4: Uint16Field = Uint16Field("spare_reg_4", 422, 1, Mode.RW, description="Spare Register 4")
        self.set_time_zone: FloatInt16Field = FloatInt16Field("set_time_zone", 272, 1, Mode.RW, units="Hours", scale_factor=self.time_zone_scale_factor, description="Time Zone -12.0 \u2026 +14.0")
        self.ags_dc_gen_absorb_voltage: FloatUint16Field = FloatUint16Field("ags_dc_gen_absorb_voltage", 282, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="DC Generator Absorb Voltage")
        self.ags_dc_gen_absorb_time: FloatUint16Field = FloatUint16Field("ags_dc_gen_absorb_time", 283, 1, Mode.RW, units="Hour", scale_factor=self.hour_scale_factor, description="DC Generator Absorb Time")
        self.ags_2_min_start_voltage: FloatUint16Field = FloatUint16Field("ags_2_min_start_voltage", 295, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="Two Minute AGS Start Voltage")
        self.ags_2_hour_start_voltage: FloatUint16Field = FloatUint16Field("ags_2_hour_start_voltage", 297, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="Two Hour AGS Start Voltage")
        self.ags_24_hour_start_voltage: FloatUint16Field = FloatUint16Field("ags_24_hour_start_voltage", 299, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="Twenty Four Hour AGS Start Voltage")
        self.hbx_grid_connect_voltage: FloatUint16Field = FloatUint16Field("hbx_grid_connect_voltage", 331, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="HBX Grid Connect Voltage")
        self.hbx_grid_connect_delay: FloatUint16Field = FloatUint16Field("hbx_grid_connect_delay", 332, 1, Mode.RW, units="Hours", scale_factor=self.hour_scale_factor, description="HBX Grid Connect Delay")
        self.hbx_grid_disconnect_voltage: FloatUint16Field = FloatUint16Field("hbx_grid_disconnect_voltage", 333, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="HBX Grid Disconnect Voltage")
        self.hbx_grid_disconnect_delay: FloatUint16Field = FloatUint16Field("hbx_grid_disconnect_delay", 334, 1, Mode.RW, units="Hours", scale_factor=self.hour_scale_factor, description="HBX Grid Disconnect Delay")
        self.load_grid_transfer_threshold: FloatUint16Field = FloatUint16Field("load_grid_transfer_threshold", 357, 1, Mode.RW, units="kWatts", scale_factor=self.voltage_scale_factor, description="Load Grid Transfer Threshold kW")
        self.load_grid_transfer_connect_battery_voltage: FloatUint16Field = FloatUint16Field("load_grid_transfer_connect_battery_voltage", 360, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="Load Grid Transfer Low Battery Connect Voltage")
        self.load_grid_transfer_re_connect_battery_voltage: FloatUint16Field = FloatUint16Field("load_grid_transfer_re_connect_battery_voltage", 361, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="Load Grid Transfer Low Battery Re-Connect Voltage")
        self.measured_system_voltage: FloatUint16Field = FloatUint16Field("measured_system_voltage", 407, 1, Mode.R, units="Volts", scale_factor=self.voltage_scale_factor, description="Current system battery voltage computed by gateway")


class ChargeControllerModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Uniquely identifies this as a SunSpec Basic Charge Controller")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of block in 16-bit registers")
        self.port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
        self.voltage_scale_factor: Int16Field = Int16Field("voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
        self.current_scale_factor: Int16Field = Int16Field("current_scale_factor", 5, 1, Mode.R, description="DC Current Scale Factor")
        self.power_scale_factor: Int16Field = Int16Field("power_scale_factor", 6, 1, Mode.R, description="DC Power Scale Factor")
        self.ah_scale_factor: Int16Field = Int16Field("ah_scale_factor", 7, 1, Mode.R, description="DC Amp Hours Scale Factor")
        self.kwh_scale_factor: Int16Field = Int16Field("kwh_scale_factor", 8, 1, Mode.R, description="DC kWH Scale Factor")
        self.charger_state: EnumUint16Field = EnumUint16Field("charger_state", 13, 1, Mode.R, enum=Enum("charger_state", [('Absorb', 3), ('Bulk', 2), ('EQ', 4), ('Float', 1), ('Silent', 0)]), description="0 = Silent; 1 = Float; 2 = Bulk; 3 = Absorb; 4 = EQ")
        self.todays_peak_voc: Uint16Field = Uint16Field("todays_peak_voc", 18, 1, Mode.R, units="Volts", description="Highest VOC today")
        self.lifetime_kwh_hours: Uint16Field = Uint16Field("lifetime_kwh_hours", 21, 1, Mode.R, units="KWH", description="Lifetime Total Kwatt Hours")
        self.temp_scale_factor: Uint16Field = Uint16Field("temp_scale_factor", 26, 1, Mode.R, description="FM80 Extreme Temperature scale factor")
        self.battery_voltage: FloatUint16Field = FloatUint16Field("battery_voltage", 9, 1, Mode.R, units="Volts", scale_factor=self.voltage_scale_factor, description="Battery Voltage")
        self.array_voltage: FloatUint16Field = FloatUint16Field("array_voltage", 10, 1, Mode.R, units="Volts", scale_factor=self.voltage_scale_factor, description="DC Source Voltage")
        self.battery_current: FloatUint16Field = FloatUint16Field("battery_current", 11, 1, Mode.R, units="Amps", scale_factor=self.current_scale_factor, description="Battery Current")
        self.array_current: FloatUint16Field = FloatUint16Field("array_current", 12, 1, Mode.R, units="Amps", scale_factor=self.power_scale_factor, description="DC Source Current")
        self.watts: FloatUint16Field = FloatUint16Field("watts", 14, 1, Mode.R, units="Watts", scale_factor=self.power_scale_factor, description="CC Wattage Output")
        self.todays_min_battery_volts: FloatUint16Field = FloatUint16Field("todays_min_battery_volts", 15, 1, Mode.R, units="Volts", scale_factor=self.voltage_scale_factor, description="Minimum Voltage for battery today")
        self.todays_max_battery_volts: FloatUint16Field = FloatUint16Field("todays_max_battery_volts", 16, 1, Mode.R, units="Volts", scale_factor=self.voltage_scale_factor, description="Maximum Voltage for battery today")
        self.voc: FloatUint16Field = FloatUint16Field("voc", 17, 1, Mode.R, units="Volts", scale_factor=self.voltage_scale_factor, description="Last Open Circuit Voltage (array)")
        self.todays_kwh: FloatUint16Field = FloatUint16Field("todays_kwh", 19, 1, Mode.R, units="KWH", scale_factor=self.kwh_scale_factor, description="Daily accumulated Kwatt hours output")
        self.todays_ah: FloatUint16Field = FloatUint16Field("todays_ah", 20, 1, Mode.R, units="AH", scale_factor=self.ah_scale_factor, description="Daily accumulated amp hours output")
        self.lifetime_k_amp_hours: FloatUint16Field = FloatUint16Field("lifetime_k_amp_hours", 22, 1, Mode.R, units="Amps", scale_factor=self.kwh_scale_factor, description="Lifetime Total K-Amp Hours")
        self.lifetime_max_watts: FloatUint16Field = FloatUint16Field("lifetime_max_watts", 23, 1, Mode.R, units="Watts", scale_factor=self.power_scale_factor, description="Lifetime Maximum Wattage")
        self.lifetime_max_battery_volts: FloatUint16Field = FloatUint16Field("lifetime_max_battery_volts", 24, 1, Mode.R, units="Volts", scale_factor=self.voltage_scale_factor, description="Lifetime Maximum Battery Voltage")
        self.lifetime_max_voc: FloatUint16Field = FloatUint16Field("lifetime_max_voc", 25, 1, Mode.R, units="Volts", scale_factor=self.voltage_scale_factor, description="Lifetime Maximum VOC")
        self.temp_output_fets: FloatInt16Field = FloatInt16Field("temp_output_fets", 27, 1, Mode.R, units="Degrees C", scale_factor=self.power_scale_factor, description="FM80 Extreme Output FET Temperature")
        self.temp_enclosure: FloatInt16Field = FloatInt16Field("temp_enclosure", 28, 1, Mode.R, units="Degrees C", scale_factor=self.power_scale_factor, description="FM80 Extreme Enclosure Temperature")


class ChargeControllerConfigurationModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack FM Series Charge Controllers")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of block in 16-bit registers")
        self.port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
        self.voltage_scale_factor: Int16Field = Int16Field("voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
        self.current_scale_factor: Int16Field = Int16Field("current_scale_factor", 5, 1, Mode.R, description="DC Current Scale Factor")
        self.hours_scale_factor: Int16Field = Int16Field("hours_scale_factor", 6, 1, Mode.R, description="Time in Hours Scale Factor")
        self.power_scale_factor: Int16Field = Int16Field("power_scale_factor", 7, 1, Mode.R, description="Power Scale Factor")
        self.ah_scale_factor: Int16Field = Int16Field("ah_scale_factor", 8, 1, Mode.R, description="Amp Hours Scale Factor")
        self.kwh_scale_factor: Int16Field = Int16Field("kwh_scale_factor", 9, 1, Mode.R, description="DC kWH Scale Factor")
        self.faults: Bit16Field = Bit16Field("faults", 10, 1, Mode.R, flags=CCconfigFaultsFlags, description="CC Error Flags: 0x0080=High VOC, 0x0040=Over Temp,  0x0020=Shorted Battery Temp Sensor, 0x0010=Fault Input Active")
        self.absorb_end_amps: Uint16Field = Uint16Field("absorb_end_amps", 13, 1, Mode.RW, units="Amps", description="Amperage to end Absorbing")
        self.eq_time_hours: Uint16Field = Uint16Field("eq_time_hours", 18, 1, Mode.RW, units="Hours", description="EQ Time Hours")
        self.auto_eq_days: Uint16Field = Uint16Field("auto_eq_days", 19, 1, Mode.RW, units="Days", description="Auto EQ Interval Days")
        self.mppt_mode: EnumUint16Field = EnumUint16Field("mppt_mode", 20, 1, Mode.RW, enum=Enum("mppt_mode", [('Auto', 0), ('U-Pick', 1)]), description="0 = Auto; 1 = U-Pick")
        self.sweep_width: EnumUint16Field = EnumUint16Field("sweep_width", 21, 1, Mode.RW, enum=Enum("sweep_width", [('Full', 0), ('Half', 1)]), description="0 = Full; 1 = Half")
        self.sweep_max_percentage: EnumUint16Field = EnumUint16Field("sweep_max_percentage", 22, 1, Mode.RW, enum=Enum("sweep_max_percentage", [('80', 0), ('85', 1), ('90', 2), ('99', 3)]), description="0 = 80; 1 = 85; 2 = 90; 3 = 99")
        self.grid_tie_mode: EnumUint16Field = EnumUint16Field("grid_tie_mode", 24, 1, Mode.RW, enum=Enum("grid_tie_mode", [('Grid Tie Mode disabled', 0), ('Grid Tie Mode enabled', 1)]), description="0 = Grid Tie Mode disabled; 1 = Grid Tie Mode enabled")
        self.temp_comp_mode: EnumUint16Field = EnumUint16Field("temp_comp_mode", 25, 1, Mode.RW, enum=Enum("temp_comp_mode", [('User Limited', 1), ('Wide', 0)]), description="0 = Wide; 1 = User Limited")
        self.temp_comp_slope: Uint16Field = Uint16Field("temp_comp_slope", 28, 1, Mode.RW, units="Milli Volts", description="RTS temp compensation Slope 2-6 mV per Degree C")
        self.auto_restart_mode: EnumUint16Field = EnumUint16Field("auto_restart_mode", 29, 1, Mode.RW, enum=Enum("auto_restart_mode", [('Off', 0), ('Restart every 90 minutes', 1), ('Restart every 90 minutes if absorb charging or float charging', 2)]), description="0 = Off; 1 = Restart every 90 minutes; 2 = Restart every 90 minutes if absorb charging or float charging")
        self.wakeup_interval: Uint16Field = Uint16Field("wakeup_interval", 32, 1, Mode.RW, units="Mins", description="How often to check for Wakeup condition")
        self.aux_mode: EnumUint16Field = EnumUint16Field("aux_mode", 33, 1, Mode.RW, enum=Enum("aux_mode", [('Diversion: Relay', 1), ('Diversion: Solid St', 2), ('Error Output', 7), ('Float', 0), ('Low Batt Disconnect', 3), ('Night Light', 8), ('PV Trigger', 6), ('Remote', 4), ('Vent Fan', 5)]), description="0 = Float; 1 = Diversion: Relay; 2 = Diversion: Solid St; 3 = Low Batt Disconnect; 4 = Remote; 5 = Vent Fan; 6 = PV Trigger; 7 = Error Output; 8 = Night Light")
        self.aux_control: EnumUint16Field = EnumUint16Field("aux_control", 34, 1, Mode.RW, enum=Enum("aux_control", [('Auto', 1), ('Off', 0), ('On', 2)]), description="0 = Off; 1 = Auto; 2 = On")
        self.aux_state: EnumUint16Field = EnumUint16Field("aux_state", 35, 1, Mode.R, enum=Enum("aux_state", [('Disabled', 0), ('Enabled', 1)]), description="0 = Disabled; 1 = Enabled")
        self.aux_polarity: EnumUint16Field = EnumUint16Field("aux_polarity", 36, 1, Mode.RW, enum=Enum("aux_polarity", [('High', 1), ('Low', 0)]), description="0 = Low; 1 = High")
        self.aux_low_battery_disconnect_delay: Uint16Field = Uint16Field("aux_low_battery_disconnect_delay", 39, 1, Mode.RW, units="Secs", description="Low Battery Disconnect Delay (secs)")
        self.night_light_on_hours: Uint16Field = Uint16Field("night_light_on_hours", 44, 1, Mode.RW, units="Hours", description="Night Light ON Time")
        self.night_light_on_hyst_time: Uint16Field = Uint16Field("night_light_on_hyst_time", 45, 1, Mode.RW, units="Mins", description="Night Light ON Hyst Time")
        self.night_light_off_hyst_time: Uint16Field = Uint16Field("night_light_off_hyst_time", 46, 1, Mode.RW, units="Mins", description="Night Light OFF Hyst Time")
        self.aux_divert_delay_time: Uint16Field = Uint16Field("aux_divert_delay_time", 49, 1, Mode.RW, units="Secs", description="AUX Divert Delay")
        self.major_firmware_number: Uint16Field = Uint16Field("major_firmware_number", 52, 1, Mode.R, description="Charge Controller Major firmware revision")
        self.mid_firmware_number: Uint16Field = Uint16Field("mid_firmware_number", 53, 1, Mode.R, description="Charge Controller Mid firmware revision")
        self.minor_firmware_number: Uint16Field = Uint16Field("minor_firmware_number", 54, 1, Mode.R, description="Charge Controller Minor firmware revision")
        self.set_data_log_day_offset: Uint16Field = Uint16Field("set_data_log_day_offset", 55, 1, Mode.RW, units="Days", description="Day offset 0-128, 0 =Today, 1 = -1 day \u2026")
        self.get_current_data_log_day_offset: Uint16Field = Uint16Field("get_current_data_log_day_offset", 56, 1, Mode.R, units="Days", description="Current Data Log Day Offset")
        self.data_log_daily_absorb_time: Uint16Field = Uint16Field("data_log_daily_absorb_time", 61, 1, Mode.R, units="Mins", description="Data Log Absorb Time Minutes")
        self.data_log_daily_float_time: Uint16Field = Uint16Field("data_log_daily_float_time", 62, 1, Mode.R, units="Mins", description="Data Log Float Time Minutes")
        self.data_log_daily_max_input_volts: Uint16Field = Uint16Field("data_log_daily_max_input_volts", 65, 1, Mode.R, units="Volts", description="Data Log maximum daily input voltage")
        self.clear_data_log_read: Uint16Field = Uint16Field("clear_data_log_read", 66, 1, Mode.R, description="Read value needed to clear data log")
        self.clear_data_log_write_complement: Uint16Field = Uint16Field("clear_data_log_write_complement", 67, 1, Mode.W, description="Write value's complement to clear data log")
        self.stats_maximum_reset_read: Uint16Field = Uint16Field("stats_maximum_reset_read", 68, 1, Mode.R, description="Read value needed to clear Stats Maximums")
        self.stats_maximum_write_complement: Uint16Field = Uint16Field("stats_maximum_write_complement", 69, 1, Mode.W, description="Write value's complement to clear Stats Maximums")
        self.stats_totals_reset_read: Uint16Field = Uint16Field("stats_totals_reset_read", 70, 1, Mode.R, description="Read value nneded to clear Stats Totals")
        self.stats_totals_write_complement: Uint16Field = Uint16Field("stats_totals_write_complement", 71, 1, Mode.W, description="Write value's complement to clear Stats Totals")
        self.serial_number: StringField = StringField("serial_number", 73, 9, Mode.R, description="Device serial number")
        self.model_number: StringField = StringField("model_number", 82, 9, Mode.R, description="Device model")
        self.absorb_volts: FloatUint16Field = FloatUint16Field("absorb_volts", 11, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="Absorb Voltage Target")
        self.absorb_time_hours: FloatUint16Field = FloatUint16Field("absorb_time_hours", 12, 1, Mode.RW, units="Hours", scale_factor=self.hours_scale_factor, description="Absorb Time Hours")
        self.rebulk_volts: FloatUint16Field = FloatUint16Field("rebulk_volts", 14, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="Voltage to re-initiate Bulk charge")
        self.float_volts: FloatUint16Field = FloatUint16Field("float_volts", 15, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="Float Voltage Target")
        self.bulk_current: FloatUint16Field = FloatUint16Field("bulk_current", 16, 1, Mode.RW, units="Amps", scale_factor=self.current_scale_factor, description="Max Output Current Limit")
        self.eq_volts: FloatUint16Field = FloatUint16Field("eq_volts", 17, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="Target Voltage for Equalize")
        self.u_pick_pwm_duty_cycle: FloatUint16Field = FloatUint16Field("u_pick_pwm_duty_cycle", 23, 1, Mode.RW, units="Percentage", scale_factor=self.voltage_scale_factor, description="Park Duty Cycle (%) (40% - 90%)")
        self.temp_comp_lower_limit_volts: FloatUint16Field = FloatUint16Field("temp_comp_lower_limit_volts", 26, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="RTS compensation lower voltage limit")
        self.temp_comp_upper_limit_volts: FloatUint16Field = FloatUint16Field("temp_comp_upper_limit_volts", 27, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="RTS compensation upper voltage limit")
        self.wakeup_voc: FloatUint16Field = FloatUint16Field("wakeup_voc", 30, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="VOC change which causes Wakeup occurs")
        self.snooze_mode_amps: FloatUint16Field = FloatUint16Field("snooze_mode_amps", 31, 1, Mode.RW, units="Amps", scale_factor=self.voltage_scale_factor, description="Snooze Mode Amps")
        self.aux_low_battery_disconnect: FloatUint16Field = FloatUint16Field("aux_low_battery_disconnect", 37, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="Low Battery Disconnect Voltage")
        self.aux_low_battery_reconnect: FloatUint16Field = FloatUint16Field("aux_low_battery_reconnect", 38, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="Low Battery Reconnect Volts")
        self.aux_vent_fan_volts: FloatUint16Field = FloatUint16Field("aux_vent_fan_volts", 40, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="Vent Fan Voltage")
        self.aux_pv_limit_volts: FloatUint16Field = FloatUint16Field("aux_pv_limit_volts", 41, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="Voltage at which PV disconnect occurs")
        self.aux_pv_limit_hold_time: FloatUint16Field = FloatUint16Field("aux_pv_limit_hold_time", 42, 1, Mode.RW, units="Secs", scale_factor=self.hours_scale_factor, description="AUX PV Trigger Hold Time")
        self.aux_night_light_thres_volts: FloatUint16Field = FloatUint16Field("aux_night_light_thres_volts", 43, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="Voltage Threshold for AUX Night Light")
        self.aux_error_battery_volts: FloatUint16Field = FloatUint16Field("aux_error_battery_volts", 47, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="Battery voltage at which Aux Error occurs")
        self.aux_divert_hold_time: FloatUint16Field = FloatUint16Field("aux_divert_hold_time", 48, 1, Mode.RW, units="Seconds", scale_factor=self.hours_scale_factor, description="AUX Diver Hold Time")
        self.aux_divert_relative_volts: FloatInt16Field = FloatInt16Field("aux_divert_relative_volts", 50, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="AUX Divert Relative Volts")
        self.aux_divert_hyst_volts: FloatUint16Field = FloatUint16Field("aux_divert_hyst_volts", 51, 1, Mode.RW, units="Volts", scale_factor=self.voltage_scale_factor, description="AUX Divert Hyst Volts")
        self.data_log_daily_ah: FloatUint16Field = FloatUint16Field("data_log_daily_ah", 57, 1, Mode.R, units="AH", scale_factor=self.ah_scale_factor, description="Data Log AH")
        self.data_log_daily_kwh: FloatUint16Field = FloatUint16Field("data_log_daily_kwh", 58, 1, Mode.R, units="KWH", scale_factor=self.kwh_scale_factor, description="Data Log kWH")
        self.data_log_daily_max_output_amps: FloatUint16Field = FloatUint16Field("data_log_daily_max_output_amps", 59, 1, Mode.R, units="Amps", scale_factor=self.voltage_scale_factor, description="Data Log maximum Output Amps")
        self.data_log_daily_max_output_watts: FloatUint16Field = FloatUint16Field("data_log_daily_max_output_watts", 60, 1, Mode.R, units="Watts", scale_factor=self.power_scale_factor, description="Data Log maximum Output Wattage")
        self.data_log_daily_min_battery_volts: FloatUint16Field = FloatUint16Field("data_log_daily_min_battery_volts", 63, 1, Mode.R, units="Volts", scale_factor=self.voltage_scale_factor, description="Data Log minimum daily battery voltage")
        self.data_log_daily_max_battery_volts: FloatUint16Field = FloatUint16Field("data_log_daily_max_battery_volts", 64, 1, Mode.R, units="Volts", scale_factor=self.voltage_scale_factor, description="Data Log maximum daily battery voltage")
        self.battery_voltage_calibrate_offset: FloatInt16Field = FloatInt16Field("battery_voltage_calibrate_offset", 72, 1, Mode.RW, units="DC Volts", scale_factor=self.voltage_scale_factor, description="Battery voltage calibration offset")


class FXInverterRealTimeModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack FX Series Inverter Status Block")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of block in 16-bit registers")
        self.port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
        self.dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
        self.ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 5, 1, Mode.R, description="AC Current Scale Factor")
        self.ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 6, 1, Mode.R, description="AC Voltage Scale Factor")
        self.ac_frequency_scale_factor: Int16Field = Int16Field("ac_frequency_scale_factor", 7, 1, Mode.R, description="AC Frequency Scale Factor")
        self.inverter_operating_mode: EnumUint16Field = EnumUint16Field("inverter_operating_mode", 13, 1, Mode.R, enum=Enum("inverter_operating_mode", [('Charger Off', 7), ('Charging', 3), ('EQ', 6), ('Float', 5), ('Inverting', 2), ('Off', 0), ('Offsetting', 14), ('Pass through', 10), ('Searching', 1), ('Selling', 9), ('Silent', 4), ('Support', 8)]), description="0=Off, 1=Searching, 2=Inverting, 3=Charging, 4=Silent, 5=Float, 6=EQ, 7=Charger Off, 8=Support, 9=Selling, 10=Pass through, 14=Offsetting")
        self.error_flags: Bit16Field = Bit16Field("error_flags", 14, 1, Mode.R, flags=FXErrorFlags, description="Bit field for errors. See FX_Error Table")
        self.warning_flags: Bit16Field = Bit16Field("warning_flags", 15, 1, Mode.R, flags=FXWarningFlags, description="Bit field for warnings See FX_Warning Table")
        self.aux_output_state: EnumUint16Field = EnumUint16Field("aux_output_state", 18, 1, Mode.R, enum=Enum("aux_output_state", [('Disabled', 0), ('Enabled', 1)]), description="0 = Disabled; 1 = Enabled")
        self.transformer_temperature: Int16Field = Int16Field("transformer_temperature", 19, 1, Mode.R, units="Degrees C", description="Transformer temp in degrees C")
        self.capacitor_temperature: Int16Field = Int16Field("capacitor_temperature", 20, 1, Mode.R, units="Degrees C", description="Capacitor temp in degrees C")
        self.fet_temperature: Int16Field = Int16Field("fet_temperature", 21, 1, Mode.R, units="Degrees C", description="FET temp in degrees C")
        self.ac_input_state: EnumUint16Field = EnumUint16Field("ac_input_state", 24, 1, Mode.R, enum=Enum("ac_input_state", [('AC Use', 1), ('AC_Drop', 0)]), description="1=AC Use, 0=AC_Drop")
        self.sell_status: Bit16Field = Bit16Field("sell_status", 27, 1, Mode.R, flags=FXSellStatusFlags, description="Bit field for sell status See FX_Sell_Status Table")
        self.kwh_scale_factor: Int16Field = Int16Field("kwh_scale_factor", 28, 1, Mode.R, description="AC kWh scale factor")
        self.inverter_output_current: FloatUint16Field = FloatUint16Field("inverter_output_current", 8, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="Inverter output current")
        self.inverter_charge_current: FloatUint16Field = FloatUint16Field("inverter_charge_current", 9, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="Inverter charger current")
        self.inverter_buy_current: FloatUint16Field = FloatUint16Field("inverter_buy_current", 10, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="Inverter buy current")
        self.inverter_sell_current: FloatUint16Field = FloatUint16Field("inverter_sell_current", 11, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="Inverter sell current")
        self.output_ac_voltage: FloatUint16Field = FloatUint16Field("output_ac_voltage", 12, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Output AC Voltage")
        self.battery_voltage: FloatUint16Field = FloatUint16Field("battery_voltage", 16, 1, Mode.R, units="Volts DC", scale_factor=self.dc_voltage_scale_factor, description="Battery Voltage")
        self.temp_compensated_target_voltage: FloatUint16Field = FloatUint16Field("temp_compensated_target_voltage", 17, 1, Mode.R, units="Volts DC", scale_factor=self.dc_voltage_scale_factor, description="Temperature compensated target battery voltage")
        self.ac_input_frequency: FloatUint16Field = FloatUint16Field("ac_input_frequency", 22, 1, Mode.R, units="Hz", scale_factor=self.ac_frequency_scale_factor, description="Selected AC Input frequency HZ")
        self.ac_input_voltage: FloatUint16Field = FloatUint16Field("ac_input_voltage", 23, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Selected Input AC Voltage")
        self.minimum_ac_input_voltage: FloatUint16Field = FloatUint16Field("minimum_ac_input_voltage", 25, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Minimum Input AC Voltage (Write to clear value)")
        self.maximum_ac_input_voltage: FloatUint16Field = FloatUint16Field("maximum_ac_input_voltage", 26, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Maximum Input AC Voltage (Write to clear value)")
        self.buy_kwh: FloatUint16Field = FloatUint16Field("buy_kwh", 29, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily Buy kWh")
        self.sell_kwh: FloatUint16Field = FloatUint16Field("sell_kwh", 30, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily Sell kWh")
        self.output_kwh: FloatUint16Field = FloatUint16Field("output_kwh", 31, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily Output kWh")
        self.charger_kwh: FloatUint16Field = FloatUint16Field("charger_kwh", 32, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily Charger kWh")
        self.output_kw: FloatUint16Field = FloatUint16Field("output_kw", 33, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Output kW")
        self.buy_kw: FloatUint16Field = FloatUint16Field("buy_kw", 34, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Buy kW")
        self.sell_kw: FloatUint16Field = FloatUint16Field("sell_kw", 35, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Sell kW")
        self.charge_kw: FloatUint16Field = FloatUint16Field("charge_kw", 36, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Charge kW")
        self.load_kw: FloatUint16Field = FloatUint16Field("load_kw", 37, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Load kW")
        self.ac_couple_kw: FloatUint16Field = FloatUint16Field("ac_couple_kw", 38, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="AC Coupled kW")


class FXInverterConfigurationModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack FX Series Inverter  Configuration Block")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of block in 16-bit registers")
        self.port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
        self.dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
        self.ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 5, 1, Mode.R, description="AC Current Scale Factor")
        self.ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 6, 1, Mode.R, description="AC Voltage Scale Factor")
        self.time_scale_factor: Int16Field = Int16Field("time_scale_factor", 7, 1, Mode.R, description="Time Scale Factor")
        self.major_firmware_number: Uint16Field = Uint16Field("major_firmware_number", 8, 1, Mode.R, description="Inverter Major firmware revision")
        self.mid_firmware_number: Uint16Field = Uint16Field("mid_firmware_number", 9, 1, Mode.R, description="Inverter Mid firmware revision")
        self.minor_firmware_number: Uint16Field = Uint16Field("minor_firmware_number", 10, 1, Mode.R, description="Inverter Minor firmware revision")
        self.search_sensitivity: Uint16Field = Uint16Field("search_sensitivity", 18, 1, Mode.RW, description="Search sensitivity")
        self.search_pulse_length: Uint16Field = Uint16Field("search_pulse_length", 19, 1, Mode.RW, units="Cycles", description="Search pulse length")
        self.search_pulse_spacing: Uint16Field = Uint16Field("search_pulse_spacing", 20, 1, Mode.RW, units="Cycles", description="Search pulse spacing")
        self.ac_input_type: EnumUint16Field = EnumUint16Field("ac_input_type", 21, 1, Mode.RW, enum=Enum("ac_input_type", [('Gen', 1), ('Grid', 0), ('Grid Zero', 2)]), description="0=Grid, 1=Gen, 2=Grid Zero")
        self.input_support: EnumUint16Field = EnumUint16Field("input_support", 22, 1, Mode.RW, enum=Enum("input_support", [('No (only valid if AC Input Type is Gen)', 0), ('Yes', 1)]), description="1=Yes, 0=No (only valid if AC Input Type is Gen)")
        self.charger_operating_mode: EnumUint16Field = EnumUint16Field("charger_operating_mode", 26, 1, Mode.RW, enum=Enum("charger_operating_mode", [('Charger Auto', 1), ('Charger Off', 0), ('Charger On', 2)]), description="0=Charger Off, 1=Charger Auto, 2=Charger On")
        self.grid_transfer_delay: Uint16Field = Uint16Field("grid_transfer_delay", 29, 1, Mode.RW, units="Minutes", description="Grid Input AC connect delay")
        self.gen_transfer_delay: Uint16Field = Uint16Field("gen_transfer_delay", 32, 1, Mode.RW, units="Cycles", description="Gen Input AC transfer delay")
        self.aux_mode: EnumUint16Field = EnumUint16Field("aux_mode", 37, 1, Mode.RW, enum=Enum("aux_mode", [('AC Drop', 8), ('Cool Fan', 5), ('Divert AC', 7), ('Divert DC', 6), ('Fault', 3), ('Gen Alert', 2), ('Load Shed', 1), ('Remote', 0), ('Vent Fan', 4)]), description="0=Remote, 1=Load Shed, 2=Gen Alert, 3=Fault, 4=Vent Fan, 5=Cool Fan, 6=Divert DC, 7=Divert AC, 8=AC Drop")
        self.aux_control: EnumUint16Field = EnumUint16Field("aux_control", 38, 1, Mode.RW, enum=Enum("aux_control", [('Auto', 1), ('Off', 0), ('On', 2)]), description="0 = Off; 1 = Auto; 2 = On")
        self.aux_gen_alert_on_delay: Uint16Field = Uint16Field("aux_gen_alert_on_delay", 41, 1, Mode.RW, units="Minutes", description="Gen Alert On delay minutes")
        self.aux_gen_alert_off_delay: Uint16Field = Uint16Field("aux_gen_alert_off_delay", 43, 1, Mode.RW, units="Minutes", description="Gen Alert Off delay minutes")
        self.aux_vent_fan_off_period: Uint16Field = Uint16Field("aux_vent_fan_off_period", 45, 1, Mode.RW, units="Minutes", description="Van Fan Off delay minutes")
        self.aux_divert_off_delay: Uint16Field = Uint16Field("aux_divert_off_delay", 47, 1, Mode.RW, units="Minutes", description="Divert Off delay minutes")
        self.stacking_mode: EnumUint16Field = EnumUint16Field("stacking_mode", 48, 1, Mode.RW, enum=Enum("stacking_mode", [('1-2phase Master', 0), ('3phase Classic B', 17), ('3phase Classic C', 18), ('3phase Master', 4), ('3phase OB Slave A', 14), ('3phase OB Slave B', 15), ('3phase OB Slave C', 16), ('3phase Slave', 5), ('CLASSIC_SLAVE_11', 11), ('Classic Slave', 1), ('Independent', 19), ('Master', 10), ('OB Slave L1', 2), ('OB Slave L2', 3), ('OB_SLAVE_L1_12', 12), ('OB_SLAVE_L2_13', 13)]), description="0=1-2phase Master, 1=Classic Slave, 2=OB Slave L1, 3=OB Slave L2, 4=3phase Master, 5=3phase Slave,10=Master, 11=Classic Slave, 12=OB Slave L1, 13=OB Slave L2, 14=3phase OB Slave A, 15=3phase OB Slave B, 16=3phase OB Slave C, 17=3phase Classic B, 18=3phase Classic C, 19=Independent")
        self.master_power_save_level: Uint16Field = Uint16Field("master_power_save_level", 49, 1, Mode.RW, description="Master inverter power save level")
        self.slave_power_save_level: Uint16Field = Uint16Field("slave_power_save_level", 50, 1, Mode.RW, description="Slave inverter power save level")
        self.grid_tie_window: EnumUint16Field = EnumUint16Field("grid_tie_window", 52, 1, Mode.RW, enum=Enum("grid_tie_window", [('IEEE', 0), ('User', 1)]), description="0=IEEE, 1=User")
        self.grid_tie_enable: EnumUint16Field = EnumUint16Field("grid_tie_enable", 53, 1, Mode.RW, enum=Enum("grid_tie_enable", [('No', 0), ('Yes', 1)]), description="1=Yes, 0=No")
        self.ac_input_voltage_calibrate_factor: Int16Field = Int16Field("ac_input_voltage_calibrate_factor", 54, 1, Mode.RW, units="Volts AC", description="AC input voltage calibration factor")
        self.ac_output_voltage_calibrate_factor: Int16Field = Int16Field("ac_output_voltage_calibrate_factor", 55, 1, Mode.RW, units="Volts AC", description="AC output voltage calibration factor")
        self.serial_number: StringField = StringField("serial_number", 57, 9, Mode.R, description="Device serial number")
        self.model_number: StringField = StringField("model_number", 66, 9, Mode.R, description="Device model")
        self.absorb_volts: FloatUint16Field = FloatUint16Field("absorb_volts", 11, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Absorb Voltage Target")
        self.absorb_time_hours: FloatUint16Field = FloatUint16Field("absorb_time_hours", 12, 1, Mode.RW, units="Hours", scale_factor=self.time_scale_factor, description="Absorb Time Hours")
        self.float_volts: FloatUint16Field = FloatUint16Field("float_volts", 13, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Float Voltage Target")
        self.float_time_hours: FloatUint16Field = FloatUint16Field("float_time_hours", 14, 1, Mode.RW, units="Hours", scale_factor=self.time_scale_factor, description="Float Time Hours")
        self.re_float_volts: FloatUint16Field = FloatUint16Field("re_float_volts", 15, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="ReFloat Voltage Target")
        self.eq_volts: FloatUint16Field = FloatUint16Field("eq_volts", 16, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="EQ Voltage Target")
        self.eq_time_hours: FloatUint16Field = FloatUint16Field("eq_time_hours", 17, 1, Mode.RW, units="Hours", scale_factor=self.time_scale_factor, description="EQ Time Hours")
        self.grid_ac_input_current_limit: FloatUint16Field = FloatUint16Field("grid_ac_input_current_limit", 23, 1, Mode.RW, units="Amps", scale_factor=self.ac_current_scale_factor, description="Grid AC input current limit")
        self.gen_ac_input_current_limit: FloatUint16Field = FloatUint16Field("gen_ac_input_current_limit", 24, 1, Mode.RW, units="Amps", scale_factor=self.ac_current_scale_factor, description="Gen AC input current limit")
        self.charger_ac_input_current_limit: FloatUint16Field = FloatUint16Field("charger_ac_input_current_limit", 25, 1, Mode.RW, units="Amps", scale_factor=self.ac_current_scale_factor, description="Charger AC input current limit")
        self.grid_lower_input_voltage_limit: FloatUint16Field = FloatUint16Field("grid_lower_input_voltage_limit", 27, 1, Mode.RW, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Grid Input AC voltage lower limit")
        self.grid_upper_input_voltage_limit: FloatUint16Field = FloatUint16Field("grid_upper_input_voltage_limit", 28, 1, Mode.RW, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Grid Input AC voltage upper limit")
        self.gen_lower_input_voltage_limit: FloatUint16Field = FloatUint16Field("gen_lower_input_voltage_limit", 30, 1, Mode.RW, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Gen Input AC voltage lower limit")
        self.gen_upper_input_voltage_limit: FloatUint16Field = FloatUint16Field("gen_upper_input_voltage_limit", 31, 1, Mode.RW, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Gen Input AC voltage upper limit")
        self.gen_connect_delay: FloatUint16Field = FloatUint16Field("gen_connect_delay", 33, 1, Mode.RW, units="Minutes", scale_factor=self.time_scale_factor, description="Gen Input AC connect delay")
        self.ac_output_voltage: FloatUint16Field = FloatUint16Field("ac_output_voltage", 34, 1, Mode.RW, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="AC output Voltage")
        self.low_battery_cut_out_voltage: FloatUint16Field = FloatUint16Field("low_battery_cut_out_voltage", 35, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Battery cut-out voltage")
        self.low_battery_cut_in_voltage: FloatUint16Field = FloatUint16Field("low_battery_cut_in_voltage", 36, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Battery cut-in voltage")
        self.aux_load_shed_enable_voltage: FloatUint16Field = FloatUint16Field("aux_load_shed_enable_voltage", 39, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Load Shed enable voltage")
        self.aux_gen_alert_on_voltage: FloatUint16Field = FloatUint16Field("aux_gen_alert_on_voltage", 40, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Gen Alert On voltage")
        self.aux_gen_alert_off_voltage: FloatUint16Field = FloatUint16Field("aux_gen_alert_off_voltage", 42, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Gen Alert Off voltage")
        self.aux_vent_fan_enable_voltage: FloatUint16Field = FloatUint16Field("aux_vent_fan_enable_voltage", 44, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Vent Fan enable voltage")
        self.aux_divert_enable_voltage: FloatUint16Field = FloatUint16Field("aux_divert_enable_voltage", 46, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="DC Divert enable voltage")
        self.sell_volts: FloatUint16Field = FloatUint16Field("sell_volts", 51, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Sell Voltage Target")
        self.battery_voltage_calibrate_factor: FloatInt16Field = FloatInt16Field("battery_voltage_calibrate_factor", 56, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Battery voltage calibration factor")


class SplitPhaseRadianInverterRealTimeModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack Radian Series Split Phase Inverter Status Block")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of block in 16-bit registers")
        self.port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
        self.dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
        self.ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 5, 1, Mode.R, description="AC Current Scale Factor")
        self.ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 6, 1, Mode.R, description="AC Voltage Scale Factor")
        self.ac_frequency_scale_factor: Int16Field = Int16Field("ac_frequency_scale_factor", 7, 1, Mode.R, description="AC Frequency Scale Factor")
        self.inverter_operating_mode: EnumInt16Field = EnumInt16Field("inverter_operating_mode", 22, 1, Mode.R, enum=Enum("inverter_operating_mode", [('Charger Off', 7), ('Charging', 3), ('EQ', 6), ('Float', 5), ('Inverting', 2), ('Off', 0), ('Offsetting', 14), ('Pass through', 10), ('Searching', 1), ('Selling', 9), ('Silent', 4), ('Support', 8)]), description="0=Off, 1=Searching, 2=Inverting, 3=Charging, 4=Silent, 5=Float, 6=EQ, 7=Charger Off, 8=Support, 9=Selling, 10=Pass through, 14=Offsetting")
        self.error_flags: Bit16Field = Bit16Field("error_flags", 23, 1, Mode.R, flags=GSSplitErrorFlags, description="Bit field for errors. See GS_Error table")
        self.warning_flags: Bit16Field = Bit16Field("warning_flags", 24, 1, Mode.R, flags=GSSplitWarningFlags, description="Bit field for warnings See GS_Warning table")
        self.aux_output_state: EnumInt16Field = EnumInt16Field("aux_output_state", 27, 1, Mode.R, enum=Enum("aux_output_state", [('Disabled', 0), ('Enabled', 1)]), description="0 = Disabled; 1 = Enabled")
        self.aux_relay_output_state: EnumInt16Field = EnumInt16Field("aux_relay_output_state", 28, 1, Mode.R, enum=Enum("aux_relay_output_state", [('Disabled', 0), ('Enabled', 1)]), description="0 = Disabled; 1 = Enabled")
        self.l_module_transformer_temperature: Int16Field = Int16Field("l_module_transformer_temperature", 29, 1, Mode.R, units="Degrees C", description="Left module transformer temp in degrees C")
        self.l_module_capacitor_temperature: Int16Field = Int16Field("l_module_capacitor_temperature", 30, 1, Mode.R, units="Degrees C", description="Left module capacitor temp in degrees C")
        self.l_module_fet_temperature: Int16Field = Int16Field("l_module_fet_temperature", 31, 1, Mode.R, units="Degrees C", description="Left module FET temp in degrees C")
        self.r_module_transformer_temperature: Int16Field = Int16Field("r_module_transformer_temperature", 32, 1, Mode.R, units="Degrees C", description="Right module transformer temp in degrees C")
        self.r_module_capacitor_temperature: Int16Field = Int16Field("r_module_capacitor_temperature", 33, 1, Mode.R, units="Degrees C", description="Right module capacitor temp in degrees C")
        self.r_module_fet_temperature: Int16Field = Int16Field("r_module_fet_temperature", 34, 1, Mode.R, units="Degrees C", description="Right module FET temp in degrees C")
        self.battery_temperature: Int16Field = Int16Field("battery_temperature", 35, 1, Mode.R, units="Degrees C", description="Battery temp in degrees C")
        self.ac_input_selection: EnumInt16Field = EnumInt16Field("ac_input_selection", 36, 1, Mode.R, enum=Enum("ac_input_selection", [('Gen', 1), ('Grid', 0)]), description="0=Grid, 1=Gen")
        self.ac_input_state: EnumInt16Field = EnumInt16Field("ac_input_state", 39, 1, Mode.R, enum=Enum("ac_input_state", [('AC Use', 1), ('AC_Drop', 0)]), description="1=AC Use, 0=AC_Drop")
        self.sell_status: Bit16Field = Bit16Field("sell_status", 42, 1, Mode.R, flags=GSSplitSellStatusFlags, description="Bit field for sell status See GS_Sell_Status table")
        self.kwh_scale_factor: Int16Field = Int16Field("kwh_scale_factor", 43, 1, Mode.R, description="AC kWh scale factor")
        self.gt_number: Uint16Field = Uint16Field("gt_number", 61, 1, Mode.R, description="GT Number sent from Inverter to Charge Controller")
        self.l1_inverter_output_current: FloatInt16Field = FloatInt16Field("l1_inverter_output_current", 8, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="L1 inverter output current")
        self.l1_inverter_charge_current: FloatInt16Field = FloatInt16Field("l1_inverter_charge_current", 9, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="L1 inverter charger current")
        self.l1_inverter_buy_current: FloatInt16Field = FloatInt16Field("l1_inverter_buy_current", 10, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="L1 inverter buy current")
        self.l1_inverter_sell_current: FloatInt16Field = FloatInt16Field("l1_inverter_sell_current", 11, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="L1 inverter sell current")
        self.l1_grid_input_ac_voltage: FloatInt16Field = FloatInt16Field("l1_grid_input_ac_voltage", 12, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="L1 Grid Input AC Voltage")
        self.l1_gen_input_ac_voltage: FloatInt16Field = FloatInt16Field("l1_gen_input_ac_voltage", 13, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="L1 Gen Input AC Voltage")
        self.l1_output_ac_voltage: FloatInt16Field = FloatInt16Field("l1_output_ac_voltage", 14, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="L1 Output AC Voltage")
        self.l2_inverter_output_current: FloatInt16Field = FloatInt16Field("l2_inverter_output_current", 15, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="L2 inverter output current")
        self.l2_inverter_charge_current: FloatInt16Field = FloatInt16Field("l2_inverter_charge_current", 16, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="L2 inverter charger current")
        self.l2_inverter_buy_current: FloatInt16Field = FloatInt16Field("l2_inverter_buy_current", 17, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="L2 inverter buy current")
        self.l2_inverter_sell_current: FloatInt16Field = FloatInt16Field("l2_inverter_sell_current", 18, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="L2 inverter sell current")
        self.l2_grid_input_ac_voltage: FloatInt16Field = FloatInt16Field("l2_grid_input_ac_voltage", 19, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="L2 Grid Input AC Voltage")
        self.l2_gen_input_ac_voltage: FloatInt16Field = FloatInt16Field("l2_gen_input_ac_voltage", 20, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="L2 Gen Input AC Voltage")
        self.l2_output_ac_voltage: FloatInt16Field = FloatInt16Field("l2_output_ac_voltage", 21, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="L2 Output AC Voltage")
        self.battery_voltage: FloatInt16Field = FloatInt16Field("battery_voltage", 25, 1, Mode.R, units="Volts DC", scale_factor=self.dc_voltage_scale_factor, description="Battery Voltage")
        self.temp_compensated_target_voltage: FloatInt16Field = FloatInt16Field("temp_compensated_target_voltage", 26, 1, Mode.R, units="Volts DC", scale_factor=self.dc_voltage_scale_factor, description="Temperature compensated target battery voltage")
        self.ac_input_frequency: FloatInt16Field = FloatInt16Field("ac_input_frequency", 37, 1, Mode.R, units="Hz", scale_factor=self.ac_frequency_scale_factor, description="Selected AC Input frequency HZ")
        self.ac_input_voltage: FloatInt16Field = FloatInt16Field("ac_input_voltage", 38, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Selected Input AC Voltage")
        self.minimum_ac_input_voltage: FloatInt16Field = FloatInt16Field("minimum_ac_input_voltage", 40, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Minimum Input AC Voltage (Write to clear stored value)")
        self.maximum_ac_input_voltage: FloatInt16Field = FloatInt16Field("maximum_ac_input_voltage", 41, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Maximum Input AC Voltage (Write to clear stored value)")
        self.ac1_l1_buy_kwh: FloatUint16Field = FloatUint16Field("ac1_l1_buy_kwh", 44, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily AC1 Buy L1 kWh")
        self.ac2_l1_buy_kwh: FloatUint16Field = FloatUint16Field("ac2_l1_buy_kwh", 45, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily AC2 Buy L1 kWh")
        self.ac1_l1_sell_kwh: FloatUint16Field = FloatUint16Field("ac1_l1_sell_kwh", 46, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily AC1 Sell L1 kWh")
        self.ac2_l1_sell_kwh: FloatUint16Field = FloatUint16Field("ac2_l1_sell_kwh", 47, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily AC2 Sell L1 kWh")
        self.l1_output_kwh: FloatUint16Field = FloatUint16Field("l1_output_kwh", 48, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily Output L1 kWh")
        self.ac1_l2_buy_kwh: FloatUint16Field = FloatUint16Field("ac1_l2_buy_kwh", 49, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily AC1 Buy L2 kWh")
        self.ac2_l2_buy_kwh: FloatUint16Field = FloatUint16Field("ac2_l2_buy_kwh", 50, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily AC1 Sell L2 kWh")
        self.ac1_l2_sell_kwh: FloatUint16Field = FloatUint16Field("ac1_l2_sell_kwh", 51, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily AC1 Sell L2 kWh")
        self.ac2_l2_sell_kwh: FloatUint16Field = FloatUint16Field("ac2_l2_sell_kwh", 52, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily AC2 Sell L2 kWh")
        self.l2_output_kwh: FloatUint16Field = FloatUint16Field("l2_output_kwh", 53, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily Output L2 kWh")
        self.charger_kwh: FloatUint16Field = FloatUint16Field("charger_kwh", 54, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily Charger kWh")
        self.output_kw: FloatUint16Field = FloatUint16Field("output_kw", 55, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Output kW")
        self.buy_kw: FloatUint16Field = FloatUint16Field("buy_kw", 56, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Buy kW")
        self.sell_kw: FloatUint16Field = FloatUint16Field("sell_kw", 57, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Sell kW")
        self.charge_kw: FloatUint16Field = FloatUint16Field("charge_kw", 58, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Charge kW")
        self.load_kw: FloatUint16Field = FloatUint16Field("load_kw", 59, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Load kW")
        self.ac_couple_kw: FloatUint16Field = FloatUint16Field("ac_couple_kw", 60, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="AC Coupled kW")


class RadianInverterConfigurationModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack Radian Series Split Phase Inverter  Configuration Block")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of block in 16-bit registers")
        self.port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
        self.dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
        self.ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 5, 1, Mode.R, description="AC Current Scale Factor")
        self.ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 6, 1, Mode.R, description="AC Voltage Scale Factor")
        self.time_scale_factor: Int16Field = Int16Field("time_scale_factor", 7, 1, Mode.R, description="Time Scale Factor")
        self.major_firmware_number: Uint16Field = Uint16Field("major_firmware_number", 8, 1, Mode.R, description="Inverter Major firmware revision")
        self.mid_firmware_number: Uint16Field = Uint16Field("mid_firmware_number", 9, 1, Mode.R, description="Inverter Mid firmware revision")
        self.minor_firmware_number: Uint16Field = Uint16Field("minor_firmware_number", 10, 1, Mode.R, description="Inverter Minor firmware revision")
        self.search_sensitivity: Uint16Field = Uint16Field("search_sensitivity", 18, 1, Mode.RW, description="Search sensitivity")
        self.search_pulse_length: Uint16Field = Uint16Field("search_pulse_length", 19, 1, Mode.RW, units="Cycles", description="Search pulse length")
        self.search_pulse_spacing: Uint16Field = Uint16Field("search_pulse_spacing", 20, 1, Mode.RW, units="Cycles", description="Search pulse spacing")
        self.ac_input_select_priority: EnumUint16Field = EnumUint16Field("ac_input_select_priority", 21, 1, Mode.RW, enum=Enum("ac_input_select_priority", [('Gen', 1), ('Grid', 0)]), description="0=Grid, 1=Gen")
        self.charger_operating_mode: EnumUint16Field = EnumUint16Field("charger_operating_mode", 25, 1, Mode.RW, enum=Enum("charger_operating_mode", [('All Inverter Charging Disabled', 0), ('Bulk and Float Charging Enabled', 1)]), description="0=All Inverter Charging Disabled, 1=Bulk and Float Charging Enabled")
        self.ac_coupled: EnumUint16Field = EnumUint16Field("ac_coupled", 26, 1, Mode.R, enum=Enum("ac_coupled", [('No', 0), ('Yes', 1)]), description="0=No, 1=Yes")
        self.grid_input_mode: EnumUint16Field = EnumUint16Field("grid_input_mode", 27, 1, Mode.RW, enum=Enum("grid_input_mode", [('Backup', 4), ('Generator', 0), ('Grid Tied', 2), ('Grid Zero', 6), ('Mini Grid', 5), ('Support', 1), ('UPS', 3)]), description="Grid Input Mode: 0=Generator, 1=Support, 2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero")
        self.grid_transfer_delay: Uint16Field = Uint16Field("grid_transfer_delay", 30, 1, Mode.RW, units="msecs", description="Grid Input AC transfer delay")
        self.gen_input_mode: EnumUint16Field = EnumUint16Field("gen_input_mode", 32, 1, Mode.RW, enum=Enum("gen_input_mode", [('Backup', 4), ('Generator', 0), ('Grid Tied', 2), ('Grid Zero', 6), ('Mini Grid', 5), ('Support', 1), ('UPS', 3)]), description="Grid Input Mode: 0=Generator, 1=Support, 2=Grid Tied, 3=UPS, 4=Backup, 5=Mini Grid, 6=Grid Zero")
        self.gen_transfer_delay: Uint16Field = Uint16Field("gen_transfer_delay", 35, 1, Mode.RW, units="msecs", description="Gen Input AC transfer delay")
        self.aux_mode: EnumUint16Field = EnumUint16Field("aux_mode", 40, 1, Mode.RW, enum=Enum("aux_mode", [('AC Divert', 9), ('AC Source Status', 8), ('Cool Fan', 5), ('DC Divert', 6), ('Fault', 3), ('Gen Alert', 2), ('Grid Limit/IEEE', 7), ('Load Shed', 1), ('Vent Fan', 4)]), description="1=Load Shed, 2=Gen Alert, 3=Fault, 4=Vent Fan, 5=Cool Fan, 6=DC Divert, 7=Grid Limit/IEEE ,8=AC Source Status,9=AC Divert")
        self.aux_control: EnumUint16Field = EnumUint16Field("aux_control", 41, 1, Mode.RW, enum=Enum("aux_control", [('Auto', 1), ('Off', 0), ('On', 2)]), description="0 = Off; 1 = Auto; 2 = On")
        self.aux_relay_mode: EnumUint16Field = EnumUint16Field("aux_relay_mode", 46, 1, Mode.RW, enum=Enum("aux_relay_mode", [('AC Divert', 9), ('AC Source Status', 8), ('Cool Fan', 5), ('DC Divert', 6), ('Fault', 3), ('Gen Alert', 2), ('Grid Limit/IEEE', 7), ('Load Shed', 1), ('Vent Fan', 4)]), description="1=Load Shed, 2=Gen Alert, 3=Fault, 4=Vent Fan, 5=Cool Fan, 6=DC Divert, 7=Grid Limit/IEEE ,8=AC Source Status,9=AC Divert")
        self.aux_relay_control: EnumUint16Field = EnumUint16Field("aux_relay_control", 47, 1, Mode.RW, enum=Enum("aux_relay_control", [('Auto', 2), ('Off', 0), ('On', 1)]), description="0 = Off; 1 = On; 2 = Auto")
        self.stacking_mode: EnumUint16Field = EnumUint16Field("stacking_mode", 52, 1, Mode.RW, enum=Enum("stacking_mode", [('B Phase Master', 17), ('C Phase Master', 18), ('Master', 10), ('Slave', 12)]), description="10=Master, 12=Slave, 17=B Phase Master, 18=C Phase Master")
        self.master_power_save_level: Uint16Field = Uint16Field("master_power_save_level", 53, 1, Mode.RW, description="Master inverter power save level")
        self.slave_power_save_level: Uint16Field = Uint16Field("slave_power_save_level", 54, 1, Mode.RW, description="Slave inverter power save level")
        self.grid_tie_window: EnumUint16Field = EnumUint16Field("grid_tie_window", 56, 1, Mode.RW, enum=Enum("grid_tie_window", [('IEEE', 0), ('User (GS8048 Only)', 1)]), description="0=IEEE, 1=User (GS8048 Only)")
        self.grid_tie_enable: EnumUint16Field = EnumUint16Field("grid_tie_enable", 57, 1, Mode.RW, enum=Enum("grid_tie_enable", [('No', 0), ('Yes', 1)]), description="1=Yes, 0=No")
        self.grid_ac_input_voltage_calibrate_factor: Int16Field = Int16Field("grid_ac_input_voltage_calibrate_factor", 58, 1, Mode.RW, units="Volts AC", description="Grid AC input voltage calibration factor")
        self.gen_ac_input_voltage_calibrate_factor: Int16Field = Int16Field("gen_ac_input_voltage_calibrate_factor", 59, 1, Mode.RW, units="Volts AC", description="Gen AC input voltage calibration factor")
        self.ac_output_voltage_calibrate_factor: Int16Field = Int16Field("ac_output_voltage_calibrate_factor", 60, 1, Mode.RW, units="Volts AC", description="AC output voltage calibration factor")
        self.mini_grid_lbx_delay: Uint16Field = Uint16Field("mini_grid_lbx_delay", 64, 1, Mode.RW, units="Hours", description="Mini Grid LBX reconnect to Grid Delay Time")
        self.serial_number: StringField = StringField("serial_number", 67, 9, Mode.R, description="Device serial number")
        self.model_number: StringField = StringField("model_number", 76, 9, Mode.R, description="Device model")
        self.module_control: EnumUint16Field = EnumUint16Field("module_control", 85, 1, Mode.RW, enum=Enum("module_control", [('Auto', 0), ('Both', 3), ('Left', 1), ('Right', 2)]), description="0=Auto, 1=Left, 2=Right, 3=Both")
        self.model_select: EnumUint16Field = EnumUint16Field("model_select", 86, 1, Mode.RW, enum=Enum("model_select", [('Full', 0), ('Half', 1)]), description="0=Full, 1=Half")
        self.ee_write_enable: EnumUint16Field = EnumUint16Field("ee_write_enable", 91, 1, Mode.RW, enum=Enum("ee_write_enable", [('Disable', 0), ('Enable', 1)]), description="EEPROM Write Enable 1= Enable, 0= Disable")
        self.absorb_volts: FloatUint16Field = FloatUint16Field("absorb_volts", 11, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Absorb Voltage Target")
        self.absorb_time_hours: FloatUint16Field = FloatUint16Field("absorb_time_hours", 12, 1, Mode.RW, units="Hours", scale_factor=self.time_scale_factor, description="Absorb Time Hours")
        self.float_volts: FloatUint16Field = FloatUint16Field("float_volts", 13, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Float Voltage Target")
        self.float_time_hours: FloatUint16Field = FloatUint16Field("float_time_hours", 14, 1, Mode.RW, units="Hours", scale_factor=self.time_scale_factor, description="Float Time Hours")
        self.re_float_volts: FloatUint16Field = FloatUint16Field("re_float_volts", 15, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="ReFloat Voltage Target")
        self.eq_volts: FloatUint16Field = FloatUint16Field("eq_volts", 16, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="EQ Voltage Target")
        self.eq_time_hours: FloatUint16Field = FloatUint16Field("eq_time_hours", 17, 1, Mode.RW, units="Hours", scale_factor=self.time_scale_factor, description="EQ Time Hours")
        self.grid_ac_input_current_limit: FloatUint16Field = FloatUint16Field("grid_ac_input_current_limit", 22, 1, Mode.RW, units="Amps", scale_factor=self.ac_current_scale_factor, description="Grid AC input current limit")
        self.gen_ac_input_current_limit: FloatUint16Field = FloatUint16Field("gen_ac_input_current_limit", 23, 1, Mode.RW, units="Amps", scale_factor=self.ac_current_scale_factor, description="Gen AC input current limit")
        self.charger_ac_input_current_limit: FloatUint16Field = FloatUint16Field("charger_ac_input_current_limit", 24, 1, Mode.RW, units="Amps", scale_factor=self.ac_current_scale_factor, description="Charger AC input current limit")
        self.grid_lower_input_voltage_limit: FloatUint16Field = FloatUint16Field("grid_lower_input_voltage_limit", 28, 1, Mode.RW, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Grid Input AC voltage lower limit")
        self.grid_upper_input_voltage_limit: FloatUint16Field = FloatUint16Field("grid_upper_input_voltage_limit", 29, 1, Mode.RW, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Grid Input AC voltage upper limit")
        self.grid_connect_delay: FloatUint16Field = FloatUint16Field("grid_connect_delay", 31, 1, Mode.RW, units="Minutes", scale_factor=self.time_scale_factor, description="Grid Input AC connect delay")
        self.gen_lower_input_voltage_limit: FloatUint16Field = FloatUint16Field("gen_lower_input_voltage_limit", 33, 1, Mode.RW, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Gen Input AC voltage lower limit")
        self.gen_upper_input_voltage_limit: FloatUint16Field = FloatUint16Field("gen_upper_input_voltage_limit", 34, 1, Mode.RW, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Gen Input AC voltage upper limit")
        self.gen_connect_delay: FloatUint16Field = FloatUint16Field("gen_connect_delay", 36, 1, Mode.RW, units="Minutes", scale_factor=self.time_scale_factor, description="Gen Input AC connect delay")
        self.ac_output_voltage: FloatUint16Field = FloatUint16Field("ac_output_voltage", 37, 1, Mode.RW, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="AC output Voltage")
        self.low_battery_cut_out_voltage: FloatUint16Field = FloatUint16Field("low_battery_cut_out_voltage", 38, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Battery cut-out voltage")
        self.low_battery_cut_in_voltage: FloatUint16Field = FloatUint16Field("low_battery_cut_in_voltage", 39, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Battery cut-in voltage")
        self.aux_on_battery_voltage: FloatUint16Field = FloatUint16Field("aux_on_battery_voltage", 42, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="AUX ON battery voltage")
        self.aux_on_delay_time: FloatUint16Field = FloatUint16Field("aux_on_delay_time", 43, 1, Mode.RW, units="Minutes", scale_factor=self.time_scale_factor, description="AUX ON Delay")
        self.aux_off_battery_voltage: FloatUint16Field = FloatUint16Field("aux_off_battery_voltage", 44, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="AUX OFF battery voltage")
        self.aux_off_delay_time: FloatUint16Field = FloatUint16Field("aux_off_delay_time", 45, 1, Mode.RW, units="Minutes", scale_factor=self.time_scale_factor, description="AUX OFF Delay")
        self.aux_relay_on_battery_voltage: FloatUint16Field = FloatUint16Field("aux_relay_on_battery_voltage", 48, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="AUX Relay ON battery voltage")
        self.aux_relay_on_delay_time: FloatUint16Field = FloatUint16Field("aux_relay_on_delay_time", 49, 1, Mode.RW, units="Minutes", scale_factor=self.time_scale_factor, description="AUX Relay ON Delay")
        self.aux_relay_off_battery_voltage: FloatUint16Field = FloatUint16Field("aux_relay_off_battery_voltage", 50, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="AUX Relay OFF battery voltage")
        self.aux_relay_off_delay_time: FloatUint16Field = FloatUint16Field("aux_relay_off_delay_time", 51, 1, Mode.RW, units="Minutes", scale_factor=self.time_scale_factor, description="AUX Relay OFF Delay")
        self.sell_volts: FloatUint16Field = FloatUint16Field("sell_volts", 55, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Sell Voltage Target")
        self.battery_voltage_calibrate_factor: FloatInt16Field = FloatInt16Field("battery_voltage_calibrate_factor", 61, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Battery voltage calibration factor")
        self.re_bulk_volts: FloatUint16Field = FloatUint16Field("re_bulk_volts", 62, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="ReBulk Voltage Target")
        self.mini_grid_lbx_volts: FloatUint16Field = FloatUint16Field("mini_grid_lbx_volts", 63, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Mini Grid LBX reconnect to Grid Battery Voltage")
        self.grid_zero_do_d_volts: FloatUint16Field = FloatUint16Field("grid_zero_do_d_volts", 65, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Grid Zero DoD Voltage")
        self.grid_zero_do_d_max_offset_ac_amps: FloatUint16Field = FloatUint16Field("grid_zero_do_d_max_offset_ac_amps", 66, 1, Mode.RW, units="Amps", scale_factor=self.ac_current_scale_factor, description="Grid Zero Maximum Offset AC Amps")
        self.low_battery_cut_out_delay: FloatUint16Field = FloatUint16Field("low_battery_cut_out_delay", 87, 1, Mode.RW, units="Seconds xx.x", scale_factor=self.dc_voltage_scale_factor, description="Low Battery Cut Out Delay")
        self.high_battery_cut_out_voltage: FloatUint16Field = FloatUint16Field("high_battery_cut_out_voltage", 88, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="High Battery Cut Out Voltage")
        self.high_battery_cut_in_voltage: FloatUint16Field = FloatUint16Field("high_battery_cut_in_voltage", 89, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="High Battery Cut In Voltage")
        self.high_battery_cut_out_delay: FloatUint16Field = FloatUint16Field("high_battery_cut_out_delay", 90, 1, Mode.RW, units="Seconds xx.x", scale_factor=self.dc_voltage_scale_factor, description="High Battery Cut Out Delay")


class SinglePhaseRadianInverterRealTimeModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack Radian Series Split Phase Inverter Status Block")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of block in 16-bit registers")
        self.port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
        self.dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
        self.ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 5, 1, Mode.R, description="AC Current Scale Factor")
        self.ac_voltage_scale_factor: Int16Field = Int16Field("ac_voltage_scale_factor", 6, 1, Mode.R, description="AC Voltage Scale Factor")
        self.ac_frequency_scale_factor: Int16Field = Int16Field("ac_frequency_scale_factor", 7, 1, Mode.R, description="AC Frequency Scale Factor")
        self.inverter_operating_mode: EnumUint16Field = EnumUint16Field("inverter_operating_mode", 15, 1, Mode.R, enum=Enum("inverter_operating_mode", [('Charger Off', 7), ('Charging', 3), ('EQ', 6), ('Float', 5), ('Inverting', 2), ('Off', 0), ('Offsetting', 14), ('Pass through', 10), ('Searching', 1), ('Selling', 9), ('Silent', 4), ('Support', 8)]), description="0=Off, 1=Searching, 2=Inverting, 3=Charging, 4=Silent, 5=Float, 6=EQ, 7=Charger Off, 8=Support, 9=Selling, 10=Pass through, 14=Offsetting")
        self.error_flags: Bit16Field = Bit16Field("error_flags", 16, 1, Mode.R, flags=GSSingleErrorFlags, description="Bit field for errors. See GS_Error Table")
        self.warning_flags: Bit16Field = Bit16Field("warning_flags", 17, 1, Mode.R, flags=GSSingleWarningFlags, description="Bit field for warnings See GS_Warning Table")
        self.aux_output_state: EnumUint16Field = EnumUint16Field("aux_output_state", 20, 1, Mode.R, enum=Enum("aux_output_state", [('Disabled', 0), ('Enabled', 1)]), description="0 = Disabled; 1 = Enabled")
        self.aux_relay_output_state: EnumUint16Field = EnumUint16Field("aux_relay_output_state", 21, 1, Mode.R, enum=Enum("aux_relay_output_state", [('Disabled', 0), ('Enabled', 1)]), description="0 = Disabled; 1 = Enabled")
        self.l_module_transformer_temperature: Int16Field = Int16Field("l_module_transformer_temperature", 22, 1, Mode.R, units="Degrees C", description="Left module transformer temp in degrees C")
        self.l_module_capacitor_temperature: Int16Field = Int16Field("l_module_capacitor_temperature", 23, 1, Mode.R, units="Degrees C", description="Left module capacitor temp in degrees C")
        self.l_module_fet_temperature: Int16Field = Int16Field("l_module_fet_temperature", 24, 1, Mode.R, units="Degrees C", description="Left module FET temp in degrees C")
        self.r_module_transformer_temperature: Int16Field = Int16Field("r_module_transformer_temperature", 25, 1, Mode.R, units="Degrees C", description="Right module transformer temp in degrees C")
        self.r_module_capacitor_temperature: Int16Field = Int16Field("r_module_capacitor_temperature", 26, 1, Mode.R, units="Degrees C", description="Right module capacitor temp in degrees C")
        self.r_module_fet_temperature: Int16Field = Int16Field("r_module_fet_temperature", 27, 1, Mode.R, units="Degrees C", description="Right module FET temp in degrees C")
        self.battery_temperature: Int16Field = Int16Field("battery_temperature", 28, 1, Mode.R, units="Degrees C", description="Battery temp in degrees C")
        self.ac_input_selection: EnumUint16Field = EnumUint16Field("ac_input_selection", 29, 1, Mode.R, enum=Enum("ac_input_selection", [('Gen', 1), ('Grid', 0)]), description="0=Grid, 1=Gen")
        self.ac_input_state: EnumUint16Field = EnumUint16Field("ac_input_state", 32, 1, Mode.R, enum=Enum("ac_input_state", [('AC Use', 1), ('AC_Drop', 0)]), description="1=AC Use, 0=AC_Drop")
        self.sell_status: Bit16Field = Bit16Field("sell_status", 35, 1, Mode.R, flags=GSSingleSellStatusFlags, description="Bit field for sell status See GS_Sell_Status Table")
        self.kwh_scale_factor: Int16Field = Int16Field("kwh_scale_factor", 36, 1, Mode.R, description="AC kWh scale factor")
        self.gt_number: Uint16Field = Uint16Field("gt_number", 49, 1, Mode.R, description="GT Number sent from Inverter to Charge Controller")
        self.inverter_output_current: FloatUint16Field = FloatUint16Field("inverter_output_current", 8, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="Inverter output current")
        self.inverter_charge_current: FloatUint16Field = FloatUint16Field("inverter_charge_current", 9, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="Inverter charger current")
        self.inverter_buy_current: FloatUint16Field = FloatUint16Field("inverter_buy_current", 10, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="Inverter buy current")
        self.inverter_sell_current: FloatUint16Field = FloatUint16Field("inverter_sell_current", 11, 1, Mode.R, units="Amps", scale_factor=self.ac_current_scale_factor, description="Inverter sell current")
        self.grid_input_ac_voltage: FloatUint16Field = FloatUint16Field("grid_input_ac_voltage", 12, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Grid Input AC Voltage")
        self.gen_input_ac_voltage: FloatUint16Field = FloatUint16Field("gen_input_ac_voltage", 13, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Gen Input AC Voltage")
        self.output_ac_voltage: FloatUint16Field = FloatUint16Field("output_ac_voltage", 14, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Output AC Voltage")
        self.battery_voltage: FloatUint16Field = FloatUint16Field("battery_voltage", 18, 1, Mode.R, units="Volts DC", scale_factor=self.dc_voltage_scale_factor, description="Battery Voltage")
        self.temp_compensated_target_voltage: FloatUint16Field = FloatUint16Field("temp_compensated_target_voltage", 19, 1, Mode.R, units="Volts DC", scale_factor=self.dc_voltage_scale_factor, description="Temperature compensated target battery voltage")
        self.ac_input_frequency: FloatUint16Field = FloatUint16Field("ac_input_frequency", 30, 1, Mode.R, units="Hz", scale_factor=self.ac_frequency_scale_factor, description="Selected AC Input frequency HZ")
        self.ac_input_voltage: FloatUint16Field = FloatUint16Field("ac_input_voltage", 31, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Selected Input AC Voltage")
        self.minimum_ac_input_voltage: FloatUint16Field = FloatUint16Field("minimum_ac_input_voltage", 33, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Minimum Input AC Voltage (Write to clear value)")
        self.maximum_ac_input_voltage: FloatUint16Field = FloatUint16Field("maximum_ac_input_voltage", 34, 1, Mode.R, units="Volts AC", scale_factor=self.ac_voltage_scale_factor, description="Maximum Input AC Voltage (Write to clear value)")
        self.ac1_buy_kwh: FloatUint16Field = FloatUint16Field("ac1_buy_kwh", 37, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily AC1 Buy kWh")
        self.ac2_buy_kwh: FloatUint16Field = FloatUint16Field("ac2_buy_kwh", 38, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily AC2 Buy kWh")
        self.ac1_sell_kwh: FloatUint16Field = FloatUint16Field("ac1_sell_kwh", 39, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily AC1 Sell kWh")
        self.ac2_sell_kwh: FloatUint16Field = FloatUint16Field("ac2_sell_kwh", 40, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily AC2 Sell kWh")
        self.output_kwh: FloatUint16Field = FloatUint16Field("output_kwh", 41, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily Output kWh")
        self.charger_kwh: FloatUint16Field = FloatUint16Field("charger_kwh", 42, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Daily Charger kWh")
        self.output_kw: FloatUint16Field = FloatUint16Field("output_kw", 43, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Output kW")
        self.buy_kw: FloatUint16Field = FloatUint16Field("buy_kw", 44, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Buy kW")
        self.sell_kw: FloatUint16Field = FloatUint16Field("sell_kw", 45, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Sell kW")
        self.charge_kw: FloatUint16Field = FloatUint16Field("charge_kw", 46, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Charger kW")
        self.load_kw: FloatUint16Field = FloatUint16Field("load_kw", 47, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Load kW")
        self.ac_couple_kw: FloatUint16Field = FloatUint16Field("ac_couple_kw", 48, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="AC Coupled kW")


class FLEXnetDCRealTimeModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack FLEXnet DC Battery Monitor Status Block")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of block in 16-bit registers")
        self.port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on Outback network")
        self.dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
        self.dc_current_scale_factor: Int16Field = Int16Field("dc_current_scale_factor", 5, 1, Mode.R, description="DC Current Scale Factor")
        self.time_scale_factor: Int16Field = Int16Field("time_scale_factor", 6, 1, Mode.R, description="Time Scale Factor")
        self.kwh_scale_factor: Int16Field = Int16Field("kwh_scale_factor", 7, 1, Mode.R, description="Kilo Watt Hours Scale Factor")
        self.kw_scale_factor: Int16Field = Int16Field("kw_scale_factor", 8, 1, Mode.R, description="Kilo Watt Scale Factor")
        self.battery_temperature: Int16Field = Int16Field("battery_temperature", 14, 1, Mode.R, units="Degrees C", description="Battery Temperature C")
        self.status_flags: Bit16Field = Bit16Field("status_flags", 15, 1, Mode.R, flags=FNStatusFlags, description="See FN Status Table")
        self.shunt_a_accumulated_ah: Int16Field = Int16Field("shunt_a_accumulated_ah", 16, 1, Mode.R, units="AH", description="Shunt A Accumulated_AH")
        self.shunt_b_accumulated_ah: Int16Field = Int16Field("shunt_b_accumulated_ah", 18, 1, Mode.R, units="AH", description="Shunt B Accumulated_AH")
        self.shunt_c_accumulated_ah: Int16Field = Int16Field("shunt_c_accumulated_ah", 20, 1, Mode.R, units="AH", description="Shunt C Accumulated_AH")
        self.state_of_charge: Uint16Field = Uint16Field("state_of_charge", 28, 1, Mode.R, units="Percent", description="Current Battery State of Charge")
        self.todays_minimum_soc: Uint16Field = Uint16Field("todays_minimum_soc", 29, 1, Mode.R, units="Percent", description="Todays minimum SOC")
        self.todays_maximum_soc: Uint16Field = Uint16Field("todays_maximum_soc", 30, 1, Mode.R, units="Percent", description="Todays maximum SOC")
        self.todays_net_input_ah: Uint16Field = Uint16Field("todays_net_input_ah", 31, 1, Mode.R, units="AH", description="Todays NET input AH")
        self.todays_net_output_ah: Uint16Field = Uint16Field("todays_net_output_ah", 33, 1, Mode.R, units="AH", description="Todays NET output AH")
        self.todays_net_battery_ah: Int16Field = Int16Field("todays_net_battery_ah", 35, 1, Mode.R, units="AH", description="Todays NET battery AH")
        self.charge_factor_corrected_net_battery_ah: Int16Field = Int16Field("charge_factor_corrected_net_battery_ah", 37, 1, Mode.R, units="AH", description="Charge factor corrected NET battery AH")
        self.todays_minimum_battery_time: Uint32Field = Uint32Field("todays_minimum_battery_time", 40, 2, Mode.R, units="Seconds", description="Todays minimum battery voltage time UTC")
        self.todays_maximum_battery_time: Uint32Field = Uint32Field("todays_maximum_battery_time", 43, 2, Mode.R, units="Seconds", description="Todays maximum battery voltage time UTC")
        self.cycle_charge_factor: Uint16Field = Uint16Field("cycle_charge_factor", 45, 1, Mode.R, units="Percent", description="Cycle Charge Factor")
        self.cycle_kwh_charge_efficiency: Uint16Field = Uint16Field("cycle_kwh_charge_efficiency", 46, 1, Mode.R, units="Percent", description="Cycle kWh Charge Efficiency")
        self.lifetime_k_ah_removed: Uint16Field = Uint16Field("lifetime_k_ah_removed", 48, 1, Mode.R, units="AH", description="Lifetime kAH removed from battery")
        self.shunt_a_historical_returned_to_battery_ah: Uint16Field = Uint16Field("shunt_a_historical_returned_to_battery_ah", 49, 1, Mode.R, units="AH", description="Shunt A historical returned to battery AH")
        self.shunt_a_historical_removed_from_battery_ah: Uint16Field = Uint16Field("shunt_a_historical_removed_from_battery_ah", 51, 1, Mode.R, units="AH", description="Shunt A historical removed from battery AH")
        self.shunt_b_historical_returned_to_battery_ah: Uint16Field = Uint16Field("shunt_b_historical_returned_to_battery_ah", 57, 1, Mode.R, units="AH", description="Shunt B historical returned to battery AH")
        self.shunt_b_historical_removed_from_battery_ah: Uint16Field = Uint16Field("shunt_b_historical_removed_from_battery_ah", 59, 1, Mode.R, units="AH", description="Shunt B historical removed from battery AH")
        self.shunt_c_historical_returned_to_battery_ah: Uint16Field = Uint16Field("shunt_c_historical_returned_to_battery_ah", 65, 1, Mode.R, units="AH", description="Shunt C historical returned to battery AH")
        self.shunt_c_historical_removed_from_battery_ah: Uint16Field = Uint16Field("shunt_c_historical_removed_from_battery_ah", 67, 1, Mode.R, units="AH", description="Shunt C historical removed from battery AH")
        self.shunt_a_reset_maximum_data: Uint16Field = Uint16Field("shunt_a_reset_maximum_data", 73, 1, Mode.R, description="Read value needed to reset shunt A maximum data")
        self.shunt_a_reset_maximum_data_write_complement: Uint16Field = Uint16Field("shunt_a_reset_maximum_data_write_complement", 74, 1, Mode.W, description="Write value's complement to reset shunt A maximum data")
        self.shunt_b_reset_maximum_data: Uint16Field = Uint16Field("shunt_b_reset_maximum_data", 75, 1, Mode.R, description="Read value needed to reset shunt B maximum data")
        self.shunt_b_reset_maximum_data_write_complement: Uint16Field = Uint16Field("shunt_b_reset_maximum_data_write_complement", 76, 1, Mode.W, description="Write value's complement to reset shunt B maximum data")
        self.shunt_c_reset_maximum_data: Uint16Field = Uint16Field("shunt_c_reset_maximum_data", 77, 1, Mode.R, description="Read value needed to reset shunt C maximum data")
        self.shunt_c_reset_maximum_data_write_complement: Uint16Field = Uint16Field("shunt_c_reset_maximum_data_write_complement", 78, 1, Mode.W, description="Write value's complement to reset shunt C maximum data")
        self.shunt_a_current: FloatInt16Field = FloatInt16Field("shunt_a_current", 9, 1, Mode.R, units="Amps", scale_factor=self.dc_current_scale_factor, description="Shunt A current")
        self.shunt_b_current: FloatInt16Field = FloatInt16Field("shunt_b_current", 10, 1, Mode.R, units="Amps", scale_factor=self.dc_current_scale_factor, description="Shunt B current")
        self.shunt_c_current: FloatInt16Field = FloatInt16Field("shunt_c_current", 11, 1, Mode.R, units="Amps", scale_factor=self.dc_current_scale_factor, description="Shunt C current")
        self.battery_voltage: FloatUint16Field = FloatUint16Field("battery_voltage", 12, 1, Mode.R, units="Volts", scale_factor=self.dc_voltage_scale_factor, description="Battery Voltage")
        self.battery_current: FloatInt16Field = FloatInt16Field("battery_current", 13, 1, Mode.R, units="Amps", scale_factor=self.dc_current_scale_factor, description="Battery Current")
        self.shunt_a_accumulated_kwh: FloatInt16Field = FloatInt16Field("shunt_a_accumulated_kwh", 17, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Shunt A Accumulated_kWh")
        self.shunt_b_accumulated_kwh: FloatInt16Field = FloatInt16Field("shunt_b_accumulated_kwh", 19, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Shunt B Accumulated_kWh")
        self.shunt_c_accumulated_kwh: FloatInt16Field = FloatInt16Field("shunt_c_accumulated_kwh", 21, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Shunt C Accumulated_kWh")
        self.input_current: FloatUint16Field = FloatUint16Field("input_current", 22, 1, Mode.R, units="Amps", scale_factor=self.dc_current_scale_factor, description="Total_input_current")
        self.output_current: FloatUint16Field = FloatUint16Field("output_current", 23, 1, Mode.R, units="Amps", scale_factor=self.dc_current_scale_factor, description="Total_output_current")
        self.input_kw: FloatUint16Field = FloatUint16Field("input_kw", 24, 1, Mode.R, units="kW", scale_factor=self.kw_scale_factor, description="Total_input_kWatts")
        self.output_kw: FloatUint16Field = FloatUint16Field("output_kw", 25, 1, Mode.R, units="kW", scale_factor=self.kw_scale_factor, description="Total_output_kWatts")
        self.net_kw: FloatInt16Field = FloatInt16Field("net_kw", 26, 1, Mode.R, units="kW", scale_factor=self.kw_scale_factor, description="Total_net_kWatts")
        self.days_since_charge_parameters_met: FloatUint16Field = FloatUint16Field("days_since_charge_parameters_met", 27, 1, Mode.R, units="Days", scale_factor=self.time_scale_factor, description="Days Since Charge Parameters Met")
        self.todays_net_input_kwh: FloatUint16Field = FloatUint16Field("todays_net_input_kwh", 32, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Todays NET input kWh")
        self.todays_net_output_kwh: FloatUint16Field = FloatUint16Field("todays_net_output_kwh", 34, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Todays NET output kWh")
        self.todays_net_battery_kwh: FloatInt16Field = FloatInt16Field("todays_net_battery_kwh", 36, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Todays NET battery kWh")
        self.charge_factor_corrected_net_battery_kwh: FloatInt16Field = FloatInt16Field("charge_factor_corrected_net_battery_kwh", 38, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Charge factor corrected NET battery kWh")
        self.todays_minimum_battery_voltage: FloatUint16Field = FloatUint16Field("todays_minimum_battery_voltage", 39, 1, Mode.R, units="Volts", scale_factor=self.dc_voltage_scale_factor, description="Todays minimum battery voltage")
        self.todays_maximum_battery_voltage: FloatUint16Field = FloatUint16Field("todays_maximum_battery_voltage", 42, 1, Mode.R, units="Volts", scale_factor=self.dc_voltage_scale_factor, description="Todays maximum battery voltage")
        self.total_days_at_100_percent: FloatUint16Field = FloatUint16Field("total_days_at_100_percent", 47, 1, Mode.R, units="Days", scale_factor=self.time_scale_factor, description="Total days at 100% charged")
        self.shunt_a_historical_returned_to_battery_kwh: FloatUint16Field = FloatUint16Field("shunt_a_historical_returned_to_battery_kwh", 50, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Shunt A historical returned to battery kWh")
        self.shunt_a_historical_removed_from_battery_kwh: FloatUint16Field = FloatUint16Field("shunt_a_historical_removed_from_battery_kwh", 52, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Shunt A historical removed from battery kWh")
        self.shunt_a_maximum_charge_rate: FloatUint16Field = FloatUint16Field("shunt_a_maximum_charge_rate", 53, 1, Mode.R, units="Amps", scale_factor=self.dc_current_scale_factor, description="Shunt A historical maximum charge rate Amps")
        self.shunt_a_maximum_charge_rate_kw: FloatUint16Field = FloatUint16Field("shunt_a_maximum_charge_rate_kw", 54, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Shunt A historical maximum charge rate kW")
        self.shunt_a_maximum_discharge_rate: FloatInt16Field = FloatInt16Field("shunt_a_maximum_discharge_rate", 55, 1, Mode.R, units="Amps", scale_factor=self.dc_current_scale_factor, description="Shunt A historical maximum discharge rate Amps")
        self.shunt_a_maximum_discharge_rate_kw: FloatInt16Field = FloatInt16Field("shunt_a_maximum_discharge_rate_kw", 56, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Shunt A historical maximum discharge rate kW")
        self.shunt_b_historical_returned_to_battery_kwh: FloatUint16Field = FloatUint16Field("shunt_b_historical_returned_to_battery_kwh", 58, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Shunt B historical returned to battery kWh")
        self.shunt_b_historical_removed_from_battery_kwh: FloatUint16Field = FloatUint16Field("shunt_b_historical_removed_from_battery_kwh", 60, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Shunt B historical removed from battery kWh")
        self.shunt_b_maximum_charge_rate: FloatUint16Field = FloatUint16Field("shunt_b_maximum_charge_rate", 61, 1, Mode.R, units="Amps", scale_factor=self.dc_current_scale_factor, description="Shunt B historical maximum charge rate Amps")
        self.shunt_b_maximum_charge_rate_kw: FloatUint16Field = FloatUint16Field("shunt_b_maximum_charge_rate_kw", 62, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Shunt B historical maximum charge rate kW")
        self.shunt_b_maximum_discharge_rate: FloatInt16Field = FloatInt16Field("shunt_b_maximum_discharge_rate", 63, 1, Mode.R, units="Amps", scale_factor=self.dc_current_scale_factor, description="Shunt B historical maximum discharge rate Amps")
        self.shunt_b_maximum_discharge_rate_kw: FloatInt16Field = FloatInt16Field("shunt_b_maximum_discharge_rate_kw", 64, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Shunt B historical maximum discharge rate kW")
        self.shunt_c_historical_returned_to_battery_kwh: FloatUint16Field = FloatUint16Field("shunt_c_historical_returned_to_battery_kwh", 66, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Shunt C historical returned to battery kWh")
        self.shunt_c_historical_removed_from_battery_kwh: FloatUint16Field = FloatUint16Field("shunt_c_historical_removed_from_battery_kwh", 68, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Shunt C historical removed from battery kWh")
        self.shunt_c_maximum_charge_rate: FloatUint16Field = FloatUint16Field("shunt_c_maximum_charge_rate", 69, 1, Mode.R, units="Amps", scale_factor=self.dc_current_scale_factor, description="Shunt C historical maximum charge rate Amps")
        self.shunt_c_maximum_charge_rate_kw: FloatUint16Field = FloatUint16Field("shunt_c_maximum_charge_rate_kw", 70, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Shunt C historical maximum charge rate kW")
        self.shunt_c_maximum_discharge_rate: FloatInt16Field = FloatInt16Field("shunt_c_maximum_discharge_rate", 71, 1, Mode.R, units="Amps", scale_factor=self.dc_current_scale_factor, description="Shunt C historical maximum discharge rate Amps")
        self.shunt_c_maximum_discharge_rate_kw: FloatInt16Field = FloatInt16Field("shunt_c_maximum_discharge_rate_kw", 72, 1, Mode.R, units="kW", scale_factor=self.kwh_scale_factor, description="Shunt C historical maximum discharge rate kW")


class FLEXnetDCConfigurationModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack FLEXnet-DC Battery Monitor Configuration Block")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of block in 16-bit registers")
        self.port_number: Uint16Field = Uint16Field("port_number", 3, 1, Mode.R, description="Port number on OutBack network")
        self.dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 4, 1, Mode.R, description="DC Voltage Scale Factor")
        self.dc_current_scale_factor: Int16Field = Int16Field("dc_current_scale_factor", 5, 1, Mode.R, description="DC Current Scale Factor")
        self.kwh_scale_factor: Int16Field = Int16Field("kwh_scale_factor", 6, 1, Mode.R, description="Kilo Watt Hours Scale Factor")
        self.major_firmware_number: Uint16Field = Uint16Field("major_firmware_number", 7, 1, Mode.R, description="FLEXnet-DC Major firmware revision")
        self.mid_firmware_number: Uint16Field = Uint16Field("mid_firmware_number", 8, 1, Mode.R, description="FLEXnet-DC Mid firmware revision")
        self.minor_firmware_number: Uint16Field = Uint16Field("minor_firmware_number", 9, 1, Mode.R, description="FLEXnet-DC Minor firmware revision")
        self.battery_capacity: Uint16Field = Uint16Field("battery_capacity", 10, 1, Mode.RW, units="AH", description="Battery AH capacity")
        self.charged_time: Uint16Field = Uint16Field("charged_time", 12, 1, Mode.RW, units="Minutes", description="Battery Charged Time Minutes")
        self.charge_factor: Uint16Field = Uint16Field("charge_factor", 14, 1, Mode.RW, units="Percent", description="Battery Charge Factor")
        self.shunt_a_enabled: EnumUint16Field = EnumUint16Field("shunt_a_enabled", 15, 1, Mode.RW, enum=Enum("shunt_a_enabled", [('Disabled', 1), ('Enabled', 0)]), description="0=Enabled, 1=Disabled")
        self.shunt_b_enabled: EnumUint16Field = EnumUint16Field("shunt_b_enabled", 16, 1, Mode.RW, enum=Enum("shunt_b_enabled", [('Disabled', 1), ('Enabled', 0)]), description="0=Enabled, 1=Disabled")
        self.shunt_c_enabled: EnumUint16Field = EnumUint16Field("shunt_c_enabled", 17, 1, Mode.RW, enum=Enum("shunt_c_enabled", [('Disabled', 1), ('Enabled', 0)]), description="0=Enabled, 1=Disabled")
        self.relay_control: EnumUint16Field = EnumUint16Field("relay_control", 18, 1, Mode.RW, enum=Enum("relay_control", [('Auto', 1), ('Off', 0), ('On', 2)]), description="0 = Off; 1 = Auto; 2 = On")
        self.relay_invert_logic: EnumUint16Field = EnumUint16Field("relay_invert_logic", 19, 1, Mode.RW, enum=Enum("relay_invert_logic", [('Invert Logic', 0), ('Normal', 1)]), description="0=Invert Logic,1=Normal")
        self.relay_soc_high: Uint16Field = Uint16Field("relay_soc_high", 22, 1, Mode.RW, units="Percent", description="Relay high SOC enable")
        self.relay_soc_low: Uint16Field = Uint16Field("relay_soc_low", 23, 1, Mode.RW, units="Percent", description="Relay low SOC enable")
        self.relay_high_enable_delay: Uint16Field = Uint16Field("relay_high_enable_delay", 24, 1, Mode.RW, units="Minutes", description="Relay High Enable Delay")
        self.relay_low_enable_delay: Uint16Field = Uint16Field("relay_low_enable_delay", 25, 1, Mode.RW, units="Minutes", description="Relay Low Enable Delay")
        self.set_data_log_day_offset: Uint16Field = Uint16Field("set_data_log_day_offset", 26, 1, Mode.RW, units="Days", description="Day offset 0-400, 0 =Today, 1 = -1 day \u2026")
        self.get_current_data_log_day_offset: Uint16Field = Uint16Field("get_current_data_log_day_offset", 27, 1, Mode.R, units="Days", description="Current Data Log Day Offset")
        self.datalog_minimum_soc: Uint16Field = Uint16Field("datalog_minimum_soc", 28, 1, Mode.R, units="Percent", description="Datalog minimum SOC")
        self.datalog_input_ah: Uint16Field = Uint16Field("datalog_input_ah", 29, 1, Mode.R, units="AH", description="Datalog input AH")
        self.datalog_output_ah: Uint16Field = Uint16Field("datalog_output_ah", 31, 1, Mode.R, units="AH", description="Datalog output AH")
        self.datalog_net_ah: Uint16Field = Uint16Field("datalog_net_ah", 33, 1, Mode.R, units="AH", description="Datalog NET AH")
        self.clear_data_log_read: Uint16Field = Uint16Field("clear_data_log_read", 35, 1, Mode.R, description="Read value needed to clear data log")
        self.clear_data_log_write_complement: Uint16Field = Uint16Field("clear_data_log_write_complement", 36, 1, Mode.W, description="Write value's complement to clear data log")
        self.serial_number: StringField = StringField("serial_number", 37, 9, Mode.R, description="Device serial number")
        self.model_number: StringField = StringField("model_number", 46, 9, Mode.R, description="Device model")
        self.charged_volts: FloatUint16Field = FloatUint16Field("charged_volts", 11, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Battery Charged Voltage")
        self.battery_charged_amps: FloatUint16Field = FloatUint16Field("battery_charged_amps", 13, 1, Mode.RW, units="Amps", scale_factor=self.dc_current_scale_factor, description="Battery Charged Return Amps")
        self.relay_high_voltage: FloatUint16Field = FloatUint16Field("relay_high_voltage", 20, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Relay high voltage enable")
        self.relay_low_voltage: FloatUint16Field = FloatUint16Field("relay_low_voltage", 21, 1, Mode.RW, units="DC Volts", scale_factor=self.dc_voltage_scale_factor, description="Relay low voltage enable")
        self.datalog_input_kwh: FloatUint16Field = FloatUint16Field("datalog_input_kwh", 30, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Datalog input kWh")
        self.datalog_output_kwh: FloatUint16Field = FloatUint16Field("datalog_output_kwh", 32, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Datalog output kWh")
        self.datalog_net_kwh: FloatUint16Field = FloatUint16Field("datalog_net_kwh", 34, 1, Mode.R, units="kWh", scale_factor=self.kwh_scale_factor, description="Datalog NET kWh")


class OutBackSystemControlModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="Vendor Extension for OutBack System Control Block")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of block in 16-bit registers")
        self.dc_voltage_scale_factor: Int16Field = Int16Field("dc_voltage_scale_factor", 3, 1, Mode.R, description="DC Voltage Scale Factor")
        self.ac_current_scale_factor: Int16Field = Int16Field("ac_current_scale_factor", 4, 1, Mode.R, description="AC Current Scale Factor")
        self.time_scale_factor: Int16Field = Int16Field("time_scale_factor", 5, 1, Mode.R, description="Charge Time Scale Factor")
        self.bulk_charge_enable_disable: EnumUint16Field = EnumUint16Field("bulk_charge_enable_disable", 6, 1, Mode.W, enum=Enum("bulk_charge_enable_disable", [('Start Bulk', 1), ('Start EQ Charge', 3), ('Stop Bulk', 2), ('Stop EQ Charge', 4)]), description="1=Start Bulk, 2=Stop Bulk, 3=Start EQ Charge, 4= Stop EQ Charge")
        self.inverter_ac_drop_use: EnumUint16Field = EnumUint16Field("inverter_ac_drop_use", 7, 1, Mode.W, enum=Enum("inverter_ac_drop_use", [('Drop', 2), ('Use', 1)]), description="1=Use, 2=Drop")
        self.set_inverter_mode: EnumUint16Field = EnumUint16Field("set_inverter_mode", 8, 1, Mode.W, enum=Enum("set_inverter_mode", [('Off', 1), ('On', 3), ('Search', 2)]), description="1=Off, 2=Search, 3=On")
        self.grid_tie_mode: EnumUint16Field = EnumUint16Field("grid_tie_mode", 9, 1, Mode.W, enum=Enum("grid_tie_mode", [('Disable', 2), ('Enable', 1)]), description="1=Enable, 2=Disable")
        self.set_inverter_charger_mode: EnumUint16Field = EnumUint16Field("set_inverter_charger_mode", 10, 1, Mode.W, enum=Enum("set_inverter_charger_mode", [('Auto', 2), ('Off', 1), ('On', 3)]), description="1=Off, 2=Auto, 3=On")
        self.control_status: Bit16Field = Bit16Field("control_status", 11, 1, Mode.R, flags=OBControlStatusFlags, description="Bit field for status. See OB_Control_Status Table")
        self.set_ags_op_mode: EnumUint16Field = EnumUint16Field("set_ags_op_mode", 21, 1, Mode.RW, enum=Enum("set_ags_op_mode", [('Auto', 2), ('Off', 0), ('On', 1)]), description="AGS Operating Mode: 0=Off, 1=On, 2=Auto")
        self.ags_operational_state: EnumUint16Field = EnumUint16Field("ags_operational_state", 22, 1, Mode.R, enum=Enum("ags_operational_state", [(' GEN_AWAITING_AC', 5), (' GEN_COOLDOWN', 4), (' GEN_RUNNING', 2), (' GEN_STARTING', 1), (' GEN_WARMUP', 3), ('GEN_STOP', 0)]), description="GEN_STOP=0, GEN_STARTING=1, GEN_RUNNING=2, GEN_WARMUP=3, GEN_COOLDOWN=4, GEN_AWAITING_AC=5")
        self.ags_operational_state_timer: Uint16Field = Uint16Field("ags_operational_state_timer", 23, 1, Mode.R, units="Seconds", description="Number of seconds that OB_AGS_Operational_State has been in current state. If Operational State is 0 then timer=0")
        self.gen_last_run_start_time_gmt: Uint32Field = Uint32Field("gen_last_run_start_time_gmt", 24, 2, Mode.R, units="Seconds", description="Generator last start time in GMT seconds")
        self.gen_last_start_run_duration: Uint32Field = Uint32Field("gen_last_start_run_duration", 26, 2, Mode.R, units="Seconds", description="Last Generator Start Run Duration Seconds")
        self.set_sell_voltage: FloatUint16Field = FloatUint16Field("set_sell_voltage", 12, 1, Mode.RW, units="Volts", scale_factor=self.dc_voltage_scale_factor, description="Global Sell Voltage")
        self.set_radian_inverter_sell_current_limit: FloatUint16Field = FloatUint16Field("set_radian_inverter_sell_current_limit", 13, 1, Mode.RW, units="Amps", scale_factor=self.ac_current_scale_factor, description="Radian Inverter Sell Current Limit")
        self.set_absorb_voltage: FloatUint16Field = FloatUint16Field("set_absorb_voltage", 14, 1, Mode.RW, units="Volts", scale_factor=self.dc_voltage_scale_factor, description="Global Absorb Voltage")
        self.set_absorb_time: FloatUint16Field = FloatUint16Field("set_absorb_time", 15, 1, Mode.RW, units="Hours", scale_factor=self.time_scale_factor, description="Time in tenths of hour")
        self.set_float_voltage: FloatUint16Field = FloatUint16Field("set_float_voltage", 16, 1, Mode.RW, units="Volts", scale_factor=self.dc_voltage_scale_factor, description="Global Float Voltage")
        self.set_float_time: FloatUint16Field = FloatUint16Field("set_float_time", 17, 1, Mode.RW, units="Hours", scale_factor=self.time_scale_factor, description="Time in tenths of hour")
        self.set_inverter_charger_current_limit: FloatUint16Field = FloatUint16Field("set_inverter_charger_current_limit", 18, 1, Mode.RW, units="Amps", scale_factor=self.ac_current_scale_factor, description="Inverter Charger Current Limit")
        self.set_inverter_ac1_current_limit: FloatUint16Field = FloatUint16Field("set_inverter_ac1_current_limit", 19, 1, Mode.RW, units="Amps", scale_factor=self.ac_current_scale_factor, description="Inverter AC1 input Current Limit")
        self.set_inverter_ac2_current_limit: FloatUint16Field = FloatUint16Field("set_inverter_ac2_current_limit", 20, 1, Mode.RW, units="Amps", scale_factor=self.ac_current_scale_factor, description="Inverter AC2 input Current Limit")


class OPTICSPacketStatisticsModel(Model):
    
    def __init__(self):
        self.did: Uint16Field = Uint16Field("did", 1, 1, Mode.R, description="OPTICS Packet Stats DID")
        self.length: Uint16Field = Uint16Field("length", 2, 1, Mode.R, units="Registers", description="Length of OPTICS Packet Status Block")
        self.bt_min: Uint16Field = Uint16Field("bt_min", 3, 1, Mode.R, units="msecs", description="Boot packet minimum time")
        self.bt_max: Uint16Field = Uint16Field("bt_max", 4, 1, Mode.R, units="msecs", description="Boot packet maximum time")
        self.bt_ave: Uint16Field = Uint16Field("bt_ave", 5, 1, Mode.R, units="msecs", description="Boot packet average time")
        self.bt_attempts: Uint16Field = Uint16Field("bt_attempts", 6, 1, Mode.R, description="Boot packet number of attempts")
        self.bt_errors: Uint16Field = Uint16Field("bt_errors", 7, 1, Mode.R, description="Boot packet error returned from server count")
        self.bt_timeouts: Uint16Field = Uint16Field("bt_timeouts", 8, 1, Mode.R, description="Boot packet timeout from server count")
        self.bt_packet_timeout: Uint16Field = Uint16Field("bt_packet_timeout", 9, 1, Mode.R, units="secs", description="Boot packet current gateway timeout")
        self.mp_min: Uint16Field = Uint16Field("mp_min", 10, 1, Mode.R, units="msecs", description="Map packet minimum time")
        self.mp_max: Uint16Field = Uint16Field("mp_max", 11, 1, Mode.R, units="msecs", description="Map packet maximum time")
        self.mp_ave: Uint16Field = Uint16Field("mp_ave", 12, 1, Mode.R, units="msecs", description="Map packet average time")
        self.mp_attempts: Uint16Field = Uint16Field("mp_attempts", 13, 1, Mode.R, description="Map packet number of attempts")
        self.mp_errors: Uint16Field = Uint16Field("mp_errors", 14, 1, Mode.R, description="Map packet error returned from server count")
        self.mp_timeouts: Uint16Field = Uint16Field("mp_timeouts", 15, 1, Mode.R, description="Map packet timeout from server count")
        self.mp_packet_timeout: Uint16Field = Uint16Field("mp_packet_timeout", 16, 1, Mode.R, units="secs", description="Map packet current gateway timeout")
        self.cu_min: Uint16Field = Uint16Field("cu_min", 17, 1, Mode.R, units="msecs", description="Config packet minimum time")
        self.cu_max: Uint16Field = Uint16Field("cu_max", 18, 1, Mode.R, units="msecs", description="Config packet maximum time")
        self.cu_ave: Uint16Field = Uint16Field("cu_ave", 19, 1, Mode.R, units="msecs", description="Config packet average time")
        self.cu_attempts: Uint16Field = Uint16Field("cu_attempts", 20, 1, Mode.R, description="Config packet number of attempts")
        self.cu_errors: Uint16Field = Uint16Field("cu_errors", 21, 1, Mode.R, description="Config packet error returned from server count")
        self.cu_timeouts: Uint16Field = Uint16Field("cu_timeouts", 22, 1, Mode.R, description="Config packet timeout from server count")
        self.cu_packet_timeout: Uint16Field = Uint16Field("cu_packet_timeout", 23, 1, Mode.R, units="secs", description="Config packet current gateway timeout")
        self.su_min: Uint16Field = Uint16Field("su_min", 24, 1, Mode.R, units="msecs", description="Status packet minimum time")
        self.su_max: Uint16Field = Uint16Field("su_max", 25, 1, Mode.R, units="msecs", description="Status packet maximum time")
        self.su_ave: Uint16Field = Uint16Field("su_ave", 26, 1, Mode.R, units="msecs", description="Status packet average time")
        self.su_attempts: Uint16Field = Uint16Field("su_attempts", 27, 1, Mode.R, description="Status packet number of attempts")
        self.su_errors: Uint16Field = Uint16Field("su_errors", 28, 1, Mode.R, description="Status packet error returned from server count")
        self.su_timeouts: Uint16Field = Uint16Field("su_timeouts", 29, 1, Mode.R, description="Status packet timeout from server count")
        self.su_packet_timeout: Uint16Field = Uint16Field("su_packet_timeout", 30, 1, Mode.R, units="secs", description="Status packet current gateway timeout")
        self.pg_min: Uint16Field = Uint16Field("pg_min", 31, 1, Mode.R, units="msecs", description="Ping packet minimum time")
        self.pg_max: Uint16Field = Uint16Field("pg_max", 32, 1, Mode.R, units="msecs", description="Ping packet maximum time")
        self.pg_ave: Uint16Field = Uint16Field("pg_ave", 33, 1, Mode.R, units="msecs", description="Ping packet average time")
        self.pg_attempts: Uint16Field = Uint16Field("pg_attempts", 34, 1, Mode.R, description="Ping packet number of attempts")
        self.pg_errors: Uint16Field = Uint16Field("pg_errors", 35, 1, Mode.R, description="Ping packet error returned from server count")
        self.pg_timeouts: Uint16Field = Uint16Field("pg_timeouts", 36, 1, Mode.R, description="Ping packet timeout from server count")
        self.pg_packet_timeout: Uint16Field = Uint16Field("pg_packet_timeout", 37, 1, Mode.R, units="secs", description="Ping packet current gateway timeout")
        self.mb_min: Uint16Field = Uint16Field("mb_min", 38, 1, Mode.R, units="msecs", description="Modbus packet minimum time")
        self.mb_max: Uint16Field = Uint16Field("mb_max", 39, 1, Mode.R, units="msecs", description="Modbus packet maximum time")
        self.mb_ave: Uint16Field = Uint16Field("mb_ave", 40, 1, Mode.R, units="msecs", description="Modbus packet average time")
        self.mb_attempts: Uint16Field = Uint16Field("mb_attempts", 41, 1, Mode.R, description="Modbus packet number of attempts")
        self.mb_errors: Uint16Field = Uint16Field("mb_errors", 42, 1, Mode.R, description="Modbus packet error returned from server count")
        self.mb_timeouts: Uint16Field = Uint16Field("mb_timeouts", 43, 1, Mode.R, description="Modbus packet timeout from server count")
        self.mb_packet_timeout: Uint16Field = Uint16Field("mb_packet_timeout", 44, 1, Mode.R, units="secs", description="Modbus packet current gateway timeout")
        self.fu_min: Uint16Field = Uint16Field("fu_min", 45, 1, Mode.R, units="msecs", description="File IO packet minimum time")
        self.fu_max: Uint16Field = Uint16Field("fu_max", 46, 1, Mode.R, units="msecs", description="File IO packet maximum time")
        self.fu_ave: Uint16Field = Uint16Field("fu_ave", 47, 1, Mode.R, units="msecs", description="File IO packet average time")
        self.fu_attempts: Uint16Field = Uint16Field("fu_attempts", 48, 1, Mode.R, description="File IO packet number of attempts")
        self.fu_errors: Uint16Field = Uint16Field("fu_errors", 49, 1, Mode.R, description="File IO packet error returned from server count")
        self.fu_timeouts: Uint16Field = Uint16Field("fu_timeouts", 50, 1, Mode.R, description="File IO packet timeout from server count")
        self.fu_packet_timeout: Uint16Field = Uint16Field("fu_packet_timeout", 51, 1, Mode.R, units="secs", description="File IO packet current gateway timeout")
        self.ev_min: Uint16Field = Uint16Field("ev_min", 52, 1, Mode.R, units="msecs", description="Event packet minimum time")
        self.ev_max: Uint16Field = Uint16Field("ev_max", 53, 1, Mode.R, units="msecs", description="Event packet maximum time")
        self.ev_ave: Uint16Field = Uint16Field("ev_ave", 54, 1, Mode.R, units="msecs", description="Event packet average time")
        self.ev_attempts: Uint16Field = Uint16Field("ev_attempts", 55, 1, Mode.R, description="Event packet number of attempts")
        self.ev_errors: Uint16Field = Uint16Field("ev_errors", 56, 1, Mode.R, description="Event packet error returned from server count")
        self.ev_timeouts: Uint16Field = Uint16Field("ev_timeouts", 57, 1, Mode.R, description="Event packet timeout from server count")
        self.ev_packet_timeout: Uint16Field = Uint16Field("ev_packet_timeout", 58, 1, Mode.R, units="secs", description="Event packet current gateway timeout")


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
