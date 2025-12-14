from typing import Dict, Any, List, Optional
from src.db.connection import execute_query


def search_modules(
    level: str,
    search: Optional[str] = None,
    limit: int = 10,
) -> List[Dict[str, Any]]:
    sql = """
        SELECT
            module_id,
            module_number,
            name,
            white_label,
            cover,
            card,
            color
        FROM modules_catalog
        WHERE level = %(level)s
          AND (
              %(search)s IS NULL
              OR name -> 'en' ILIKE %(pattern)s
              OR name -> 'es' ILIKE %(pattern)s
              OR white_label ILIKE %(pattern)s
          )
        ORDER BY module_number ASC
        LIMIT %(limit)s;
    """

    params = {
        "level": level,
        "search": search,
        "pattern": f"%{search}%" if search else None,
        "limit": limit,
    }

    rows = execute_query(sql, params)

    return [
        {
            "module_id": r["module_id"],
            "order": r["module_number"],
            "name": r["name"],
            "label": r["white_label"],
            "assets": {"cover": r["cover"], "card": r["card"]},
            "color": r["color"],
        }
        for r in rows
    ]

def get_topics_by_module(module_id: str) -> List[Dict[str, Any]]:
    sql = """
        SELECT
            topic_id,
            topic_number,
            jsonname,
            name,
            quiz,
            eval,
            diag
        FROM topics_catalog
        WHERE module_id = %(module_id)s
        ORDER BY topic_number ASC;
    """

    rows = execute_query(sql, {"module_id": module_id})

    return [
        {
            "topic_id": r["topic_id"],
            "order": r["topic_number"],
            "key": r["jsonname"],
            "name": r["name"],
            "flags": {
                "quiz": r["quiz"],
                "eval": r["eval"],
                "diag": r["diag"],
            },
        }
        for r in rows
    ]
