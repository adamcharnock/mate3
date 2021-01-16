from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder

BYTEORDER = Endian.Big
WORDORDER = Endian.Big


def get_decoder(registers):
    return BinaryPayloadDecoder.fromRegisters(registers=registers, byteorder=BYTEORDER, wordorder=WORDORDER)


def get_encoder():
    return BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Big)
