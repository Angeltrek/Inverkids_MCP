from typing import Dict, Callable, Any

from src.config.tool_names import (
    GET_MODULES,
    GET_TOPICS_BY_MODULE,
    GET_TEXTS_BY_TOPIC,
    GET_ACTIVITY,
    GET_ACTIVITIES_BY_TOPIC,
    GET_STUDENT_GRADE_SUMMARY,
    GET_STUDENTS_BY_PERFORMANCE,
    SEARCH_USERS_BY_NAME,
    REQUEST_GUARDIAN_CONTACT,
    SEARCH_TEXTS,
)

from .curriculum import (
    get_modules_handler,
    get_topics_by_module_handler,
)

from .texts import (
    get_texts_by_topic_handler,
    search_texts_handler,
)

from .activities import (
    get_activity_handler,
    get_activities_by_topic_handler,
)

from .performance import (
    get_student_grade_summary_handler,
    get_students_by_performance_handler,
)

from .users import (
    search_users_by_name_handler,
)

from .communication import (
    request_guardian_contact_handler,
)


ToolHandler = Callable[[Dict[str, Any]], Dict[str, Any]]


def get_tool_handler_registry() -> Dict[str, ToolHandler]:
    return {
        GET_MODULES: get_modules_handler,
        GET_TOPICS_BY_MODULE: get_topics_by_module_handler,
        
        GET_TEXTS_BY_TOPIC: get_texts_by_topic_handler,
        SEARCH_TEXTS: search_texts_handler,

        GET_ACTIVITY: get_activity_handler,
        GET_ACTIVITIES_BY_TOPIC: get_activities_by_topic_handler,

        GET_STUDENT_GRADE_SUMMARY: get_student_grade_summary_handler,
        GET_STUDENTS_BY_PERFORMANCE: get_students_by_performance_handler,

        SEARCH_USERS_BY_NAME: search_users_by_name_handler,

        REQUEST_GUARDIAN_CONTACT: request_guardian_contact_handler,
    }
