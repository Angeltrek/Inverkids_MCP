from src.controllers.grades_controller import (
    get_grades_by_level,
    get_grades_by_group,
    get_grades_by_student,
    get_grades_by_module,
    get_grades_by_topic,
    get_grades_by_activity,
    get_grade_detail,
    get_grades_summary,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_grades_by_level_handler(
    *,
    backend_client: BackendClient,
    level: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_grades_by_level(
        backend_client=backend_client,
        level=level,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_grades_by_group_handler(
    *,
    backend_client: BackendClient,
    group_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_grades_by_group(
        backend_client=backend_client,
        group_id=group_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_grades_by_student_handler(
    *,
    backend_client: BackendClient,
    student_id: str | None = None,
    limit: int = 20,
    offset: int = 0,
):
    return get_grades_by_student(
        backend_client=backend_client,
        student_id=student_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_grades_by_module_handler(
    *,
    backend_client: BackendClient,
    module_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_grades_by_module(
        backend_client=backend_client,
        module_id=module_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_grades_by_topic_handler(
    *,
    backend_client: BackendClient,
    topic_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_grades_by_topic(
        backend_client=backend_client,
        topic_id=topic_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_grades_by_activity_handler(
    *,
    backend_client: BackendClient,
    activity_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_grades_by_activity(
        backend_client=backend_client,
        activity_id=activity_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_grade_detail_handler(
    *,
    backend_client: BackendClient,
    grade_id: str,
):
    return get_grade_detail(
        backend_client=backend_client,
        grade_id=grade_id,
    )


@with_error_handling
@with_backend_client
def get_grades_summary_handler(
    *,
    backend_client: BackendClient,
    module_id: str,
):
    return get_grades_summary(
        backend_client=backend_client,
        module_id=module_id,
    )
