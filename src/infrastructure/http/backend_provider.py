import os

from src.infrastructure.http.backend_client import BackendClient
from src.infrastructure.config.settings.settings import load_settings

_settings = load_settings()


def get_backend_client(token: str | None = None) -> BackendClient:

    auth_token = token or _settings.backend.auth_token

    return BackendClient(
        base_url=_settings.backend.base_url,
        token=auth_token,
        timeout=_settings.backend.timeout,
        max_retries=_settings.backend.max_retries,
    )
