from src.mcp.app import mcp
from src.mcp.handlers.skills_handlers import (
    get_skills_handler,
    get_skills_by_type_handler,
    search_skills_handler,
    get_skill_detail_handler,
)


PRIVACY_NOTE = (
    "\n\n**Privacy & Data Protection:** All data accessed through this tool is "
    "non-sensitive educational content (learning materials, curriculum structure). "
    "Internal identifiers (IDs) are used for system operations but should not be "
    "exposed to end users. When presenting information, use human-readable names "
    "and descriptions instead of technical identifiers."
)


@mcp.tool(
    name="get_skills",
    description=(
        "List educational skills and competencies tracked in the system. Skills are "
        "cross-cutting abilities (e.g., 'problem-solving', 'critical thinking', "
        "'reading comprehension') that span multiple subjects and grade levels."
        "\n\n**Parameters:**"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Use Case:** Map activities to competency frameworks or track skill development."
        + PRIVACY_NOTE
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
    name="get_skills_by_type",
    description=(
        "Filter skills by category/type."
        "Skill types help organize competencies by domain."
        "\n\n**Parameters:**"
        "\n- skill_type: Category of skills to retrieve"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        + PRIVACY_NOTE
    ),
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
        "Search for skills using natural language queries. Searches skill names and "
        "descriptions in both Spanish and English. Useful for finding competencies "
        "related to specific learning goals."
        "\n\n**Parameters:**"
        "\n- query: Search term"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Search Behavior:** Case-insensitive, partial matching, bilingual (ES/EN)."
        + PRIVACY_NOTE
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
    description=(
        "Get comprehensive information about a specific skill including its definition, "
        "associated learning standards, and progression across grade levels."
        "\n\n**Parameters:**"
        "\n- skill_id: Internal skill identifier (use internally)"
        + PRIVACY_NOTE
    ),
)
def get_skill_detail(skill_id: str):
    return get_skill_detail_handler(skill_id=skill_id)
