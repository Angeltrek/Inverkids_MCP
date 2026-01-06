from src.mcp.app import mcp
from src.mcp.handlers.skills_handlers import (
    get_skills_handler,
    get_skills_by_type_handler,
    search_skills_handler,
    get_skill_detail_handler,
)


@mcp.tool(
    name="get_skills",
    description="List all skills ordered by skill type. Supports pagination.",
)
def get_skills(
    limit: int = 20,
    offset: int = 0,
):
    return get_skills_handler(
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_skills_by_type",
    description="List skills filtered by skill type. Supports pagination.",
)
def get_skills_by_type(
    skill_type: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_skills_by_type_handler(
        skill_type=skill_type,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="search_skills",
    description=(
        "Search skills by name or description (es/en). "
        "ILIKE search. Supports pagination."
    ),
)
def search_skills(
    query: str,
    limit: int = 20,
    offset: int = 0,
):
    return search_skills_handler(
        query=query,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_skill_detail",
    description="Get full skill detail by skill ID.",
)
def get_skill_detail(skill_id: str):
    return get_skill_detail_handler(skill_id=skill_id)
