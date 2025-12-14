from typing import Dict, Any

from src.db.queries.curriculum import (
    search_modules,
    get_topics_by_module,
)
from src.db.queries.texts import get_texts_by_topic
from src.db.queries.activities import (
    get_activity_by_id,
    get_activities_by_topic,
)
from src.db.queries.performance import (
    get_student_grade_summary,
    get_students_by_performance,
)

def get_modules_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    level = args["level"]
    search = args.get("search")

    modules = search_modules(level=level, search=search)

    return {"modules": modules}

def get_topics_by_module_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    module_id = args["module_id"]

    topics = get_topics_by_module(module_id)

    return {"topics": topics}

def get_texts_by_topic_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    topic_id = args["topic_id"]
    limit = args.get("limit", 5)

    texts = get_texts_by_topic(topic_id=topic_id, limit=limit)

    return {"texts": texts}

def get_activity_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    activity_id = args["activity_id"]

    activity = get_activity_by_id(activity_id)

    return {"activity": activity}

def get_activities_by_topic_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    topic_id = args["topic_id"]
    activity_type = args.get("activity_type")
    limit = args.get("limit", 5)

    activities = get_activities_by_topic(
        topic_id=topic_id,
        activity_type=activity_type,
        limit=limit,
    )

    return {"activities": activities}

def get_student_grade_summary_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    scope = args["scope"]
    scope_id = args["scope_id"]

    summary = get_student_grade_summary(
        scope=scope,
        scope_id=scope_id,
    )

    return {"summary": summary}

def get_students_by_performance_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    order = args["order"]
    limit = args.get("limit", 5)

    students = get_students_by_performance(
        order=order,
        limit=limit,
    )

    return {"students": students}

def request_guardian_contact_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "status": "queued",
        "reason": args["reason"],
        "channel": args["channel"],
    }
