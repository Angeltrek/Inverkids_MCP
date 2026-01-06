from src.mcp.app import mcp
from src.mcp.handlers.groups_handlers import (
    get_groups_by_school_handler,
    get_group_detail_handler,
)


@mcp.tool(
    name="get_groups_by_school",
    description="List groups belonging to a specific school. Supports pagination.",
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
    description="Get full group detail by group ID.",
)
def get_group_detail(group_id: str):
    return get_group_detail_handler(group_id=group_id)
