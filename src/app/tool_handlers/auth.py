import os
from src.auth.client import AuthClient


def _get_backend_base_url():
    value = os.getenv("BACKEND_BASE_URL")
    if not value:
        raise RuntimeError("BACKEND_BASE_URL is not set")
    return value


def login_handler(enrollment_id: str, password: str) -> dict:
    if not enrollment_id or not password:
        raise ValueError("enrollment_id and password are required")

    auth = AuthClient(base_url=_get_backend_base_url())

    session = auth.login_with_enrollment(
        enrollment_id=enrollment_id,
        password=password,
    )

    return {
        "user": session.user,
        "token": session.token,
    }
