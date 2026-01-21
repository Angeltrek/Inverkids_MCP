from src.controllers.tags_controller import get_tags
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_tags_handler(
    *, 
    backend_client: BackendClient, 
    limit: int, 
    offset: int
):
    return get_tags(
        backend_client=backend_client,
        limit=limit,
        offset=offset,
    )
