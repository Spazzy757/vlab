from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class TargetingGeoLocationGeoEntities(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        country: str = ...
        key: str = ...
        name: str = ...
        region: str = ...
        region_id: str = ...
