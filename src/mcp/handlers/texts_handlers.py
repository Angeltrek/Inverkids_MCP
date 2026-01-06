from src.controllers.texts_controller import (
    get_texts,
    get_texts_by_module,
    get_texts_by_topic,
    get_texts_by_level,
    get_home_texts,
    get_entry_texts,
    get_texts_by_type,
    get_texts_by_skill,
    search_texts_by_name,
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
):
    return get_texts(
        backend_client=backend_client,
        module_id=module_id,
    )


@with_error_handling
@with_backend_client
def get_texts_by_module_handler(
    *,
    backend_client: BackendClient,
    module_id: str,
):
    return get_texts_by_module(
        backend_client=backend_client,
        module_id=module_id,
    )


@with_error_handling
@with_backend_client
def get_texts_by_topic_handler(
    *,
    backend_client: BackendClient,
    topic_id: str,
):
    return get_texts_by_topic(
        backend_client=backend_client,
        topic_id=topic_id,
    )


@with_error_handling
@with_backend_client
def get_texts_by_level_handler(
    *,
    backend_client: BackendClient,
    level: str,
):
    return get_texts_by_level(
        backend_client=backend_client,
        level=level,
    )


@with_error_handling
@with_backend_client
def get_home_texts_handler(
    *,
    backend_client: BackendClient,
):
    return get_home_texts(backend_client=backend_client)


@with_error_handling
@with_backend_client
def get_entry_texts_handler(
    *,
    backend_client: BackendClient,
):
    return get_entry_texts(backend_client=backend_client)


@with_error_handling
@with_backend_client
def get_texts_by_type_handler(
    *,
    backend_client: BackendClient,
    text_type: str,
):
    return get_texts_by_type(
        backend_client=backend_client,
        text_type=text_type,
    )


@with_error_handling
@with_backend_client
def get_texts_by_skill_handler(
    *,
    backend_client: BackendClient,
    skill_id: str,
):
    return get_texts_by_skill(
        backend_client=backend_client,
        skill_id=skill_id,
    )


@with_error_handling
@with_backend_client
def search_texts_by_name_handler(
    *,
    backend_client: BackendClient,
    query: str,
):
    return search_texts_by_name(
        backend_client=backend_client,
        query=query,
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
