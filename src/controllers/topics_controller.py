from src.infrastructure.config.constants.endpoint_constants import (
    MCP_TOPICS,
    MCP_TOPICS_BY_LEVEL,
    MCP_TOPIC_DETAIL,
    MCP_TOPICS_BY_TAGS,
)
from src.infrastructure.http.backend_client import BackendClient


def get_topics(
    *,
    backend_client: BackendClient,
    module_id: str | None,
    limit: int,
    offset: int,
):
    return backend_client.get(
        MCP_TOPICS,
        params={
            "module_id": module_id,
            "limit": limit,
            "offset": offset,
        },
    )


def get_topics_by_level(
    *,
    backend_client: BackendClient,
    level: str,
    limit: int,
    offset: int,
):
    return backend_client.get(
        MCP_TOPICS_BY_LEVEL,
        params={
            "level": level,
            "limit": limit,
            "offset": offset,
        },
    )


def get_topic_detail(
    *,
    backend_client: BackendClient,
    topic_id: str,
):
    return backend_client.get(
        MCP_TOPIC_DETAIL,
        params={"topic_id": topic_id},
    )


def get_topics_by_tags(
    *, 
    backend_client: BackendClient, 
    tags: list[str], 
    limit: int, 
    offset: int
):
    params = {
        "limit": limit,
        "offset": offset,
    }

    for tag in tags:
        params.setdefault("tags[]", []).append(tag)

    return backend_client.get(
        MCP_TOPICS_BY_TAGS,
        params=params,
    )