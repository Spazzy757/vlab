from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class DeliveryCheckExtraInfo(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        adgroup_ids: str = ...
        campaign_ids: str = ...
        countries: str = ...
