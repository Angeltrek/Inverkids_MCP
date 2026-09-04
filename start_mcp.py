import sys
from pathlib import Path

from src.mcp.app import mcp

from src.utils.logging_config import setup_logging
from src.mcp.app import settings

setup_logging(settings.mcp.log_level)

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import src.mcp.tools.activities
import src.mcp.tools.component_alternatives
import src.mcp.tools.modules
import src.mcp.tools.feedback
import src.mcp.tools.grades
import src.mcp.tools.groups
import src.mcp.tools.schools
import src.mcp.tools.skills
import src.mcp.tools.texts
import src.mcp.tools.topics
import src.mcp.tools.users
import src.mcp.tools.tags


def main():
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
