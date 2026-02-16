from src.mcp.app import mcp
from src.mcp.handlers.modules_handlers import (
    get_modules_handler,
    get_modules_by_white_label_handler,
    get_modules_by_level_and_white_label_handler,
    get_modules_by_number_handler,
    get_module_detail_handler,
)


@mcp.tool(
    name="get_modules",
    description=(
        "List all available curriculum modules ordered by level and sequence number."
        "Modules are major units of learning content that group related topics together"
        "Parameters:"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_modules(limit: int = 20, offset: int = 0):
    return get_modules_handler(limit=limit, offset=offset)


@mcp.tool(
    name="get_modules_by_white_label",
    description=(
        "Filter modules by white label brand/curriculum version. White labels represent"
        "different curriculum implementations or school partnerships."
        "Parameters:"
        "- white_label: Brand identifier."
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
        "In Inverkids School environments, always use"
        "`inverkids_school_v3` as the white_label "
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
        "Filter modules by both academic level and white label. This is the most precise"
        "way to get curriculum content for a specific grade in a specific school context."
        "Parameters:"
        "- level: Academic level"
        "- white_label: Brand identifier"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
        "In Inverkids School environments, always use "
        "`inverkids_school_v3` as the white_label "
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
        "Get modules by their sequence number within the curriculum. Module numbers"
        "indicate the recommended order of instruction (Module 1, Module 2, etc.)."
        "Parameters:"
        "- module_number: Sequence number (integer)"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
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
    name="get_module_detail",
    description=(
        "Retrieve comprehensive information about a specific module including full description"
        "Parameters:"
        "- module_id: Internal module identifier (use internally)"
    ),
)
def get_module_detail(module_id: str):
    return get_module_detail_handler(module_id=module_id)
