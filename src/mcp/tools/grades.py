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


PRIVACY_NOTE = (
    "\n\n**Privacy & Data Protection:** All data accessed through this tool is "
    "non-sensitive educational content (learning materials, curriculum structure). "
    "Internal identifiers (IDs) are used for system operations but should not be "
    "exposed to end users. When presenting information, use human-readable names "
    "and descriptions instead of technical identifiers."
)


@mcp.tool(
    name="get_grades_by_level",
    description=(
        "Retrieve grade records for students in a specific academic level. Grades represent "
        "performance scores on completed activities. This tool provides aggregate data for "
        "level-wide analysis (not individual student PII)."
        "\n\n**Parameters:**"
        "\n- level: Academic level ('1' through '12')"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Note:** Grades are educational performance metrics, not personally identifiable."
        + PRIVACY_NOTE
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
        "Get grade records for a specific learning group/class. Groups are collections of "
        "students that learn together. Use this for class-level performance analysis."
        "\n\n**Parameters:**"
        "\n- group_id: Internal group identifier (use internally)"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        + PRIVACY_NOTE
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
        "Access grade records for a specific student. If no student_id is provided, "
        "defaults to the current authenticated user's grades. Use this to show students "
        "their own progress and performance."
        "\n\n**Parameters:**"
        "\n- student_id: Internal user identifier (optional, use internally)"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Privacy:** When presenting grades, show only the student's own data or "
        "aggregated/anonymized class data."
        + PRIVACY_NOTE
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
        "Filter grade records by learning module. Useful for understanding student "
        "performance within a specific curriculum module."
        "\n\n**Parameters:**"
        "\n- module_id: Internal module identifier (use internally)"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        + PRIVACY_NOTE
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
        "Filter grade records by learning topic. Topics are subdivisions of modules "
        "focusing on specific concepts. Use this for topic-level performance analysis."
        "\n\n**Parameters:**"
        "\n- topic_id: Internal topic identifier (use internally)"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        + PRIVACY_NOTE
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
        "Get all grade records for a specific activity. Shows how students performed "
        "on a particular exercise. Useful for activity-level difficulty assessment."
        "\n\n**Parameters:**"
        "\n- activity_id: Internal activity identifier (use internally)"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        + PRIVACY_NOTE
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
        "Retrieve complete details for a specific grade record including score, "
        "submission time, feedback, and performance metadata."
        "\n\n**Parameters:**"
        "\n- grade_id: Internal grade identifier (use internally)"
        + PRIVACY_NOTE
    ),
)
def get_grade_detail(grade_id: str):
    return get_grade_detail_handler(grade_id=grade_id)


@mcp.tool(
    name="get_grades_summary",
    description=(
        "Get statistical summary of grades for a module including count, average, "
        "minimum, and maximum scores. Useful for understanding overall module difficulty "
        "and student performance trends."
        "\n\n**Parameters:**"
        "\n- module_id: Internal module identifier (use internally)"
        "\n\n**Returns:** Aggregated statistics (count, avg, min, max) - no individual student data."
        + PRIVACY_NOTE
    ),
)
def get_grades_summary(module_id: str):
    return get_grades_summary_handler(module_id=module_id)
