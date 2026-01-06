from src.mcp.app import mcp
from src.mcp.handlers.groups_handlers import (
    get_groups_by_school_handler,
    get_group_detail_handler,
)


PRIVACY_NOTE = (
    "\n\n**Privacy & Data Protection:** All data accessed through this tool is "
    "non-sensitive educational content (learning materials, curriculum structure). "
    "Internal identifiers (IDs) are used for system operations but should not be "
    "exposed to end users. When presenting information, use human-readable names "
    "and descriptions instead of technical identifiers."
)


@mcp.tool(
    name="get_groups_by_school",
    description=(
        "List learning groups (classes) within a specific school. Groups are collections "
        "of students that learn together under a teacher. Use this to understand school "
        "organization and class structure."
        "\n\n**Parameters:**"
        "\n- school_id: Internal school identifier (use internally)"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Returns:** Group names, levels, and metadata (no student personal information)."
        + PRIVACY_NOTE
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
        "Get detailed information about a learning group including its name, level, "
        "schedule, and associated teachers. Does not expose individual student data."
        "\n\n**Parameters:**"
        "\n- group_id: Internal group identifier (use internally)"
        + PRIVACY_NOTE
    ),
)
def get_group_detail(group_id: str):
    return get_group_detail_handler(group_id=group_id)
