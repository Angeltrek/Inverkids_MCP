from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class GetTopicsInput:
    pass


@dataclass(frozen=True)
class GetTopicContentInput:
    topic_id: str


@dataclass(frozen=True)
class GetActivityContentInput:
    activity_id: str

@dataclass(frozen=True)
class GetTextContentInput:
    module_number: int
    topic_number: int
    text_number: int
    white_label: Optional[str] = None
    level: Optional[str] = None


@dataclass(frozen=True)
class GetBookContentInput:
    module_number: int
    topic_number: int
    book_number: int
    white_label: Optional[str] = None
    level: Optional[str] = None


@dataclass(frozen=True)
class GetVideoContentInput:
    module_number: int
    topic_number: int
    video_number: int
    white_label: Optional[str] = None
    level: Optional[str] = None


@dataclass(frozen=True)
class GetGameContentInput:
    module_number: int
    topic_number: int
    game_number: int
    white_label: Optional[str] = None
    level: Optional[str] = None
