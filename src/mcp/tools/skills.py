from src.mcp.app import mcp
from src.mcp.handlers.skills_handlers import (
    get_skills_handler,
    get_skills_by_type_handler,
    search_skills_handler,
    get_skill_detail_handler,
)


@mcp.tool(
    name="get_skills",
    description="List all skills ordered by skill type.",
)
def get_skills():
    return get_skills_handler()


@mcp.tool(
    name="get_skills_by_type",
    description="List skills filtered by skill type.",
)
def get_skills_by_type(skill_type: str):
    return get_skills_by_type_handler(skill_type=skill_type)


@mcp.tool(
    name="search_skills",
    description=(
        "Search skills by name or description (es/en). "
        "ILIKE search, max 20 results."
    ),
)
def search_skills(query: str):
    return search_skills_handler(query=query)


@mcp.tool(
    name="get_skill_detail",
    description="Get full skill detail by skill ID.",
)
def get_skill_detail(skill_id: str):
    return get_skill_detail_handler(skill_id=skill_id)
