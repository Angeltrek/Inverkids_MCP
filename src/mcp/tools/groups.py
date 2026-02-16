from src.mcp.app import mcp
from src.mcp.handlers.groups_handlers import (
    get_groups_by_school_handler,
    get_group_detail_handler,
)


@mcp.tool(
    name="get_groups_by_school",
    description=(
        "List learning groups (classes) within a specific school. Groups are collections"
        "of students that learn together under a teacher."
        "Parameters:"
        "- school_id: Internal school identifier (use internally)"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_groups_by_school(
    school_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_groups_by_school_handler(
        school_id=school_id,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_group_detail",
    description=(
        "Get detailed information about a learning group including its name, level,"
        "schedule, and associated teachers. Does not expose individual student data."
        "Parameters:"
        "- group_id: Internal group identifier (use internally)"
    ),
)
def get_group_detail(group_id: str):
    return get_group_detail_handler(group_id=group_id)
