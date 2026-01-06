from src.controllers.topics_controller import (
    get_topics,
    get_topics_by_level,
    get_topics_with_quiz,
    get_topics_with_eval,
    get_topics_with_diag,
    get_topics_without_assessment,
    get_last_topic_by_module,
    search_topics_by_name,
    search_topics_by_name_in_module,
    get_topic_detail,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_topics_handler(
    *,
    backend_client: BackendClient,
    module_id: str | None,
    limit: int,
    offset: int,
):
    return get_topics(
        backend_client=backend_client,
        module_id=module_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_topics_by_level_handler(
    *,
    backend_client: BackendClient,
    level: str,
    limit: int,
    offset: int,
):
    return get_topics_by_level(
        backend_client=backend_client,
        level=level,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_topics_with_quiz_handler(
    *,
    backend_client: BackendClient,
    limit: int,
    offset: int,
):
    return get_topics_with_quiz(
        backend_client=backend_client,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_topics_with_eval_handler(
    *,
    backend_client: BackendClient,
    limit: int,
    offset: int,
):
    return get_topics_with_eval(
        backend_client=backend_client,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_topics_with_diag_handler(
    *,
    backend_client: BackendClient,
    limit: int,
    offset: int,
):
    return get_topics_with_diag(
        backend_client=backend_client,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_topics_without_assessment_handler(
    *,
    backend_client: BackendClient,
    limit: int,
    offset: int,
):
    return get_topics_without_assessment(
        backend_client=backend_client,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_last_topic_by_module_handler(
    *,
    backend_client: BackendClient,
    module_id: str,
):
    return get_last_topic_by_module(
        backend_client=backend_client,
        module_id=module_id,
    )


@with_error_handling
@with_backend_client
def search_topics_by_name_handler(
    *,
    backend_client: BackendClient,
    query: str,
    limit: int,
    offset: int,
):
    return search_topics_by_name(
        backend_client=backend_client,
        query=query,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def search_topics_by_name_in_module_handler(
    *,
    backend_client: BackendClient,
    module_id: str,
    query: str,
    limit: int,
    offset: int,
):
    return search_topics_by_name_in_module(
        backend_client=backend_client,
        module_id=module_id,
        query=query,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_topic_detail_handler(
    *,
    backend_client: BackendClient,
    topic_id: str,
):
    return get_topic_detail(
        backend_client=backend_client,
        topic_id=topic_id,
    )
