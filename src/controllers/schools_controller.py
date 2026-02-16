from src.infrastructure.config.constants.endpoint_constants import (
    MCP_SCHOOLS_LIST,
    MCP_SCHOOL_DETAIL,
)
from src.infrastructure.http.backend_client import BackendClient


def get_schools_list(
    *,
    backend_client: BackendClient,
    limit: int = 20,
    offset: int = 0,
):
    return backend_client.get(
        MCP_SCHOOLS_LIST,
        params={
            "limit": limit,
            "offset": offset,
        },
    )


def get_school_detail(
    *,
    backend_client: BackendClient,
    school_id: str,
):
    return backend_client.get(
        MCP_SCHOOL_DETAIL,
        params={"school_id": school_id},
    )
