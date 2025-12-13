"""
Public LLM client entrypoint.

This module exposes the LLMClient abstraction to the application
while hiding provider selection and configuration details.

No SDKs, no environment variables, no business logic.
"""

from src.llm.contracts import LLMClient
from src.llm.factory import create_llm_client


def get_llm_client() -> LLMClient:
    """
    Return an LLMClient instance.

    This function acts as the single access point for the application
    to interact with an LLM.
    """
    return create_llm_client()
