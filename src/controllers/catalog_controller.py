from src.infrastructure.config.constants.endpoint_constants import (
    CATALOG_FULL,
    MCP_ACTIVITIES,
    MCP_MODULES,
    MCP_TEXTS,
    MCP_TOPICS,
)
from src.infrastructure.http.backend_client import BackendClient


def get_full_catalog(
    level: str,
    white_label: str,
    user_lang: str,
    backend_client: BackendClient,
):
    return backend_client.get(
        CATALOG_FULL,
        params={
            "level": level,
            "white_label": white_label,
            "userLang": user_lang,
        },
    )


def get_modules(
    *,
    backend_client: BackendClient,
    level: str | None = None,
    white_label: str | None = None,
    module_id: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
):
    return backend_client.get(
        MCP_MODULES,
        params={
            "level": level,
            "white_label": white_label,
            "module_id": module_id,
            "limit": limit,
            "offset": offset,
        },
    )


def get_topics(
    *,
    backend_client: BackendClient,
    module_id: str | None = None,
    level: str | None = None,
    topic_id: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
):
    return backend_client.get(
        MCP_TOPICS,
        params={
            "module_id": module_id,
            "level": level,
            "topic_id": topic_id,
            "limit": limit,
            "offset": offset,
        },
    )


def get_activities(
    *,
    backend_client: BackendClient,
    topic_id: str | None = None,
    module_id: str | None = None,
    level: str | None = None,
    activity_id: str | None = None,
    activity_type: str | None = None,
    include_content: bool = False,
    limit: int | None = None,
    offset: int | None = None,
):
    return backend_client.get(
        MCP_ACTIVITIES,
        params={
            "topic_id": topic_id,
            "module_id": module_id,
            "level": level,
            "activity_id": activity_id,
            "activity_type": activity_type,
            "include_content": str(include_content).lower(),
            "limit": limit,
            "offset": offset,
        },
    )


def get_texts(
    *,
    backend_client: BackendClient,
    topic_id: str | None = None,
    module_id: str | None = None,
    level: str | None = None,
    text_id: str | None = None,
    include_content: bool = False,
    limit: int | None = None,
    offset: int | None = None,
):
    return backend_client.get(
        MCP_TEXTS,
        params={
            "topic_id": topic_id,
            "module_id": module_id,
            "level": level,
            "text_id": text_id,
            "include_content": str(include_content).lower(),
            "limit": limit,
            "offset": offset,
        },
    )