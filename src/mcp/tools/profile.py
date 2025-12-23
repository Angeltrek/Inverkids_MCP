from src.mcp.app import mcp
from src.mcp.handlers.profile_handlers import get_profile_handler


@mcp.tool(
    name="get_profile",
    description="Retrieve the authenticated user's profile.",
)
def get_profile(token: str):
    return get_profile_handler(token=token)
