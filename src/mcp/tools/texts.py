from src.mcp.app import mcp
from src.mcp.handlers.texts_handlers import (
    get_texts_handler,
    get_texts_by_module_handler,
    get_texts_by_topic_handler,
    get_texts_by_level_handler,
    get_texts_by_type_handler,
    get_texts_by_skill_handler,
    get_text_detail_handler,
)


@mcp.tool(
    name="get_texts",
    description=(
        "List reading materials and text-based learning resources."
        "Parameters:"
        "- module_id: Filter by module (optional, internal ID)"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_texts(
    module_id: str | None = None,
    limit: int = 20,
    offset: int = 0,
):
    return get_texts_handler(
        module_id=module_id,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_texts_by_module",
    description=(
        "List all reading texts associated with a specific module. Use this to find all"
        "text-based resources that support learning within a curriculum unit."
        "Parameters:"
        "- module_id: Internal module identifier (use internally)"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_texts_by_module(
    module_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_texts_by_module_handler(
        module_id=module_id,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_texts_by_topic",
    description=(
        "List reading materials specific to a topic. Topics are narrower than modules,"
        "so this provides the most targeted text resources for a learning unit."
        "Parameters:"
        "- topic_id: Internal topic identifier (use internally)"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_texts_by_topic(
    topic_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_texts_by_topic_handler(
        topic_id=topic_id,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_texts_by_level",
    description=(
        "Filter reading texts by academic grade level (1-9). Ensures texts match"
        "student reading ability and content complexity."
        "Parameters:"
        "- level: Academic level"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_texts_by_level(
    level: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_texts_by_level_handler(
        level=level,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_texts_by_type",
    description=(
        "Filter texts by their pedagogical type."
        "Parameters:"
        "- text_type: Type/genre of text to filter by"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_texts_by_type(
    text_type: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_texts_by_type_handler(
        text_type=text_type,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_texts_by_skill",
    description=(
        "Find reading texts that develop or assess specific skills."
        "Skills are cross-cutting competencies."
        "Parameters:"
        "- skill_id: Internal skill identifier (use internally)"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_texts_by_skill(
    skill_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_texts_by_skill_handler(
        skill_id=skill_id,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_text_detail",
    description=(
        "Get complete details for a specific text including full content."
        "Parameters:"
        "- text_id: Internal text identifier (use internally)"
    ),
)
def get_text_detail(text_id: str):
    return get_text_detail_handler(text_id=text_id)
