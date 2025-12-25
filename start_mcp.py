import sys
from pathlib import Path

from src.mcp.app import mcp

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import src.mcp.tools.auth
import src.mcp.tools.catalog
import src.mcp.tools.courses
import src.mcp.tools.groups
import src.mcp.tools.users
import src.mcp.tools.schools
import src.mcp.tools.evaluation


def main():
    mcp.run()


if __name__ == "__main__":
    main()