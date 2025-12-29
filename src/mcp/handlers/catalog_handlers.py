from src.controllers.catalog_controller import (
    get_activities,
    get_full_catalog,
    get_modules,
    get_texts,
    get_topics,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_full_catalog_handler(
    *,
    level: str,
    white_label: str,
    user_lang: str,
    backend_client: BackendClient,
):
    return get_full_catalog(
        level,
        white_label,
        user_lang,
        backend_client,
    )


@with_error_handling
@with_backend_client
def get_modules_handler(
    *,
    backend_client: BackendClient,
    level: str | None = None,
    white_label: str | None = None,
    module_id: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
):
    return get_modules(
        backend_client=backend_client,
        level=level,
        white_label=white_label,
        module_id=module_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_topics_handler(
    *,
    backend_client: BackendClient,
    module_id: str | None = None,
    level: str | None = None,
    topic_id: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
):
    return get_topics(
        backend_client=backend_client,
        module_id=module_id,
        level=level,
        topic_id=topic_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_activities_handler(
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
    return get_activities(
        backend_client=backend_client,
        topic_id=topic_id,
        module_id=module_id,
        level=level,
        activity_id=activity_id,
        activity_type=activity_type,
        include_content=include_content,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_texts_handler(
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
    return get_texts(
        backend_client=backend_client,
        topic_id=topic_id,
        module_id=module_id,
        level=level,
        text_id=text_id,
        include_content=include_content,
        limit=limit,
        offset=offset,
    )
