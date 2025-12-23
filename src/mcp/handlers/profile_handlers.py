from src.infrastructure.http.backend_client import BackendClient
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.controllers.profile_controller import get_profile


@with_error_handling
@with_backend_client
def get_profile_handler(
    *,
    backend_client: BackendClient,
):
    return get_profile(backend_client)
