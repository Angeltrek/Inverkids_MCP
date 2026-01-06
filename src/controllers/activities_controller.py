from src.infrastructure.config.constants.endpoint_constants import (
    MCP_ACTIVITIES_BY_MODULE,
    MCP_ACTIVITIES_BY_TYPE,
    MCP_FIRST_ACTIVITY_BY_TOPIC,
    MCP_EXTRA_ACTIVITIES,
    MCP_ACTIVITIES_BY_SKILL,
    MCP_ACTIVITIES_BY_LEVEL,
    MCP_SEARCH_ACTIVITIES_BY_NAME,
    MCP_ACTIVITY_DETAIL,
)
from src.infrastructure.http.backend_client import BackendClient


def get_activities_by_module(
    *,
    backend_client: BackendClient,
    module_id: str,
    limit: int,
    offset: int,
):
    return backend_client.get(
        MCP_ACTIVITIES_BY_MODULE,
        params={
            "module_id": module_id,
            "limit": limit,
            "offset": offset,
        },
    )


def get_activities_by_type(
    *,
    backend_client: BackendClient,
    activity_type: str,
    limit: int,
    offset: int,
):
    return backend_client.get(
        MCP_ACTIVITIES_BY_TYPE,
        params={
            "activity_type": activity_type,
            "limit": limit,
            "offset": offset,
        },
    )


def get_first_activity_by_topic(
    *,
    backend_client: BackendClient,
    topic_id: str,
):
    return backend_client.get(
        MCP_FIRST_ACTIVITY_BY_TOPIC,
        params={"topic_id": topic_id},
    )


def get_extra_activities(
    *,
    backend_client: BackendClient,
    limit: int,
    offset: int,
):
    return backend_client.get(
        MCP_EXTRA_ACTIVITIES,
        params={"limit": limit, "offset": offset},
    )


def get_activities_by_skill(
    *,
    backend_client: BackendClient,
    skill_id: str,
    limit: int,
    offset: int,
):
    return backend_client.get(
        MCP_ACTIVITIES_BY_SKILL,
        params={
            "skill_id": skill_id,
            "limit": limit,
            "offset": offset,
        },
    )


def get_activities_by_level(
    *,
    backend_client: BackendClient,
    level: str,
    limit: int,
    offset: int,
):
    return backend_client.get(
        MCP_ACTIVITIES_BY_LEVEL,
        params={
            "level": level,
            "limit": limit,
            "offset": offset,
        },
    )


def search_activities_by_name(
    *,
    backend_client: BackendClient,
    query: str,
    limit: int,
    offset: int,
):
    return backend_client.get(
        MCP_SEARCH_ACTIVITIES_BY_NAME,
        params={
            "q": query,
            "limit": limit,
            "offset": offset,
        },
    )


def get_activity_detail(
    *,
    backend_client: BackendClient,
    activity_id: str,
):
    return backend_client.get(
        MCP_ACTIVITY_DETAIL,
        params={"activity_id": activity_id},
    )
