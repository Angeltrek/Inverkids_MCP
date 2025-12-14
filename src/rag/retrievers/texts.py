from typing import List, Optional
from src.db.queries.texts import search_texts
from src.rag.types import ContextDocument


def retrieve_texts(
    query: str,
    topic_id: Optional[str],
    limit: int,
) -> List[ContextDocument]:

    rows = search_texts(query=query, topic_id=topic_id, limit=limit)

    return [
        {
            "type": "text",
            "id": r["text_id"],
            "title": r["name"],
            "content": r["content"],
        }
        for r in rows
    ]
