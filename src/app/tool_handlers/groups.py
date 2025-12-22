import re
from typing import Union, Iterable

from src.backend.client import BackendClient
from src.config.constants.endpoint_constants import (
    GROUPS_LIST,
    GROUPS_BY_LEVEL,
    GROUP_USERS,
)


def normalize_level(level: Union[str, int]) -> str:
    if isinstance(level, int):
        return str(level)

    level_str = str(level).strip().lower()

    match = re.search(r"\d+", level_str)
    if match:
        return match.group()

    return level_str


def get_groups_handler(
    *,
    backend_client: BackendClient,
):
    return backend_client.get(GROUPS_LIST)


def get_groups_by_level_handler(
    *,
    level: Union[str, int],
    backend_client: BackendClient,
):
    normalized_level = normalize_level(level)

    return backend_client.post(
        GROUPS_BY_LEVEL,
        json={"level": normalized_level},
    )


def get_group_users_handler(
    *,
    group_ids: Iterable[str],
    backend_client: BackendClient,
):
    return backend_client.post(
        GROUP_USERS,
        json={"group_ids[]": list(group_ids)},
    )
