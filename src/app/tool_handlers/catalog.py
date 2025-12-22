from src.backend.client import BackendClient
from src.config.constants.endpoint_constants import CATALOG_FULL


def get_full_catalog_handler(
    *,
    level: str,
    white_label: str,
    user_lang: str,
    backend_client: BackendClient,
):

    response = backend_client.get(
        CATALOG_FULL,
        params={
            "level": level,
            "white_label": white_label,
            "userLang": user_lang,
        },
    )

    return response
