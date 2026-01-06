from src.mcp.app import mcp
from src.mcp.handlers.activities_handlers import (
    get_activities_by_module_handler,
    get_activities_by_type_handler,
    get_first_activity_by_topic_handler,
    get_extra_activities_handler,
    get_activities_by_skill_handler,
    get_activities_by_level_handler,
    search_activities_by_name_handler,
    get_activity_detail_handler,
)


@mcp.tool(
    name="get_activities_by_module",
    description="List activities belonging to a specific module. Supports pagination.",
)
def get_activities_by_module(
    module_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_activities_by_module_handler(
        module_id=module_id,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_activities_by_type",
    description="List activities filtered by activity type. Supports pagination.",
)
def get_activities_by_type(
    activity_type: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_activities_by_type_handler(
        activity_type=activity_type,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_first_activity_by_topic",
    description="Get the first activity of a topic.",
)
def get_first_activity_by_topic(topic_id: str):
    return get_first_activity_by_topic_handler(topic_id=topic_id)


@mcp.tool(
    name="get_extra_activities",
    description="List all extra (optional) activities. Supports pagination.",
)
def get_extra_activities(limit: int = 20, offset: int = 0):
    return get_extra_activities_handler(limit=limit, offset=offset)


@mcp.tool(
    name="get_activities_by_skill",
    description="List activities associated with a skill. Supports pagination.",
)
def get_activities_by_skill(
    skill_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_activities_by_skill_handler(
        skill_id=skill_id,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_activities_by_level",
    description="List activities filtered by academic level. Supports pagination.",
)
def get_activities_by_level(
    level: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_activities_by_level_handler(
        level=level,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="search_activities_by_name",
    description="Search activities by name (ILIKE). Supports pagination.",
)
def search_activities_by_name(
    query: str,
    limit: int = 20,
    offset: int = 0,
):
    return search_activities_by_name_handler(
        query=query,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_activity_detail",
    description="Get full activity detail by activity ID.",
)
def get_activity_detail(activity_id: str):
    return get_activity_detail_handler(activity_id=activity_id)
