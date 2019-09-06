from pymodbus.client.sync import ModbusTcpClient as ModbusClient

from mate3.structures import SingleInverterBlock, ChargeControllerBlock, FlexnetDcBlock
from mate3.io import decode_int16


def parse_single_inverter_block(client: ModbusClient, reg: int):
    response = client.read_holding_registers(reg + 2, 1)
    port = int(response.registers[0])

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
        port=port,
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
    response = client.read_holding_registers(reg + 2, 1)
    port = int(response.registers[0])

    response = client.read_holding_registers(reg + 8, 1)
    battery_voltage = int(response.registers[0]) * 0.1

    response = client.read_holding_registers(reg + 9, 1)
    array_voltage = int(response.registers[0]) * 0.1

    response = client.read_holding_registers(reg + 10, 1)
    battery_current = int(response.registers[0])

    response = client.read_holding_registers(reg + 11, 1)
    array_current = int(response.registers[0])

    response = client.read_holding_registers(reg + 12, 1)
    charger_state = int(response.registers[0])

    return ChargeControllerBlock(
        port=port,
        battery_voltage=battery_voltage,
        array_voltage=array_voltage,
        battery_current=battery_current,
        array_current=array_current,
        charger_state=charger_state,
    )


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
