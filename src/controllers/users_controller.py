from src.infrastructure.config.constants.endpoint_constants import (
    MCP_USERS_LIST,
    MCP_USER_DETAIL,
)
from src.infrastructure.http.backend_client import BackendClient

def get_users_list(
    *,
    backend_client: BackendClient,
):
    return backend_client.get(MCP_USERS_LIST)


def get_user_detail(
    *,
    backend_client: BackendClient,
    user_id: str,
):
    return backend_client.get(
        MCP_USER_DETAIL,
        params={"user_id": user_id},
    )
