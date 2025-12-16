from typing import List, Dict, Any

from src.llm.prompts.loader import load_prompt
from src.config.constants.llm_constants import (
    LLM_ROLE_SYSTEM,
    LLM_ROLE_USER,
    LLM_KEY_ROLE,
    LLM_KEY_CONTENT,
)
from src.config.constants.prompt_constants import (
    PROMPT_SYSTEM,
    PROMPT_INTENT,
    PROMPT_FORMATTER,
)


def build_context(user_prompt: str) -> List[Dict[str, Any]]:
    return [
        {
            LLM_KEY_ROLE: LLM_ROLE_SYSTEM,
            LLM_KEY_CONTENT: load_prompt(PROMPT_SYSTEM),
        },
        {
            LLM_KEY_ROLE: LLM_ROLE_SYSTEM,
            LLM_KEY_CONTENT: load_prompt(PROMPT_INTENT),
        },
        {
            LLM_KEY_ROLE: LLM_ROLE_SYSTEM,
            LLM_KEY_CONTENT: load_prompt(PROMPT_FORMATTER),
        },
        {
            LLM_KEY_ROLE: LLM_ROLE_USER,
            LLM_KEY_CONTENT: user_prompt,
        },
    ]
