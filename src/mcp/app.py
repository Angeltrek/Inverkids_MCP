from mcp.server.fastmcp import FastMCP
from src.infrastructure.config.settings.settings import load_settings

settings = load_settings()

mcp = FastMCP(
    name=settings.mcp.name,
    host=settings.mcp.host,
    port=settings.mcp.port,
)
