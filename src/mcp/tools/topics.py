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


PRIVACY_NOTE = (
    "\n\n**Privacy & Data Protection:** All data accessed through this tool is "
    "non-sensitive educational content (learning materials, curriculum structure). "
    "Internal identifiers (IDs) are used for system operations but should not be "
    "exposed to end users. When presenting information, use human-readable names "
    "and descriptions instead of technical identifiers."
)


@mcp.tool(
    name="get_topics",
    description=(
        "List learning topics within the curriculum. Topics are subdivisions of modules "
        "that focus on specific concepts. "
        "Can be filtered by module to see all topics in a particular learning unit."
        "\n\n**Parameters:**"
        "\n- module_id: Filter by module (optional, internal ID)"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Use Case:** Browse curriculum structure or find all topics in a module to create learning sequences."
        + PRIVACY_NOTE
    ),
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
    description=(
        "Filter topics by academic grade level (1-12). Use this to find age-appropriate "
        "topics that match a student's current educational level."
        "\n\n**Parameters:**"
        "\n- level: Academic level ('1' through '12')"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Use Case:** Creating grade-specific curriculum plans or finding topics suitable for a student's level."
        + PRIVACY_NOTE
    ),
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
    description=(
        "List topics that include quiz assessments. Quizzes are formative assessments "
        "embedded within topics to check understanding."
        "\n\n**Parameters:**"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Use Case:** Finding topics with built-in practice assessments for self-evaluation."
        + PRIVACY_NOTE
    ),
)
def get_topics_with_quiz(limit: int = 20, offset: int = 0):
    return get_topics_with_quiz_handler(limit=limit, offset=offset)


@mcp.tool(
    name="get_topics_with_eval",
    description=(
        "List topics that include formal evaluations. Evaluations are summative assessments "
        "used to measure mastery of topic content."
        "\n\n**Parameters:**"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Use Case:** Finding topics with formal assessment components for progress tracking."
        + PRIVACY_NOTE
    ),
)
def get_topics_with_eval(limit: int = 20, offset: int = 0):
    return get_topics_with_eval_handler(limit=limit, offset=offset)


@mcp.tool(
    name="get_topics_with_diag",
    description=(
        "List topics that include diagnostic assessments. Diagnostics are pre-assessments "
        "used to identify student knowledge gaps before starting instruction."
        "\n\n**Parameters:**"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Use Case:** Finding topics with diagnostic tools to assess baseline knowledge."
        + PRIVACY_NOTE
    ),
)
def get_topics_with_diag(limit: int = 20, offset: int = 0):
    return get_topics_with_diag_handler(limit=limit, offset=offset)


@mcp.tool(
    name="get_topics_without_assessment",
    description=(
        "List topics that have no quiz, evaluation, or diagnostic components. These are "
        "purely instructional topics focused on content delivery and practice."
        "\n\n**Parameters:**"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Use Case:** Finding topics for non-graded learning or exploratory study."
        + PRIVACY_NOTE
    ),
)
def get_topics_without_assessment(limit: int = 20, offset: int = 0):
    return get_topics_without_assessment_handler(limit=limit, offset=offset)


@mcp.tool(
    name="get_last_topic_by_module",
    description=(
        "Get the final/concluding topic in a module. This is typically the most advanced "
        "or culminating topic that synthesizes module learning."
        "\n\n**Parameters:**"
        "\n- module_id: Internal module identifier (use internally)"
        "\n\n**Use Case:** Finding the end point of a module's learning sequence or identifying advanced topics."
        + PRIVACY_NOTE
    ),
)
def get_last_topic_by_module(module_id: str):
    return get_last_topic_by_module_handler(module_id=module_id)


@mcp.tool(
    name="search_topics_by_name",
    description=(
        "Search for topics using natural language queries. Searches topic titles and "
        "descriptions to find relevant learning units."
        "\n\n**Parameters:**"
        "\n- query: Search term"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Search Behavior:** Case-insensitive, partial matching enabled."
        "\n\n**Use Case:** Student asks 'I want to learn about X' - search topics first to find relevant content."
        + PRIVACY_NOTE
    ),
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
    description=(
        "Search for topics within a specific module. Narrows search scope to ensure results "
        "are contextually relevant to the module being studied."
        "\n\n**Parameters:**"
        "\n- module_id: Internal module identifier (use internally)"
        "\n- query: Search term within that module"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Use Case:** Student is working through a module and asks about a specific concept within it."
        + PRIVACY_NOTE
    ),
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
    description=(
        "Get comprehensive information about a specific topic including full description."
        "\n\n**Parameters:**"
        "\n- topic_id: Internal topic identifier (use internally)"
        "\n\n**Returns:** Complete topic data with all metadata and instructional context."
        + PRIVACY_NOTE
    ),
)
def get_topic_detail(topic_id: str):
    return get_topic_detail_handler(topic_id=topic_id)
