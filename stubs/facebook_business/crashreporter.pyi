from enum import Enum
from facebook_business.api import FacebookAdsApi as FacebookAdsApi, FacebookRequest as FacebookRequest
from facebook_business.exceptions import FacebookError as FacebookError, FacebookRequestError as FacebookRequestError
from facebook_business.session import FacebookSession as FacebookSession
from typing import Any

class Reasons(Enum):
    API: str = ...
    SDK: str = ...

class CrashReporter:
    reporter_instance: Any = ...
    logger: Any = ...
    def __init__(self, app_id: Any, excepthook: Any) -> None: ...
    @classmethod
    def enable(cls) -> None: ...
    @classmethod
    def disable(cls) -> None: ...
    @classmethod
    def enableLogging(cls) -> None: ...
    @classmethod
    def disableLogging(cls) -> None: ...
    @classmethod
    def logging(cls, info: Any) -> None: ...