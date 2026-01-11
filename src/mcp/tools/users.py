from src.mcp.app import mcp
from src.mcp.handlers.users_handlers import (
    get_users_list_handler,
    get_user_detail_handler,
)


@mcp.tool(
    name="get_users_list",
    description=(
        "List student and child user profiles accessible to the authenticated requester. "
        "Access is role-based: teachers see their students, parents see their children, "
        "admins see school-wide users."
        "\n\n**Parameters:**"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Returns:** Basic user profiles (names, levels, groups) - no sensitive personal data."
        "\n\n**Use Case:** Teachers viewing their class roster, parents checking children's accounts."
        "\n\n**Important:** Never expose user IDs in responses. Present only names and educational context."
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
        "\n\n**Parameters:**"
        "\n- user_id: Internal user identifier (use internally)"
        "\n\n**Returns:** Educational profile data (no sensitive personal information like contact details)."
        "\n\n**Privacy Rule:** Only show user details if: (1) it's the user's own profile, "
        "or (2) requester has authorized access (teacher viewing student, parent viewing child)."
        "\n\n**Important:** Do not expose the user_id in your response. Reference users by name only."
    ),
)
def get_user_detail(user_id: str):
    return get_user_detail_handler(user_id=user_id)
