from src.app.dto.performance import (
    StudentGradeSummaryInput,
    StudentsByPerformanceInput,
)
from src.db.queries.performance import (
    get_student_grade_summary,
    get_students_by_performance,
)


def get_student_grade_summary_handler(args):
    dto = StudentGradeSummaryInput(
        scope=args["scope"],
        scope_id=args["scope_id"],
        metric=args.get("metric", "average"),
    )

    result = get_student_grade_summary(
        scope=dto.scope,
        scope_id=dto.scope_id,
    )

    if dto.metric == "average":
        value = result["average"]
    elif dto.metric == "latest":
        value = result["latest"]
    else:
        value = None

    return {
        "scope": dto.scope,
        "scope_id": dto.scope_id,
        "metric": dto.metric,
        "value": value,
    }


def get_students_by_performance_handler(args):
    dto = StudentsByPerformanceInput(
        scope=args["scope"],
        scope_id=args.get("scope_id"),
        order=args["order"],
        limit=args.get("limit", 5),
    )

    students = get_students_by_performance(
        order=dto.order,
        limit=dto.limit,
    )

    return {
        "scope": dto.scope,
        "students": students,
    }
