from src.infrastructure.config.constants.endpoint_constants import (
    MCP_ACTIVITIES_BY_MODULE,
    MCP_ACTIVITIES_BY_SKILL,
    MCP_ACTIVITIES_BY_LEVEL,
    MCP_ACTIVITY_DETAIL,
    MCP_GENERATE_ACTIVITY_PDF,
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


def get_activity_detail(
    *,
    backend_client: BackendClient,
    activity_id: str,
):
    return backend_client.get(
        MCP_ACTIVITY_DETAIL,
        params={"activity_id": activity_id},
    )


def generate_activity_pdf(
    *,
    backend_client: BackendClient,
    activity: dict,
):
    return backend_client.post(
        MCP_GENERATE_ACTIVITY_PDF,
        json={
            "activity": activity
        },
    )