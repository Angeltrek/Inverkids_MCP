from src.controllers.catalog_controller import get_full_catalog
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_full_catalog_handler(
    *,
    level: str,
    white_label: str,
    user_lang: str,
    backend_client: BackendClient,
):
    return get_full_catalog(
        level,
        white_label,
        user_lang,
        backend_client,
    )
