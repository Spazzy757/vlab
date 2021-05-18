from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class ContentDeliveryReport(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        content_name: str = ...
        content_url: str = ...
        creator_name: str = ...
        creator_url: str = ...
        estimated_impressions: str = ...
    class Platform:
        audience_network: str = ...
        facebook: str = ...
        hidden_aaa: str = ...
        instagram: str = ...
        messenger: str = ...
        unknown: str = ...
        whatsapp: str = ...
    class Position:
        all_placements: str = ...
        an_classic: str = ...
        facebook_groups_feed: str = ...
        facebook_stories: str = ...
        feed: str = ...
        groups: str = ...
        hidden_aaa: str = ...
        instagram_explore: str = ...
        instagram_igtv: str = ...
        instagram_stories: str = ...
        instant_article: str = ...
        instream_video: str = ...
        jobs_browser: str = ...
        marketplace: str = ...
        messenger_inbox: str = ...
        messenger_stories: str = ...
        others: str = ...
        rewarded_video: str = ...
        right_hand_column: str = ...
        search: str = ...
        status: str = ...
        suggested_video: str = ...
        unknown: str = ...
        video_feeds: str = ...
