from src.controllers.schools_controller import get_schools
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_schools_handler(
    *,
    backend_client: BackendClient,
    white_label: str | None = None,
):
    return get_schools(
        backend_client=backend_client,
        white_label=white_label,
    )
