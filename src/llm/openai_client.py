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
            return {
                "tool_calls": [
                    {
                        "id": tc.id,
                        "name": tc.function.name,
                        "arguments": tc.function.arguments,
                    }
                    for tc in message.tool_calls
                ]
            }

        return {
            "content": message.content or "",
        }
