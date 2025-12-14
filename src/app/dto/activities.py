from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class GetActivityInput:
    activity_id: str

@dataclass(frozen=True)
class GetActivitiesByTopicInput:
    topic_id: str
    activity_type: Optional[str] = None
    limit: int = 5
