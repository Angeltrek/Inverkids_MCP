import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=== MCP Server Starting ===", file=sys.stderr, flush=True)
print(f"Working directory: {os.getcwd()}", file=sys.stderr, flush=True)
print(f"Python: {sys.executable}", file=sys.stderr, flush=True)

try:
    import asyncio
    from src.mcp.app import mcp

    import src.mcp.tools.auth
    import src.mcp.tools.catalog
    import src.mcp.tools.courses
    import src.mcp.tools.groups
    import src.mcp.tools.profile
    
    print("All imports successful, starting server...", file=sys.stderr, flush=True)
    
    asyncio.run(mcp.run())
    
except KeyboardInterrupt:
    print("Server stopped by user", file=sys.stderr, flush=True)
except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr, flush=True)
    import traceback
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)