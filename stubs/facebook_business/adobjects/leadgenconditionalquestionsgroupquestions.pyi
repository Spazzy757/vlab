from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class LeadGenConditionalQuestionsGroupQuestions(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        field_key: str = ...
        input_type: str = ...
        name: str = ...
