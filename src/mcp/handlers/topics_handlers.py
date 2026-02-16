from src.controllers.topics_controller import (
    get_topics,
    get_topics_by_level,
    get_topic_detail,
    get_topics_by_tags,
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
def get_topic_detail_handler(
    *,
    backend_client: BackendClient,
    topic_id: str,
):
    return get_topic_detail(
        backend_client=backend_client,
        topic_id=topic_id,
    )


@with_error_handling
@with_backend_client
def get_topics_by_tags_handler(
    *, 
    backend_client: BackendClient, 
    tags: list[str], 
    limit: int, 
    offset: int
):
    return get_topics_by_tags(
        backend_client=backend_client,
        tags=tags,
        limit=limit,
        offset=offset,
    )
