from src.controllers.groups_controller import (
    get_groups_by_school,
    get_group_detail,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_groups_by_school_handler(
    *,
    backend_client: BackendClient,
    school_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_groups_by_school(
        backend_client=backend_client,
        school_id=school_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_group_detail_handler(
    *,
    backend_client: BackendClient,
    group_id: str,
):
    return get_group_detail(
        backend_client=backend_client,
        group_id=group_id,
    )
