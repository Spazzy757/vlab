from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class AdCreativePhotoDataMediaElements(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        element_id: str = ...
        element_type: str = ...
        x: str = ...
        y: str = ...
