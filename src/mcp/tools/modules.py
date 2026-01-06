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
    description="List all modules ordered by level and module number. Supports pagination.",
)
def get_modules(limit: int = 20, offset: int = 0):
    return get_modules_handler(limit=limit, offset=offset)


@mcp.tool(
    name="get_modules_by_level",
    description="List modules filtered by academic level. Supports pagination.",
)
def get_modules_by_level(level: str, limit: int = 20, offset: int = 0):
    return get_modules_by_level_handler(level=level, limit=limit, offset=offset)


@mcp.tool(
    name="get_modules_by_white_label",
    description="List modules filtered by white label. Supports pagination.",
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
    description="List modules filtered by level and white label. Supports pagination.",
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
    description="Get modules by module number. Supports pagination.",
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
    description="Get the last module available for a given level.",
)
def get_last_module_by_level(level: str):
    return get_last_module_by_level_handler(level=level)


@mcp.tool(
    name="search_modules_by_name",
    description="Search modules by name (ILIKE). Supports pagination.",
)
def search_modules_by_name(query: str, limit: int = 20, offset: int = 0):
    return search_modules_by_name_handler(
        query=query,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_module_detail",
    description="Get full module detail by module ID.",
)
def get_module_detail(module_id: str):
    return get_module_detail_handler(module_id=module_id)
