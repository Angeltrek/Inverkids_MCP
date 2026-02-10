from src.controllers.activities_controller import (
    get_activities_by_module,
    get_activities_by_skill,
    get_activities_by_level,
    get_activity_detail,
    generate_activity,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_activities_by_module_handler(
    *,
    backend_client: BackendClient,
    module_id: str,
    limit: int,
    offset: int,
):
    return get_activities_by_module(
        backend_client=backend_client,
        module_id=module_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_activities_by_skill_handler(
    *,
    backend_client: BackendClient,
    skill_id: str,
    limit: int,
    offset: int,
):
    return get_activities_by_skill(
        backend_client=backend_client,
        skill_id=skill_id,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_activities_by_level_handler(
    *,
    backend_client: BackendClient,
    level: str,
    limit: int,
    offset: int,
):
    return get_activities_by_level(
        backend_client=backend_client,
        level=level,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_activity_detail_handler(
    *,
    backend_client: BackendClient,
    activity_id: str,
):
    return get_activity_detail(
        backend_client=backend_client,
        activity_id=activity_id,
    )


@with_error_handling
@with_backend_client
def generate_activity_handler(
    *,
    backend_client: BackendClient,
    activity: dict,
    teacher: dict,
    module_ids: list[str],
    topic_ids: list[str],
):
    return generate_activity(
        backend_client=backend_client,
        activity=activity,
        teacher=teacher,
        module_ids=module_ids,
        topic_ids=topic_ids,
    )
