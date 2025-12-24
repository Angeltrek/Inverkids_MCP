from src.mcp.app import mcp
from src.mcp.handlers.catalog_handlers import (
    get_activities_handler,
    get_full_catalog_handler,
    get_modules_handler,
    get_texts_handler,
    get_topics_handler,
)


@mcp.tool(
    name="get_full_catalog",
    description="Retrieve the complete catalog hierarchy.",
)
def get_full_catalog(
    level: str,
    white_label: str,
    user_lang: str,
    token: str,
):
    return get_full_catalog_handler(
        level=level,
        white_label=white_label,
        user_lang=user_lang,
        token=token,
    )


@mcp.tool(
    name="get_modules",
    description="Retrieve learning modules filtered by level, white label, or module id.",
)
def get_modules(
    token: str,
    level: str | None = None,
    white_label: str | None = None,
    module_id: str | None = None,
):
    return get_modules_handler(
        token=token,
        level=level,
        white_label=white_label,
        module_id=module_id,
    )


@mcp.tool(
    name="get_topics",
    description="Retrieve topics filtered by module, level, or topic id.",
)
def get_topics(
    token: str,
    module_id: str | None = None,
    level: str | None = None,
    topic_id: str | None = None,
):
    return get_topics_handler(
        token=token,
        module_id=module_id,
        level=level,
        topic_id=topic_id,
    )


@mcp.tool(
    name="get_activities",
    description="Retrieve activities filtered by topic, module, level, or activity type. Use include_content only when necessary.",
)
def get_activities(
    token: str,
    topic_id: str | None = None,
    module_id: str | None = None,
    level: str | None = None,
    activity_id: str | None = None,
    activity_type: str | None = None,
    include_content: bool = False,
):
    return get_activities_handler(
        token=token,
        topic_id=topic_id,
        module_id=module_id,
        level=level,
        activity_id=activity_id,
        activity_type=activity_type,
        include_content=include_content,
    )


@mcp.tool(
    name="get_texts",
    description="Retrieve learning texts. Content is excluded by default to save tokens.",
)
def get_texts(
    token: str,
    topic_id: str | None = None,
    module_id: str | None = None,
    level: str | None = None,
    text_id: str | None = None,
    include_content: bool = False,
):
    return get_texts_handler(
        token=token,
        topic_id=topic_id,
        module_id=module_id,
        level=level,
        text_id=text_id,
        include_content=include_content,
    )
