from dataclasses import dataclass
from typing import Optional, Literal

UserType = Literal["student", "teacher", "parent"]

@dataclass(frozen=True)
class SearchUsersInput:
    query: str
    user_type: Optional[UserType] = None
    limit: int = 5
