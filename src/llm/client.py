"""
Public LLM client entrypoint.

No SDKs
No environment variables
No business logic
"""

from src.llm.contracts import LLMClient
from src.llm.factory import create_llm_client


def get_llm_client() -> LLMClient:
    """
    Single access point for obtaining an LLM client.
    """
    return create_llm_client()
