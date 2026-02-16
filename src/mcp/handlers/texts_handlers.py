from src.controllers.texts_controller import (
    get_texts,
    get_texts_by_module,
    get_texts_by_topic,
    get_texts_by_level,
    get_texts_by_type,
    get_texts_by_skill,
    get_text_detail,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_texts_handler(
    *,
    backend_client: BackendClient,
    module_id: str | None = None,
    limit: int = 20,
    offset: int = 0,
):
    return get_texts(
        backend_client=backend_client,
        module_id=module_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_texts_by_module_handler(
    *,
    backend_client: BackendClient,
    module_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_texts_by_module(
        backend_client=backend_client,
        module_id=module_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_texts_by_topic_handler(
    *,
    backend_client: BackendClient,
    topic_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_texts_by_topic(
        backend_client=backend_client,
        topic_id=topic_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_texts_by_level_handler(
    *,
    backend_client: BackendClient,
    level: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_texts_by_level(
        backend_client=backend_client,
        level=level,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_texts_by_type_handler(
    *,
    backend_client: BackendClient,
    text_type: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_texts_by_type(
        backend_client=backend_client,
        text_type=text_type,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_texts_by_skill_handler(
    *,
    backend_client: BackendClient,
    skill_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_texts_by_skill(
        backend_client=backend_client,
        skill_id=skill_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_text_detail_handler(
    *,
    backend_client: BackendClient,
    text_id: str,
):
    return get_text_detail(
        backend_client=backend_client,
        text_id=text_id,
    )
