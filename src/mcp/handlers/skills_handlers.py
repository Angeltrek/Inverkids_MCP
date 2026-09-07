from src.controllers.skills_controller import (
    get_skills,
    search_skills_by_keywords,
    get_skill_detail,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_skills_handler(
    *,
    backend_client: BackendClient,
    limit: int = 20,
    offset: int = 0,
):
    return get_skills(
        backend_client=backend_client,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def search_skills_by_keywords_handler(
    *,
    backend_client: BackendClient,
    keywords: list[str],
    lang: str = "es",
    white_label: str | None = None,
    level: str | None = None,
):
    return search_skills_by_keywords(
        backend_client=backend_client,
        keywords=keywords,
        lang=lang,
        white_label=white_label,
        level=level,
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
