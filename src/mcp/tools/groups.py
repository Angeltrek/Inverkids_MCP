from src.mcp.app import mcp
from src.mcp.handlers.groups_handlers import (
    get_groups_by_school_handler,
    get_group_detail_handler,
)


@mcp.tool(
    name="get_groups_by_school",
    description="List groups belonging to a specific school.",
)
def get_groups_by_school(school_id: str):
    return get_groups_by_school_handler(school_id=school_id)


@mcp.tool(
    name="get_group_detail",
    description="Get full group detail by group ID.",
)
def get_group_detail(group_id: str):
    return get_group_detail_handler(group_id=group_id)
