from typing import List, Dict, Any


def curriculum_tools() -> List[Dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": "get_modules",
                "description": "Retrieve curriculum modules for a given educational level.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "level": {"type": "string"},
                    },
                    "required": ["level"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_topics_by_module",
                "description": "Retrieve topics belonging to a module.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "module_id": {"type": "string"},
                    },
                    "required": ["module_id"],
                    "additionalProperties": False,
                },
            },
        },
    ]
