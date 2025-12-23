from src.infrastructure.http.backend_client import BackendClient
from src.infrastructure.config.constants.endpoint_constants import (
    COURSES_LIST,
    COURSES_DATA,
    COURSES_NAMES,
)


def get_courses(backend_client: BackendClient):
    return backend_client.get(COURSES_LIST)


def get_courses_by_user_type(
    user_type: str,
    backend_client: BackendClient,
):
    return backend_client.get(
        COURSES_LIST,
        params={"user_type": user_type},
    )


def get_courses_names(
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


def get_courses_data(
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
