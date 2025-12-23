import os
from src.infrastructure.http.backend_client import BackendClient


def get_backend_client(token: str) -> BackendClient:
    base_url = os.getenv("BACKEND_BASE_URL")
    if not base_url:
        raise RuntimeError("BACKEND_BASE_URL is not set")

    if not token:
        raise PermissionError("Authentication token required")

    return BackendClient(
        base_url=base_url,
        token=token,
    )
