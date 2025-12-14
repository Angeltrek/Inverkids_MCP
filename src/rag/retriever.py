from typing import List, Optional

from src.rag.types import ContextDocument

from src.rag.retrievers.texts import retrieve_texts
from src.rag.retrievers.activities import retrieve_activities
from src.rag.retrievers.curriculum import retrieve_modules
from src.rag.retrievers.users import retrieve_users


def retrieve_context(
    *,
    query: str,
    topic_id: Optional[str] = None,
    level: Optional[str] = None,
    limit: int = 5,
) -> List[ContextDocument]:
    """
    Retrieve passive contextual information to help the LLM
    understand the user's question.

    This function MUST NOT:
    - execute business logic
    - compute grades
    - access sensitive or scoped data
    """

    context: List[ContextDocument] = []

    context.extend(
        retrieve_texts(
            query=query,
            topic_id=topic_id,
            limit=limit,
        )
    )

    if topic_id:
        context.extend(
            retrieve_activities(
                topic_id=topic_id,
                limit=3,
            )
        )

    if level:
        context.extend(
            retrieve_modules(
                query=query,
                level=level,
                limit=3,
            )
        )

    context.extend(
        retrieve_users(
            query=query,
            limit=3,
        )
    )

    return context
