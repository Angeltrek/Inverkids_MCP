from src.infrastructure.config.constants.endpoint_constants import (
    MCP_MODULES,
    MCP_MODULES_BY_LEVEL,
    MCP_MODULES_BY_WHITE_LABEL,
    MCP_MODULES_BY_LEVEL_AND_WHITE_LABEL,
    MCP_MODULES_BY_NUMBER,
    MCP_LAST_MODULE_BY_LEVEL,
    MCP_SEARCH_MODULES_BY_NAME,
    MCP_MODULE_DETAIL,
)
from src.infrastructure.http.backend_client import BackendClient


def get_modules(
    *,
    backend_client: BackendClient,
):
    return backend_client.get(MCP_MODULES)


def get_modules_by_level(
    *,
    backend_client: BackendClient,
    level: str,
):
    return backend_client.get(
        MCP_MODULES_BY_LEVEL,
        params={"level": level},
    )


def get_modules_by_white_label(
    *,
    backend_client: BackendClient,
    white_label: str,
):
    return backend_client.get(
        MCP_MODULES_BY_WHITE_LABEL,
        params={"white_label": white_label},
    )


def get_modules_by_level_and_white_label(
    *,
    backend_client: BackendClient,
    level: str,
    white_label: str,
):
    return backend_client.get(
        MCP_MODULES_BY_LEVEL_AND_WHITE_LABEL,
        params={
            "level": level,
            "white_label": white_label,
        },
    )


def get_modules_by_number(
    *,
    backend_client: BackendClient,
    module_number: int,
):
    return backend_client.get(
        MCP_MODULES_BY_NUMBER,
        params={"module_number": module_number},
    )


def get_last_module_by_level(
    *,
    backend_client: BackendClient,
    level: str,
):
    return backend_client.get(
        MCP_LAST_MODULE_BY_LEVEL,
        params={"level": level},
    )


def search_modules_by_name(
    *,
    backend_client: BackendClient,
    query: str,
):
    return backend_client.get(
        MCP_SEARCH_MODULES_BY_NAME,
        params={"q": query},
    )


def get_module_detail(
    *,
    backend_client: BackendClient,
    module_id: str,
):
    return backend_client.get(
        MCP_MODULE_DETAIL,
        params={"module_id": module_id},
    )
