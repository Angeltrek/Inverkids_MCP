import sys
import os
from pathlib import Path


print("INICIANDO SERVIDOR MCP", file=sys.stderr)
print(f"Python: {sys.executable}", file=sys.stderr)
print(f"CWD: {os.getcwd()}", file=sys.stderr)

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

print(f"PROJECT_ROOT agregado: {PROJECT_ROOT}", file=sys.stderr)

try:
    import asyncio
    from src.mcp.app import mcp
    import src.mcp.tools.auth
    import src.mcp.tools.catalog
    import src.mcp.tools.courses
    import src.mcp.tools.groups
    import src.mcp.tools.profile

    if __name__ == "__main__":
        asyncio.run(mcp.run())
        
except Exception as e:
    print(f"ERROR FATAL: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)