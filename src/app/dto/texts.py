from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class GetTextsByTopicInput:
    topic_id: str
    limit: int = 5

@dataclass(frozen=True)
class SearchTextsInput:
    query: str
    topic_id: Optional[str] = None
    limit: int = 5