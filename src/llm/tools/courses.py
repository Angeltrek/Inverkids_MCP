from typing import List, Dict, Any


def courses_tools() -> List[Dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": "get_courses",
                "description": "Retrieve the list of available courses.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_courses_by_user_type",
                "description": "Retrieve courses filtered by user type (Student, Teacher, Parent).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_type": {
                            "type": "string",
                            "enum": ["Student", "Teacher", "Parent"],
                        },
                    },
                    "required": ["user_type"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_courses_names",
                "description": "Retrieve course names by level and white label.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "level": {
                            "type": "string",
                            "description": "Academic level (e.g. primaria, secundaria, 1, 2, 3, 4, 5, 6, 7, 8, 9).",
                        },
                        "label": {
                            "type": "string",
                            "description": "White label identifier (e.g. inverkids_school_v3).",
                        },
                    },
                    "required": ["level", "label"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_courses_data",
                "description": "Retrieve full course data by level and white label.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "level": {
                            "type": "string",
                            "description": "Academic level (e.g. primaria, secundaria, 1, 2, 3, 4, 5, 6, 7, 8, 9).",
                        },
                        "label": {
                            "type": "string",
                            "description": "White label identifier (e.g. inverkids_school_v3).",
                        },
                    },
                    "required": ["level", "label"],
                    "additionalProperties": False,
                },
            },
        },
    ]
