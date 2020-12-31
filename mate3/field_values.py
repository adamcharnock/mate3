import dataclasses as dc
from functools import wraps
from typing import Any, Iterable, Optional

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
        client: "Mate3Client",  # Can't type it to Mate3Client as circular imports suck ...
        field: Field,
        scale_factor: Optional["FieldValue"],
        address: int,
        raw_value: Any,
        implemented: bool,
    ):
        self._client = client
        self.field = field
        self._scale_factor = scale_factor
        self._address = address
        self._raw_value = raw_value
        self._implemented = implemented

        # Sense check the scale factor
        if scale_factor is not None:
            if not scale_factor.implemented:
                raise RuntimeError("scale_factor should be implemented.")
            if not isinstance(scale_factor.value, int):
                raise RuntimeError("scale_factor should be an integer.")
            if scale_factor.value < -10 or scale_factor.value > 10:
                raise RuntimeError("scale_factor should be between -10 and 10.")

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
        return " | ".join(ss)

    @property
    def implemented(self) -> bool:
        return self._implemented

    @property
    def scale_factor(self) -> Optional[int]:
        return None if self._scale_factor is None else self._scale_factor.value

    @property
    def address(self) -> int:
        return self._address

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

    @value.setter
    def value(self, value):
        self.write(value)

    def write(self, value):
        logger.info(f"Attempting to write {value} to {self.name}")
        # TODO: ensure the type of value is correct
        if self.field.mode not in (Mode.W, Mode.RW):
            raise RuntimeError("Can't write to this field!")
        if not self._implemented:
            raise RuntimeError("This field is marked as not implemented, so you shouldn't write to it!")
        # Scale if needed:
        if self._should_be_scaled:
            # TODO: Time limit on scale_factor being applicable?
            # Scale it:
            value = value / 10 ** self._scale_factor.value
            # Round it to what it should be after scaling:
            # TODO: raise error if too many digits specified
            value = int(round(value, 0))

        # OK, now convert to registers:
        registers = self.field.to_registers(value)
        logger.info(f"writing {value} to {self.name} as registers {registers} at address {self._address}")

        # Do the write
        self._client._client.write_registers(self._address, registers)

    def read(self):
        if self.field.mode not in (Mode.R, Mode.RW):
            raise RuntimeError("Can't read from this field!")

        # First, read the scale factor if needed:
        if self._should_be_scaled:
            self.scale_factor.read()

        # OK, read the appropriate registers:
        logger.info(f"Reading {self.name} from address {self._address}")
        registers = self._client._client.read_holding_registers(address=self._address, count=self.field.size)
        logger.debug(f"Read {registers} for {self.name} from {self._address}")

        self._implemented, self._raw_value = self.field.from_registers(registers)


@dc.dataclass
class ModelValues:
    """
    A base dataclass to extend with all the actual FieldValues for a given Model.
    """

    model: Model = dc.field(metadata={"field": False})
    address: Optional[int] = dc.field(metadata={"field": False})

    def fields(self, modes: Optional[Iterable[Mode]] = None):
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
