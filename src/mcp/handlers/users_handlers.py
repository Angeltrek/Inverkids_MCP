from src.controllers.users_controller import (
    get_current_user,
    get_users,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_users_handler(*, 
    backend_client: BackendClient
):
    return get_users(backend_client)


@with_error_handling
@with_backend_client
def get_current_user_handler(
    *,
    backend_client: BackendClient,
):
    return get_current_user(backend_client)