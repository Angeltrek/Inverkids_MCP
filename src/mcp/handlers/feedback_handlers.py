from src.controllers.feedback_controller import (
    get_feedback_list,
    get_feedback_detail,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_feedback_list_handler(
    *,
    backend_client: BackendClient,
    module_id: str | None = None,
    topic_id: str | None = None,
    limit: int = 20,
    offset: int = 0,
):
    return get_feedback_list(
        backend_client=backend_client,
        module_id=module_id,
        topic_id=topic_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_feedback_detail_handler(
    *,
    backend_client: BackendClient,
    feedback_id: str,
):
    return get_feedback_detail(
        backend_client=backend_client,
        feedback_id=feedback_id,
    )
