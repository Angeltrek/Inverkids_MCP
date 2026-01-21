from src.mcp.app import mcp
from src.mcp.handlers.activities_handlers import (
    get_activities_by_module_handler,
    get_activities_by_skill_handler,
    get_activities_by_level_handler,
    get_activity_detail_handler,
)


@mcp.tool(
    name="get_activities_by_module",
    description=(
        "Retrieve educational activities that belong to a specific learning module."
        "Parameters:"
        "- module_id: Internal module identifier (use internally, don't expose to users)"
        "- limit: Maximum number of results per page (default: 20)"
        "- offset: Starting position for pagination (default: 0)"
    ),
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
    name="get_activities_by_skill",
    description=(
        "Find activities that develop or assess a specific learning skill."
        "Parameters:"
        "- skill_id: Internal skill identifier (use internally)"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
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
    description=(
        "Filter activities by academic grade level (1-9). Level indicates the difficulty"
        "Parameters:"
        "- level: Academic level as string"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
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
    name="get_activity_detail",
    description=(
        "Retrieve complete details for a specific activity. "
        "Parameters:"
        "- activity_id: Internal activity identifier (use internally)"
    ),
)
def get_activity_detail(activity_id: str):
    return get_activity_detail_handler(activity_id=activity_id)
