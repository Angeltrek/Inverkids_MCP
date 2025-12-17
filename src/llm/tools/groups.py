from typing import List, Dict, Any


def groups_tools() -> List[Dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": "get_groups",
                "description": "Retrieve groups accessible to the current user.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_groups_by_level",
                "description": "Retrieve groups filtered by academic level.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "level": {"type": "string"},
                    },
                    "required": ["level"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_group_users",
                "description": "Retrieve students belonging to one or more groups.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "group_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["group_ids"],
                },
            },
        },
    ]
