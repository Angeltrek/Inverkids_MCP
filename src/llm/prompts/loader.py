from functools import lru_cache

from src.llm.prompts.prompts import prompt_path


@lru_cache
def load_prompt(prompt_name: str) -> str:
    path = prompt_path(prompt_name)
    return path.read_text(encoding="utf-8")
