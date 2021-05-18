from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from facebook_business.exceptions import FacebookBadObjectError as FacebookBadObjectError
from typing import Any, Optional

class ObjectParser:
    def __init__(self, api: Optional[Any] = ..., target_class: Optional[Any] = ..., reuse_object: Optional[Any] = ..., custom_parse_method: Optional[Any] = ...) -> None: ...
    def parse_single(self, response: Any): ...
    def parse_multiple(self, response: Any): ...
