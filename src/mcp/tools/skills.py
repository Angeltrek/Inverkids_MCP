from src.mcp.app import mcp
from src.mcp.handlers.skills_handlers import (
    get_skills_handler,
    search_skills_by_keywords_handler,
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
    name="search_skills_by_keywords",
    description=(
        "Search the skills catalog (CHAs: competencias, habilidades, actitudes) by "
        "keywords, returning up to 50 matching skills with the fields needed to assign "
        "them to an activity component: skill_id, description, ambito, subambito, "
        "domain, dimension. "
        "Each keyword is matched (case-insensitive, partial match) against the skill "
        "description and against its ambito and subambito names; results from all "
        "keywords are combined without duplicates. "
        "Use this to retrieve candidate skills for a component; the full catalog is too "
        "large to process in one request. "
        "To build the keywords list, extract the main topic words from the component's "
        "text and from the activity name (e.g. for a component about counting coins, "
        "use ['dinero', 'moneda', 'contar']). Use single words in Spanish, 3 to 6 of "
        "them, with correct accents. "
        "If no skill matches the given keywords, the search automatically retries with "
        "a broad fallback keyword list, so it will rarely return empty. "
        "When the request payload provides white_label and level, pass BOTH unchanged: "
        "the search (and its fallback) is then restricted to skills of that level, each "
        "result includes its 'levels', and the response reports level_filtered=true. "
        "Parameters:"
        "- keywords: List of search words extracted from the component/activity"
        "- lang: Language for skill text, 'es' or 'en' (default: 'es')"
        "- white_label: Brand/catalog the component belongs to, e.g. 'inverkids_school_v3' (optional, use with level)"
        "- level: Level of the component within that white_label, e.g. '1' or 'Finanzas Personales' (optional, use with white_label)"
    ),
)
def search_skills_by_keywords(
    keywords: list[str],
    lang: str = "es",
    white_label: str | None = None,
    level: str | None = None,
):
    return search_skills_by_keywords_handler(
        keywords=keywords,
        lang=lang,
        white_label=white_label,
        level=level,
    )


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
