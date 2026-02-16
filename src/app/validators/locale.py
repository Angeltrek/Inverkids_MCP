import re

from src.app.validators.common import validate_required
from src.utils.exceptions import ValidationError


def validate_language(lang: str) -> str:
    validate_required(lang, "language")

    lang = lang.strip().lower()

    if not re.match(r"^[a-z]{2}$", lang):
        raise ValidationError(
            "Invalid language code. Expected ISO 639-1 (e.g., 'es', 'en')",
            field="language",
        )

    return lang
