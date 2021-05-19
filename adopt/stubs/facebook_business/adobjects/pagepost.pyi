from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject as AbstractCrudObject
from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from facebook_business.adobjects.objectparser import ObjectParser as ObjectParser
from facebook_business.api import FacebookRequest as FacebookRequest
from facebook_business.typechecker import TypeChecker as TypeChecker
from typing import Any, Optional

class PagePost(AbstractCrudObject):
    def __init__(self, fbid: Optional[Any] = ..., parent_id: Optional[Any] = ..., api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        actions: str = ...
        admin_creator: str = ...
        allowed_advertising_objectives: str = ...
        application: str = ...
        backdated_time: str = ...
        call_to_action: str = ...
        can_reply_privately: str = ...
        child_attachments: str = ...
        comments_mirroring_domain: str = ...
        coordinates: str = ...
        created_time: str = ...
        delivery_growth_optimizations: str = ...
        entities: str = ...
        event: str = ...
        expanded_height: str = ...
        expanded_width: str = ...
        feed_targeting: str = ...
        formatting: str = ...
        field_from: str = ...
        full_picture: str = ...
        height: str = ...
        icon: str = ...
        id: str = ...
        implicit_place: str = ...
        instagram_eligibility: str = ...
        is_app_share: str = ...
        is_eligible_for_promotion: str = ...
        is_expired: str = ...
        is_hidden: str = ...
        is_inline_created: str = ...
        is_instagram_eligible: str = ...
        is_popular: str = ...
        is_published: str = ...
        is_spherical: str = ...
        live_video_eligibility: str = ...
        message: str = ...
        message_tags: str = ...
        multi_share_end_card: str = ...
        multi_share_optimized: str = ...
        parent_id: str = ...
        permalink_url: str = ...
        picture: str = ...
        place: str = ...
        privacy: str = ...
        promotable_id: str = ...
        promotion_status: str = ...
        properties: str = ...
        publishing_stats: str = ...
        scheduled_publish_time: str = ...
        shares: str = ...
        status_type: str = ...
        story: str = ...
        story_tags: str = ...
        subscribed: str = ...
        target: str = ...
        targeting: str = ...
        timeline_visibility: str = ...
        translations: str = ...
        updated_time: str = ...
        via: str = ...
        video_buying_eligibility: str = ...
        width: str = ...
        will_be_autocropped_when_deliver_to_instagram: str = ...
    class With:
        location: str = ...
    class BackdatedTimeGranularity:
        day: str = ...
        hour: str = ...
        min: str = ...
        month: str = ...
        none: str = ...
        year: str = ...
    class FeedStoryVisibility:
        hidden: str = ...
        visible: str = ...
    class TimelineVisibility:
        forced_allow: str = ...
        hidden: str = ...
        normal: str = ...
    def api_delete(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def api_get(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def api_update(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_attachments(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_comments(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def create_comment(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_dynamic_posts(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_insights(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., is_async: bool = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def delete_likes(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_likes(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def create_like(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_reactions(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_shared_posts(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_sponsor_tags(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_to(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...