import re
from typing import Union, Iterable
from src.mcp.decorators import with_backend_client, with_error_handling
from src.app.validators import Validator
from src.backend.client import BackendClient
from src.config.constants.endpoint_constants import (
    GROUPS_LIST,
    GROUPS_BY_LEVEL,
    GROUP_USERS,
)


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

@with_error_handling
@with_backend_client  
def get_groups_by_level_handler(level, backend_client=None):
    level = Validator.validate_level(level)
    
    return backend_client.post(
        GROUPS_BY_LEVEL,
        json={"level": level}
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
