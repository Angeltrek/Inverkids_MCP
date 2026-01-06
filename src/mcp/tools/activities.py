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
    description="List activities belonging to a specific module.",
)
def get_activities_by_module(module_id: str):
    return get_activities_by_module_handler(module_id=module_id)


@mcp.tool(
    name="get_activities_by_type",
    description="List activities filtered by activity type.",
)
def get_activities_by_type(activity_type: str):
    return get_activities_by_type_handler(activity_type=activity_type)


@mcp.tool(
    name="get_first_activity_by_topic",
    description="Get the first activity of a topic.",
)
def get_first_activity_by_topic(topic_id: str):
    return get_first_activity_by_topic_handler(topic_id=topic_id)


@mcp.tool(
    name="get_extra_activities",
    description="List all extra (optional) activities.",
)
def get_extra_activities():
    return get_extra_activities_handler()


@mcp.tool(
    name="get_activities_by_skill",
    description="List activities associated with a skill.",
)
def get_activities_by_skill(skill_id: str):
    return get_activities_by_skill_handler(skill_id=skill_id)


@mcp.tool(
    name="get_activities_by_level",
    description="List activities filtered by academic level.",
)
def get_activities_by_level(level: str):
    return get_activities_by_level_handler(level=level)


@mcp.tool(
    name="search_activities_by_name",
    description="Search activities by name (ILIKE, max 20 results).",
)
def search_activities_by_name(query: str):
    return search_activities_by_name_handler(query=query)


@mcp.tool(
    name="get_activity_detail",
    description="Get full activity detail by activity ID.",
)
def get_activity_detail(activity_id: str):
    return get_activity_detail_handler(activity_id=activity_id)
