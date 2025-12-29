from src.mcp.app import mcp
from src.mcp.handlers.evaluation_handlers import (
    get_feedback_handler,
    get_grades_handler,
)


@mcp.tool(
    name="get_grades",
    description=(
        "List student grades filtered by academic context. "
        "Access is role-restricted. "
        "Paginated (default offset: 10, max limit: 50)."
    ),
)

def get_grades(
    token: str,
    level: str | None = None,
    group_id: str | None = None,
    student_id: str | None = None,
    module_id: str | None = None,
    topic_id: str | None = None,
    activity_id: str | None = None,
    grade_type: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
):
    return get_grades_handler(
        token=token,
        level=level,
        group_id=group_id,
        student_id=student_id,
        module_id=module_id,
        topic_id=topic_id,
        activity_id=activity_id,
        grade_type=grade_type,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_feedback",
    description=(
        "List student feedback and ratings filtered by academic context. "
        "Access is role-restricted. "
        "Paginated (default offset: 10, max limit: 50)."
    ),
)

def get_feedback(
    token: str,
    level: str | None = None,
    group_id: str | None = None,
    student_id: str | None = None,
    module_id: str | None = None,
    topic_id: str | None = None,
    rating: int | None = None,
    limit: int | None = None,
    offset: int | None = None,
):
    return get_feedback_handler(
        token=token,
        level=level,
        group_id=group_id,
        student_id=student_id,
        module_id=module_id,
        topic_id=topic_id,
        rating=rating,
        limit=limit,
        offset=offset,
    )
