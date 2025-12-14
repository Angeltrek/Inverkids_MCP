from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class LLMClient(ABC):
    """
    Port definition for any LLM provider.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str,
        tools: Optional[List[Dict[str, Any]]] = None,
    ) -> Dict[str, Any]:
        """
        Generate a response from a prompt.

        The response may be:
        - plain text
        - a tool call
        """
        raise NotImplementedError
