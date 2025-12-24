from src.mcp.app import mcp
from src.mcp.handlers.users_handlers import (
    get_current_user_handler,
    get_users_handler,
)


@mcp.tool(
    name="get_users",
    description="Retrieve users accessible to the current user based on role and group access.",
)
def get_users(token: str):
    return get_users_handler(token=token)


@mcp.tool(
    name="get_profile",
    description="Retrieve the authenticated user's profile.",
)
def get_profile(token: str):
    return get_current_user_handler(token=token)
