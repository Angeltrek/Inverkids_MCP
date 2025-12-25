from src.mcp.app import mcp
from src.mcp.handlers.schools_handlers import get_schools_handler


@mcp.tool(
    name="get_schools",
    description=(
        "Retrieve schools accessible to the current user. "
        "Admins may see all schools. Administrators see assigned schools. "
        "Other users see only their own school. "
        "Optionally filter by white label."
    ),
)
def get_schools(
    token: str,
    white_label: str | None = None,
):
    return get_schools_handler(
        token=token,
        white_label=white_label,
    )
