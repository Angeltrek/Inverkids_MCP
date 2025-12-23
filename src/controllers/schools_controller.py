from src.infrastructure.http.backend_client import BackendClient
from src.infrastructure.config.constants.endpoint_constants import MCP_SCHOOLS


def get_schools(
    *,
    backend_client: BackendClient,
    white_label: str | None = None,
):

    return backend_client.get(
        MCP_SCHOOLS,
        params={"white_label": white_label} if white_label else None,
    )
