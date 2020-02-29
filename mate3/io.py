import logging
import socket
import struct
from typing import Tuple, Optional

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

from mate3.base_structures import Device

logger = logging.getLogger(__name__)

SUNSPEC_REGISTER_OFFSET = 40000


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


def combine_ints(ints):
    out = 0
    for i in ints:
        out = out << 16
        out |= i
    return out


def int16s_to_str(ints):
    int8s = []
    for i in ints:
        int8s.append(i >> 8)
        int8s.append(i & 255)
    chars = map(chr, int8s)
    return ''.join(chars).strip("\0")


def int_to_ip_address(int_ip_address: int):
    return socket.inet_ntoa(struct.pack("!I", int_ip_address))


def read_block_information(client: ModbusClient, block_starting_register) -> Tuple[Optional[int], Optional[Device]]:
    """Read information about the block at the given starting register

    This will return the block size, and the device the block represents.
    """
    response = client.read_holding_registers(block_starting_register, count=4)
    raise_modbus_exception(response)

    device_id = response.registers[0]

    try:
        device = Device(device_id)
    except ValueError:
        logger.warning(f"Unknown device type with device ID {device_id}")
        return None, None

    if device == Device.sunspec_header:
        block_size = int(response.registers[3]) + 2
    else:
        block_size = int(response.registers[1])

    return block_size, device


def raise_modbus_exception(response):
    if isinstance(response, Exception):
        raise response
