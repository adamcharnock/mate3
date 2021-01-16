import dataclasses as dc
import socket
import struct
from abc import ABCMeta, abstractmethod
from datetime import datetime
from enum import Enum, IntFlag
from functools import wraps
from typing import Any, Optional, Tuple
from uuid import uuid4

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder


class Mode(Enum):
    R = "r"
    W = "w"
    RW = "rw"


@dc.dataclass
class FieldRead:
    address: int
    time: datetime
    registers: Tuple[int]
    guid: int = dc.field(default_factory=lambda: uuid4().int)


def has_been_read(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        if self._last_read is None:
            raise RuntimeError(f"{f} can only be called after field {self.name} has been read")
        return f(self, *args, **kwargs)

    return wrapper


class Field(metaclass=ABCMeta):
    def __init__(self, name: str, start: int, size: int, mode: Mode, description: Optional[str] = None):
        self.name = name
        self.start = start
        self.size = size
        self.mode = mode
        self.description = description

        # Internal state (all None until read)
        self._last_read: Optional[FieldRead] = None
        self._value = None
        self._implemented = None

    @property
    def end(self):
        return self.start + self.size

    @property
    def last_read(self):
        return self._last_read

    @last_read.setter
    def last_read(self, read: FieldRead):
        self._last_read = read

    @property
    @has_been_read
    def value(self):
        """
        OK, we get a bit clever here in that we only decode fields lazily. This is for two reasons - firstly, it can
        save decoding everything on the first run (when you're getting devices etc.) and secondly it resolves some
        inter-field dependency (e.g. to read a scaled field we first need to read the scale factor ... and you say we
        could do that, but reading sequential fields can be nicer for the mate3)
        """
        if self.mode not in (Mode.R, Mode.RW):
            raise RuntimeError("Can't read from this field!")
        if not self.implemented:
            return None
        decoder = BinaryPayloadDecoder.fromRegisters(
            registers=self._last_read.registers, byteorder=Endian.Big, wordorder=Endian.Big
        )

        return self.decode_from_registers(decoder)

    @abstractmethod
    def decode_from_registers(self, decoder: BinaryPayloadDecoder) -> Any:
        pass

    @abstractmethod
    def encode_to_payload(self, value: Any, encoder: BinaryPayloadBuilder):
        pass

    @property
    def implemented(self) -> bool:
        return self._implemented


class IntegerField(Field):
    """
    And IntegerField will have an integer value, and optionally has units and a scale factor.
    """

    def __init__(self, *args, units: Optional[str] = None, **kwargs):
        self.units = units
        super().__init__(*args, **kwargs)

    @property
    @abstractmethod
    def _modbus_decode_type(self) -> str:
        """
        Something like '8bit_int'
        """
        pass

    @property
    @abstractmethod
    def _not_implemented_value(self) -> Any:
        """
        E.g. -0x8000 for Int16
        """
        pass

    def decode_from_registers(self, decoder: BinaryPayloadDecoder) -> int:
        return getattr(decoder, "decode_" + self._modbus_decode_type)()

    def encode_to_payload(self, value: int, encoder: BinaryPayloadBuilder):
        if not isinstance(value, int):
            raise TypeError("value needs to be an int!")
        return getattr(encoder, "add_" + self._modbus_decode_type)(value)

    @property
    def implemented(self) -> bool:
        return self.value != self._not_implemented_value


class Uint16Field(IntegerField):
    _modbus_decode_type = "16bit_uint"
    _not_implemented_value = 0xFFFF


class Int16Field(IntegerField):
    _modbus_decode_type = "16bit_int"
    # 0x8000 is the not-implemented value before decoding, as per spec, which is -0x8000 after decoding:
    _not_implemented_value = -0x8000


class Uint32Field(IntegerField):
    _modbus_decode_type = "32bit_uint"
    _not_implemented_value = 0xFFFFFFFF


class Int32Field(IntegerField):
    _modbus_decode_type = "32bit_int"
    # 0x80000000 is the not-implement value before decoding, as per spec, which is -0x80000000 after decoding:
    # TODO: check this!
    _not_implemented_value = -0x80000000


class FloatField(IntegerField):
    def __init__(
        self,
        *args,
        scale_factor: int,
        **kwargs,
    ):
        if not isinstance(scale_factor, int):
            raise TypeError("scale_factor should be an int!")
        self._scale_factor = scale_factor
        super().__init__(*args, **kwargs)

    @property
    def scale_factor(self) -> Optional[int]:
        return self._scale_factor

    def _check_scale_factor(self):
        if not self._scale_factor.implemented:
            raise RuntimeError(f"Scale factor {self._scale_factor} should be implemented.")
        if self._scale_factor.scale_factor is not None:
            raise RuntimeError(f"Scale factor {self._scale_factor} shouldn't have it's own scale factor!")
        if self._scale_factor.value is None:
            raise RuntimeError(f"Scale factor {self._scale_factor} should not be None.")
        sf = self.scale_factor.value
        if not isinstance(sf, int):
            raise RuntimeError(f"Scale factor {self._scale_factor} should be an integer.")
        if sf < -10 or sf > 10:
            raise RuntimeError(f"Scale factor {self._scale_factor} should be between -10 and 10.")
        return sf

    def decode_from_registers(self, decoder: BinaryPayloadDecoder) -> float:

        # First get our scale factor:
        sf = self._check_scale_factor()

        # Sweet. Now get the integer value and scale it:
        value = super().decode_from_registers(decoder)
        value *= 10 ** sf
        # Round it to what it should be after scaling:
        return round(value, -sf if sf < 0 else 0)

    def encode_to_payload(self, value: float, encoder: BinaryPayloadBuilder) -> None:
        if not isinstance(value, float):
            raise TypeError("value must be a Float")

        # Get our scale factor:
        sf = self._check_scale_factor()

        # Raise to the right power:
        scaled_value = value / (10 ** sf)
        # Round it to what it should be after scaling:
        # TODO: raise error if too many digits specified
        scaled_value = int(round(scaled_value, 0))

        return super().encode_to_payload(value, encoder)


class FloatInt16Field(FloatField, Int16Field):
    pass


class FloatInt32Field(FloatField, Int32Field):
    pass


class FloatUint16Field(FloatField, Uint16Field):
    pass


class FloatUint32Field(FloatField, Uint32Field):
    pass


class StringField(Field):
    def decode_from_registers(self, decoder: BinaryPayloadDecoder) -> str:
        bites = decoder.decode_string(size=self.size * 2)  # Size * 2 as size is in 16 bit units, i.e. 2 bytes.
        return bites.rstrip(b"\x00")

    @property
    @has_been_read
    def implemented(self) -> bool:
        return self.last_read.value != "\x00" * self.size * 2

    def encode_to_payload(self, value: str, encoder: BinaryPayloadBuilder):
        if not isinstance(value, str):
            raise ValueError("Expected str!")
        if len(value) > self.size * 2:
            raise ValueError(f"String must be less than {self.size * 2} characters")
        # Pad with "\0" if needed:
        value = value.ljust(self.size * 2, "\0")
        # Encode to ascii:
        value = value.encode("ascii")
        # Finally, do it:
        return encoder.add_string(value)


class BitfieldMixin:
    """
    This would have been simpler if they were normal on/off flags, however Outback has specified different meaning to
    "on" and "off", unfortunately.
    """

    def __init__(self, *args, flags: IntFlag, **kwargs):
        self.flags = flags
        super().__init__(*args, **kwargs)

    def _get_flags(self, value, mx, not_implemented):
        # TODO: as per spec ... "if the most significant bit in a bitfield is set, all other bits shall be ignored"
        if value == not_implemented:
            # As per sunspec, this is "not implemented"
            return False, None
        elif value < 0 or value > mx:
            raise ValueError(f"{self.__class__.__name__} should be between 0 and {mx}")
        return True, self.flags(value)

    def _set_flags(self, flags):
        if not isinstance(flags, self.flags):
            raise ValueError("Should be a flag of type {self.flags}")
        return flags.value


class Bit16Field(BitfieldMixin, Uint16Field):
    """
    The actual IntFlags are in the flags attr, and this is a basic wrapper that e.g. checks the value is implemented
    before using the flags, etc.
    """

    def _from_registers(self, registers):
        implemented, value = super()._from_registers(registers)
        if not implemented:
            return False, None
        return self._get_flags(value, mx=0x7FFF, not_implemented=0xFFFF)

    def _to_registers(self, flags):
        value = self._set_flags(flags)
        return super()._to_registers(value)


class Bit32Field(BitfieldMixin, Uint32Field):
    """
    The actual IntFlags are in the flags attr, and this is a basic wrapper that e.g. checks the value is implemented
    before using the flags, etc.

    NB: According to the spec this shouldn't exist. But Outback have created it anyway. We'll assume it's just meant to
    be a bit16 for now ...
    """

    def _from_registers(self, registers):
        implemented, value = super()._from_registers(registers)
        if not implemented:
            return False, None
        return self._get_flags(value, mx=0x7FFFFFFF, not_implemented=0xFFFFFFFF)

    def _to_registers(self, flags):
        value = self._set_flags(flags)
        return super()._to_registers(value)


class EnumMixin:
    def __init__(self, *args, options: Enum, **kwargs):
        self.options = options
        super().__init__(*args, **kwargs)

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


class EnumUint16Field(EnumMixin, Uint16Field):
    pass


class EnumInt16Field(EnumMixin, Int16Field):
    pass


class AddressField(Uint32Field):
    def decode_from_registers(self, decoder: BinaryPayloadDecoder) -> str:
        uint32 = super().decode_from_registers(decoder)
        return socket.inet_ntoa(struct.pack("!I", uint32))

    @property
    @has_been_read
    def implemented(self) -> bool:
        # Not implemented if raw value is 0, which equates to 0.0.0.0 when inet_ntoa'd
        return self._last_read.value != "0.0.0.0"

    # def encode_to_payload(self, value: int, encoder: BinaryPayloadBuilder):
    #     return getattr(encoder, "add_" + self._modbus_decode_type)(value)


class DescribedIntFlag(IntFlag):
    """
    An IntFlag we can use like this:

        @unique
        class MyFlags(DescribedIntFlag):
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
