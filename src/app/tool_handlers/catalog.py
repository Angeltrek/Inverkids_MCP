from src.app.models.catalog import GetFullCatalogInput
from src.backend.client import BackendClient
from src.config.constants.endpoint_constants import CATALOG_FULL


def get_full_catalog_handler(args, *, backend_client: BackendClient):
    """
    Calls backend full catalog endpoint.
    """

    dto = GetFullCatalogInput(
        level=args["level"],
        white_label=args["white_label"],
        user_lang=args["user_lang"],
    )

    response = backend_client.get(
        CATALOG_FULL,
        params={
            "level": dto.level,
            "white_label": dto.white_label,
            "userLang": dto.user_lang,
        },
    )

    return response
