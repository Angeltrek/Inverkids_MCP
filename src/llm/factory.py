from src.config.settings import load_llm_settings
from src.llm.contracts import LLMClient
from src.llm.openai_client import OpenAIClient
from src.config.llm_constants import DEFAULT_LLM_PROVIDER


def create_llm_client() -> LLMClient:
    """
    Composition root for LLM clients.
    """

    settings = load_llm_settings()

    if settings.provider == DEFAULT_LLM_PROVIDER:
        return OpenAIClient(settings)

    raise RuntimeError(f"Unsupported LLM provider: {settings.provider}")
