from src.mcp.app import mcp
from src.mcp.handlers.evaluation_handlers import (
    get_grades_handler,
    get_feedback_handler,
)


@mcp.tool(
    name="get_grades",
    description="Retrieve student grades. Access is automatically restricted based on user role.",
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
    )


@mcp.tool(
    name="get_feedback",
    description="Retrieve student feedback and ratings. Access is restricted by user role.",
)
def get_feedback(
    token: str,
    level: str | None = None,
    group_id: str | None = None,
    student_id: str | None = None,
    module_id: str | None = None,
    topic_id: str | None = None,
    rating: int | None = None,
):
    return get_feedback_handler(
        token=token,
        level=level,
        group_id=group_id,
        student_id=student_id,
        module_id=module_id,
        topic_id=topic_id,
        rating=rating,
    )
