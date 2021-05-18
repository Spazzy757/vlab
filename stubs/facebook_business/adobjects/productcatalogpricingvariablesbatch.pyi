from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class ProductCatalogPricingVariablesBatch(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        errors: str = ...
        errors_total_count: str = ...
        handle: str = ...
        status: str = ...
