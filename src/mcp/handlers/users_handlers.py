from src.controllers.users_controller import (
    get_users_list,
    get_user_detail,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_users_list_handler(
    *,
    backend_client: BackendClient,
    limit: int = 20,
    offset: int = 0,
):
    return get_users_list(
        backend_client=backend_client,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_user_detail_handler(
    *,
    backend_client: BackendClient,
    user_id: str,
):
    return get_user_detail(
        backend_client=backend_client,
        user_id=user_id,
    )
