from src.mcp.app import mcp
from src.mcp.handlers.users_handlers import (
    get_users_list_handler,
    get_user_detail_handler,
)


@mcp.tool(
    name="get_users_list",
    description="List student and child users accessible to the requester. Supports pagination.",
)
def get_users_list(
    limit: int = 20,
    offset: int = 0,
):
    return get_users_list_handler(
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_user_detail",
    description="Get full user profile by user ID.",
)
def get_user_detail(user_id: str):
    return get_user_detail_handler(user_id=user_id)
