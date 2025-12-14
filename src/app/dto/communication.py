from dataclasses import dataclass
from typing import Literal

Channel = Literal["email", "whatsapp", "internal"]

@dataclass(frozen=True)
class RequestGuardianContactInput:
    reason: str
    channel: Channel
