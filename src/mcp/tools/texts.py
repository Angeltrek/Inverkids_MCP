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
    description="List texts, optionally filtered by module ID. Supports pagination.",
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
    description="List texts belonging to a module. Supports pagination.",
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
    description="List texts belonging to a topic. Supports pagination.",
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
    description="List texts filtered by academic level. Supports pagination.",
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
    description="List texts marked as home texts. Supports pagination.",
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
    description="List texts marked as entry texts. Supports pagination.",
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
    description="List texts filtered by text type. Supports pagination.",
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
    description="List texts associated with a skill. Supports pagination.",
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
    description="Search texts by name (ILIKE). Supports pagination.",
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
    description="Get full text detail by text ID.",
)
def get_text_detail(text_id: str):
    return get_text_detail_handler(text_id=text_id)
