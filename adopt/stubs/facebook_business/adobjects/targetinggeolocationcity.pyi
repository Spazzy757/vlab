from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class TargetingGeoLocationCity(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        country: str = ...
        distance_unit: str = ...
        key: str = ...
        name: str = ...
        radius: str = ...
        region: str = ...
        region_id: str = ...