from src.controllers.activities_controller import (
    get_activities_by_module,
    get_activities_by_type,
    get_first_activity_by_topic,
    get_extra_activities,
    get_activities_by_skill,
    get_activities_by_level,
    search_activities_by_name,
    get_activity_detail,
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
def get_activities_by_type_handler(
    *,
    backend_client: BackendClient,
    activity_type: str,
    limit: int,
    offset: int,
):
    return get_activities_by_type(
        backend_client=backend_client,
        activity_type=activity_type,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_first_activity_by_topic_handler(
    *,
    backend_client: BackendClient,
    topic_id: str,
):
    return get_first_activity_by_topic(
        backend_client=backend_client,
        topic_id=topic_id,
    )


@with_error_handling
@with_backend_client
def get_extra_activities_handler(
    *,
    backend_client: BackendClient,
    limit: int,
    offset: int,
):
    return get_extra_activities(
        backend_client=backend_client,
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
def search_activities_by_name_handler(
    *,
    backend_client: BackendClient,
    query: str,
    limit: int,
    offset: int,
):
    return search_activities_by_name(
        backend_client=backend_client,
        query=query,
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
