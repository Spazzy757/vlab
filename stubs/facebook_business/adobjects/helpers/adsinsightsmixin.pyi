class AdsInsightsMixin:
    class Increment:
        monthly: str = ...
        all_days: str = ...
    class Operator:
        all: str = ...
        any: str = ...
        contain: str = ...
        equal: str = ...
        greater_than: str = ...
        greater_than_or_equal: str = ...
        in_: str = ...
        in_range: str = ...
        less_than: str = ...
        less_than_or_equal: str = ...
        none: str = ...
        not_contain: str = ...
        not_equal: str = ...
        not_in: str = ...
        not_in_range: str = ...
