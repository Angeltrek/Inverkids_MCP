from src.infrastructure.http.backend_client import BackendClient
from src.infrastructure.config.constants.endpoint_constants import (
    MCP_USERS,
    MCP_PROFILE,
)


def get_users(backend_client: BackendClient):
    return backend_client.get(MCP_USERS)


def get_current_user(backend_client: BackendClient):
    return backend_client.get(MCP_PROFILE)
