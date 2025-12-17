from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class GetGroupsInput:
    pass


@dataclass(frozen=True)
class GetGroupsByLevelInput:
    level: str


@dataclass(frozen=True)
class GetGroupUsersInput:
    group_ids: List[str]

