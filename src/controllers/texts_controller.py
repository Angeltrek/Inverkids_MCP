from src.infrastructure.config.constants.endpoint_constants import (
    MCP_TEXTS,
    MCP_TEXTS_BY_MODULE,
    MCP_TEXTS_BY_TOPIC,
    MCP_TEXTS_BY_LEVEL,
    MCP_TEXTS_BY_TYPE,
    MCP_TEXTS_BY_SKILL,
    MCP_TEXT_DETAIL,
)
from src.infrastructure.http.backend_client import BackendClient


def get_texts(
    *,
    backend_client: BackendClient,
    module_id: str | None = None,
    limit: int = 20,
    offset: int = 0,
):
    return backend_client.get(
        MCP_TEXTS,
        params={
            "module_id": module_id,
            "limit": limit,
            "offset": offset,
        },
    )


def get_texts_by_module(
    *,
    backend_client: BackendClient,
    module_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return backend_client.get(
        MCP_TEXTS_BY_MODULE,
        params={
            "module_id": module_id,
            "limit": limit,
            "offset": offset,
        },
    )


def get_texts_by_topic(
    *,
    backend_client: BackendClient,
    topic_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return backend_client.get(
        MCP_TEXTS_BY_TOPIC,
        params={
            "topic_id": topic_id,
            "limit": limit,
            "offset": offset,
        },
    )


def get_texts_by_level(
    *,
    backend_client: BackendClient,
    level: str,
    limit: int = 20,
    offset: int = 0,
):
    return backend_client.get(
        MCP_TEXTS_BY_LEVEL,
        params={
            "level": level,
            "limit": limit,
            "offset": offset,
        },
    )


def get_texts_by_type(
    *,
    backend_client: BackendClient,
    text_type: str,
    limit: int = 20,
    offset: int = 0,
):
    return backend_client.get(
        MCP_TEXTS_BY_TYPE,
        params={
            "text_type": text_type,
            "limit": limit,
            "offset": offset,
        },
    )


def get_texts_by_skill(
    *,
    backend_client: BackendClient,
    skill_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return backend_client.get(
        MCP_TEXTS_BY_SKILL,
        params={
            "skill_id": skill_id,
            "limit": limit,
            "offset": offset,
        },
    )


def get_text_detail(
    *,
    backend_client: BackendClient,
    text_id: str,
):
    return backend_client.get(
        MCP_TEXT_DETAIL,
        params={"text_id": text_id},
    )
