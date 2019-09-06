import logging
from typing import Tuple, Optional

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

from mate3.structures import Device


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


def read_block(client: ModbusClient, basereg) -> Tuple[Optional[int], Optional[Device]]:
    register = client.read_holding_registers(basereg)
    device_id = register.registers[0]

    try:
        device = Device(device_id)
    except ValueError:
        logging.warning(f"Unknown device type with device ID {device_id}")
        return None, None

    # Peek at block size
    register = client.read_holding_registers(basereg + 1)
    block_size = int(register.registers[0])

    return block_size, device
