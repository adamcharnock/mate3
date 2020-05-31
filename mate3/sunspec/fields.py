import socket
import struct
from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional


class Mode(Enum):
    R = "r"
    W = "w"
    RW = "rw"


class BitfieldDescriptionMixin:
    def __new__(cls, value, description):
        obj = super().__new__(cls, value)  # , description)
        obj._value_ = value
        obj._description = description
        return obj

    @property
    def description(self):
        if self.name is not None:
            return self._description
        return f"Combination of flags: {self.set_flags()}"

    def set_flags(self):
        flags = []
        for flag in self.__class__:
            if flag.value & self.value == flag.value:
                flags.append(flag)
        return flags


@dataclass
class Field:
    """
    Not a register - a specific field we care about (regardless of how it's split across registers etc.)
    """

    # TODO: abcmetaclass to ensure _to_registers and _from_registers are implemented

    start: int
    size: int
    mode: Mode
    description: Optional[str]

    @property
    def end(self):
        return self.start + self.size

    def from_registers(self, registers):
        if self.mode == Mode.W:
            raise RuntimeError("Can't read from a write-only field!")
        if not all(isinstance(i, int) for i in registers):
            raise ValueError("Registers should be an iterable of ints!")
        if len(registers) != self.size:
            raise ValueError(f"Expected {self.size} registers!")
        return self._from_registers(registers)

    def to_registers(self, value):
        if self.mode == Mode.R:
            raise RuntimeError("Can't write to a read-only field!")
        registers = self._to_registers(value)
        if len(registers) != self.size:
            raise ValueError(f"Expected {self.size} registers!")
        return registers


@dataclass
class IntegerField(Field):
    units: Optional[str] = None
    scale_factor: Optional[Field] = None  # TODO: should be IntegerField ...
    # TODO: add a check that the size is right for the field type?


@dataclass(frozen=False)
class Uint16Field(IntegerField):
    def _from_registers(self, registers):
        val = registers[0]
        if val == 0xFFFF:
            # as per sunspec, this is "not implemented" TODO before after cconversion?
            return False, None
        return True, val

    def _to_registers(self, value):
        if not isinstance(value, int):
            raise ValueError("Expected an integer!")
        if value < 0 or value > 0xFFFF - 1:
            raise ValueError("int16 must be between 0 and 0xffff - 1")
        return (value,)


@dataclass
class Int16Field(IntegerField):
    def _from_registers(self, registers):
        # signed_value = registers[0]
        # TODO
        # Outback has some bugs in their firmware it seems. The FlexNet DC Shunt current measurements
        # return an offset from 65535 for negative values. No reading should ever be higher then 2000. So use that
        # if signed_value > 32768 + 2000:
        #    return signed_value - 65535
        # elif signed_value >= 32768:
        #    return int(32768 - signed_value)
        # else:
        #    return signed_value
        val = registers[0]
        if val == 0x8000:
            # as per sunspec, this is "not implemented" TODO before after cconversion?
            return False, None
        # two's complement:
        bits = 16
        if (val & (1 << (bits - 1))) != 0:  # if sign bit is set e.g., 8bit: 128-255
            val = val - (1 << bits)  # compute negative value
        return True, val

    def _to_registers(self, value):
        if not isinstance(value, int):
            raise ValueError("Expected an integer!")
        if value < -0x7FFF or value > 0x7FFF:
            raise ValueError("int16 must be between -+0x7fff")
        return (value,)


@dataclass
class Uint32Field(IntegerField):
    def _from_registers(self, registers):
        val = (registers[0] << 16) | registers[1]
        if val == 0xFFFFFFFF:
            # as per sunspec, this is "not implemented" TODO before after cconversion?
            return False, None
        return True, val

    def _to_registers(self, value):
        if not isinstance(value, int):
            raise ValueError("Expected an integer!")
        if value < 0 or value > 0xFFFFFFFF - 1:
            raise ValueError("int16 must be between 0 and 0xffffffff-1")
        return (value >> 16, value & 0xFFFF)


@dataclass
class Int32Field(IntegerField):
    def _from_registers(self, registers):
        val = (registers[0] << 16) | registers[1]
        if val == 0x80000000:
            # as per sunspec, this is "not implemented" TODO before after cconversion?
            return False, None
        return True, val

    def _to_registers(self, value):
        if not isinstance(value, int):
            raise ValueError("Expected an integer!")
        if value < -0x7FFFFFFF or value > 0x7FFFFFFF:
            raise ValueError("int16 must be between -+0x7fffffff")
        return (value >> 16, value & 0xFFFF)


@dataclass
class StringField(Field):
    def _from_registers(self, registers):
        # as per sunspec, if all registers are 0, the not implemented:
        if all(i == 0 for i in registers):
            return False, None
        int8s = []
        for i in registers:
            int8s.append(i >> 8)
            int8s.append(i & 255)
        chars = map(chr, int8s)
        return True, "".join(chars).strip("\0")

    def _to_registers(self, value):
        if not isinstance(value, str):
            raise ValueError("Expected str!")
        if len(value) != self.size * 2:
            raise ValueError(f"String must be of size {self.size * 2}")
        int8s = [ord(i) for i in value]
        int16s = []
        for i in range(self.size):
            int16s.append((int8s[i] << 8) & int8s[i + 1])
        return tuple(int16s)


class BitfieldMixin:
    """
    This would have been simpler if they were normal on/off flags, however Outback has specified different meaning to
    "on" and "off", unfortunately.
    """

    def _get_flags(self, value, mx, not_implemented):

        # TODO: as per spec ... "if the most significant bit in a bitfield is set, all other bits shall be ignored"
        if value == not_implemented:
            # as per sunspec, this is "not implemented" TODO before after cconversion?
            return False, None
        elif value < 0 or value > mx:
            raise ValueError(f"{self.__class__.__name__} should be between 0 and {mx}")
        return True, self.flags(value)

    def _set_flags(self, flags):
        raise NotImplementedError("Need to test this ...")
        if not isinstance(flags, self.flags):
            raise ValueError("Should be a flag of type {self.flags}")
        return flags.value


@dataclass
class Bit16Field(Uint16Field, BitfieldMixin):
    flags: Any = None  # TODO: made this default=None just to get rid of dataclass errors ... should be None

    def _from_registers(self, registers):
        implemented, value = super()._from_registers(registers)
        if not implemented:
            return False, None
        return self._get_flags(value, mx=0x7FFF, not_implemented=0xFFFF)

    def _to_registers(self, flags):
        value = self._set_flags(flags)
        return super()._to_registers(value)


@dataclass
class Bit32Field(Uint32Field, BitfieldMixin):
    """
    According to the spec this shouldn't exist. But Outback have created it anyway. We'll assume it's just mean to be
    a bit16 for now ...
    """

    flags: Any = None  # TODO: made this default=None just to get rid of dataclass errors ... should be None

    def _from_registers(self, registers):
        implemented, value = super()._from_registers(registers)
        if not implemented:
            return False, None
        return self._get_flags(value, mx=0x7FFF, not_implemented=0xFFFF)

    def _to_registers(self, flags):
        value = self._set_flags(flags)
        return super()._to_registers(value)


class EnumMixin:
    def _get_option(self, val):
        if val is None:
            return None
        return self.options(val)

    def _set_option(self, val):
        if not isinstance(val, self.options):
            raise ValueError(f"Expected {self.options}")
        return val.value


# TODO: remove duplication below ...


@dataclass
class EnumUint16Field(Uint16Field, EnumMixin):
    options: Any = None  # TODO enum? TODO: made this default = None to get rid of dataclass errors, but shouldn't be None

    def _from_registers(self, registers):
        implemented, val = super()._from_registers(registers)
        if not implemented:
            return False, None
        return True, self._get_option(val)

    def _to_registers(self, value):
        value = super()._set_option(value)
        return super()._to_registers(value)


@dataclass
class EnumInt16Field(Int16Field, EnumMixin):
    options: Any = None  # TODO: enum? TODO: made this default = None to get rid of dataclass errors, but shouldn't be None

    def _from_registers(self, registers):
        implemented, val = super()._from_registers(registers)
        if not implemented:
            return False, None
        return True, self._get_option(val)

    def _to_registers(self, value):
        value = super()._set_option(value)
        return super()._to_registers(value)


@dataclass
class EnumUint32Field(Uint32Field, EnumMixin):
    options: Any = None  # TODO enum? TODO: made this default = None to get rid of dataclass errors, but shouldn't be None

    def _from_registers(self, registers):
        implemented, val = super()._from_registers(registers)
        if not implemented:
            return False, None
        return True, self._get_option(val)

    def _to_registers(self, value):
        value = super()._set_option(value)
        return super()._to_registers(value)


@dataclass
class EnumInt32Field(Int32Field, EnumMixin):
    options: Any = None  # TODO enum? TODO: made this default = None to get rid of dataclass errors, but shouldn't be None

    def _from_registers(self, registers):
        implemented, val = super()._from_registers(registers)
        if not implemented:
            return False, None
        return True, self._get_option(val)

    def _to_registers(self, value):
        value = super()._set_option(value)
        return super()._to_registers(value)


@dataclass
class AddressField(Field):
    def _from_registers(self, registers):
        val = (registers[0] << 16) | registers[1]
        if val == 0:
            # as per spec, this isn't implemented
            return False, None
        return True, socket.inet_ntoa(struct.pack("!I", val))

    def _to_registers(self, value):
        raise NotImplementedError()
