#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import logging
import contextlib
import psycopg2.pool

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y%m%d %H:%M:%S')
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

    # print("int16 RAW: {!s}".format(signed_value))

    if signed_value > 32768+2000:
        return signed_value - 65535
    elif signed_value >= 32768:
        return int(32768 - signed_value)
    else:
        return signed_value


def get_common_block(basereg):
    """ Read and return the sunspec common information
    block.

    :returns: A dictionary of the common block information
    """
    length = 69
    response = client.read_holding_registers(basereg, length + 2)
    decoder = BinaryPayloadDecoder.fromRegisters(response.registers,
                                                 byteorder=Endian.Big,
                                                 wordorder=Endian.Big)

    return {
        'SunSpec_ID': decoder.decode_32bit_uint(),
        'SunSpec_DID': decoder.decode_16bit_uint(),
        'SunSpec_Length': decoder.decode_16bit_uint(),
        'Manufacturer': decoder.decode_string(size=32),
        'Model': decoder.decode_string(size=32),
        'Options': decoder.decode_string(size=16),
        'Version': decoder.decode_string(size=16),
        'SerialNumber': decoder.decode_string(size=32),
        'DeviceAddress': decoder.decode_16bit_uint(),
        'Next_DID': decoder.decode_16bit_uint(),
        'Next_DID_Length': decoder.decode_16bit_uint(),
    }


# Read SunSpec header
def getSunSpec(basereg):
    # Read two bytes from basereg, a SUNSPEC device will start with 0x53756e53
    # As 8bit ints they are 21365, 28243
    try:
        response = client.read_holding_registers(basereg, 2)
    except:
        return None

    if response.registers[0] == 21365 and response.registers[1] == 28243:
        logging.info(".. SunSpec device found. Reading Manufacturer info")
    else:
        return None

    # There is a 16 bit string at basereg + 4 that contains Manufacturer
    response = client.read_holding_registers(basereg + 4, 16)

    decoder = BinaryPayloadDecoder.fromRegisters(response.registers,
                                                 byteorder=Endian.Big,
                                                 wordorder=Endian.Big)
    manufacturer = decoder.decode_string(16)
    if b"OUTBACK_POWER" in manufacturer.upper():
        logging.info(".. Outback Power device found")
    else:
        logging.info(".. Not an Outback Power device. Detected " + manufacturer)
        return None

    try:
        register = client.read_holding_registers(basereg + 3)
    except:
        return None

    blocksize = int(register.registers[0])

    return blocksize


def getBlock(basereg):
    try:
        register = client.read_holding_registers(basereg)
    except:
        return None

    blockID = int(register.registers[0])

    # Peek at block style
    try:
        register = client.read_holding_registers(basereg + 1)
    except:
        return None

    blocksize = int(register.registers[0])
    blockname = None

    try:
        blockname = mate3_did[blockID]
    except:
        print
        "ERROR: Unknown device type with DID=" + str(blockID)

    return {"size": blocksize, "DID": blockname}


print
"------------------------------------------------"
print
" MATE3 ModBus Interface"
print
"------------------------------------------------"

mate3_ip = '192.168.1.246'
mate3_modbus = 502

sunspec_start_reg = 40000

# Define the dictionary mapping SUNSPEC DID's to Outback names
# Device IDs definitions = (DID)
# AXS_APP_NOTE.PDF from Outback website has the data
mate3_did = {
    64110: "Outback block", 64111: "Charge Controller Block", 64112: "Charge Controller Configuration block",
    64115: "Split Phase Radian Inverter Real Time Block", 64116: "Radian Inverter Configuration Block",
    64117: "Single Phase Radian Inverter Real Time Block", 64113: "FX Inverter Real Time Block",
    64114: "FX Inverter Configuration Block", 64119: "FLEXnet-DC Configuration Block",
    64118: "FLEXnet-DC Real Time Block",
    64120: "Outback System Control Block", 101: "SunSpec Inverter - Single Phase",
    102: "SunSpec Inverter - Split Phase",
    103: "SunSpec Inverter - Three Phase", 64255: "OpticsRE Statistics Block", 65535: "End of SunSpec"
}

# Try to build the mate3 MODBUS connection
logging.info("Building MATE3 MODBUS connection")
# Mate3 connection
try:
    client = ModbusClient(mate3_ip, mate3_modbus)
    logging.info(".. Make sure we are indeed connected to an Outback power system")
    reg = sunspec_start_reg
    size = getSunSpec(reg)

    if size is None:
        logging.info("We have failed to detect an Outback system. Exciting")
        exit()

except:
    client.close()
    logging.info(".. Failed to connect to MATE3. Enable SUNSPEC and check port. Exciting")
    raise
    exit()

logging.info(".. Connected OK to an Outback system")

# TEST TEST TEST
# print get_common_block(reg)

startReg = reg + size + 4

pool = psycopg2.pool.SimpleConnectionPool(minconn=1, maxconn=2, dbname="postgres", host="127.0.0.1", port=5432, user="postgres", password="password")


@contextlib.contextmanager
def get_db_connection():
    connection = pool.getconn()
    yield connection
    pool.putconn(connection)


# Interrogation loop
while True:
    reg = startReg
    for block in range(0, 30):
        # print "Getting data from Register=" + str(reg) + " last size was {size}")
        blockResult = getBlock(reg)

        if "Single Phase Radian Inverter Real Time Block" in blockResult['DID']:
            logging.info(".. Detected a Single Phase Radian Inverter Real Time Block")
            response = client.read_holding_registers(reg + 2, 1)
            gs_single_inverter_port = int(response.registers[0])
            logging.info(f".... Connected on HUB port {gs_single_inverter_port}")

            # Inverter Output current
            response = client.read_holding_registers(reg + 7, 1)
            gs_single_inverter_output_current = int(response.registers[0])
            logging.info(f".... Inverted output current (A) {gs_single_inverter_output_current}")

            response = client.read_holding_registers(reg + 8, 1)
            gs_single_inverter_charge_current = int(response.registers[0])
            logging.info(f".... Charger current (A) {gs_single_inverter_charge_current}")

            response = client.read_holding_registers(reg + 9, 1)
            gs_single_inverter_buy_current = int(response.registers[0])
            logging.info(f".... Input current (A) {gs_single_inverter_buy_current}")

            response = client.read_holding_registers(reg + 13, 1)
            gs_single_output_ac_voltage = int(response.registers[0])
            logging.info(f".... Voltage Out (V) {gs_single_output_ac_voltage}")

            response = client.read_holding_registers(reg + 14, 1)
            gs_single_inverter_operating_mode = int(response.registers[0])
            logging.info(f".... Inverter Operating Mode {gs_single_inverter_operating_mode}")

            response = client.read_holding_registers(reg + 17, 1)
            gs_single_battery_voltage = int(response.registers[0]) * 0.1
            logging.info(f".... Battery voltage (V) {gs_single_battery_voltage}")

            response = client.read_holding_registers(reg + 18, 1)
            gs_single_temp_compensated_target_voltage = int(response.registers[0]) * 0.1
            logging.info(f".... Battery target voltage - temp compensated (V) {gs_single_temp_compensated_target_voltage}")

            response = client.read_holding_registers(reg + 27, 1)
            gs_single_battery_temperature = decode_int16(int(response.registers[0]))
            logging.info(f".... Battery temperature (V) {gs_single_battery_temperature}")

            response = client.read_holding_registers(reg + 30, 1)
            gs_single_ac_input_voltage = int(response.registers[0])
            logging.info(f".... AC Input Voltage {gs_single_ac_input_voltage}")

            response = client.read_holding_registers(reg + 31, 1)
            gs_single_ac_input_state = int(response.registers[0])
            logging.info(f".... AC USE (Y/N) {gs_single_ac_input_state}")

        if "Charge Controller Block" in blockResult['DID']:
            logging.info(".. Detected a Charge Controller Block")

            response = client.read_holding_registers(reg + 2, 1)
            cc_batt_port = int(response.registers[0])
            logging.info(f".... Connected on HUB port {cc_batt_port}")

            response = client.read_holding_registers(reg + 8, 1)
            cc_batt_voltage = int(response.registers[0]) * 0.1
            logging.info(f".... CC Battery Voltage (V) {cc_batt_voltage}")

            response = client.read_holding_registers(reg + 9, 1)
            cc_array_voltage = int(response.registers[0]) * 0.1
            logging.info(f".... CC Array Voltage {cc_array_voltage}")

            response = client.read_holding_registers(reg + 10, 1)
            cc_batt_current = int(response.registers[0])
            logging.info(f".... CC Battery Current (A) {cc_batt_current}")

            response = client.read_holding_registers(reg + 11, 1)
            cc_array_current = int(response.registers[0])
            logging.info(f".... CC Array Current (A) {cc_array_current}")

            response = client.read_holding_registers(reg + 12, 1)
            cc_charger_state = int(response.registers[0])
            logging.info(f".... CC Charger State {cc_charger_state}")  # 0=Silent,1=Float,2=Bulk,3=Absorb,4=EQ

        if "FLEXnet-DC Real Time Block" in blockResult['DID']:
            logging.info(".. Detect a FLEXnet-DC Real Time Block")

            response = client.read_holding_registers(reg + 2, 1)
            fn_shunt_a_port = int(response.registers[0])
            logging.info(f".... Connected on HUB port {fn_shunt_a_port}")

            response = client.read_holding_registers(reg + 8, 1)
            fn_shunt_a_current = decode_int16(int(response.registers[0])) * 0.1
            logging.info(f".... FN Shunt A Current (A) {fn_shunt_a_current}")

            response = client.read_holding_registers(reg + 9, 1)
            fn_shunt_b_current = decode_int16(int(response.registers[0])) * 0.1
            logging.info(f".... FN Shunt B Current (A) {fn_shunt_b_current}")

            response = client.read_holding_registers(reg + 10, 1)
            fn_shunt_c_current = decode_int16(int(response.registers[0])) * 0.1
            logging.info(f".... FN Shunt C Current (A) {fn_shunt_c_current}")

            response = client.read_holding_registers(reg + 11, 1)
            fn_battery_voltage = int(response.registers[0]) * 0.1
            logging.info(f".... FN Battery Voltage {fn_battery_voltage}")

            response = client.read_holding_registers(reg + 13, 1)
            fn_battery_temperature = decode_int16(int(response.registers[0]))
            logging.info(f".... FN Battery Temperature {fn_battery_temperature}")

            response = client.read_holding_registers(reg + 27, 1)
            fn_state_of_charge = int(response.registers[0])
            logging.info(f".... FN State of Charge {fn_state_of_charge}")

        if "End of SunSpec" not in blockResult['DID']:
            reg = reg + blockResult['size'] + 2
        else:
            break

    time.sleep(3)
