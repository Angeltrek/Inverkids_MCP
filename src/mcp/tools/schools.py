from src.mcp.app import mcp
from src.mcp.handlers.schools_handlers import (
    get_schools_list_handler,
    get_school_detail_handler,
)


@mcp.tool(
    name="get_schools_list",
    description=(
        "List educational institutions (schools) accessible to the authenticated user. "
        "Returns basic school information including names and locations. This is non-sensitive "
        "institutional data, not personal information."
        "\n\n**Parameters:**"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Access:** Results are filtered based on user permissions (teachers see their "
        "schools, admins see all schools, etc.)."
    ),
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
    description=(
        "Get detailed information about a specific school including name, address, "
        "contact information, and organizational structure. This is public or semi-public "
        "institutional data."
        "\n\n**Parameters:**"
        "\n- school_id: Internal school identifier (use internally)"
    ),
)
def get_school_detail(school_id: str):
    return get_school_detail_handler(school_id=school_id)
