import dataclasses as dc
from datetime import datetime
from typing import Any, Iterable, Optional, Tuple

from loguru import logger

from mate3.sunspec.fields import Field, Mode
from mate3.sunspec.model_base import Model


class FieldValue:
    """
    A FieldValue is really just a container to store values read from a particular Field, with nice utilities like
    automatically applying scale factors, and marking things as dirty etc.
    """

    def __init__(
        self,
        client,  # TODO: Can't type it to Mate3Client as circular imports suck ...
        field: Field,
        scale_factor: Optional["FieldValue"],
        address: int,
        registers: Iterable[int],
        raw_value: Any,
        implemented: bool,
        read_time: datetime,
    ):
        self._client = client
        self.field = field
        self._scale_factor = scale_factor
        self._address = address
        self._registers = tuple(registers)  # immutability is nice
        self._raw_value = raw_value
        self._implemented = implemented
        self._last_read = read_time

    @property
    def name(self) -> str:
        # Just the field name ...
        return self.field.name

    def __repr__(self):
        ss = [f"FieldValue[{self.field.name}]"]
        ss.append(f"{self.field.mode}")
        ss.append("Implemented" if self._implemented else "Not implemented")
        if self._scale_factor is not None:
            ss.append(f"Scale factor: {self._scale_factor.value}")
            ss.append(f"Unscaled value: {self._raw_value}")
        if self._implemented:
            ss.append(f"Value: {self.value}")
        ss.append(f"Read @ {self.last_read}")
        return " | ".join(ss)

    @property
    def implemented(self) -> bool:
        return self._implemented

    @property
    def last_read(self) -> datetime:
        return self._last_read

    @property
    def scale_factor(self) -> Optional[int]:
        if self._scale_factor is None:
            return None

        # Sense check the scale factor
        if not self._scale_factor.implemented:
            raise RuntimeError(f"Scale factor {self._scale_factor} should be implemented.")
        if self._scale_factor.scale_factor is not None:
            raise RuntimeError(f"Scale factor {self._scale_factor} shouldn't have it's own scale factor!")
        if self._scale_factor.value is None:
            raise RuntimeError(f"Scale factor {self._scale_factor} should not be None.")
        if not isinstance(self._scale_factor.value, int):
            raise RuntimeError(f"Scale factor {self._scale_factor} should be an integer.")
        if self._scale_factor.value < -10 or self._scale_factor.value > 10:
            raise RuntimeError(f"Scale factor {self._scale_factor} should be between -10 and 10.")
        return self._scale_factor

    @property
    def address(self) -> int:
        return self._address

    @property
    def registers(self) -> Tuple[int]:
        return self._registers

    @property
    def raw_value(self) -> Any:
        if self.field.mode not in (Mode.R, Mode.RW):
            raise RuntimeError("Can't read from this field!")
        return self._raw_value

    @property
    def _should_be_scaled(self):
        return self._scale_factor is not None

    @property
    def value(self) -> Any:
        if self.field.mode not in (Mode.R, Mode.RW):
            raise RuntimeError("Can't read from this field!")
        if not self._implemented:
            return None
        if not self._should_be_scaled:
            return self._raw_value
        # OK, should be scaled, so let's scale it:
        scale_factor = self._scale_factor.value
        value = self._raw_value * 10 ** scale_factor
        # Round it to what it should be after scaling:
        return round(value, -scale_factor if scale_factor < 0 else 0)

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
        # TODO: ensure the type of value is correct
        if self.field.mode not in (Mode.W, Mode.RW):
            raise RuntimeError("Can't write to this field!")
        if not self._implemented:
            raise RuntimeError("This field is marked as not implemented, so you shouldn't write to it!")
        # Scale if needed:
        scaled_value = value
        if self._should_be_scaled:
            # TODO: Time limit on scale_factor being applicable?
            # Scale it:
            scaled_value = value / 10 ** self._scale_factor.value
            # Round it to what it should be after scaling:
            # TODO: raise error if too many digits specified
            scaled_value = int(round(scaled_value, 0))

        # OK, now convert to registers:
        registers = self.field.to_registers(scaled_value)
        logger.debug(f"Writing {scaled_value} to {self.name} as registers {registers} at address {self._address}")

        # Do the write
        self._client._client.write_registers(self._address, registers)

        # Now read it and check the value is what we intended:
        self.read()
        if value != self.value:
            raise RuntimeError(
                f"Write 'succeeded' but after re-reading to check, the current value is {self.value} and not {value}"
            )

    def read(self):
        if self.field.mode not in (Mode.R, Mode.RW):
            raise RuntimeError("Can't read from this field!")

        # First, read the scale factor if needed:
        if self._should_be_scaled:
            self.scale_factor.read()

        # OK, read the appropriate registers:
        logger.debug(f"Reading {self.name} from address {self._address}")
        read_time = datetime.now()
        registers = self._client._client.read_holding_registers(address=self._address, count=self.field.size)
        logger.debug(f"Read {registers} for {self.name} from {self._address}")

        self._implemented, self._raw_value = self.field.from_registers(registers)
        self._last_read = read_time

    def to_dict(self):
        return {
            "implemented": self.implemented,
            "scale_factor": self.scale_factor.value if self.scale_factor is not None else None,
            "address": self.address,
            "registers": self.registers,
            "raw_value": self.raw_value
            if self.raw_value is None or isinstance(self.raw_value, (str, int, float))
            else repr(self.raw_value),
            "value": self.value
            if self.value is None or isinstance(self.value, (str, int, float))
            else repr(self.value),
        }


@dc.dataclass
class ModelValues:
    """
    A base dataclass to extend with all the actual FieldValues for a given Model.
    """

    model: Model = dc.field(metadata={"field": False})
    address: Optional[int] = dc.field(metadata={"field": False})

    def fields(self, modes: Optional[Iterable[Mode]] = None) -> Iterable[FieldValue]:
        """
        Often we want to loop through all the fields for a model - ignoring those that aren't 'real' fields such as
        _address above, or the 'config' field that often gets added when a device has the 'realtime' and 'config'
        models.
        """
        for field in dc.fields(self):
            if field.metadata.get("field", True):
                field_ = getattr(self, field.name)
                if modes is None or field_.field.mode in modes:
                    yield field_
