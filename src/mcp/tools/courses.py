from src.mcp.app import mcp
from src.mcp.handlers.courses_handlers import (
    get_courses_handler,
    get_courses_by_user_type_handler,
    get_courses_names_handler,
    get_courses_data_handler,
)


@mcp.tool(name="get_courses", description="Retrieve the list of available courses.")
def get_courses(token: str):
    return get_courses_handler(token=token)


@mcp.tool(
    name="get_courses_by_user_type",
    description="Retrieve courses filtered by user type.",
)
def get_courses_by_user_type(user_type: str, token: str):
    return get_courses_by_user_type_handler(
        user_type=user_type,
        token=token,
    )


@mcp.tool(
    name="get_courses_names",
    description="Retrieve course names by level and white label.",
)
def get_courses_names(level: str, label: str, token: str):
    return get_courses_names_handler(
        level=level,
        label=label,
        token=token,
    )


@mcp.tool(
    name="get_courses_data",
    description="Retrieve full course data by level and white label.",
)
def get_courses_data(level: str, label: str, token: str):
    return get_courses_data_handler(
        level=level,
        label=label,
        token=token,
    )
