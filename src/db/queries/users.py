from typing import List, Dict, Any, Optional
from src.db.connection import execute_query


def search_users_by_name(
    query: str,
    user_type: Optional[str] = None,
    limit: int = 5,
) -> List[Dict[str, Any]]:
    sql = """
        SELECT
            id,
            name,
            nickname,
            user_type,
            school_id
        FROM users
        WHERE
            (
                name ILIKE %(pattern)s
                OR nickname ILIKE %(pattern)s
            )
            AND (%(user_type)s IS NULL OR user_type = %(user_type)s)
        ORDER BY name ASC
        LIMIT %(limit)s;
    """

    rows = execute_query(
        sql,
        {
            "pattern": f"%{query}%",
            "user_type": user_type,
            "limit": limit,
        },
    )

    return [
        {
            "user_id": r["id"],
            "name": r["name"],
            "nickname": r["nickname"],
            "user_type": r["user_type"],
            "school_id": r["school_id"],
        }
        for r in rows
    ]
