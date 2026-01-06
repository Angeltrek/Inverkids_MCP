from src.infrastructure.config.constants.endpoint_constants import (
    MCP_SKILLS,
    MCP_SKILLS_BY_TYPE,
    MCP_SEARCH_SKILLS,
    MCP_SKILL_DETAIL,
)
from src.infrastructure.http.backend_client import BackendClient


def get_skills(
    *,
    backend_client: BackendClient,
):
    return backend_client.get(MCP_SKILLS)


def get_skills_by_type(
    *,
    backend_client: BackendClient,
    skill_type: str,
):
    return backend_client.get(
        MCP_SKILLS_BY_TYPE,
        params={"skill_type": skill_type},
    )


def search_skills(
    *,
    backend_client: BackendClient,
    query: str,
):
    return backend_client.get(
        MCP_SEARCH_SKILLS,
        params={"q": query},
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
