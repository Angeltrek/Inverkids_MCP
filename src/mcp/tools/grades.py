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
    description=(
        "Retrieve grade records for students in a specific academic level. This tool provides"
        "aggregate data for level-wide analysis (not individual student PII)."
        "Parameters:"
        "- level: Academic level"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
        "Note: Grades are educational performance metrics, not personally identifiable."
    ),
)
def get_grades_by_level(
    level: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_grades_by_level_handler(
        level=level,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_grades_by_group",
    description=(
        "Get grade records for a specific learning group/class."
        "Use this for class-level performance analysis."
        "Parameters:"
        "- group_id: Internal group identifier (use internally)"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_grades_by_group(
    group_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_grades_by_group_handler(
        group_id=group_id,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_grades_by_student",
    description=(
        "Access grade records for a specific student."
        "Use this to show students their own progress and performance."
        "Parameters:"
        "- student_id: Internal user identifier (optional, use internally)"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_grades_by_student(
    student_id: str | None = None,
    limit: int = 20,
    offset: int = 0,
):
    return get_grades_by_student_handler(
        student_id=student_id,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_grades_by_module",
    description=(
        "Filter grade records by learning module. Useful for understanding student"
        "performance within a specific curriculum module."
        "Parameters:"
        "- module_id: Internal module identifier (use internally)"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_grades_by_module(
    module_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_grades_by_module_handler(
        module_id=module_id,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_grades_by_topic",
    description=(
        "Filter grade records by learning topic. Topics are subdivisions of modules"
        "focusing on specific concepts. Use this for topic-level performance analysis."
        "Parameters:"
        "- topic_id: Internal topic identifier (use internally)"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_grades_by_topic(
    topic_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_grades_by_topic_handler(
        topic_id=topic_id,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_grades_by_activity",
    description=(
        "Get all grade records for a specific activity. Shows how students performed"
        "on a particular exercise. Useful for activity-level difficulty assessment."
        "Parameters:"
        "- activity_id: Internal activity identifier (use internally)"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_grades_by_activity(
    activity_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_grades_by_activity_handler(
        activity_id=activity_id,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_grade_detail",
    description=(
        "Retrieve complete details for a specific grade record including score,"
        "submission time, feedback, and performance metadata."
        "Parameters:"
        "- grade_id: Internal grade identifier (use internally)"
    ),
)
def get_grade_detail(grade_id: str):
    return get_grade_detail_handler(grade_id=grade_id)


@mcp.tool(
    name="get_grades_summary",
    description=(
        "Get statistical summary of grades for a module including count, average,"
        "minimum, and maximum scores. Useful for understanding overall module difficulty"
        "and student performance trends."
        "Parameters:"
        "- module_id: Internal module identifier (use internally)"
    ),
)
def get_grades_summary(module_id: str):
    return get_grades_summary_handler(module_id=module_id)
