import os
from src.models.settings.settings import Settings
from src.models.settings.backend import BackendConfig
from src.models.settings.mcp import MCPConfig
from .env import load_environment

def load_settings() -> Settings:
    """
    Build Settings from environment variables.
    """
    load_environment()

    base_url = os.getenv("BACKEND_BASE_URL")
    if not base_url:
        raise RuntimeError(
            "BACKEND_BASE_URL environment variable is required. "
            "Please set it in your .env file."
        )

    return Settings(
        backend=BackendConfig(
            base_url=base_url,
            timeout=int(os.getenv("HTTP_TIMEOUT", "30")),
            max_retries=int(os.getenv("MAX_RETRIES", "3")),
            auth_timeout=int(os.getenv("AUTH_TIMEOUT", "10")),
        ),
        mcp=MCPConfig(
            name=os.getenv("MCP_NAME", "inverkids-mcp"),
            log_level=os.getenv("LOG_LEVEL", "INFO"),
        ),
    )
