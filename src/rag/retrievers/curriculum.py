from typing import List, Optional
from src.db.queries.curriculum import search_modules
from src.rag.types import ContextDocument


def retrieve_modules(
    query: str,
    level: Optional[str],
    limit: int,
) -> List[ContextDocument]:

    if not level:
        return []

    rows = search_modules(level=level, search=query, limit=limit)

    return [
        {
            "type": "module",
            "id": r["module_id"],
            "title": r["label"],
            "content": f"Module covering {r['label']}",
        }
        for r in rows
    ]
