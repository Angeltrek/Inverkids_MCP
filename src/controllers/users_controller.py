from src.infrastructure.config.constants.endpoint_constants import (
    MCP_PROFILE,
    MCP_USERS,
)
from src.infrastructure.http.backend_client import BackendClient


def get_users(backend_client: BackendClient):
    return backend_client.get(MCP_USERS)


def get_current_user(backend_client: BackendClient):
    return backend_client.get(MCP_PROFILE)
