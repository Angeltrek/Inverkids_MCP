from dataclasses import dataclass
from typing import Any, Callable, Dict, Mapping

from src.utils.errors import ToolRoutingError

# Optional: if you add src/llm/tool_names.py use these imports.
# Otherwise, replace tool names with plain strings.
from src.llm.tool_names import (
    GET_MODULES,
    GET_TOPICS_BY_MODULE,
    GET_TEXTS_BY_TOPIC,
    GET_ACTIVITY,
    GET_ACTIVITIES_BY_TOPIC,
    GET_STUDENT_GRADE_SUMMARY,
    GET_STUDENTS_BY_PERFORMANCE,
    SEARCH_USERS_BY_NAME,
    REQUEST_GUARDIAN_CONTACT,
)

ToolHandler = Callable[[Dict[str, Any]], Dict[str, Any]]


@dataclass(frozen=True)
class ToolCall:
    name: str
    arguments: Dict[str, Any]


def _parse_tool_call(raw: Dict[str, Any]) -> ToolCall:
    """
    Parse and validate minimal tool-call structure.
    This is structural validation only (no business rules).
    """
    if not isinstance(raw, dict):
        raise ToolRoutingError("Tool call must be a dictionary")

    name = raw.get("name")
    arguments = raw.get("arguments")

    if not isinstance(name, str) or not name.strip():
        raise ToolRoutingError("Tool call missing valid 'name'")

    if not isinstance(arguments, dict):
        raise ToolRoutingError("Tool call 'arguments' must be a dictionary")

    return ToolCall(name=name, arguments=arguments)


def _get_registry() -> Mapping[str, ToolHandler]:
    """
    Explicit allow-list mapping. Keep it small, readable, and closed.
    Handlers are imported lazily to avoid heavy imports at cold start.
    """
    # NOTE: These handlers don't exist yet. In Feature 5, they will wrap db/queries + rag.
    # For now, you can implement them as simple functions in the relevant future modules.
    from src.app.tool_handlers import (  # noqa: WPS433 (local import by design)
        get_modules_handler,
        get_topics_by_module_handler,
        get_texts_by_topic_handler,
        get_activity_handler,
        get_activities_by_topic_handler,
        get_student_grade_summary_handler,
        get_students_by_performance_handler,
        search_users_by_name_handler,
        request_guardian_contact_handler,
    )

    return {
        GET_MODULES: get_modules_handler,
        GET_TOPICS_BY_MODULE: get_topics_by_module_handler,
        GET_TEXTS_BY_TOPIC: get_texts_by_topic_handler,
        GET_ACTIVITY: get_activity_handler,
        GET_ACTIVITIES_BY_TOPIC: get_activities_by_topic_handler,
        GET_STUDENT_GRADE_SUMMARY: get_student_grade_summary_handler,
        GET_STUDENTS_BY_PERFORMANCE: get_students_by_performance_handler,
        SEARCH_USERS_BY_NAME: search_users_by_name_handler,
        REQUEST_GUARDIAN_CONTACT: request_guardian_contact_handler,
    }


def route_tool_call(raw_tool_call: Dict[str, Any]) -> Dict[str, Any]:
    """
    Route tool calls from the LLM to backend functions safely and explicitly.
    """
    tool_call = _parse_tool_call(raw_tool_call)

    registry = _get_registry()
    handler = registry.get(tool_call.name)

    if handler is None:
        raise ToolRoutingError(f"Tool '{tool_call.name}' is not supported")

    return handler(tool_call.arguments)
