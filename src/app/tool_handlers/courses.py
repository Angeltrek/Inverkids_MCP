from src.backend.client import BackendClient
from src.mcp.decorators import with_backend_client, with_error_handling
from src.app.validators import Validator
from src.config.constants.endpoint_constants import (
    COURSES_LIST,
    COURSES_DATA,
    COURSES_NAMES,
)


@with_error_handling
@with_backend_client
def get_courses_handler(backend_client=None):
    return backend_client.get(COURSES_LIST)


def get_courses_by_user_type_handler(
    *,
    user_type: str,
    backend_client: BackendClient,
):
    return backend_client.get(
        COURSES_LIST,
        params={"user_type": user_type},
    )


def get_courses_names_handler(
    *,
    level: str,
    label: str,
    backend_client: BackendClient,
):
    return backend_client.get(
        COURSES_NAMES,
        params={
            "level": level,
            "label": label,
        },
    )


def get_courses_data_handler(
    *,
    level: str,
    label: str,
    backend_client: BackendClient,
):
    return backend_client.get(
        COURSES_DATA,
        params={
            "level": level,
            "label": label,
        },
    )
