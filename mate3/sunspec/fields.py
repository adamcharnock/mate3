import dataclasses as dc
import socket
import struct
from abc import ABCMeta, abstractmethod
from enum import Enum, IntFlag
from typing import Optional


class Mode(Enum):
    R = "r"
    W = "w"
    RW = "rw"


@dc.dataclass
class Field(metaclass=ABCMeta):
    """
    A Field is a representation of a field on a SunSpec model, with nice utilities such as converting to/from the
    underlying registers.
    """

    name: str
    start: int
    size: int
    mode: Mode
    description: Optional[str] = None

    @property
    def end(self):
        return self.start + self.size

    def from_registers(self, registers):
        """
        Decode registers into the actual value.
        """
        if self.mode not in (Mode.R, Mode.RW):
            raise RuntimeError("Can't read from a write-only field!")
        if not all(isinstance(i, int) for i in registers):
            raise ValueError("Registers should be an iterable of ints!")
        if len(registers) != self.size:
            raise ValueError(f"Expected {self.size} registers!")
        return self._from_registers(registers)

    def to_registers(self, value):
        """
        Encode a value into registers.
        """
        if self.mode not in (Mode.W, Mode.RW):
            raise RuntimeError("Can't write to a read-only field!")
        registers = self._to_registers(value)
        if len(registers) != self.size:
            raise ValueError(f"Expected {self.size} registers!")
        return registers

    @abstractmethod
    def _from_registers(self, registers):
        """
        Method to override that actually does the conversion, sans checks.
        """
        pass

    @abstractmethod
    def _to_registers(self, value):
        """
        Method to override that actually does the conversion, sans checks.
        """
        pass


@dc.dataclass
class IntegerField(Field):
    """
    And IntegerField will have an integer value, and optionally has units and a scale factor.
    """

    units: Optional[str] = None
    scale_factor: Optional[Field] = None  # TODO: should be IntegerField but can't refer to itself in definition ...


@dc.dataclass
class Uint16Field(IntegerField):
    def _from_registers(self, registers):
        val = registers[0]
        if val == 0xFFFF:
            # As per sunspec, this is "not implemented"
            return False, None
        return True, val

    def _to_registers(self, value):
        if not isinstance(value, int):
            raise ValueError("Expected an integer!")
        if value < 0 or value > 0xFFFF - 1:
            raise ValueError("int16 must be between 0 and 0xffff - 1")
        return (value,)


@dc.dataclass
class Int16Field(IntegerField):
    def _from_registers(self, registers):
        val = registers[0]
        if val == 0x8000:
            # As per sunspec, this is "not implemented"
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


@dc.dataclass
class Uint32Field(IntegerField):
    def _from_registers(self, registers):
        val = (registers[0] << 16) | registers[1]
        if val == 0xFFFFFFFF:
            # As per sunspec, this is "not implemented"
            return False, None
        return True, val

    def _to_registers(self, value):
        if not isinstance(value, int):
            raise ValueError("Expected an integer!")
        if value < 0 or value > 0xFFFFFFFF - 1:
            raise ValueError("int16 must be between 0 and 0xffffffff-1")
        return (value >> 16, value & 0xFFFF)


@dc.dataclass
class StringField(Field):
    def _from_registers(self, registers):
        # As per sunspec, if all registers are 0, the not implemented:
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
            # As per sunspec, this is "not implemented"
            return False, None
        elif value < 0 or value > mx:
            raise ValueError(f"{self.__class__.__name__} should be between 0 and {mx}")
        return True, self.flags(value)

    def _set_flags(self, flags):
        raise NotImplementedError("Need to test this ...")
        if not isinstance(flags, self.flags):
            raise ValueError("Should be a flag of type {self.flags}")
        return flags.value


@dc.dataclass
class Bit16Field(BitfieldMixin, Uint16Field):
    """
    The actual IntFlags are in the flags attr, and this is a basic wrapper that e.g. checks the value is implemented
    before using the flags, etc.
    """

    flags: IntFlag = None  # None isn't possible - just need it for dataclass since there are defaults already defined

    def _from_registers(self, registers):
        implemented, value = super()._from_registers(registers)
        if not implemented:
            return False, None
        return self._get_flags(value, mx=0x7FFF, not_implemented=0xFFFF)

    def _to_registers(self, flags):
        value = self._set_flags(flags)
        return super()._to_registers(value)


@dc.dataclass
class Bit32Field(BitfieldMixin, Uint32Field):
    """
    The actual IntFlags are in the flags attr, and this is a basic wrapper that e.g. checks the value is implemented
    before using the flags, etc.
    
    NB: According to the spec this shouldn't exist. But Outback have created it anyway. We'll assume it's just meant to
    be a bit16 for now ...
    """

    flags: IntFlag = None  # None isn't possible - just need it for dataclass since there are defaults already defined

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

    def _from_registers(self, registers):
        implemented, val = super()._from_registers(registers)
        if not implemented:
            return False, None
        return True, self._get_option(val)

    def _to_registers(self, value):
        value = self._set_option(value)
        return super()._to_registers(value)


@dc.dataclass
class EnumUint16Field(EnumMixin, Uint16Field):
    options: Enum = None  # None isn't possible - just need it for dataclass since there are defaults defined in parents


@dc.dataclass
class EnumInt16Field(EnumMixin, Int16Field):
    options: Enum = None  # None isn't possible - just need it for dataclass since there are defaults defined in parents


@dc.dataclass
class AddressField(Field):
    def _from_registers(self, registers):
        val = (registers[0] << 16) | registers[1]
        if val == 0:
            # As per spec, this isn't implemented
            return False, None
        return True, socket.inet_ntoa(struct.pack("!I", val))

    def _to_registers(self, value):
        raise NotImplementedError()


class BitfieldDescriptionMixin:
    """
    A mixin that allows us to define something as

        @unique
        class MyFlags(BitfieldDescriptionMixin, IntFlag):
            a = 1, "a description"
            b = 2, "b description"

    Where each member now has a `.description` attribute (as opposed to just the usual name and value).
    """

    def __new__(cls, value, description):
        obj = super().__new__(cls, value)  # , description)
        obj._value_ = value
        obj._description = description
        return obj

    @property
    def description(self):
        if self.name is not None:
            return self._description
        return f"Combination of flags: {self.get_set_flags()}"

    def get_set_flags(self):
        """
        Convenience method to determine which flags are set, as a list. TODO: better name, this confusing!
        """
        flags = []
        for flag in self.__class__:
            if flag.value & self.value == flag.value:
                flags.append(flag)
        return flags
