from src.mcp.app import mcp
from src.mcp.handlers.virtual_modules_handlers import (
    create_virtual_module_handler,
    get_virtual_module_detail_handler,
    get_virtual_modules_handler,
)
from typing import List, Dict, Optional


@mcp.tool(
    name="create_virtual_module",
    description=(
        "Create a virtual module and associate it with existing topics.\n"
        "Parameters:\n"
        "- pbl_name: PBL name this virtual module belongs to\n"
        "- name: localized name (e.g. {'en': '...', 'es': '...'})\n"
        "- description: localized description (e.g. {'en': '...', 'es': '...'})\n"
        "- topic_ids: ordered list of topic UUIDs\n"
        "- white_label: optional (default: inverkids_school_v3)\n"
    ),
)
def create_virtual_module(
    pbl_name: str,
    name: Dict[str, str],
    description: Dict[str, str],
    topic_ids: List[str],
    white_label: Optional[str] = "inverkids_school_v3",
):
    return create_virtual_module_handler(
        pbl_name=pbl_name,
        name=name,
        description=description,
        topic_ids=topic_ids,
        white_label=white_label,
    )


@mcp.tool(
    name="get_virtual_modules",
    description=(
        "List all virtual modules created via chat."
        "Parameters:"
        "- limit: Maximum results (default: 20)"
        "- offset: Pagination offset (default: 0)"
    ),
)
def get_virtual_modules(
    limit: int = 20, 
    offset: int = 0
):
    return get_virtual_modules_handler(
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_virtual_module_detail",
    description=(
        "Retrieve full details of a virtual module, including its associated topics."
        "Parameters:"
        "- virtual_module_id: Virtual module UUID"
    ),
)
def get_virtual_module_detail(virtual_module_id: str):
    return get_virtual_module_detail_handler(
        virtual_module_id=virtual_module_id
    )
