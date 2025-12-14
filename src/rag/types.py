from dataclasses import dataclass
from typing import Dict, Any


@dataclass(frozen=True)
class ContextDocument:
    type: str
    id: str
    title: str
    content: str
    metadata: Dict[str, Any]
