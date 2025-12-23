from typing import Iterable
from src.infrastructure.http.backend_client import BackendClient
from src.infrastructure.config.constants.endpoint_constants import (
    GROUPS_LIST,
    GROUPS_BY_LEVEL,
    GROUP_USERS,
)


def get_groups(backend_client: BackendClient):
    return backend_client.get(GROUPS_LIST)


def get_groups_by_level(level: str, backend_client: BackendClient):

    return backend_client.post(
        GROUPS_BY_LEVEL,
        json={"level": level},
    )


def get_group_users(
    group_ids: Iterable[str],
    backend_client: BackendClient,
):
    return backend_client.post(
        GROUP_USERS,
        json={"group_ids[]": list(group_ids)},
    )
