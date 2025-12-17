from src.backend.client import BackendClient
from src.config.constants.endpoint_constants import (
    COURSES_LIST,
    COURSES_DATA,
    COURSES_NAMES,
)
from src.app.models.courses import (
    GetCoursesInput,
    GetCoursesByUserTypeInput,
    GetCoursesNamesInput,
    GetCoursesDataInput,
)


def get_courses_handler(args, *, backend_client: BackendClient):
    dto = GetCoursesInput()
    return backend_client.get(COURSES_LIST)


def get_courses_by_user_type_handler(args, *, backend_client: BackendClient):
    dto = GetCoursesByUserTypeInput(
        user_type=args["user_type"]
    )
    return backend_client.get(
        COURSES_LIST,
        params={"user_type": dto.user_type},
    )


def get_courses_names_handler(args, *, backend_client: BackendClient):
    dto = GetCoursesNamesInput(
        level=args["level"],
        label=args["label"],
    )
    return backend_client.get(
        COURSES_NAMES,
        params={
            "level": dto.level,
            "label": dto.label,
        },
    )


def get_courses_data_handler(args, *, backend_client: BackendClient):
    dto = GetCoursesDataInput(
        level=args["level"],
        label=args["label"],
    )
    return backend_client.get(
        COURSES_DATA,
        params={
            "level": dto.level,
            "label": dto.label,
        },
    )
