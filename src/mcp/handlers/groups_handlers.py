from collections.abc import Iterable

from src.controllers.groups_controller import (
    get_group_users,
    get_groups,
    get_groups_by_level,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_groups_handler(*, backend_client: BackendClient):
    return get_groups(backend_client)


@with_error_handling
@with_backend_client
def get_groups_by_level_handler(
    level: str,
    *,
    backend_client: BackendClient,
):
    return get_groups_by_level(level, backend_client)


@with_error_handling
@with_backend_client
def get_group_users_handler(
    *,
    group_ids: Iterable[str],
    backend_client: BackendClient,
):
    return get_group_users(group_ids, backend_client)
