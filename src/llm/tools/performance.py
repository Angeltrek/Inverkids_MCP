from typing import List, Dict, Any


def performance_tools() -> List[Dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": "get_student_grade_summary",
                "description": "Retrieve summarized academic performance data.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scope": {"type": "string", "enum": ["module", "topic"]},
                        "scope_id": {"type": "string"},
                        "metric": {
                            "type": "string",
                            "enum": ["average", "latest", "trend"],
                            "default": "average",
                        },
                    },
                    "required": ["scope", "scope_id"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_students_by_performance",
                "description": "Rank students by academic performance.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scope": {
                            "type": "string",
                            "enum": ["module", "topic", "global"],
                        },
                        "scope_id": {"type": "string"},
                        "order": {
                            "type": "string",
                            "enum": ["lowest", "highest"],
                        },
                        "limit": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 20,
                            "default": 5,
                        },
                    },
                    "required": ["scope", "order"],
                    "additionalProperties": False,
                },
            },
        },
    ]
