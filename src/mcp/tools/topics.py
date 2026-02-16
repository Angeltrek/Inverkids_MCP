from src.mcp.app import mcp
from src.mcp.handlers.topics_handlers import (
    get_topics_handler,
    get_topics_by_level_handler,
    get_topic_detail_handler,
    get_topics_by_tags_handler,
)


@mcp.tool(
    name="get_topics",
    description=(
        "List learning topics within the curriculum. "
        "Can be filtered by module to see all topics in a particular learning unit."
        "Parameters:"
        "- module_id: Filter by module (optional, internal ID)"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_topics(
    module_id: str | None = None,
    limit: int = 20,
    offset: int = 0,
):
    return get_topics_handler(
        module_id=module_id,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_topics_by_level",
    description=(
        "Filter topics by academic grade level (1-9). Use this to find age-appropriate "
        "topics that match a student's current educational level."
        "Parameters:"
        "- level: Academic level"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_topics_by_level(
    level: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_topics_by_level_handler(
        level=level,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_topic_detail",
    description=(
        "Get comprehensive information about a specific topic including full description."
        "Parameters:"
        "- topic_id: Internal topic identifier (use internally)"
    ),
)
def get_topic_detail(topic_id: str):
    return get_topic_detail_handler(topic_id=topic_id)


@mcp.tool(
    name="get_topics_by_tags",
    description=(
        "Retrieve curriculum topics that match one or more tags. "
        "Returns topics that contain at least one of the provided tags."
        "Parameters:"
        "- tags: List of tag strings"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_topics_by_tags(
    tags: list[str],
    limit: int = 20,
    offset: int = 0,
):
    return get_topics_by_tags_handler(
        tags=tags,
        limit=limit,
        offset=offset,
    )
