from src.mcp.app import mcp
from src.backend.context import get_backend_client
from src.app.tool_handlers.groups import (
    get_groups_handler,
    get_groups_by_level_handler,
    get_group_users_handler,
)


@mcp.tool(name="get_groups", description="Retrieve groups accessible to the current user.")
def get_groups(token: str):
    client = get_backend_client(token)
    return get_groups_handler(backend_client=client)


@mcp.tool(
    name="get_groups_by_level",
    description="Retrieve groups filtered by academic level.",
)
def get_groups_by_level(level: str | int, token: str):
    client = get_backend_client(token)
    return get_groups_by_level_handler(
        level=level,
        backend_client=client,
    )


@mcp.tool(
    name="get_group_users",
    description="Retrieve students belonging to one or more groups.",
)
def get_group_users(group_ids: list[str], token: str):
    client = get_backend_client(token)
    return get_group_users_handler(
        group_ids=group_ids,
        backend_client=client,
    )
