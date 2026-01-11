from src.mcp.app import mcp
from src.mcp.handlers.modules_handlers import (
    get_modules_handler,
    get_modules_by_level_handler,
    get_modules_by_white_label_handler,
    get_modules_by_level_and_white_label_handler,
    get_modules_by_number_handler,
    get_last_module_by_level_handler,
    search_modules_by_name_handler,
    get_module_detail_handler,
)


@mcp.tool(
    name="get_modules",
    description=(
        "List all available curriculum modules ordered by level and sequence number. "
        "Modules are major units of learning content that group related topics together "
        "\n\n**Parameters:**"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Returns:** Module titles, descriptions, levels, and sequence information."
    ),
)
def get_modules(limit: int = 20, offset: int = 0):
    return get_modules_handler(limit=limit, offset=offset)


@mcp.tool(
    name="get_modules_by_level",
    description=(
        "Filter modules by academic grade level (1-12). Use this to find age-appropriate "
        "curriculum content for students at a specific level."
        "\n\n**Parameters:**"
        "\n- level: Academic level ('1' through '12')"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
    ),
)
def get_modules_by_level(level: str, limit: int = 20, offset: int = 0):
    return get_modules_by_level_handler(level=level, limit=limit, offset=offset)


@mcp.tool(
    name="get_modules_by_white_label",
    description=(
        "Filter modules by white label brand/curriculum version. White labels represent "
        "different curriculum implementations or school partnerships."
        "\n\n**Parameters:**"
        "\n- white_label: Brand identifier (recommended: 'inverkids_school_v3' for Inverkids School)"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n In Inverkids School environments, always use "
        "\n `inverkids_school_v3` as the white_label "
    ),
)
def get_modules_by_white_label(
    white_label: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_modules_by_white_label_handler(
        white_label=white_label,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_modules_by_level_and_white_label",
    description=(
        "Filter modules by both academic level and white label. This is the most precise "
        "way to get curriculum content for a specific grade in a specific school context."
        "\n\n**Parameters:**"
        "\n- level: Academic level ('1' through '12')"
        "\n- white_label: Brand identifier (recommended: 'inverkids_school_v3')"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n In Inverkids School environments, always use "
        "\n `inverkids_school_v3` as the white_label "
    ),
)
def get_modules_by_level_and_white_label(
    level: str,
    white_label: str,
    limit: int = 20,
    offset: int = 0,
):
    return get_modules_by_level_and_white_label_handler(
        level=level,
        white_label=white_label,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_modules_by_number",
     description=(
        "Get modules by their sequence number within the curriculum. Module numbers "
        "indicate the recommended order of instruction (Module 1, Module 2, etc.)."
        "\n\n**Parameters:**"
        "\n- module_number: Sequence number (integer)"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
    ),
)
def get_modules_by_number(
    module_number: int,
    limit: int = 20,
    offset: int = 0,
):
    return get_modules_by_number_handler(
        module_number=module_number,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_last_module_by_level",
    description=(
        "Get the final/most advanced module available for a given academic level. "
        "Useful for understanding curriculum scope or finding end-of-year content."
        "\n\n**Parameters:**"
        "\n- level: Academic level ('1' through '12')"
    ),
)
def get_last_module_by_level(level: str):
    return get_last_module_by_level_handler(level=level)


@mcp.tool(
    name="search_modules_by_name",
    description=(
        "Search curriculum modules using natural language queries. Searches module "
        "titles and descriptions to find relevant content."
        "\n\n**Parameters:**"
        "\n- query: Search term (e.g., 'fractions', 'history', 'biology')"
        "\n- limit: Maximum results (default: 20)"
        "\n- offset: Pagination offset (default: 0)"
        "\n\n**Search Behavior:** Case-insensitive, partial matching enabled."
    ),
)
def search_modules_by_name(query: str, limit: int = 20, offset: int = 0):
    return search_modules_by_name_handler(
        query=query,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_module_detail",
    description=(
        "Retrieve comprehensive information about a specific module including full description"
        "\n\n**Parameters:**"
        "\n- module_id: Internal module identifier (use internally)"
    ),
)
def get_module_detail(module_id: str):
    return get_module_detail_handler(module_id=module_id)
