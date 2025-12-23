from typing import Any
from src.utils.exceptions import ValidationError


def validate_required(value: Any, field_name: str) -> Any:
    if value is None or (isinstance(value, str) and not value.strip()):
        raise ValidationError(f"{field_name} is required", field=field_name)
    return value
