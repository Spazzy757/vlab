from facebook_business.api import FacebookAdsApi as FacebookAdsApi
from facebook_business.exceptions import FacebookError as FacebookError
from facebook_business.session import FacebookSession as FacebookSession
from typing import Any

class ProductCatalogMixin:
    class Role:
        admin: str = ...
    class Availability:
        available_for_order: str = ...
        in_stock: str = ...
        out_of_stock: str = ...
        preorder: str = ...
    class AgeGroup:
        adult: str = ...
        infant: str = ...
        kids: str = ...
        newborn: str = ...
        toddler: str = ...
    class Gender:
        men: str = ...
        women: str = ...
        unisex: str = ...
    class Condition:
        new: str = ...
        refurbished: str = ...
        used: str = ...
    def add_user(self, user: Any, role: Any): ...
    def remove_user(self, user: Any): ...
    def add_external_event_sources(self, pixel_ids: Any): ...
    def remove_external_event_sources(self, pixel_ids: Any): ...
    def update_product(self, retailer_id: Any, **kwargs: Any): ...
    def b64_encoded_id(self, retailer_id: Any): ...
