import logging

from src.app.validators import validate_enrollment_id, validate_password
from src.infrastructure.config.settings.settings import load_settings
from src.infrastructure.http.auth_client import AuthClient

logger = logging.getLogger(__name__)
settings = load_settings()


class AuthService:
    @staticmethod
    def login(enrollment_id: str, password: str) -> dict:
        enrollment_id = validate_enrollment_id(enrollment_id)
        validate_password(password)

        logger.info(
            "Login attempt",
            extra={"enrollment_id": enrollment_id},
        )

        auth = AuthClient(
            base_url=settings.backend.base_url,
            timeout=settings.backend.auth_timeout,
        )

        session = auth.login_with_enrollment(
            enrollment_id=enrollment_id,
            password=password,
        )

        logger.info(
            "Login successful",
            extra={
                "enrollment_id": enrollment_id,
                "user_id": session.user.get("id"),
            },
        )

        return {
            "user": session.user,
            "token": session.token,
        }
