from src.mcp.app import mcp
from src.mcp.handlers.grades_handlers import (
    get_grades_by_level_handler,
    get_grades_by_group_handler,
    get_grades_by_student_handler,
    get_grades_by_module_handler,
    get_grades_by_topic_handler,
    get_grades_by_activity_handler,
    get_grade_detail_handler,
    get_grades_summary_handler,
)


@mcp.tool(
    name="get_grades_by_level",
    description="List grades for all students in a given academic level.",
)
def get_grades_by_level(level: str):
    return get_grades_by_level_handler(level=level)


@mcp.tool(
    name="get_grades_by_group",
    description="List grades for a specific group.",
)
def get_grades_by_group(group_id: str):
    return get_grades_by_group_handler(group_id=group_id)


@mcp.tool(
    name="get_grades_by_student",
    description="List grades for a student (defaults to current user if omitted).",
)
def get_grades_by_student(student_id: str | None = None):
    return get_grades_by_student_handler(student_id=student_id)


@mcp.tool(
    name="get_grades_by_module",
    description="List grades associated with a module.",
)
def get_grades_by_module(module_id: str):
    return get_grades_by_module_handler(module_id=module_id)


@mcp.tool(
    name="get_grades_by_topic",
    description="List grades associated with a topic.",
)
def get_grades_by_topic(topic_id: str):
    return get_grades_by_topic_handler(topic_id=topic_id)


@mcp.tool(
    name="get_grades_by_activity",
    description="List grades associated with an activity.",
)
def get_grades_by_activity(activity_id: str):
    return get_grades_by_activity_handler(activity_id=activity_id)


@mcp.tool(
    name="get_grade_detail",
    description="Get full grade detail by grade ID.",
)
def get_grade_detail(grade_id: str):
    return get_grade_detail_handler(grade_id=grade_id)


@mcp.tool(
    name="get_grades_summary",
    description="Get grade summary (count, avg, min, max) for a module.",
)
def get_grades_summary(module_id: str):
    return get_grades_summary_handler(module_id=module_id)
