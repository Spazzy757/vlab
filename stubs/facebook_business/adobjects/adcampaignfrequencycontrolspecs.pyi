from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class AdCampaignFrequencyControlSpecs(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        event: str = ...
        interval_days: str = ...
        max_frequency: str = ...
