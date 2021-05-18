from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class AdCampaignDeliveryEstimate(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        daily_outcomes_curve: str = ...
        estimate_dau: str = ...
        estimate_mau: str = ...
        estimate_ready: str = ...
    class OptimizationGoal:
        ad_recall_lift: str = ...
        app_downloads: str = ...
        app_installs: str = ...
        brand_awareness: str = ...
        clicks: str = ...
        derived_events: str = ...
        engaged_users: str = ...
        event_responses: str = ...
        impressions: str = ...
        landing_page_views: str = ...
        lead_generation: str = ...
        link_clicks: str = ...
        none: str = ...
        offer_claims: str = ...
        offsite_conversions: str = ...
        page_engagement: str = ...
        page_likes: str = ...
        post_engagement: str = ...
        reach: str = ...
        replies: str = ...
        social_impressions: str = ...
        thruplay: str = ...
        two_second_continuous_video_views: str = ...
        value: str = ...
        visit_instagram_profile: str = ...
