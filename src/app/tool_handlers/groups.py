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


def get_groups_handler(args, *, backend_client: BackendClient):
    return backend_client.get(GROUPS_LIST)


def get_groups_by_level_handler(args, *, backend_client: BackendClient):
    dto = GetGroupsByLevelInput(level=args["level"])
    return backend_client.get(
        GROUPS_BY_LEVEL,
        params={"level": dto.level},
    )


def get_group_users_handler(args, *, backend_client: BackendClient):
    dto = GetGroupUsersInput(group_ids=args["group_ids"])
    return backend_client.get(
        GROUP_USERS,
        params={"group_ids[]": dto.group_ids},
    )