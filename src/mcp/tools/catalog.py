from src.mcp.app import mcp
from src.mcp.handlers.catalog_handlers import get_full_catalog_handler


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
    return get_full_catalog_handler(
        level=level,
        white_label=white_label,
        user_lang=user_lang,
        token=token,
    )
