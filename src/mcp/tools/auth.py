from src.mcp.app import mcp
from src.mcp.handlers.auth_handlers import login_handler
import os


DEFAULT_ENROLLMENT = os.getenv("MCP_DEFAULT_ENROLLMENT_ID")
DEFAULT_PASSWORD = os.getenv("MCP_DEFAULT_PASSWORD")


@mcp.tool(
    name="login",
    description="Authenticate using explicit credentials or a configured service identity."
)
def login(
    enrollment_id: str | None = None,
    password: str | None = None,
):
    if enrollment_id and password:
        return login_handler(
            enrollment_id=enrollment_id,
            password=password,
        )

    if DEFAULT_ENROLLMENT and DEFAULT_PASSWORD:
        return login_handler(
            enrollment_id=DEFAULT_ENROLLMENT,
            password=DEFAULT_PASSWORD,
        )