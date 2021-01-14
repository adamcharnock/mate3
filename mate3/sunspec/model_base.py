from typing import Iterable, Optional

from mate3.sunspec.fields import Mode


class Model:
    """
    Base model for Sunspec models - which are really just containers for Fields.
    """

    @classmethod
    def fields(cls, modes: Optional[Iterable[Mode]] = None):
        """
        Often we want to loop through all the fields for a model - ignoring those that aren't 'real' fields such as
        _address above, or the 'config' field that often gets added when a device has the 'realtime' and 'config'
        models.
        """
        for field in cls.__model_fields__:
            if modes is None or field.mode in modes:
                yield field
