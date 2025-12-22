import sys
import os
from pathlib import Path

print("=" * 60, file=sys.stderr)
print("INICIANDO SERVIDOR MCP", file=sys.stderr)
print(f"Python: {sys.executable}", file=sys.stderr)
print(f"CWD: {os.getcwd()}", file=sys.stderr)
print("=" * 60, file=sys.stderr)

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

print(f"PROJECT_ROOT agregado: {PROJECT_ROOT}", file=sys.stderr)

try:
    import asyncio
    print("asyncio importado", file=sys.stderr)
    
    from src.mcp.app import mcp
    print("mcp app importado", file=sys.stderr)
    
    import src.mcp.tools.auth
    print("auth importado", file=sys.stderr)
    
    import src.mcp.tools.catalog
    print("catalog importado", file=sys.stderr)
    
    import src.mcp.tools.courses
    print("courses importado", file=sys.stderr)
    
    import src.mcp.tools.groups
    print("groups importado", file=sys.stderr)
    
    import src.mcp.tools.profile
    print("profile importado", file=sys.stderr)
    
    print("Todas las importaciones exitosas", file=sys.stderr)
    print("Iniciando servidor...", file=sys.stderr)
    
    if __name__ == "__main__":
        asyncio.run(mcp.run())
        
except Exception as e:
    print(f"ERROR FATAL: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)