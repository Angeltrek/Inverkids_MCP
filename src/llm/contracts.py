from abc import ABC, abstractmethod


class LLMClient(ABC):
    """
    Port definition for any LLM provider.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a textual response from a prompt.
        """
        raise NotImplementedError
