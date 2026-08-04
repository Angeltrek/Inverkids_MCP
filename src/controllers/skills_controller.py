from src.infrastructure.config.constants.endpoint_constants import (
    MCP_SKILLS,
    MCP_SEARCH_SKILLS_BY_KEYWORDS,
    MCP_SKILL_DETAIL,
)
from src.infrastructure.http.backend_client import BackendClient


def get_skills(
    *,
    backend_client: BackendClient,
    limit: int = 20,
    offset: int = 0,
):
    return backend_client.get(
        MCP_SKILLS,
        params={
            "limit": limit,
            "offset": offset,
        },
    )

def search_skills_by_keywords(
    *,
    backend_client: BackendClient,
    keywords: list[str],
    lang: str = "es",
):
    return backend_client.get(
        MCP_SEARCH_SKILLS_BY_KEYWORDS,
        params={"keywords[]": keywords, "lang": lang},
    )


def get_skill_detail(
    *,
    backend_client: BackendClient,
    skill_id: str,
):
    return backend_client.get(
        MCP_SKILL_DETAIL,
        params={"skill_id": skill_id},
    )
