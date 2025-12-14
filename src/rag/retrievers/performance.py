from typing import List
from src.db.queries.performance import get_student_grade_summary
from src.rag.types import ContextDocument


def retrieve_performance_summary(
    scope: str,
    scope_id: str,
) -> List[ContextDocument]:

    summary = get_student_grade_summary(scope=scope, scope_id=scope_id)

    if not summary["average"]:
        return []

    return [
        {
            "type": "performance",
            "id": scope_id,
            "title": f"{scope.title()} Performance",
            "content": f"Average grade: {summary['average']}",
        }
    ]
