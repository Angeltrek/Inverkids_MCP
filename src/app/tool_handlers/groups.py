import re

from src.backend.client import BackendClient
from src.config.constants.endpoint_constants import (
    GROUPS_LIST,
    GROUPS_BY_LEVEL,
    GROUP_USERS,
)
from src.app.models.groups import (
    GetGroupsByLevelInput,
    GetGroupUsersInput,
)

def normalize_level(level: str | int) -> str:
    if isinstance(level, int):
        return str(level)

    level = str(level).strip().lower()

    match = re.search(r"\d+", level)
    if match:
        return match.group()

    return level

def get_groups_handler(args, *, backend_client: BackendClient):
    return backend_client.get(GROUPS_LIST)


def get_groups_by_level_handler(args, *, backend_client: BackendClient):

    dto = GetGroupsByLevelInput(level=normalize_level(args["level"]))

    return backend_client.post(
        GROUPS_BY_LEVEL,
        json={"level": dto.level},
    )


def get_group_users_handler(args, *, backend_client: BackendClient):

    dto = GetGroupUsersInput(group_ids=args["group_ids"])

    return backend_client.post(
        GROUP_USERS,
        json={"group_ids[]": dto.group_ids},
    )