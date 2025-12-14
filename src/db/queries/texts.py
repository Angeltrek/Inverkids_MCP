from typing import Dict, Any, List

from src.db.connection import execute_query


def get_texts_by_topic(
    topic_id: str,
    limit: int = 5,
) -> List[Dict[str, Any]]:
    sql = """
        SELECT
            text_id,
            text_number,
            name,
            text_content,
            requirements,
            skills,
            first,
            entry,
            home
        FROM texts_catalog
        WHERE topic_id = %(topic_id)s
        ORDER BY text_number ASC
        LIMIT %(limit)s;
    """

    rows = execute_query(
        sql,
        {
            "topic_id": topic_id,
            "limit": limit,
        },
    )

    return [
        {
            "text_id": r["text_id"],
            "order": r["text_number"],
            "name": r["name"],
            "content": r["text_content"],
            "requirements": r["requirements"],
            "skills": r["skills"],
            "flags": {
                "first": r["first"],
                "entry": r["entry"],
                "home": r["home"],
            },
        }
        for r in rows
    ]

def search_texts(
    query: str,
    topic_id: str | None = None,
    limit: int = 5,
) -> List[Dict[str, Any]]:
    sql = """
        SELECT
            text_id,
            text_number,
            name,
            text_content,
            requirements,
            skills,
            first,
            entry,
            home
        FROM texts_catalog
        WHERE
            (
                name -> 'en' ILIKE %(pattern)s
                OR name -> 'es' ILIKE %(pattern)s
                OR text_content::text ILIKE %(pattern)s
            )
            AND (%(topic_id)s IS NULL OR topic_id = %(topic_id)s)
        ORDER BY text_number ASC
        LIMIT %(limit)s;
    """

    rows = execute_query(
        sql,
        {
            "pattern": f"%{query}%",
            "topic_id": topic_id,
            "limit": limit,
        },
    )

    return [
        {
            "text_id": r["text_id"],
            "order": r["text_number"],
            "name": r["name"],
            "content": r["text_content"],
            "requirements": r["requirements"],
            "skills": r["skills"],
            "flags": {
                "first": r["first"],
                "entry": r["entry"],
                "home": r["home"],
            },
        }
        for r in rows
    ]
