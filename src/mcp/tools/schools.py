from src.mcp.app import mcp
from src.mcp.handlers.schools_handlers import (
    get_schools_list_handler,
    get_school_detail_handler,
)


@mcp.tool(
    name="get_schools_list",
    description="List all schools available to the requester. Supports pagination.",
)
def get_schools_list(
    limit: int = 20,
    offset: int = 0,
):
    return get_schools_list_handler(
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_school_detail",
    description="Get full school detail by school ID.",
)
def get_school_detail(school_id: str):
    return get_school_detail_handler(school_id=school_id)
