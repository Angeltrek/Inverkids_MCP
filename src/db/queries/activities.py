from typing import Dict, Any, List, Optional

from src.db.connection import execute_query


def get_activity_by_id(activity_id: str) -> Optional[Dict[str, Any]]:
    sql = """
        SELECT
            activity_id,
            activity_number,
            name,
            topic_id,
            module_id,
            activity_content,
            requirements,
            next,
            activity_type,
            home,
            entry,
            first,
            extra,
            skills
        FROM activities_catalog
        WHERE activity_id = %(activity_id)s;
    """

    rows = execute_query(sql, {"activity_id": activity_id})

    if not rows:
        return None

    r = rows[0]

    return {
        "activity_id": r["activity_id"],
        "order": r["activity_number"],
        "name": r["name"],
        "topic_id": r["topic_id"],
        "module_id": r["module_id"],
        "content": r["activity_content"],
        "requirements": r["requirements"],
        "next": r["next"],
        "type": r["activity_type"],
        "skills": r["skills"],
        "flags": {
            "home": r["home"],
            "entry": r["entry"],
            "first": r["first"],
            "extra": r["extra"],
        },
    }


def get_activities_by_topic(
    topic_id: str,
    activity_type: str | None = None,
    limit: int = 5,
) -> List[Dict[str, Any]]:
    sql = """
        SELECT
            activity_id,
            activity_number,
            name,
            activity_type,
            home,
            entry,
            first,
            extra
        FROM activities_catalog
        WHERE topic_id = %(topic_id)s
          AND (%(activity_type)s IS NULL OR activity_type = %(activity_type)s)
        ORDER BY activity_number ASC
        LIMIT %(limit)s;
    """

    rows = execute_query(
        sql,
        {
            "topic_id": topic_id,
            "activity_type": activity_type,
            "limit": limit,
        },
    )

    return [
        {
            "activity_id": r["activity_id"],
            "order": r["activity_number"],
            "name": r["name"],
            "type": r["activity_type"],
            "flags": {
                "home": r["home"],
                "entry": r["entry"],
                "first": r["first"],
                "extra": r["extra"],
            },
        }
        for r in rows
    ]
