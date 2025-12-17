from src.backend.client import BackendClient
from src.config.constants.endpoint_constants import (
    TOPICS_LIST,
    TOPIC_CONTENT,
    TOPIC_ACTIVITY_CONTENT,
    TOPIC_TEXT_CONTENT,
    TOPIC_BOOK_CONTENT,
    TOPIC_VIDEO_CONTENT,
    TOPIC_GAME_CONTENT,
)
from src.app.models.topics import (
    GetTextContentInput,
    GetBookContentInput,
    GetVideoContentInput,
    GetGameContentInput,
)


def get_topics_handler(args, *, backend_client: BackendClient):
    return backend_client.get(TOPICS_LIST)


def get_topic_content_handler(args, *, backend_client: BackendClient):
    return backend_client.get(
        TOPIC_CONTENT,
        params={"topic_id": args["topic_id"]},
    )


def get_activity_content_handler(args, *, backend_client: BackendClient):
    return backend_client.get(
        TOPIC_ACTIVITY_CONTENT,
        params={"activity_id": args["activity_id"]},
    )

def _build_numbered_params(dto):
    params = {
        "module_number": dto.module_number,
        "topic_number": dto.topic_number,
    }
    if dto.white_label:
        params["white_label"] = dto.white_label
    if dto.level:
        params["level"] = dto.level
    return params


def get_text_content_handler(args, *, backend_client: BackendClient):
    dto = GetTextContentInput(**args)
    params = _build_numbered_params(dto)
    params["text_number"] = dto.text_number

    return backend_client.get(TOPIC_TEXT_CONTENT, params=params)


def get_book_content_handler(args, *, backend_client: BackendClient):
    dto = GetBookContentInput(**args)
    params = _build_numbered_params(dto)
    params["book_number"] = dto.book_number

    return backend_client.get(TOPIC_BOOK_CONTENT, params=params)


def get_video_content_handler(args, *, backend_client: BackendClient):
    dto = GetVideoContentInput(**args)
    params = _build_numbered_params(dto)
    params["video_number"] = dto.video_number

    return backend_client.get(TOPIC_VIDEO_CONTENT, params=params)


def get_game_content_handler(args, *, backend_client: BackendClient):
    dto = GetGameContentInput(**args)
    params = _build_numbered_params(dto)
    params["game_number"] = dto.game_number

    return backend_client.get(TOPIC_GAME_CONTENT, params=params)
