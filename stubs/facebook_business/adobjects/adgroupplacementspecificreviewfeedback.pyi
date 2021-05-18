from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class AdgroupPlacementSpecificReviewFeedback(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        account_admin: str = ...
        ad: str = ...
        b2c: str = ...
        bsg: str = ...
        city_community: str = ...
        daily_deals: str = ...
        daily_deals_legacy: str = ...
        dpa: str = ...
        dri_counterfeit: str = ...
        facebook: str = ...
        facebook_pages_live_shopping: str = ...
        instagram: str = ...
        instagram_shop: str = ...
        lead_gen_honeypot: str = ...
        marketplace: str = ...
        marketplace_home_rentals: str = ...
        marketplace_home_sales: str = ...
        marketplace_motors: str = ...
        marketplace_shops: str = ...
        max_review_placements: str = ...
        page_admin: str = ...
        product: str = ...
        product_service: str = ...
        profile: str = ...
        seller: str = ...
        shops: str = ...
        traffic_quality: str = ...
        whatsapp: str = ...
