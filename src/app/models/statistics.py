from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class GradesInput:
    ids: List[str]


@dataclass(frozen=True)
class RatesInput:
    ids: List[str]


@dataclass(frozen=True)
class StatsInput:
    group_ids: List[str]
    user_lang: str
    user_level: str
    user_label: str


@dataclass(frozen=True)
class StatsUserInput:
    user_id: str
    user_lang: str
    user_level: str
    user_label: str


@dataclass(frozen=True)
class OverviewInput:
    school_ids: List[str]


@dataclass(frozen=True)
class OverviewGroupsInput:
    group_ids: List[str]


@dataclass(frozen=True)
class GroupProgressInput:
    group_ids: List[str]
    white_label: str
    exclude_extra: Optional[bool] = True
