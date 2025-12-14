from typing import Dict, Any

from src.db.queries.texts import (
    get_texts_by_topic,
    search_texts,
)
from src.app.dto.texts import (
    SearchTextsInput,
    GetTextsByTopicInput,
)


def get_texts_by_topic_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    dto = GetTextsByTopicInput(
        topic_id=args["topic_id"],
        limit=args.get("limit", 5),
    )

    texts = get_texts_by_topic(
        topic_id=dto.topic_id,
        limit=dto.limit,
    )

    return {"texts": texts}


def search_texts_handler(args: Dict[str, Any]) -> Dict[str, Any]:
    dto = SearchTextsInput(
        query=args["query"],
        topic_id=args.get("topic_id"),
        limit=args.get("limit", 5),
    )

    results = search_texts(
        query=dto.query,
        topic_id=dto.topic_id,
        limit=dto.limit,
    )

    return {"texts": results}
