from src.mcp.app import mcp
from src.mcp.handlers.groups_handlers import (
    get_groups_handler,
    get_groups_by_level_handler,
    get_group_users_handler,
)


@mcp.tool(
    name="get_groups",
    description="Retrieve groups accessible to the current user.",
)
def get_groups(token: str):
    return get_groups_handler(token=token)


@mcp.tool(
    name="get_groups_by_level",
    description="Retrieve groups filtered by academic level.",
)
def get_groups_by_level(level: str | int, token: str):
    return get_groups_by_level_handler(
        level=level,
        token=token,
    )


@mcp.tool(
    name="get_group_users",
    description="Retrieve students belonging to one or more groups.",
)
def get_group_users(group_ids: list[str], token: str):
    return get_group_users_handler(
        group_ids=group_ids,
        token=token,
    )
