from typing import Dict, Any, List, Optional

from src.llm.contracts import LLMClient
from src.config.constants.tool_names import GET_COURSES


class FakeLLMClient(LLMClient):
    """
    Deterministic fake LLM client for local testing.
    """

    def generate(
        self,
        prompt: str,
        tools: Optional[List[Dict[str, Any]]] = None,
    ) -> Dict[str, Any]:

        return {
            "tool_call": {
                "name": GET_COURSES,
                "arguments": {
                    "activity_id": "test-activity-id",
                },
            }
        }
