import re
from typing import List, Any
from src.utils.exceptions import ValidationError
from src.app.validators.common import validate_required


def validate_level(level: Any) -> str:
    validate_required(level, "level")

    level_str = str(level).strip().lower()
    match = re.search(r"\d+", level_str)

    if not match:
        raise ValidationError(
            f"Invalid level format: '{level}'. Must contain a number.",
            field="level",
        )

    level_num = int(match.group())

    if level_num < 1 or level_num > 12:
        raise ValidationError(
            f"Level must be between 1 and 12, got: {level_num}",
            field="level",
        )

    return str(level_num)


def validate_group_ids(group_ids: List[str]) -> List[str]:
    if not group_ids:
        raise ValidationError(
            "At least one group ID is required",
            field="group_ids",
        )

    if not isinstance(group_ids, (list, tuple)):
        raise ValidationError(
            "Group IDs must be a list",
            field="group_ids",
        )

    if len(group_ids) > 100:
        raise ValidationError(
            "Too many group IDs (maximum 100)",
            field="group_ids",
        )

    validated = []
    for idx, gid in enumerate(group_ids):
        if not gid or not isinstance(gid, str):
            raise ValidationError(
                f"Invalid group ID at index {idx}: '{gid}'",
                field="group_ids",
            )
        validated.append(gid.strip())

    return validated
