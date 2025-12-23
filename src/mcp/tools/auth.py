from src.mcp.app import mcp
from src.mcp.handlers.auth_handlers import login_handler


@mcp.tool(
    name="login",
    description="Authenticate a user using enrollment_id and password.",
)
def login(enrollment_id: str, password: str):
    return login_handler(
        enrollment_id=enrollment_id,
        password=password,
    )
