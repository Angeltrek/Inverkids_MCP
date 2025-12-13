from typing import Any, Dict


def get_modules_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    return {"tool": "get_modules", "args": args}


def get_topics_by_module_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    return {"tool": "get_topics_by_module", "args": args}


def get_texts_by_topic_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    return {"tool": "get_texts_by_topic", "args": args}


def get_activity_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    return {"tool": "get_activity", "args": args}


def get_activities_by_topic_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    return {"tool": "get_activities_by_topic", "args": args}


def get_student_grade_summary_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    return {"tool": "get_student_grade_summary", "args": args}


def get_students_by_performance_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    return {"tool": "get_students_by_performance", "args": args}


def search_users_by_name_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    return {"tool": "search_users_by_name", "args": args}


def request_guardian_contact_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    return {"tool": "request_guardian_contact", "args": args}
