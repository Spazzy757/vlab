from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class AdRecommendation(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        blame_field: str = ...
        code: str = ...
        confidence: str = ...
        importance: str = ...
        message: str = ...
        recommendation_data: str = ...
        title: str = ...
    class Confidence:
        high: str = ...
        low: str = ...
        medium: str = ...
    class Importance:
        high: str = ...
        low: str = ...
        medium: str = ...
