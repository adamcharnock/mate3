import dataclasses as dc
import socket
import struct
from abc import ABCMeta, abstractmethod
from datetime import datetime
from enum import Enum, IntFlag
from functools import wraps
from typing import Any, Optional, Tuple

from loguru import logger
from mate3.sunspec.payload import get_decoder, get_encoder
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
        self._can_reuse_cached: bool = False
        self._cached_value = None
        self._cached_implemented = None

        # And client gets set later as a convenience so we can do self.read() without specifying a client context.
        self._client = None

    @property
    def end(self):
        return self.start + self.size

    @property
    def last_read(self):
        return self._last_read

    def __repr__(self):
        name = f"{self.__class__.__name__}[{self.name}]"
        if self._last_read is None:
            return f"{name} (Unread)"
        ss = [name]
        ss.append(f"{self.mode}")
        ss.append("Implemented" if self.implemented else "Not implemented")
        ss.append(f"Value: {self.value}")
        return " | ".join(ss)

    @property
    @has_been_read
    def address(self) -> int:
        return self._last_read.address

    @property
    @has_been_read
    def registers(self) -> Tuple[int]:
        return self._last_read.registers

    @property
    @has_been_read
    def read_time(self) -> datetime:
        return self._last_read.time

    @last_read.setter
    def last_read(self, read: FieldRead):
        self._last_read = read
        self._can_reuse_cached = False
        self._cached_value = None
        self._cached_implemented = None

    def _decode(self):
        """
        OK, we get a bit clever here in that we only decode fields lazily. This is for two reasons - firstly, it can
        save decoding everything on the first run (when you're getting devices etc.) and secondly it resolves some
        inter-field dependency (e.g. to read a scaled field we first need to read the scale factor ... and you say we
        could do that, but reading sequential fields can be nicer for the mate3, and scale factors often aren't
        sequential with their field.). Put another way, it allows us to decouple reading fields (i.e. hitting modbus)
        from the decoding into pretty python types etc. So, if the _last_read is something we've seen before, just reuse
        cached decoding from last time. Otherwise, decode and then cache. This way we only decode when needed, but are
        also speedy about it if it's done multiple time.
        """
        if self.mode not in (Mode.R, Mode.RW):
            raise RuntimeError("Can't read from this field!")
        if self._can_reuse_cached:
            return

        # OK, not cached - let's read and decode:
        decoder = get_decoder(self._last_read.registers)
        self._cached_value, self._cached_implemented = self.decode_from_registers(decoder)

        # Mark as usable in cache:
        self._can_reuse_cached = True

    @property
    @has_been_read
    def value(self):
        self._decode()
        return self._cached_value

    @property
    def implemented(self) -> bool:
        self._decode()
        return self._cached_implemented

    @abstractmethod
    def decode_from_registers(self, decoder: BinaryPayloadDecoder) -> Tuple[Any, bool]:
        """
        Returns: pretty python value, and whether ir implemented
        """
        pass

    @abstractmethod
    def encode_to_payload(self, value: Any, encoder: BinaryPayloadBuilder) -> None:
        pass

    def to_dict(self):
        return {
            "implemented": self.implemented,
            "address": self.address,
            "registers": self.registers,
            "value": self.value
            if self.value is None or isinstance(self.value, (str, int, float))
            else repr(self.value),
        }

    def write(self, value):
        """
        Warning:

            Ensure you have read the LICENSE file before using this feature. Note the
            section which begins:

                THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
                EXPRESS OR IMPLIED

            Specifically, it is quite possible that you can cause damage to your equipment
            through use of this feature. Be careful!
        """
        logger.debug(f"Attempting to write {value} to {self.name}")

        if self.mode not in (Mode.W, Mode.RW):
            raise RuntimeError("Can't write to this field!")

        if not self.implemented:
            raise RuntimeError("This field is marked as not implemented, so you shouldn't write to it!")

        # OK, now convert to registers:
        encoder = get_encoder()
        self.encode_to_payload(value, encoder)
        registers = encoder.to_registers()
        logger.debug(f"Writing {self.value} to {self.name} as registers {registers} at address {self.address}")

        # Do the write
        self._client._client.write_registers(self.address, registers)

        # Now read it and check the value is what we intended:
        self.read()
        if value != self.value:
            raise RuntimeError(
                f"Write 'succeeded' but after re-reading to check, the current value is {self.value} and not {value}"
            )

    def read(self):
        if self.mode not in (Mode.R, Mode.RW):
            raise RuntimeError("Can't read from this field!")

        # OK, read the appropriate registers:
        logger.debug(f"Reading {self.name} from address {self.address}")
        read_time = datetime.now()
        registers = self._client._client.read_holding_registers(address=self.address, count=self.size)
        logger.debug(f"Read {registers} for {self.name} from {self.address}")
        self.last_read = FieldRead(address=self.address, time=read_time, registers=registers)


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

    def decode_from_registers(self, decoder: BinaryPayloadDecoder) -> Tuple[int, bool]:
        value = getattr(decoder, "decode_" + self._modbus_decode_type)()
        implemented = value != self._not_implemented_value
        return value if implemented else None, implemented

    def encode_to_payload(self, value: int, encoder: BinaryPayloadBuilder) -> None:
        if not isinstance(value, int):
            raise TypeError("value needs to be an int!")
        getattr(encoder, "add_" + self._modbus_decode_type)(value)


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
        scale_factor: IntegerField,
        **kwargs,
    ):
        self._scale_factor = scale_factor
        super().__init__(*args, **kwargs)

    @property
    def scale_factor(self) -> Optional[int]:
        return self._scale_factor

    def _check_scale_factor(self):
        if not isinstance(self._scale_factor, IntegerField):
            raise RuntimeError(f"Scale factor {self._scale_factor} should be an IntegerField.")
        if not self._scale_factor.implemented:
            raise RuntimeError(f"Scale factor {self._scale_factor} should be implemented.")
        if self._scale_factor.value is None:
            raise RuntimeError(f"Scale factor {self._scale_factor} should not be None.")
        sf = self.scale_factor.value
        if not isinstance(sf, int):
            raise RuntimeError(f"Scale factor {self._scale_factor} should be an integer.")
        if sf < -10 or sf > 10:
            raise RuntimeError(f"Scale factor {self._scale_factor} should be between -10 and 10.")
        return sf

    def decode_from_registers(self, decoder: BinaryPayloadDecoder) -> Tuple[float, bool]:

        # First get our scale factor:
        sf = self._check_scale_factor()

        # Sweet. Now get the integer value the integer way:
        value, implemented = super().decode_from_registers(decoder)
        if not implemented:
            return None, implemented
        # OK, scale it and round it to what it should be after scaling:
        value *= 10 ** sf
        return round(value, -sf if sf < 0 else 0), True

    def encode_to_payload(self, value: float, encoder: BinaryPayloadBuilder) -> None:
        # Must be float or int (int can happen when sf >= 0)
        if not isinstance(value, (int, float)):
            raise TypeError("value must be a Float")

        # TODO: check value doesn't have extra decimal places/significant figures

        # Get our scale factor:
        sf = self._check_scale_factor()

        # Raise to the right power:
        scaled_value = value / (10 ** sf)
        # Round it to what it should be after scaling:
        # TODO: raise error if too many digits specified
        scaled_value = int(round(scaled_value, 0))

        super().encode_to_payload(scaled_value, encoder)

    def read(self, *args, **kwargs):
        # First, read the scale factor, then do the normal read:
        self.scale_factor.read()
        return super().read(*args, **kwargs)


class FloatInt16Field(FloatField, Int16Field):
    pass


class FloatInt32Field(FloatField, Int32Field):
    pass


class FloatUint16Field(FloatField, Uint16Field):
    pass


class FloatUint32Field(FloatField, Uint32Field):
    pass


class StringField(Field):
    def decode_from_registers(self, decoder: BinaryPayloadDecoder) -> Tuple[str, bool]:
        bites = decoder.decode_string(size=self.size * 2)  # Size * 2 as size is in 16 bit units, i.e. 2 bytes.
        implemented = bites != b"\x00" * self.size * 2
        return bites.rstrip(b"\x00") if implemented else None, implemented

    def encode_to_payload(self, value: bytes, encoder: BinaryPayloadBuilder) -> None:
        if not isinstance(value, bytes):
            raise ValueError("Expected bytes!")
        if len(value) > self.size * 2:
            raise ValueError(f"String must be less than {self.size * 2} characters")
        # Pad with "\0" if needed:
        value = value.ljust(self.size * 2, b"\0")
        # Finally, do it:
        encoder.add_string(value)


class AddressField(Uint32Field):
    def decode_from_registers(self, decoder: BinaryPayloadDecoder) -> Tuple[str, bool]:
        uint32, _ = super().decode_from_registers(decoder)
        if uint32 == 0:
            return None, False
        return socket.inet_ntoa(struct.pack("!I", uint32)), True

    def encode_to_payload(self, value: str, encoder: BinaryPayloadBuilder):
        bites = socket.inet_aton(value)
        num = struct.unpack("!I", bites)[0]
        super().encode_to_payload(num, encoder)


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


class BitfieldMixin(metaclass=ABCMeta):
    """
    This would have been simpler if they were normal on/off flags, however Outback has specified different meaning to
    "on" and "off", unfortunately. The actual IntFlags are in the flags attr, and this is a basic wrapper that e.g.
    checks the value is implemented before using the flags, etc.
    """

    def __init__(self, *args, flags: DescribedIntFlag, **kwargs):
        self.flags = flags
        super().__init__(*args, **kwargs)

    def decode_from_registers(self, decoder: BinaryPayloadDecoder) -> Tuple[int, bool]:
        value, implemented = super().decode_from_registers(decoder)
        if not implemented:
            return None, False
        # TODO: as per spec ... "if the most significant bit in a bitfield is set, all other bits shall be ignored"
        return self.flags(value), True

    def encode_to_payload(self, value: DescribedIntFlag, encoder: BinaryPayloadBuilder) -> None:
        if not isinstance(value, self.flags):
            raise TypeError(f"value must be of type {self.flags}")
        return super().encode_to_payload(value.value, encoder)


class Bit16Field(BitfieldMixin, Uint16Field):
    pass


class Bit32Field(BitfieldMixin, Uint32Field):
    """
    NB: According to the spec this shouldn't exist. But Outback have created it anyway. We'll assume it's just meant to
    be a bit16 for now ...
    """

    pass


class EnumMixin:
    def __init__(self, *args, enum: Enum, **kwargs):
        self.enum = enum
        super().__init__(*args, **kwargs)

    def decode_from_registers(self, decoder: BinaryPayloadDecoder) -> Tuple[int, bool]:
        value, implemented = super().decode_from_registers(decoder)
        if not implemented:
            return None, False
        try:
            value = self.enum(value)
        except ValueError:
            logger.warning(
                (
                    f"{value} is not a valid value for enum {self.enum} with options {list(self.enum)} so setting as "
                    "not implemented"
                )
            )
            return None, False
        return value, True

    def encode_to_payload(self, value: Enum, encoder: BinaryPayloadBuilder) -> None:
        if not isinstance(value, self.enum):
            raise TypeError(f"value should be an instance of {self.enum}")
        return super().encode_to_payload(value.value, encoder)


class EnumUint16Field(EnumMixin, Uint16Field):
    pass


class EnumInt16Field(EnumMixin, Int16Field):
    pass
