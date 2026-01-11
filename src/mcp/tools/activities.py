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
    description=(
        "Retrieve educational activities that belong to a specific learning module. "
        "Activities are the core interactive exercises students complete (videos, quizzes, "
        "readings, interactive games). Use this when you need to find all available "
        "activities within a particular module for curriculum planning or student assignment."
        "\n\n**Parameters:**"
        "\n- module_id: Internal module identifier (use internally, don't expose to users)"
        "\n- limit: Maximum number of results per page (default: 20)"
        "\n- offset: Starting position for pagination (default: 0)"
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
    name="get_activities_by_type",
    description=(
        "Filter activities by their pedagogical type."
        "Use this to create specialized learning experiences or "
        "find activities matching specific teaching methodologies."
        "\n\n**Parameters:**"
        "\n- activity_type: Type of activity to filter by"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
    ),
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
    description=(
        "Get the introductory/first activity of a specific topic. Topics are subdivisions "
        "within modules that focus on particular concepts. This tool is useful for starting "
        "a new topic or creating a learning path that begins at the right entry point."
        "\n\n**Use Case:** When a user asks to start learning a new topic, use this "
        "to provide them with the foundational first activity."
        "\n\n**Parameters:**"
        "\n- topic_id: Internal topic identifier (use internally)"
    ),
)
def get_first_activity_by_topic(topic_id: str):
    return get_first_activity_by_topic_handler(topic_id=topic_id)


@mcp.tool(
    name="get_extra_activities",
    description=(
        "Retrieve optional/supplementary activities for additional practice. These are "
        "enrichment activities beyond the core curriculum, useful for advanced students "
        "or those needing extra practice. Supports pagination for browsing through "
        "available supplementary content."
    ),
)
def get_extra_activities(limit: int = 20, offset: int = 0):
    return get_extra_activities_handler(limit=limit, offset=offset)


@mcp.tool(
    name="get_activities_by_skill",
    description=(
        "Find activities that develop or assess a specific learning skill. "
        "Skills are cross-cutting competencies that span multiple topics and modules."
        "\n\n**Use Case:** Create skill-focused learning paths or assess student progress "
        "in particular competency areas."
        "\n\n**Parameters:**"
        "\n- skill_id: Internal skill identifier (use internally)"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
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
        "Filter activities by academic grade level (1-12). Level indicates the difficulty "
        "and age-appropriateness of content. Use this to ensure activities match student "
        "grade level and learning capacity."
        "\n\n**Parameters:**"
        "\n- level: Academic level as string ('1' through '12')"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
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
    name="search_activities_by_name",
    description=(
        "Search for activities using natural language queries. Searches activity titles "
        "and descriptions to find relevant content. Useful when students request specific "
        "topics like 'fractions' or 'money'."
        "\n\n**Parameters:**"
        "\n- query: Search term (e.g., 'multiplication', 'finance', 'money')"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Search Behavior:** Case-insensitive, partial matching enabled."
    ),
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
    description=(
        "Retrieve complete details for a specific activity including instructions, "
        "learning objectives, difficulty level, and full content. "
        "Use this when you need comprehensive information to present an activity to a user."
        "\n\n**Parameters:**"
        "\n- activity_id: Internal activity identifier (use internally)"
        "\n\n**Returns:** Full activity data including content, metadata, and pedagogical information."
    ),
)
def get_activity_detail(activity_id: str):
    return get_activity_detail_handler(activity_id=activity_id)
