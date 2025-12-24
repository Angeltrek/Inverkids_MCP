from src.app.validators.common import validate_required
from src.utils.exceptions import ValidationError


def validate_enrollment_id(enrollment_id: str) -> str:
    validate_required(enrollment_id, "enrollment_id")

    if not isinstance(enrollment_id, str):
        raise ValidationError(
            "Enrollment ID must be a string",
            field="enrollment_id",
        )

    if len(enrollment_id) < 3:
        raise ValidationError(
            "Enrollment ID too short (minimum 6 characters)",
            field="enrollment_id",
        )

    return enrollment_id


def validate_user_type(user_type: str) -> str:
    validate_required(user_type, "user_type")

    user_type = user_type.strip().lower()
    valid_types = ["student", "teacher", "admin", "parent"]

    if user_type not in valid_types:
        raise ValidationError(
            f"Invalid user type: '{user_type}'. "
            f"Must be one of: {', '.join(valid_types)}",
            field="user_type",
        )

    return user_type
