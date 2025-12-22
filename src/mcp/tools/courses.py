from src.mcp.app import mcp
from src.backend.context import get_backend_client
from src.app.tool_handlers.courses import (
    get_courses_handler,
    get_courses_by_user_type_handler,
    get_courses_names_handler,
    get_courses_data_handler,
)


@mcp.tool(name="get_courses", description="Retrieve the list of available courses.")
def get_courses(token: str):
    client = get_backend_client(token)
    return get_courses_handler(backend_client=client)


@mcp.tool(
    name="get_courses_by_user_type",
    description="Retrieve courses filtered by user type.",
)
def get_courses_by_user_type(user_type: str, token: str):
    client = get_backend_client(token)
    return get_courses_by_user_type_handler(
        user_type=user_type,
        backend_client=client,
    )


@mcp.tool(
    name="get_courses_names",
    description="Retrieve course names by level and white label.",
)
def get_courses_names(level: str, label: str, token: str):
    client = get_backend_client(token)
    return get_courses_names_handler(
        level=level,
        label=label,
        backend_client=client,
    )


@mcp.tool(
    name="get_courses_data",
    description="Retrieve full course data by level and white label.",
)
def get_courses_data(level: str, label: str, token: str):
    client = get_backend_client(token)
    return get_courses_data_handler(
        level=level,
        label=label,
        backend_client=client,
    )
