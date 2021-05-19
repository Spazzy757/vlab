from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class AdEntityTargetSpend(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        amount: str = ...
        has_error: str = ...
        is_accurate: str = ...
        is_prorated: str = ...
        is_updating: str = ...