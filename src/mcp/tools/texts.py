from src.mcp.app import mcp
from src.mcp.handlers.texts_handlers import (
    get_texts_handler,
    get_texts_by_module_handler,
    get_texts_by_topic_handler,
    get_texts_by_level_handler,
    get_home_texts_handler,
    get_entry_texts_handler,
    get_texts_by_type_handler,
    get_texts_by_skill_handler,
    search_texts_by_name_handler,
    get_text_detail_handler,
)


@mcp.tool(
    name="get_texts",
    description=(
        "List reading materials and text-based learning resources. Texts can include "
        "stories, articles, instructions, explanations, and other written content. "
        "Optionally filter by module."
        "\n\n**Parameters:**"
        "\n- module_id: Filter by module (optional, internal ID)"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
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
        "List all reading texts associated with a specific module. Use this to find all "
        "text-based resources that support learning within a curriculum unit."
        "\n\n**Parameters:**"
        "\n- module_id: Internal module identifier (use internally)"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
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
        "List reading materials specific to a topic. Topics are narrower than modules, "
        "so this provides the most targeted text resources for a learning unit."
        "\n\n**Parameters:**"
        "\n- topic_id: Internal topic identifier (use internally)"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Use Case:** Finding texts directly related to what the student is currently learning."
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
        "Filter reading texts by academic grade level (1-12). Ensures texts match "
        "student reading ability and content complexity."
        "\n\n**Parameters:**"
        "\n- level: Academic level ('1' through '12')"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Use Case:** Finding age-appropriate reading materials for literacy instruction."
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
    name="get_home_texts",
    description=(
        "List texts designated for home/independent reading. These are typically "
        "supplementary materials students can access outside the classroom."
        "\n\n**Parameters:**"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Use Case:** Providing take-home reading assignments or family engagement materials."
    ),
)
def get_home_texts(
    limit: int = 20,
    offset: int = 0,
):
    return get_home_texts_handler(
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_entry_texts",
    description=(
        "List introductory/entry-level texts. These are foundational readings that "
        "introduce new topics or serve as prerequisites for more advanced content."
        "\n\n**Parameters:**"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Use Case:** Starting a new topic - provide students with baseline readings first."
    ),
)
def get_entry_texts(
    limit: int = 20,
    offset: int = 0,
):
    return get_entry_texts_handler(
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_texts_by_type",
    description=(
        "Filter texts by their pedagogical type (e.g., 'story', 'article', 'instructions', "
        "'explanation'). Use this to match texts to specific instructional purposes."
        "\n\n**Parameters:**"
        "\n- text_type: Type/genre of text to filter by"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Use Case:** Finding specific text genres for literacy or content instruction."
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
        "\n\n**Parameters:**"
        "\n- skill_id: Internal skill identifier (use internally)"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Use Case:** Creating skill-focused reading practice or targeted intervention materials."
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
    name="search_texts_by_name",
    description=(
        "Search for reading texts using natural language queries. Searches titles and "
        "descriptions to find relevant reading materials."
        "\n\n**Parameters:**"
        "\n- query: Search term"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Search Behavior:** Case-insensitive, partial matching enabled."
        "\n\n**Use Case:** Student asks for reading about a specific topic - use this to discover texts."
    ),
)
def search_texts_by_name(
    query: str,
    limit: int = 20,
    offset: int = 0,
):
    return search_texts_by_name_handler(
        query=query,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_text_detail",
    description=(
        "Get complete details for a specific text including full content."
        "\n\n**Parameters:**"
        "\n- text_id: Internal text identifier (use internally)"
        "\n\n**Returns:** Full text with all metadata and instructional scaffolding."
    ),
)
def get_text_detail(text_id: str):
    return get_text_detail_handler(text_id=text_id)
