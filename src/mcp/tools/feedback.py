from src.mcp.app import mcp
from src.mcp.handlers.feedback_handlers import (
    get_feedback_list_handler,
    get_feedback_detail_handler,
)


@mcp.tool(
    name="get_feedback_list",
    description=(
        "Access educational feedback entries."
        "Parameters:"
        "- module_id: Filter by module (optional, internal ID)"
        "- topic_id: Filter by topic (optional, internal ID)"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_feedback_list(
    module_id: str | None = None,
    topic_id: str | None = None,
    limit: int = 20,
    offset: int = 0,
):
    return get_feedback_list_handler(
        module_id=module_id,
        topic_id=topic_id,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_feedback_detail",
    description=(
        "Get complete feedback details."
        "Parameters:"
        "- feedback_id: Internal feedback identifier (use internally)"
    ),
)
def get_feedback_detail(feedback_id: str):
    return get_feedback_detail_handler(feedback_id=feedback_id)
