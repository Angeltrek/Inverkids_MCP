from src.mcp.app import mcp
from src.mcp.handlers.skills_handlers import (
    get_skills_handler,
    get_all_skills_summary_handler,
    get_skill_detail_handler,
)


@mcp.tool(
    name="get_skills",
    description=(
        "List educational skills and competencies tracked in the system. "
        "Parameters:"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
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
    name="get_all_skills_summary",
    description=(
        "Return the FULL catalog of skills (CHAs: competencias, habilidades, actitudes) "
        "in one call, with just the fields needed to assign a skill to an activity "
        "component: skill_id, description, ambito, subambito, skill_type, domain, "
        "dimension. Use this instead of get_skills when you need to consider the whole "
        "catalog at once (e.g. to choose which skills apply to a component), rather "
        "than paging through it. "
        "Parameters:"
        "- lang: Language for skill text, 'es' or 'en' (default: 'es')"
    ),
)
def get_all_skills_summary(
    lang: str = "es",
):
    return get_all_skills_summary_handler(lang=lang)


@mcp.tool(
    name="get_skill_detail",
    description=(
        "Get comprehensive information about a specific skill including its definition, "
        "associated learning standards."
        "Parameters:"
        "- skill_id: Internal skill identifier (use internally)"
    ),
)
def get_skill_detail(skill_id: str):
    return get_skill_detail_handler(skill_id=skill_id)
