import dataclasses as dc
from datetime import datetime, timedelta
from typing import Any, Iterable, Optional

from loguru import logger

from mate3.sunspec.fields import Field, IntegerField, Mode
from mate3.sunspec.model_base import Model


class FieldValue:
    """
    A FieldValue is really just a container to store values read from a particular Field, with nice utilities like
    automatically applying scale factors, and marking things as dirty etc.
    """

    _scale_factor_cache_time = timedelta(seconds=60)

    def __init__(self, field):
        self.field: Field = field
        self._last_read: Optional[datetime] = None
        self._dirty: bool = False
        self._implemented: Optional[bool] = None
        self._value_to_write: Any = None
        self._raw_value: Any = None
        self._scale_factor: Optional[int] = None

    @property
    def name(self) -> str:
        # Just the field name ...
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
    def last_read(self) -> datetime:
        return self._last_read

    @property
    def dirty(self) -> bool:
        return self._dirty

    @property
    def implemented(self) -> bool:
        if self._last_read is None:
            raise RuntimeError("Can't access 'implemented' before the field value has been read at least once.")
        return self._implemented

    @property
    def scale_factor(self) -> int:
        if self._last_read is None:
            raise RuntimeError("Can't access 'scale_factor' before the field value has been read at least once.")
        return self._scale_factor

    @property
    def raw_value(self) -> Any:
        if self._last_read is None:
            raise RuntimeError("Can't access 'raw_value' before the field value has been read at least once.")
        return self._raw_value

    @property
    def _should_be_scaled(self):
        return isinstance(self.field, IntegerField) and self.field.scale_factor is not None

    @property
    def value(self) -> Any:
        if self._last_read is None:
            raise RuntimeError("Can't access 'value' before the field value has been read at least once.")
        if self.field.mode not in (Mode.R, Mode.RW):
            raise RuntimeError("Can't read from this field!")
        if not self._implemented:
            return None
        if not self._should_be_scaled:
            return self._raw_value
        # OK, should be scaled, so let's scale it:
        value = self._raw_value * 10 ** self._scale_factor
        # Round it to what it should be after scaling:
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
            # Scale it:
            value = value / 10 ** self._scale_factor
            # Round it to what it should be after scaling:
            self._value_to_write = int(round(value, 0))
        else:
            self._value_to_write = value
        self._dirty = True

    def _update_on_read(self, value, implemented, read_time, scale_factor_read=None):
        """
        Assumption is that if there's a scale factor, it's read at the same time as value, so they should be in sync.
        Not really a major with Outback, as the scale factors seem to be constant anyway ... but no harm in being safe.
        """
        if self._should_be_scaled:
            if scale_factor_read is None:
                raise RuntimeError(f"scale_factor_read required for field {self.field}")
            if not scale_factor_read.implemented:
                raise RuntimeError("scale_factor_read should be implemented!")
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
                raise RuntimeError("scale_factor should be an integer!")
            if scale_factor_read < -10 or scale_factor_read > 10:
                raise RuntimeError("scale_factor should be between -10 and 10")
        else:
            if scale_factor_read is not None:
                raise RuntimeError(f"No scale_factor should be provided for field {self.field}")

        self._raw_value = value
        self._scale_factor = scale_factor_read
        self._implemented = implemented
        self._last_read = read_time
        if self._value_to_write is not None:
            logger.warning(
                "A value has been set to be written, but was re-read after this, so the write will be ignored "
            )
            self._value_to_write = None
        self._dirty = False


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
