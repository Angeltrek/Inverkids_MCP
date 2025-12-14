from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional


class LLMClient(ABC):
    """
    Port definition for any LLM provider.
    """

    @abstractmethod
    def generate(
        self,
        *,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]] = None,
    ) -> Dict[str, Any]:
        """
        Generate a response from a conversation, possibly including tool calls.
        """
        raise NotImplementedError
