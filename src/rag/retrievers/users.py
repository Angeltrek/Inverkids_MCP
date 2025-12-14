from typing import List
from src.db.queries.users import search_users_by_name
from src.rag.types import ContextDocument


def retrieve_users(
    query: str,
    limit: int,
) -> List[ContextDocument]:

    rows = search_users_by_name(query=query, limit=limit)

    return [
        {
            "type": "user",
            "id": r["user_id"],
            "title": r["name"],
            "content": f"User role: {r.get('user_type', 'unknown')}",
        }
        for r in rows
    ]
