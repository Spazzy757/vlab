from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class AdCreativeInteractiveComponentsSpec(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        components: str = ...
