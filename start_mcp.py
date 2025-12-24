import sys
from pathlib import Path

from src.mcp.app import mcp

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))



def main():
    mcp.run()


if __name__ == "__main__":
    main()
