from src.infrastructure.config.constants.endpoint_constants import (
    MCP_MODULES,
    MCP_MODULES_BY_WHITE_LABEL,
    MCP_MODULES_BY_LEVEL_AND_WHITE_LABEL,
    MCP_MODULES_BY_NUMBER,
    MCP_MODULE_DETAIL,
)
from src.infrastructure.http.backend_client import BackendClient


def get_modules(*, backend_client: BackendClient, limit: int, offset: int):
    return backend_client.get(
        MCP_MODULES,
        params={"limit": limit, "offset": offset},
    )


def get_modules_by_white_label(
    *, backend_client: BackendClient, white_label: str, limit: int, offset: int
):
    return backend_client.get(
        MCP_MODULES_BY_WHITE_LABEL,
        params={"white_label": white_label, "limit": limit, "offset": offset},
    )


def get_modules_by_level_and_white_label(
    *,
    backend_client: BackendClient,
    level: str,
    white_label: str,
    limit: int,
    offset: int,
):
    return backend_client.get(
        MCP_MODULES_BY_LEVEL_AND_WHITE_LABEL,
        params={
            "level": level,
            "white_label": white_label,
            "limit": limit,
            "offset": offset,
        },
    )


def get_modules_by_number(
    *, backend_client: BackendClient, module_number: int, limit: int, offset: int
):
    return backend_client.get(
        MCP_MODULES_BY_NUMBER,
        params={
            "module_number": module_number,
            "limit": limit,
            "offset": offset,
        },
    )


def get_module_detail(*, backend_client: BackendClient, module_id: str):
    return backend_client.get(
        MCP_MODULE_DETAIL,
        params={"module_id": module_id},
    )
