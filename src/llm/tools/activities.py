from typing import List, Dict, Any


def activity_tools() -> List[Dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": "get_activity",
                "description": "Retrieve a learning activity by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "activity_id": {"type": "string"},
                    },
                    "required": ["activity_id"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_activities_by_topic",
                "description": "Retrieve activities associated with a topic.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "topic_id": {"type": "string"},
                        "activity_type": {"type": "string"},
                        "limit": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 20,
                            "default": 5,
                        },
                    },
                    "required": ["topic_id"],
                    "additionalProperties": False,
                },
            },
        },
    ]
