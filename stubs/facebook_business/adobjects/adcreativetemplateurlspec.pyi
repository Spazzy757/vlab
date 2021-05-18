from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class AdCreativeTemplateURLSpec(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        android: str = ...
        config: str = ...
        ios: str = ...
        ipad: str = ...
        iphone: str = ...
        web: str = ...
        windows_phone: str = ...
