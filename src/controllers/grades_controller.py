from src.infrastructure.config.constants.endpoint_constants import (
    MCP_GRADES_BY_LEVEL,
    MCP_GRADES_BY_GROUP,
    MCP_GRADES_BY_STUDENT,
    MCP_GRADES_BY_MODULE,
    MCP_GRADES_BY_TOPIC,
    MCP_GRADES_BY_ACTIVITY,
    MCP_GRADE_DETAIL,
    MCP_GRADES_SUMMARY,
)
from src.infrastructure.http.backend_client import BackendClient


def get_grades_by_level(
    *,
    backend_client: BackendClient,
    level: str,
):
    return backend_client.get(
        MCP_GRADES_BY_LEVEL,
        params={"level": level},
    )


def get_grades_by_group(
    *,
    backend_client: BackendClient,
    group_id: str,
):
    return backend_client.get(
        MCP_GRADES_BY_GROUP,
        params={"group_id": group_id},
    )


def get_grades_by_student(
    *,
    backend_client: BackendClient,
    student_id: str | None = None,
):
    return backend_client.get(
        MCP_GRADES_BY_STUDENT,
        params={"student_id": student_id},
    )


def get_grades_by_module(
    *,
    backend_client: BackendClient,
    module_id: str,
):
    return backend_client.get(
        MCP_GRADES_BY_MODULE,
        params={"module_id": module_id},
    )


def get_grades_by_topic(
    *,
    backend_client: BackendClient,
    topic_id: str,
):
    return backend_client.get(
        MCP_GRADES_BY_TOPIC,
        params={"topic_id": topic_id},
    )


def get_grades_by_activity(
    *,
    backend_client: BackendClient,
    activity_id: str,
):
    return backend_client.get(
        MCP_GRADES_BY_ACTIVITY,
        params={"activity_id": activity_id},
    )


def get_grade_detail(
    *,
    backend_client: BackendClient,
    grade_id: str,
):
    return backend_client.get(
        MCP_GRADE_DETAIL,
        params={"grade_id": grade_id},
    )


def get_grades_summary(
    *,
    backend_client: BackendClient,
    module_id: str,
):
    return backend_client.get(
        MCP_GRADES_SUMMARY,
        params={"module_id": module_id},
    )
