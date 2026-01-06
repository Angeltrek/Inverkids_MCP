from src.infrastructure.config.constants.endpoint_constants import (
    MCP_TOPICS,
    MCP_TOPICS_BY_LEVEL,
    MCP_TOPICS_WITH_QUIZ,
    MCP_TOPICS_WITH_EVAL,
    MCP_TOPICS_WITH_DIAG,
    MCP_TOPICS_WITHOUT_ASSESSMENT,
    MCP_LAST_TOPIC_BY_MODULE,
    MCP_SEARCH_TOPICS_BY_NAME,
    MCP_SEARCH_TOPICS_BY_NAME_IN_MODULE,
    MCP_TOPIC_DETAIL,
)
from src.infrastructure.http.backend_client import BackendClient


def get_topics(
    *,
    backend_client: BackendClient,
    module_id: str | None = None,
):
    return backend_client.get(
        MCP_TOPICS,
        params={"module_id": module_id},
    )


def get_topics_by_level(
    *,
    backend_client: BackendClient,
    level: str,
):
    return backend_client.get(
        MCP_TOPICS_BY_LEVEL,
        params={"level": level},
    )


def get_topics_with_quiz(
    *,
    backend_client: BackendClient,
):
    return backend_client.get(MCP_TOPICS_WITH_QUIZ)


def get_topics_with_eval(
    *,
    backend_client: BackendClient,
):
    return backend_client.get(MCP_TOPICS_WITH_EVAL)


def get_topics_with_diag(
    *,
    backend_client: BackendClient,
):
    return backend_client.get(MCP_TOPICS_WITH_DIAG)


def get_topics_without_assessment(
    *,
    backend_client: BackendClient,
):
    return backend_client.get(MCP_TOPICS_WITHOUT_ASSESSMENT)


def get_last_topic_by_module(
    *,
    backend_client: BackendClient,
    module_id: str,
):
    return backend_client.get(
        MCP_LAST_TOPIC_BY_MODULE,
        params={"module_id": module_id},
    )


def search_topics_by_name(
    *,
    backend_client: BackendClient,
    query: str,
):
    return backend_client.get(
        MCP_SEARCH_TOPICS_BY_NAME,
        params={"q": query},
    )


def search_topics_by_name_in_module(
    *,
    backend_client: BackendClient,
    module_id: str,
    query: str,
):
    return backend_client.get(
        MCP_SEARCH_TOPICS_BY_NAME_IN_MODULE,
        params={
            "module_id": module_id,
            "q": query,
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
