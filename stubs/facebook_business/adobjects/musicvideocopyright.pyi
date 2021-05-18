from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject as AbstractCrudObject
from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from facebook_business.adobjects.objectparser import ObjectParser as ObjectParser
from facebook_business.api import FacebookRequest as FacebookRequest
from facebook_business.typechecker import TypeChecker as TypeChecker
from typing import Any, Optional

class MusicVideoCopyright(AbstractCrudObject):
    def __init__(self, fbid: Optional[Any] = ..., parent_id: Optional[Any] = ..., api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        creation_time: str = ...
        displayed_matches_count: str = ...
        id: str = ...
        in_conflict: str = ...
        isrc: str = ...
        match_rule: str = ...
        ownership_countries: str = ...
        reference_file_status: str = ...
        ridge_monitoring_status: str = ...
        tags: str = ...
        update_time: str = ...
        video_asset: str = ...
        whitelisted_fb_users: str = ...
        whitelisted_ig_users: str = ...
    def api_get(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
