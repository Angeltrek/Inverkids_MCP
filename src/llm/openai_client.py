from openai import OpenAI
from typing import Dict, Any, List, Optional

from src.llm.contracts import LLMClient
from src.config.settings import LLMSettings


class OpenAIClient(LLMClient):
    """
    OpenAI implementation of the LLMClient port.
    """

    def __init__(self, settings: LLMSettings) -> None:
        self._client = OpenAI(api_key=settings.api_key)
        self._model = settings.model

    def generate(
        self,
        *,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]] = None,
    ) -> Dict[str, Any]:

        response = self._client.chat.completions.create(
            model=self._model,
            messages=messages,
            tools=tools,
            tool_choice="auto",
        )

        message = response.choices[0].message

        if message.tool_calls:
            tool_call = message.tool_calls[0]
            return {
                "tool_call": {
                    "id": tool_call.id,
                    "name": tool_call.function.name,
                    "arguments": tool_call.function.arguments,
                }
            }

        return {
            "content": message.content or "",
        }
