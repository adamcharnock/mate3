#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import logging
import contextlib
from typing import NamedTuple

import psycopg2.pool
import pymodbus.exceptions

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%Y%m%d %H:%M:%S"
)
logging.getLogger(__name__)


# Read SunSpec Header with logic from pymodbus example
def decode_int16(signed_value):
    """
    Negative numbers (INT16 = short)
      Some manufacturers allow negative values for some registers. Instead of an allowed integer range 0-65535,
      a range -32768 to 32767 is allowed. This is implemented as any received value in the upper range (32768-65535)
      is interpreted as negative value (in the range -32768 to -1).
      This is two’s complement and is described at http://en.wikipedia.org/wiki/Two%27s_complement.
      Help functions to calculate the two’s complement value (and back) are provided in MinimalModbus.
    """

    # Outback has some bugs in their firmware it seems. The FlexNet DC Shunt current measurements
    # return an offset from 65535 for negative values. No reading should ever be higher then 2000. So use that

    if signed_value > 32768 + 2000:
        return signed_value - 65535
    elif signed_value >= 32768:
        return int(32768 - signed_value)
    else:
        return signed_value


def get_common_block(client: ModbusClient, basereg):
    """ Read and return the sunspec common information
    block.

    :returns: A dictionary of the common block information
    """
    length = 69
    response = client.read_holding_registers(basereg, length + 2)
    decoder = BinaryPayloadDecoder.fromRegisters(
        response.registers, byteorder=Endian.Big, wordorder=Endian.Big
    )

    return {
        "SunSpec_ID": decoder.decode_32bit_uint(),
        "SunSpec_DID": decoder.decode_16bit_uint(),
        "SunSpec_Length": decoder.decode_16bit_uint(),
        "Manufacturer": decoder.decode_string(size=32),
        "Model": decoder.decode_string(size=32),
        "Options": decoder.decode_string(size=16),
        "Version": decoder.decode_string(size=16),
        "SerialNumber": decoder.decode_string(size=32),
        "DeviceAddress": decoder.decode_16bit_uint(),
        "Next_DID": decoder.decode_16bit_uint(),
        "Next_DID_Length": decoder.decode_16bit_uint(),
    }


def read_sun_spec_header(client: ModbusClient, basereg):
    # Read two bytes from basereg, a SUNSPEC device will start with 0x53756e53
    # As 8bit ints they are 21365, 28243

    response = client.read_holding_registers(basereg, 2)
    if response.registers[0] == 21365 and response.registers[1] == 28243:
        logging.info(".. SunSpec device found. Reading Manufacturer info")
    else:
        return None

    # There is a 16 bit string at basereg + 4 that contains Manufacturer
    response = client.read_holding_registers(basereg + 4, 16)

    decoder = BinaryPayloadDecoder.fromRegisters(
        response.registers, byteorder=Endian.Big, wordorder=Endian.Big
    )
    manufacturer = decoder.decode_string(16)
    if b"OUTBACK_POWER" in manufacturer.upper():
        logging.info(".. Outback Power device found")
    else:
        logging.info(".. Not an Outback Power device. Detected " + manufacturer)
        return None

    register = client.read_holding_registers(basereg + 3)
    block_size = int(register.registers[0])
    return block_size


def read_block(client: ModbusClient, basereg):
    try:
        register = client.read_holding_registers(basereg)
    except:
        raise

    block_id = int(register.registers[0])

    # Peek at block style
    register = client.read_holding_registers(basereg + 1)
    block_size = int(register.registers[0])
    block_name = None

    try:
        block_name = mate3_did[block_id]
    except:
        logging.warning(f"Unknown device type with DID={block_id}")

    return {"size": block_size, "DID": block_name}


mate3_ip = "192.168.1.246"
mate3_modbus_port = 502

sunspec_start_reg = 40000

# Define the dictionary mapping SUNSPEC DID's to Outback names
# Device IDs definitions = (DID)
# AXS_APP_NOTE.PDF from Outback website has the data
mate3_did = {
    64110: "Outback block",
    64111: "Charge Controller Block",
    64112: "Charge Controller Configuration block",
    64115: "Split Phase Radian Inverter Real Time Block",
    64116: "Radian Inverter Configuration Block",
    64117: "Single Phase Radian Inverter Real Time Block",
    64113: "FX Inverter Real Time Block",
    64114: "FX Inverter Configuration Block",
    64119: "FLEXnet-DC Configuration Block",
    64118: "FLEXnet-DC Real Time Block",
    64120: "Outback System Control Block",
    101: "SunSpec Inverter - Single Phase",
    102: "SunSpec Inverter - Split Phase",
    103: "SunSpec Inverter - Three Phase",
    64255: "OpticsRE Statistics Block",
    65535: "End of SunSpec",
}

# Try to build the mate3 MODBUS connection
logging.info("Building MATE3 MODBUS connection")
# Mate3 connection
try:
    _client = ModbusClient(mate3_ip, mate3_modbus_port)
    logging.info(".. Make sure we are indeed connected to an Outback power system")
    reg = sunspec_start_reg
    size = read_sun_spec_header(_client, reg)

    if size is None:
        logging.info("We have failed to detect an Outback system. Exciting")
        exit()

except:
    _client.close()
    logging.info(
        ".. Failed to connect to MATE3. Enable SUNSPEC and check port. Exciting"
    )
    raise
    exit()

logging.info(".. Connected OK to an Outback system")

startReg = reg + size + 4

pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=2,
    dbname="postgres",
    host="127.0.0.1",
    port=5432,
    user="postgres",
    password="password",
)


@contextlib.contextmanager
def get_db_connection():
    connection = pool.getconn()
    yield connection
    pool.putconn(connection)


class SingleInverterBlock(NamedTuple):
    port: int
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
    port: int
    battery_voltage: float
    array_voltage: float
    battery_current: float
    array_current: float
    charger_state: int


class FlexnetDcBlock(NamedTuple):
    shunt_a_port: int
    shunt_a_current: float
    shunt_b_current: float
    shunt_c_current: float
    battery_voltage: float
    battery_temperature: float
    state_of_charge: float


def parse_single_inverter_block(client):
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


def parse_charge_controller_block(client):
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


def parse_flexnet_dc_block(client):
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


# Interrogation loop
while True:
    reg = startReg
    for block in range(0, 30):
        blockResult = read_block(_client, reg)
        structure = None

        if "Single Phase Radian Inverter Real Time Block" in blockResult["DID"]:
            structure = parse_single_inverter_block(_client)

        if "Charge Controller Block" in blockResult["DID"]:
            structure = parse_charge_controller_block(_client)

        if "FLEXnet-DC Real Time Block" in blockResult["DID"]:
            structure = parse_flexnet_dc_block(_client)

        if structure:
            print(structure)

        if "End of SunSpec" not in blockResult["DID"]:
            reg = reg + blockResult["size"] + 2
        else:
            break

    time.sleep(3)
