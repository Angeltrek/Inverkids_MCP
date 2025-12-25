from dataclasses import dataclass
from typing import Any


@dataclass
class Session:
    user: dict[str, Any]
    token: str
