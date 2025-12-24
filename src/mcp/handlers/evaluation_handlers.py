from src.controllers.evaluation_controller import (
    get_grades,
    get_feedback,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_grades_handler(
    *,
    backend_client: BackendClient,
    level: str | None = None,
    group_id: str | None = None,
    student_id: str | None = None,
    module_id: str | None = None,
    topic_id: str | None = None,
    activity_id: str | None = None,
    grade_type: str | None = None,
):
    return get_grades(
        backend_client=backend_client,
        level=level,
        group_id=group_id,
        student_id=student_id,
        module_id=module_id,
        topic_id=topic_id,
        activity_id=activity_id,
        grade_type=grade_type,
    )


@with_error_handling
@with_backend_client
def get_feedback_handler(
    *,
    backend_client: BackendClient,
    level: str | None = None,
    group_id: str | None = None,
    student_id: str | None = None,
    module_id: str | None = None,
    topic_id: str | None = None,
    rating: int | None = None,
):
    return get_feedback(
        backend_client=backend_client,
        level=level,
        group_id=group_id,
        student_id=student_id,
        module_id=module_id,
        topic_id=topic_id,
        rating=rating,
    )
