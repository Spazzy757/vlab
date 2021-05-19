from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject as AbstractCrudObject
from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from facebook_business.adobjects.objectparser import ObjectParser as ObjectParser
from facebook_business.api import FacebookRequest as FacebookRequest
from facebook_business.typechecker import TypeChecker as TypeChecker
from typing import Any, Optional

class PartnerStudy(AbstractCrudObject):
    def __init__(self, fbid: Optional[Any] = ..., parent_id: Optional[Any] = ..., api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        additional_info: str = ...
        brand: str = ...
        client_name: str = ...
        emails: str = ...
        id: str = ...
        input_ids: str = ...
        is_export: str = ...
        lift_study: str = ...
        location: str = ...
        match_file_ds: str = ...
        name: str = ...
        partner_defined_id: str = ...
        partner_household_graph_dataset_id: str = ...
        status: str = ...
        study_end_date: str = ...
        study_start_date: str = ...
        study_type: str = ...
        submit_date: str = ...
    def api_get(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...