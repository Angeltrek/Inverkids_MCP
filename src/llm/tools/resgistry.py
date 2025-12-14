from typing import List, Dict, Any

from .curriculum import curriculum_tools
from .texts import text_tools
from .activities import activity_tools
from .performance import performance_tools
from .users import user_tools
from .communication import communication_tools


def get_llm_tools() -> List[Dict[str, Any]]:
    """
    Aggregate all LLM tool definitions in one place.
    """

    return (
        curriculum_tools()
        + text_tools()
        + activity_tools()
        + performance_tools()
        + user_tools()
        + communication_tools()
    )
