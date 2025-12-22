from src.mcp.app import mcp
from src.backend.context import get_backend_client
from src.app.tool_handlers.profile import get_profile_handler


@mcp.tool(
    name="get_profile",
    description="Retrieve the authenticated user's profile.",
)
def get_profile(token: str):
    client = get_backend_client(token)
    return get_profile_handler(backend_client=client)
