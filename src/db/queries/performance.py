from typing import Dict, Any, List
from src.db.connection import execute_query


def get_student_grade_summary(
    scope: str,
    scope_id: str,
) -> Dict[str, Any]:
    if scope not in {"module", "topic"}:
        raise ValueError("Invalid scope")

    sql = """
        SELECT
            AVG(grade) AS average,
            MAX(datetime) AS latest
        FROM grades
        WHERE
            (%(scope)s = 'module' AND module_id = %(scope_id)s)
            OR
            (%(scope)s = 'topic' AND topic_id = %(scope_id)s);
    """

    rows = execute_query(sql, {"scope": scope, "scope_id": scope_id})

    return {
        "scope": scope,
        "scope_id": scope_id,
        "average": rows[0]["average"] if rows else None,
        "latest": rows[0]["latest"] if rows else None,
    }


def get_students_by_performance(
    order: str,
    limit: int = 5,
) -> List[Dict[str, Any]]:
    direction = "ASC" if order == "lowest" else "DESC"

    sql = f"""
        SELECT
            u.id AS student_id,
            u.name AS student_name,
            s.name AS school_name,
            AVG(g.grade) AS average_grade
        FROM grades g
        JOIN users u ON u.id = g.student_id
        JOIN schools s ON s.id = u.school_id
        GROUP BY u.id, u.name, s.name
        ORDER BY average_grade {direction}
        LIMIT %(limit)s;
    """

    rows = execute_query(sql, {"limit": limit})

    return [
        {
            "student_id": r["student_id"],
            "student_name": r["student_name"],
            "school_name": r["school_name"],
            "average_grade": r["average_grade"],
        }
        for r in rows
    ]
