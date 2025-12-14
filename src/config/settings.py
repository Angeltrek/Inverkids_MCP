import os
from dataclasses import dataclass
from src.config.constants.env_constants import (
    ENV_LLM_PROVIDER,
    ENV_OPENAI_API_KEY,
    ENV_OPENAI_MODEL,
)
from src.config.constants.llm_constants import (
    DEFAULT_LLM_PROVIDER,
    DEFAULT_OPENAI_MODEL,
)


@dataclass(frozen=True)
class LLMSettings:
    provider: str
    api_key: str
    model: str


def load_llm_settings() -> LLMSettings:
    provider = os.getenv(ENV_LLM_PROVIDER, DEFAULT_LLM_PROVIDER)
    api_key = os.getenv(ENV_OPENAI_API_KEY)
    model = os.getenv(ENV_OPENAI_MODEL, DEFAULT_OPENAI_MODEL)

    if not api_key:
        raise RuntimeError("API_KEY is not set")

    return LLMSettings(
        provider=provider,
        api_key=api_key,
        model=model,
    )
