from abc import ABCMeta, abstractmethod
import socket
import struct
import dataclasses as dc
from datetime import datetime, timedelta
from enum import Enum, IntFlag
from typing import Any, Optional

from loguru import logger


class Mode(Enum):
    R = "r"
    W = "w"
    RW = "rw"


class BitfieldDescriptionMixin:
    """
    A mixim that allows us to define something as 
    
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
        Convenience method to determine which flags are set, as a list:
        """
        flags = []
        for flag in self.__class__:
            if flag.value & self.value == flag.value:
                flags.append(flag)
        return flags


@dc.dataclass
class Field(metaclass=ABCMeta):
    """
    Not a register - a specific field we care about (regardless of how it's split across registers etc.)
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
        if self.mode not in (Mode.R, Mode.RW):
            raise RuntimeError("Can't read from a write-only field!")
        if not all(isinstance(i, int) for i in registers):
            raise ValueError("Registers should be an iterable of ints!")
        if len(registers) != self.size:
            raise ValueError(f"Expected {self.size} registers!")
        return self._from_registers(registers)

    def to_registers(self, value):
        if self.mode not in (Mode.W, Mode.RW):
            raise RuntimeError("Can't write to a read-only field!")
        registers = self._to_registers(value)
        if len(registers) != self.size:
            raise ValueError(f"Expected {self.size} registers!")
        return registers

    @abstractmethod
    def _from_registers(self, registers):
        pass

    @abstractmethod
    def _to_registers(self, value):
        pass


@dc.dataclass
class IntegerField(Field):
    units: Optional[str] = None
    scale_factor: Optional[Field] = None  # TODO: should be IntegerField but can't refer to itself in definition ...


@dc.dataclass
class Uint16Field(IntegerField):
    def _from_registers(self, registers):
        val = registers[0]
        if val == 0xFFFF:
            # as per sunspec, this is "not implemented"
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
            # as per sunspec, this is "not implemented"
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
            # as per sunspec, this is "not implemented"
            return False, None
        return True, val

    def _to_registers(self, value):
        if not isinstance(value, int):
            raise ValueError("Expected an integer!")
        if value < 0 or value > 0xFFFFFFFF - 1:
            raise ValueError("int16 must be between 0 and 0xffffffff-1")
        return (value >> 16, value & 0xFFFF)


@dc.dataclass
class Int32Field(IntegerField):
    def _from_registers(self, registers):
        val = (registers[0] << 16) | registers[1]
        if val == 0x80000000:
            # as per sunspec, this is "not implemented"
            return False, None
        return True, val

    def _to_registers(self, value):
        if not isinstance(value, int):
            raise ValueError("Expected an integer!")
        if value < -0x7FFFFFFF or value > 0x7FFFFFFF:
            raise ValueError("int16 must be between -+0x7fffffff")
        return (value >> 16, value & 0xFFFF)


@dc.dataclass
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
            # as per sunspec, this is "not implemented"
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
class Bit16Field(Uint16Field, BitfieldMixin):
    """
    The actual IntFlags are in the flags attr, and this is a basic wrapper that e.g. checks the value is implemented
    before using the flags, etc.
    """

    flags: IntFlag = None  # None isn't possible - just need it for dataclass since there are defaults defined in parents

    def _from_registers(self, registers):
        implemented, value = super()._from_registers(registers)
        if not implemented:
            return False, None
        return self._get_flags(value, mx=0x7FFF, not_implemented=0xFFFF)

    def _to_registers(self, flags):
        value = self._set_flags(flags)
        return super()._to_registers(value)


@dc.dataclass
class Bit32Field(Uint32Field, BitfieldMixin):
    """
    The actual IntFlags are in the flags attr, and this is a basic wrapper that e.g. checks the value is implemented
    before using the flags, etc.
    
    NB: According to the spec this shouldn't exist. But Outback have created it anyway. We'll assume it's just meant to
    be a bit16 for now ...
    """

    flags: IntFlag = None  # None isn't possible - just need it for dataclass since there are defaults defined in parents

    def _from_registers(self, registers):
        implemented, value = super()._from_registers(registers)
        if not implemented:
            return False, None
        return self._get_flags(value, mx=0x7FFF, not_implemented=0xFFFF)

    def _to_registers(self, flags):
        value = self._set_flags(flags)
        return super()._to_registers(value)


@dc.dataclass
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
class EnumUint16Field(Uint16Field, EnumMixin):
    options: Enum = None  # None isn't possible - just need it for dataclass since there are defaults defined in parents


@dc.dataclass
class EnumInt16Field(Int16Field, EnumMixin):
    options: Enum = None  # None isn't possible - just need it for dataclass since there are defaults defined in parents


@dc.dataclass
class EnumUint32Field(Uint32Field, EnumMixin):
    options: Enum = None  # None isn't possible - just need it for dataclass since there are defaults defined in parents


@dc.dataclass
class EnumInt32Field(Int32Field, EnumMixin):
    options: Enum = None  # None isn't possible - just need it for dataclass since there are defaults defined in parents


@dc.dataclass
class AddressField(Field):
    def _from_registers(self, registers):
        val = (registers[0] << 16) | registers[1]
        if val == 0:
            # as per spec, this isn't implemented
            return False, None
        return True, socket.inet_ntoa(struct.pack("!I", val))

    def _to_registers(self, value):
        raise NotImplementedError()


class FieldValue:
    def __init__(self, field):
        self.field = field
        self._last_read = None
        self._dirty = False
        self._implemented = None
        self._value_to_write = None
        self._raw_value = None
        self._scale_factor = None
        self._scale_factor_cache_time = timedelta(seconds=60)

    @property
    def name(self):
        return self.field.name

    def __repr__(self):
        ss = [f"< {self.field.name}"]
        ss.append("impl" if self._implemented else "not impl")
        ss.append(f"read @ {self._last_read}")
        if self._scale_factor:
            ss.append(f"sf: {self._scale_factor}")
            ss.append(f"raw: {self._raw_value}")
        if self._implemented:
            ss.append(f"val: {self.value}")
            s = f"dirty (value to write: {self._value_to_write})" if self._dirty else "clean"
            s += " >"
            ss.append(s)
        return " | ".join(ss)

    @property
    def last_read(self):
        return self._last_read

    @property
    def dirty(self):
        return self._dirty

    @property
    def implemented(self):
        return self._implemented

    @property
    def _should_be_scaled(self):
        return isinstance(self.field, IntegerField) and self.field.scale_factor is not None

    @property
    def value(self):
        if self.field.mode not in (Mode.R, Mode.RW):
            raise RuntimeError("Can't read from this field!")
        if not self._implemented:
            return None
        if not self._should_be_scaled:
            return self._raw_value
        # scale it:
        value = self._raw_value * 10 ** self._scale_factor
        # round it to what it should be after scaling:
        return round(value, -self._scale_factor if self._scale_factor < 0 else 0)

    @value.setter
    def value(self, value):
        if self.field.mode not in (Mode.W, Mode.RW):
            raise RuntimeError("Can't write to this field!")
        if self._last_read is None:
            raise RuntimeError("You should read a field at least once before writing")
        if not self._implemented:
            raise RuntimeError("This field is marked as not implemented, so you shouldn't write to it!")
        if self._should_be_scaled:
            # Time limit on scale_factor being applicable?
            if (datetime.now() - self._last_read) > self._scale_factor_cache_time:
                raise ValueError(
                    (
                        f"You need to read this value within {self._scale_factor_cache_time} of writing to 'ensure'",
                        " the scale factor is up-to-date before you write.",
                    )
                )
            # scale it:
            value = value / 10 ** self._scale_factor
            # round it to what it should be after scaling:
            self._value_to_write = int(round(value, 0))
        else:
            self._value_to_write = value
        self._dirty = True

    def _update_on_read(self, value, implemented, read_time, scale_factor_read=None):
        """
        Assumption is that if there's a scale factor, it's read at the same time as value, so they should be in sync.
        Not really a major with Outback, as they seem to be constant anyway.
        """
        if self._should_be_scaled:
            if scale_factor_read is None:
                raise RuntimeError(f"scale_factor_read required for field {self.field}")
            if not scale_factor_read.implemented:
                raise RuntimeError(f"scale_factor_read should be implemented!")
            if (read_time - scale_factor_read.time).total_seconds() > 60:
                raise RuntimeError(
                    (
                        "The scale factor on this field was updated more than a minute since this field was. Scale "
                        "factors *shouldn't* change anyway, but there'd be problems if they did, so better safe than "
                        "sorry. However, you should never hit this error (as we try to ensure the scale factor is "
                        "always read when the field is - so if you see it, please file an issue."
                    )
                )
            scale_factor_read = scale_factor_read.value
            if not isinstance(scale_factor_read, int):
                raise RuntimeError(f"scale_factor should be an integer!")
            if scale_factor_read < -10 or scale_factor_read > 10:
                raise RuntimeError(f"scale_factor should be between -10 and 10")
        else:
            if scale_factor_read is not None:
                raise RuntimeError(f"No scale_factor should be provided for field {self.field}")

        self._raw_value = value
        self._scale_factor = scale_factor_read
        self._implemented = implemented
        self._last_read = read_time
        if self._value_to_write is not None:
            logger.warning(
                f"A value has been set to be written, but was re-read after this, so the write will be ignored "
            )
            self._value_to_write = None
        self._dirty = False


@dc.dataclass
class ModelFieldValues:
    _address: int = dc.field(metadata={"field": False})

    def __iter__(self):
        for field in dc.fields(self):
            if field.metadata.get("field", True):
                yield getattr(self, field.name)
