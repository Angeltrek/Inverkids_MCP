from src.infrastructure.http.backend_client import BackendClient
from src.infrastructure.config.constants.endpoint_constants import CATALOG_FULL


def get_full_catalog(
    level: str,
    white_label: str,
    user_lang: str,
    backend_client: BackendClient,
):
    return backend_client.get(
        CATALOG_FULL,
        params={
            "level": level,
            "white_label": white_label,
            "userLang": user_lang,
        },
    )
