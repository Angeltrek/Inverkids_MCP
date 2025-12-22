from src.mcp.app import mcp
from src.backend.context import get_backend_client
from src.app.tool_handlers.catalog import get_full_catalog_handler


@mcp.tool(
    name="get_full_catalog",
    description="Retrieve the complete catalog hierarchy.",
)
def get_full_catalog(
    level: str,
    white_label: str,
    user_lang: str,
    token: str,
):
    client = get_backend_client(token)
    return get_full_catalog_handler(
        level=level,
        white_label=white_label,
        user_lang=user_lang,
        backend_client=client,
    )
