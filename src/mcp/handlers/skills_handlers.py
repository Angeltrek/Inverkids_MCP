from src.controllers.skills_controller import (
    get_skills,
    get_skills_by_type,
    search_skills,
    get_skill_detail,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_skills_handler(
    *,
    backend_client: BackendClient,
):
    return get_skills(backend_client=backend_client)


@with_error_handling
@with_backend_client
def get_skills_by_type_handler(
    *,
    backend_client: BackendClient,
    skill_type: str,
):
    return get_skills_by_type(
        backend_client=backend_client,
        skill_type=skill_type,
    )


@with_error_handling
@with_backend_client
def search_skills_handler(
    *,
    backend_client: BackendClient,
    query: str,
):
    return search_skills(
        backend_client=backend_client,
        query=query,
    )


@with_error_handling
@with_backend_client
def get_skill_detail_handler(
    *,
    backend_client: BackendClient,
    skill_id: str,
):
    return get_skill_detail(
        backend_client=backend_client,
        skill_id=skill_id,
    )
