"""
Public LLM client entrypoint.

This module exposes the LLMClient abstraction to the application
while hiding provider selection and configuration details.

No SDKs, no environment variables, no business logic.
"""

from src.llm.contracts import LLMClient
from src.llm.factory import create_llm_client

from typing import Dict, Any
from src.llm.contracts import LLMClient

# TEMPORARY for local testing
# class FakeLLMClient(LLMClient):
#     def generate(self, prompt: str, tools=None) -> Dict[str, Any]:
#         print("LLM received prompt:", prompt)
#         print("LLM received tools:", [t["function"]["name"] for t in tools or []])

#         # Force a tool call to test Feature 3
#         return {
#             "tool_call": {
#                 "name": "get_activity",
#                 "arguments": {
#                     "activity_id": "test-activity-id"
#                 }
#             }
#         }
    



def get_llm_client() -> LLMClient:
    """
    Return an LLMClient instance.

    This function acts as the single access point for the application
    to interact with an LLM.
    """
    # return FakeLLMClient()
    return create_llm_client()
