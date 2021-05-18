from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class CommerceMerchantSettingsSetupStatus(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        deals_setup: str = ...
        marketplace_approval_status: str = ...
        marketplace_approval_status_details: str = ...
        payment_setup: str = ...
        shop_setup: str = ...
