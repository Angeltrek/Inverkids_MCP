from src.controllers.modules_controller import (
    get_modules,
    get_modules_by_level,
    get_modules_by_white_label,
    get_modules_by_level_and_white_label,
    get_modules_by_number,
    get_last_module_by_level,
    search_modules_by_name,
    get_module_detail,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_modules_handler(
    *,
    backend_client: BackendClient,
):
    return get_modules(backend_client=backend_client)


@with_error_handling
@with_backend_client
def get_modules_by_level_handler(
    *,
    backend_client: BackendClient,
    level: str,
):
    return get_modules_by_level(
        backend_client=backend_client,
        level=level,
    )


@with_error_handling
@with_backend_client
def get_modules_by_white_label_handler(
    *,
    backend_client: BackendClient,
    white_label: str,
):
    return get_modules_by_white_label(
        backend_client=backend_client,
        white_label=white_label,
    )


@with_error_handling
@with_backend_client
def get_modules_by_level_and_white_label_handler(
    *,
    backend_client: BackendClient,
    level: str,
    white_label: str,
):
    return get_modules_by_level_and_white_label(
        backend_client=backend_client,
        level=level,
        white_label=white_label,
    )


@with_error_handling
@with_backend_client
def get_modules_by_number_handler(
    *,
    backend_client: BackendClient,
    module_number: int,
):
    return get_modules_by_number(
        backend_client=backend_client,
        module_number=module_number,
    )


@with_error_handling
@with_backend_client
def get_last_module_by_level_handler(
    *,
    backend_client: BackendClient,
    level: str,
):
    return get_last_module_by_level(
        backend_client=backend_client,
        level=level,
    )


@with_error_handling
@with_backend_client
def search_modules_by_name_handler(
    *,
    backend_client: BackendClient,
    query: str,
):
    return search_modules_by_name(
        backend_client=backend_client,
        query=query,
    )


@with_error_handling
@with_backend_client
def get_module_detail_handler(
    *,
    backend_client: BackendClient,
    module_id: str,
):
    return get_module_detail(
        backend_client=backend_client,
        module_id=module_id,
    )
