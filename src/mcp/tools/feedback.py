from src.mcp.app import mcp
from src.mcp.handlers.feedback_handlers import (
    get_feedback_list_handler,
    get_feedback_detail_handler,
)


@mcp.tool(
    name="get_feedback_list",
    description=(
        "List feedback entries, optionally filtered by module or topic. "
        "Ordered by most recent."
    ),
)
def get_feedback_list(
    module_id: str | None = None,
    topic_id: str | None = None,
):
    return get_feedback_list_handler(
        module_id=module_id,
        topic_id=topic_id,
    )


@mcp.tool(
    name="get_feedback_detail",
    description="Get full feedback detail by feedback ID.",
)
def get_feedback_detail(feedback_id: str):
    return get_feedback_detail_handler(feedback_id=feedback_id)
