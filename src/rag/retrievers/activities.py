from typing import List, Optional
from src.db.queries.activities import get_activities_by_topic
from src.rag.types import ContextDocument


def retrieve_activities(
    topic_id: Optional[str],
    limit: int,
) -> List[ContextDocument]:

    if not topic_id:
        return []

    rows = get_activities_by_topic(topic_id=topic_id, limit=limit)

    return [
        {
            "type": "activity",
            "id": r["activity_id"],
            "title": r["name"],
            "content": f"Activity type: {r['type']}",
        }
        for r in rows
    ]
