from src.mcp.app import mcp
from src.mcp.handlers.tags_handlers import get_tags_handler

@mcp.tool(
    name="get_tags",
    description=(
        "List all available topic tags. Tags are used to categorize and "
        "filter curriculum topics."
        "Parameters:"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_tags(
    limit: int = 20, 
    offset: int = 0
):
    return get_tags_handler(
        limit=limit,
        offset=offset
    )
