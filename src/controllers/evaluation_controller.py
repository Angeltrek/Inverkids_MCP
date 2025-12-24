from src.infrastructure.config.constants.endpoint_constants import (
    MCP_GRADES,
    MCP_FEEDBACK,
)
from src.infrastructure.http.backend_client import BackendClient


def get_grades(
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
    return backend_client.get(
        MCP_GRADES,
        params={
            "level": level,
            "group_id": group_id,
            "student_id": student_id,
            "module_id": module_id,
            "topic_id": topic_id,
            "activity_id": activity_id,
            "grade_type": grade_type,
        },
    )


def get_feedback(
    *,
    backend_client: BackendClient,
    level: str | None = None,
    group_id: str | None = None,
    student_id: str | None = None,
    module_id: str | None = None,
    topic_id: str | None = None,
    rating: int | None = None,
):
    return backend_client.get(
        MCP_FEEDBACK,
        params={
            "level": level,
            "group_id": group_id,
            "student_id": student_id,
            "module_id": module_id,
            "topic_id": topic_id,
            "rating": rating,
        },
    )
