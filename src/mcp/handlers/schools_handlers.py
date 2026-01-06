from src.controllers.schools_controller import (
    get_schools_list,
    get_school_detail,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_schools_list_handler(
    *,
    backend_client: BackendClient,
):
    return get_schools_list(backend_client=backend_client)


@with_error_handling
@with_backend_client
def get_school_detail_handler(
    *,
    backend_client: BackendClient,
    school_id: str,
):
    return get_school_detail(
        backend_client=backend_client,
        school_id=school_id,
    )
