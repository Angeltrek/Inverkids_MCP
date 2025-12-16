from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

PROMPTS_BASE_PATH = PROJECT_ROOT / "src" / "llm" / "prompts"

def prompt_path(prompt_name: str) -> Path:
    return PROMPTS_BASE_PATH / f"{prompt_name}.txt"
