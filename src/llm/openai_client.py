from openai import OpenAI

from src.llm.contracts import LLMClient
from src.config.settings import LLMSettings
from src.config.llm_constants import (
    LLM_ROLE_USER,
    LLM_MESSAGE_ROLE_KEY,
    LLM_MESSAGE_CONTENT_KEY,
)


class OpenAIClient(LLMClient):
    """
    OpenAI implementation of the LLMClient port.
    """

    def __init__(self, settings: LLMSettings) -> None:
        self._client = OpenAI(api_key=settings.api_key)
        self._model = settings.model

    def generate(self, prompt: str) -> str:
        response = self._client.chat.completions.create(
            model=self._model,
            messages=[
                {
                    LLM_MESSAGE_ROLE_KEY: LLM_ROLE_USER,
                    LLM_MESSAGE_CONTENT_KEY: prompt,
                }
            ],
        )

        return response.choices[0].message.content or ""
