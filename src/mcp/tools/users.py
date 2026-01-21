from src.mcp.app import mcp
from src.mcp.handlers.users_handlers import (
    get_users_list_handler,
    get_user_detail_handler,
)


@mcp.tool(
    name="get_users_list",
    description=(
        "List student and child user profiles accessible to the authenticated requester."
        "Access is role-based: teachers see their students, parents see their children,"
        "admins see school-wide users."
        "Parameters:"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
        "Important: Never expose user IDs in responses. Present only names and educational context."
    ),
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
    description=(
        "Get detailed profile information for a specific user including grade level, "
        "group memberships, learning preferences, and progress summary."
        "Parameters:"
        "- user_id: Internal user identifier (use internally)"
    ),
)
def get_user_detail(user_id: str):
    return get_user_detail_handler(user_id=user_id)
