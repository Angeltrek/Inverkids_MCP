from typing import List, Dict, Any

from .catalog import catalog_tools
from .courses import courses_tools
from .groups import groups_tools
from .profile import profile_tools
from .statistics import statistics_tools
from .topics import topic_tools


def get_llm_tools() -> List[Dict[str, Any]]:
    """
    Aggregate all LLM tool definitions in one place.
    """

    return (
        catalog_tools()
        + courses_tools()
        + groups_tools()
        + profile_tools()
        + statistics_tools()
        + topic_tools()
    )
