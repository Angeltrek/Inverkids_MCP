from typing import List
from src.infrastructure.http.backend_client import BackendClient
from src.infrastructure.config.constants.endpoint_constants import (
    MCP_CREATE_VIRTUAL_MODULE,
    MCP_VIRTUAL_MODULES,
    MCP_VIRTUAL_MODULE_DETAIL,
)
from typing import List, Dict, Optional


def create_virtual_module(
    *,
    backend_client: BackendClient,
    pbl_name: Dict[str, str],
    module_number: int,
    level: str,
    name: Dict[str, str],
    description: Dict[str, str],
    topic_ids: List[str],
    white_label: Optional[str] = "inverkids_school_v3",
):
    return backend_client.post(
        MCP_CREATE_VIRTUAL_MODULE,
        json={
            "pbl_name": pbl_name,
            "module_number": module_number,
            "level": level,
            "white_label": white_label,
            "name": name,
            "description": description,
            "topic_ids": topic_ids,
        },
    )


def get_virtual_modules(
    *,
    backend_client: BackendClient,
    limit: int,
    offset: int,
):
    return backend_client.get(
        MCP_VIRTUAL_MODULES,
        params={
            "limit": limit,
            "offset": offset,
        },
    )


def get_virtual_module_detail(
    *,
    backend_client: BackendClient,
    virtual_module_id: str,
):
    return backend_client.get(
        MCP_VIRTUAL_MODULE_DETAIL,
        params={"virtual_module_id": virtual_module_id},
    )
