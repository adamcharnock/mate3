from typing import Iterable, Optional

from mate3.sunspec.fields import Field, Mode


class Model:
    """
    Base model for Sunspec models - which are really just containers for Fields.
    """

    def fields(self, modes: Optional[Iterable[Mode]] = None) -> Iterable[Field]:
        """
        Often we want to loop through all the fields for a model - ignoring those that aren't 'real' fields such as
        _address above, or the 'config' field that often gets added when a device has the 'realtime' and 'config'
        models.
        """
        for field in vars(self).values():
            if modes is None or field.mode in modes:
                yield field
