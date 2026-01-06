from src.infrastructure.config.constants.endpoint_constants import (
    MCP_GROUPS_LIST,
    MCP_GROUP_DETAIL,
)
from src.infrastructure.http.backend_client import BackendClient


def get_groups_by_school(
    *,
    backend_client: BackendClient,
    school_id: str,
):
    return backend_client.get(
        MCP_GROUPS_LIST,
        params={"school_id": school_id},
    )


def get_group_detail(
    *,
    backend_client: BackendClient,
    group_id: str,
):
    return backend_client.get(
        MCP_GROUP_DETAIL,
        params={"group_id": group_id},
    )
