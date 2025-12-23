from src.infrastructure.http.backend_client import BackendClient
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.controllers.courses_controller import (
    get_courses,
    get_courses_by_user_type,
    get_courses_names,
    get_courses_data,
)


@with_error_handling
@with_backend_client
def get_courses_handler(*, backend_client: BackendClient):
    return get_courses(backend_client)


@with_error_handling
@with_backend_client
def get_courses_by_user_type_handler(
    *,
    user_type: str,
    backend_client: BackendClient,
):
    return get_courses_by_user_type(user_type, backend_client)


@with_error_handling
@with_backend_client
def get_courses_names_handler(
    *,
    level: str,
    label: str,
    backend_client: BackendClient,
):
    return get_courses_names(level, label, backend_client)


@with_error_handling
@with_backend_client
def get_courses_data_handler(
    *,
    level: str,
    label: str,
    backend_client: BackendClient,
):
    return get_courses_data(level, label, backend_client)
