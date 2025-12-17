from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Session:
    user: Dict[str, Any]
    token: str
