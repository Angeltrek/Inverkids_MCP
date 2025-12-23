from src.app.validators.common import validate_required
from src.utils.exceptions import ValidationError


def validate_password(password: str) -> None:
    validate_required(password, "password")

    if not isinstance(password, str):
        raise ValidationError("Password must be a string", field="password")

    if len(password) < 6:
        raise ValidationError(
            "Password must be at least 6 characters long",
            field="password",
        )

    if len(password) > 128:
        raise ValidationError(
            "Password too long (maximum 128 characters)",
            field="password",
        )


def validate_token(token: str) -> str:
    validate_required(token, "token")

    if not isinstance(token, str):
        raise ValidationError("Token must be a string", field="token")

    token = token.strip()

    if len(token) < 10:
        raise ValidationError(
            "Invalid token format (too short)",
            field="token",
        )

    return token
