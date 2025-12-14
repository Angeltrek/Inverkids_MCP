from decimal import Decimal
from typing import Any


def json_safe(obj: Any):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Type {type(obj)} not serializable")
