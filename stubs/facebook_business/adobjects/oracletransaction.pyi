from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject as AbstractCrudObject
from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from facebook_business.adobjects.objectparser import ObjectParser as ObjectParser
from facebook_business.api import FacebookRequest as FacebookRequest
from facebook_business.typechecker import TypeChecker as TypeChecker
from typing import Any, Optional

class OracleTransaction(AbstractCrudObject):
    def __init__(self, fbid: Optional[Any] = ..., parent_id: Optional[Any] = ..., api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        ad_account_ids: str = ...
        amount: str = ...
        amount_due: str = ...
        billed_amount_details: str = ...
        billing_period: str = ...
        campaign: str = ...
        cdn_download_uri: str = ...
        currency: str = ...
        download_uri: str = ...
        due_date: str = ...
        entity: str = ...
        id: str = ...
        invoice_date: str = ...
        invoice_id: str = ...
        invoice_type: str = ...
        liability_type: str = ...
        payment_status: str = ...
        payment_term: str = ...
        type: str = ...
    class Type:
        cm: str = ...
        inv: str = ...
    def api_get(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_campaigns(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_data(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
