import asyncio
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.mcp.app import mcp

import src.mcp.tools.auth
import src.mcp.tools.catalog
import src.mcp.tools.courses
import src.mcp.tools.groups
import src.mcp.tools.profile


def main():
    asyncio.run(mcp.run())


if __name__ == "__main__":
    main()
