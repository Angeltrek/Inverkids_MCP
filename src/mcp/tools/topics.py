from src.mcp.app import mcp
from src.mcp.handlers.topics_handlers import (
    get_topics_handler,
    get_topics_by_level_handler,
    get_topics_with_quiz_handler,
    get_topics_with_eval_handler,
    get_topics_with_diag_handler,
    get_topics_without_assessment_handler,
    get_last_topic_by_module_handler,
    search_topics_by_name_handler,
    search_topics_by_name_in_module_handler,
    get_topic_detail_handler,
)


@mcp.tool(
    name="get_topics",
    description="List topics, optionally filtered by module ID. Supports pagination.",
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
    description="List topics by academic level. Supports pagination.",
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
    name="get_topics_with_quiz",
    description="List topics that include quizzes. Supports pagination.",
)
def get_topics_with_quiz(limit: int = 20, offset: int = 0):
    return get_topics_with_quiz_handler(limit=limit, offset=offset)


@mcp.tool(
    name="get_topics_with_eval",
    description="List topics that include evaluations. Supports pagination.",
)
def get_topics_with_eval(limit: int = 20, offset: int = 0):
    return get_topics_with_eval_handler(limit=limit, offset=offset)


@mcp.tool(
    name="get_topics_with_diag",
    description="List topics that include diagnostics. Supports pagination.",
)
def get_topics_with_diag(limit: int = 20, offset: int = 0):
    return get_topics_with_diag_handler(limit=limit, offset=offset)


@mcp.tool(
    name="get_topics_without_assessment",
    description="List topics without quiz, eval, or diagnostic. Supports pagination.",
)
def get_topics_without_assessment(limit: int = 20, offset: int = 0):
    return get_topics_without_assessment_handler(limit=limit, offset=offset)


@mcp.tool(
    name="get_last_topic_by_module",
    description="Get the last topic in a module.",
)
def get_last_topic_by_module(module_id: str):
    return get_last_topic_by_module_handler(module_id=module_id)


@mcp.tool(
    name="search_topics_by_name",
    description="Search topics by name (ILIKE). Supports pagination.",
)
def search_topics_by_name(
    query: str,
    limit: int = 20,
    offset: int = 0,
):
    return search_topics_by_name_handler(
        query=query,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="search_topics_by_name_in_module",
    description="Search topics by name within a specific module. Supports pagination.",
)
def search_topics_by_name_in_module(
    module_id: str,
    query: str,
    limit: int = 20,
    offset: int = 0,
):
    return search_topics_by_name_in_module_handler(
        module_id=module_id,
        query=query,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_topic_detail",
    description="Get full topic detail by topic ID.",
)
def get_topic_detail(topic_id: str):
    return get_topic_detail_handler(topic_id=topic_id)
