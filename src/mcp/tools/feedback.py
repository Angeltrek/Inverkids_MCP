from src.mcp.app import mcp
from src.mcp.handlers.feedback_handlers import (
    get_feedback_list_handler,
    get_feedback_detail_handler,
)


@mcp.tool(
    name="get_feedback_list",
    description=(
        "Access educational feedback entries (teacher comments, system-generated feedback, "
        "peer reviews). Feedback can be filtered by module and/or topic to find relevant "
        "instructional guidance. This is non-sensitive educational commentary focused on "
        "learning improvement."
        "\n\n**Parameters:**"
        "\n- module_id: Filter by module (optional, internal ID)"
        "\n- topic_id: Filter by topic (optional, internal ID)"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Use Case:** Retrieve feedback to understand common learning challenges "
        "or provide contextualized support to users."
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
        "Get complete feedback details including the full comment, context, timestamp, "
        "and associated learning materials. Use this to provide students with comprehensive "
        "feedback on their work."
        "\n\n**Parameters:**"
        "\n- feedback_id: Internal feedback identifier (use internally)"
    ),
)
def get_feedback_detail(feedback_id: str):
    return get_feedback_detail_handler(feedback_id=feedback_id)
