from src.infrastructure.config.constants.endpoint_constants import MCP_SCHOOLS
from src.infrastructure.http.backend_client import BackendClient


def get_schools(
    *,
    backend_client: BackendClient,
    white_label: str | None = None,
):

    return backend_client.get(
        MCP_SCHOOLS,
        params={"white_label": white_label} if white_label else None,
    )
