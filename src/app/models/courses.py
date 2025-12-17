from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class GetCoursesInput:
    pass


@dataclass(frozen=True)
class GetCoursesByUserTypeInput:
    user_type: str


@dataclass(frozen=True)
class GetCoursesNamesInput:
    level: str
    label: str


@dataclass(frozen=True)
class GetCoursesDataInput:
    level: str
    label: str


@dataclass(frozen=True)
class GetTopicsNamesByCourseInput:
    level: str
    label: str
    module_number: int
