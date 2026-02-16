from src.infrastructure.config.constants.endpoint_constants import MCP_TAGS_LIST
from src.infrastructure.http.backend_client import BackendClient


def get_tags(
    *, 
    backend_client: BackendClient, 
    limit: int, 
    offset: int
):
    return backend_client.get(
        MCP_TAGS_LIST,
        params={
            "limit": limit, 
            "offset": offset
        },
    )
