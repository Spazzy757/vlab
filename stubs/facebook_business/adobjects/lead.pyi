from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject as AbstractCrudObject
from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from facebook_business.adobjects.objectparser import ObjectParser as ObjectParser
from facebook_business.api import FacebookRequest as FacebookRequest
from facebook_business.typechecker import TypeChecker as TypeChecker
from typing import Any, Optional

class Lead(AbstractCrudObject):
    def __init__(self, fbid: Optional[Any] = ..., parent_id: Optional[Any] = ..., api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        ad_id: str = ...
        ad_name: str = ...
        adset_id: str = ...
        adset_name: str = ...
        campaign_id: str = ...
        campaign_name: str = ...
        created_time: str = ...
        custom_disclaimer_responses: str = ...
        field_data: str = ...
        form_id: str = ...
        home_listing: str = ...
        id: str = ...
        is_organic: str = ...
        partner_name: str = ...
        platform: str = ...
        retailer_item_id: str = ...
        vehicle: str = ...
    @classmethod
    def get_endpoint(cls): ...
    def api_delete(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def api_get(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
