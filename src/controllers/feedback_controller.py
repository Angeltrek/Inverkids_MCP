from src.infrastructure.config.constants.endpoint_constants import (
    MCP_FEEDBACK_LIST,
    MCP_FEEDBACK_DETAIL,
)
from src.infrastructure.http.backend_client import BackendClient


def get_feedback_list(
    *,
    backend_client: BackendClient,
    module_id: str | None = None,
    topic_id: str | None = None,
    limit: int = 20,
    offset: int = 0,
):
    return backend_client.get(
        MCP_FEEDBACK_LIST,
        params={
            "module_id": module_id,
            "topic_id": topic_id,
            "limit": limit,
            "offset": offset,
        },
    )


def get_feedback_detail(
    *,
    backend_client: BackendClient,
    feedback_id: str,
):
    return backend_client.get(
        MCP_FEEDBACK_DETAIL,
        params={"feedback_id": feedback_id},
    )
