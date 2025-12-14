from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class GetModulesInput:
    level: str
    search: Optional[str] = None
    limit: int = 10


@dataclass(frozen=True)
class GetTopicsByModuleInput:
    module_id: str
