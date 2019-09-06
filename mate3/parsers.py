from enum import Enum
from functools import lru_cache
from typing import NewType, NamedTuple, Type, Union, Dict

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

from mate3.structures import SingleInverterBlock, ChargeControllerBlock, FlexnetDcBlock
from mate3.io import decode_int16


class Mode(Enum):
    R = "r"
    W = "w"
    RW = "rw"


R = Mode.R
W = Mode.W
RW = Mode.RW

uint16 = NewType("uint16", int)
int16 = NewType("int16", int)


class Field(NamedTuple):
    start: int
    size: int
    mode: Mode
    type: Type
    units: str
    description: str
    scale_factor: Union[None, str, float] = None


class BaseParser(object):

    structure = None

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


class ChargeControllerParser(BaseParser):
    did = Field(
        start=1,
        size=1,
        mode=R,
        type=uint16,
        units="N/A",
        description="Uniquely identifies this as a SunSpec Basic Charge Controller",
    )
    length = Field(
        start=2,
        size=1,
        mode=R,
        type=uint16,
        units="Registers",
        description="Length of block in 16-bit registers",
    )
    port_number = Field(
        start=3,
        size=1,
        mode=R,
        type=uint16,
        units="N/A",
        description="Port number on Outback network",
    )
    voltage_sf = Field(
        start=4,
        size=1,
        mode=R,
        type=int16,
        units="N/A",
        description="DC Voltage Scale Factor",
    )
    current_sf = Field(
        start=5,
        size=1,
        mode=R,
        type=int16,
        units="N/A",
        description="DC Current Scale Factor",
    )
    power_sf = Field(
        start=6,
        size=1,
        mode=R,
        type=int16,
        units="N/A",
        description="DC Power Scale Factor",
    )
    ah_sf = Field(
        start=7,
        size=1,
        mode=R,
        type=int16,
        units="N/A",
        description="DC Amp Hours Scale Factor",
    )
    kwh_sf = Field(
        start=8,
        size=1,
        mode=R,
        type=int16,
        units="N/A",
        description="DC kWH Scale Factor",
    )
    batt_voltage = Field(
        start=9,
        size=1,
        mode=R,
        type=uint16,
        units="Volts",
        scale_factor="voltage_sf",
        description="Battery Voltage",
    )
    array_voltage = Field(
        start=10,
        size=1,
        mode=R,
        type=uint16,
        units="Volts",
        scale_factor="voltage_sf",
        description="DC Source Voltage",
    )
    batt_current = Field(
        start=11,
        size=1,
        mode=R,
        type=uint16,
        units="Amps",
        scale_factor="current_sf",
        description="Battery Current",
    )
    array_current = Field(
        start=12,
        size=1,
        mode=R,
        type=uint16,
        units="Amps",
        scale_factor="power_sf",
        description="DC Source Current",
    )
    charger_state = Field(
        start=13,
        size=1,
        mode=R,
        type=uint16,
        units="Enumerated",
        description="0 = Silent; 1 = Float; 2 = Bulk; 3 = Absorb; 4 = EQ",
    )
    watts = Field(
        start=14,
        size=1,
        mode=R,
        type=uint16,
        units="Watts",
        scale_factor="power_sf",
        description="CC Wattage Output",
    )
    todays_min_battery_volts = Field(
        start=15,
        size=1,
        mode=R,
        type=uint16,
        units="Volts",
        scale_factor="voltage_sf",
        description="Minimum Voltage for battery today",
    )
    todays_max_battery_volts = Field(
        start=16,
        size=1,
        mode=R,
        type=uint16,
        units="Volts",
        scale_factor="voltage_sf",
        description="Maximum Voltage for battery today",
    )
    voc = Field(
        start=17,
        size=1,
        mode=R,
        type=uint16,
        units="Volts",
        scale_factor="voltage_sf",
        description="Last Open Circuit Voltage (array)",
    )
    todays_peak_voc = Field(
        start=18,
        size=1,
        mode=R,
        type=uint16,
        units="Volts",
        description="Highest VOC today",
    )
    todays_kwh = Field(
        start=19,
        size=1,
        mode=R,
        type=uint16,
        units="KWH",
        scale_factor="kwh_sf",
        description="Daily accumulated Kwatt hours output",
    )
    todays_ah = Field(
        start=20,
        size=1,
        mode=R,
        type=uint16,
        units="AH",
        scale_factor="ah_sf",
        description="Daily accumulated amp hours output",
    )
    lifetime_kwh_hours = Field(
        start=21,
        size=1,
        mode=R,
        type=uint16,
        units="KWH",
        description="Lifetime Total Kwatt Hours",
    )
    lifetime_kamp_hours = Field(
        start=22,
        size=1,
        mode=R,
        type=uint16,
        units="Amps",
        scale_factor="kwh_sf",
        description="Lifetime Total K-Amp Hours",
    )
    lifetime_max_watts = Field(
        start=23,
        size=1,
        mode=R,
        type=uint16,
        units="Watts",
        scale_factor="power_sf",
        description="Lifetime Maximum Wattage",
    )
    lifetime_max_battery_volts = Field(
        start=24,
        size=1,
        mode=R,
        type=uint16,
        units="Volts",
        scale_factor="voltage_sf",
        description="Lifetime Maximum Battery Voltage",
    )
    lifetime_max_voc = Field(
        start=25,
        size=1,
        mode=R,
        type=uint16,
        units="Volts",
        scale_factor="voltage_sf",
        description="Lifetime Maximum VOC",
    )
    temp_sf = Field(
        start=26,
        size=1,
        mode=R,
        type=uint16,
        units="N/A",
        description="FM80 Extreme Temperature scale factor",
    )
    temp_output_fets = Field(
        start=27,
        size=1,
        mode=R,
        type=int16,
        units="Degrees C",
        scale_factor="power_sf",
        description="FM80 Extreme Output FET Temperature",
    )
    temp_enclosure = Field(
        start=28,
        size=1,
        mode=R,
        type=int16,
        units="Degrees C",
        scale_factor="power_sf",
        description="FM80 Extreme Enclosure Temperature",
    )

    structure = ChargeControllerBlock


def parse_single_inverter_block(client: ModbusClient, reg: int):
    response = client.read_holding_registers(reg + 2, 1)
    port_number = int(response.registers[0])

    # Inverter Output current
    response = client.read_holding_registers(reg + 7, 1)
    output_current = int(response.registers[0])

    response = client.read_holding_registers(reg + 8, 1)
    charge_current = int(response.registers[0])

    response = client.read_holding_registers(reg + 9, 1)
    buy_current = int(response.registers[0])

    response = client.read_holding_registers(reg + 13, 1)
    output_ac_voltage = int(response.registers[0])

    response = client.read_holding_registers(reg + 14, 1)
    operating_mode = int(response.registers[0])

    response = client.read_holding_registers(reg + 17, 1)
    battery_voltage = int(response.registers[0]) * 0.1

    response = client.read_holding_registers(reg + 18, 1)
    temp_compensated_target_voltage = int(response.registers[0]) * 0.1

    response = client.read_holding_registers(reg + 27, 1)
    battery_temperature = decode_int16(int(response.registers[0]))

    response = client.read_holding_registers(reg + 30, 1)
    ac_input_voltage = int(response.registers[0])

    response = client.read_holding_registers(reg + 31, 1)
    ac_input_state = int(response.registers[0])

    return SingleInverterBlock(
        port_number=port_number,
        output_current=output_current,
        charge_current=charge_current,
        buy_current=buy_current,
        output_ac_voltage=output_ac_voltage,
        operating_mode=operating_mode,
        battery_voltage=battery_voltage,
        temp_compensated_target_voltage=temp_compensated_target_voltage,
        battery_temperature=battery_temperature,
        ac_input_voltage=ac_input_voltage,
        ac_input_state=ac_input_state,
    )


def parse_charge_controller_block(client: ModbusClient, reg: int):
    return ChargeControllerParser().parse(client, reg)


def parse_flexnet_dc_block(client: ModbusClient, reg: int):
    response = client.read_holding_registers(reg + 2, 1)
    shunt_a_port = int(response.registers[0])

    response = client.read_holding_registers(reg + 8, 1)
    shunt_a_current = decode_int16(int(response.registers[0])) * 0.1

    response = client.read_holding_registers(reg + 9, 1)
    shunt_b_current = decode_int16(int(response.registers[0])) * 0.1

    response = client.read_holding_registers(reg + 10, 1)
    shunt_c_current = decode_int16(int(response.registers[0])) * 0.1

    response = client.read_holding_registers(reg + 11, 1)
    battery_voltage = int(response.registers[0]) * 0.1

    response = client.read_holding_registers(reg + 13, 1)
    battery_temperature = decode_int16(int(response.registers[0]))

    response = client.read_holding_registers(reg + 27, 1)
    state_of_charge = int(response.registers[0])

    return FlexnetDcBlock(
        shunt_a_port=shunt_a_port,
        shunt_a_current=shunt_a_current,
        shunt_b_current=shunt_b_current,
        shunt_c_current=shunt_c_current,
        battery_voltage=battery_voltage,
        battery_temperature=battery_temperature,
        state_of_charge=state_of_charge,
    )
