from src.config.settings import load_llm_settings
from src.llm.contracts import LLMClient
from src.llm.openai_client import OpenAIClient
from src.llm.fake_client import FakeLLMClient
from src.config.llm_constants import DEFAULT_LLM_PROVIDER


def create_llm_client() -> LLMClient:
    settings = load_llm_settings()

    if settings.provider == "fake":
        return FakeLLMClient()

    if settings.provider == DEFAULT_LLM_PROVIDER:
        return OpenAIClient(settings)

    raise RuntimeError(f"Unsupported LLM provider: {settings.provider}")
