from mcp.server.fastmcp import FastMCP
from src.infrastructure.config.settings.settings import load_settings

import json, logging
from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent

logger = logging.getLogger(__name__)

class SafeFastMCP(FastMCP):
    async def call_tool(self, name, arguments):
        try:
            return await super().call_tool(name, arguments)
        except Exception as e:
            logger.error("Tool failed: %s", name, exc_info=True)
            known = sorted(t.name for t in self._tool_manager.list_tools())
            return [TextContent(type="text", text=json.dumps({
                "ok": False,
                "error": type(e).__name__,
                "message": str(e),
                "available_tools": known,
            }))]

settings = load_settings()

mcp = SafeFastMCP(
    name=settings.mcp.name,
    host=settings.mcp.host,
    port=settings.mcp.port,
    stateless_http=True,
    json_response=True
)
