from typing import List, Dict, Any


def text_tools() -> List[Dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": "get_texts_by_topic",
                "description": "Retrieve instructional texts for a topic.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "topic_id": {"type": "string"},
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
        {
            "type": "function",
            "function": {
                "name": "search_texts",
                "description": "Search instructional texts by title or content.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "minLength": 2,
                        },
                        "topic_id": {
                            "type": "string",
                            "description": "Optional topic scope",
                        },
                        "limit": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 20,
                            "default": 5,
                        },
                    },
                    "required": ["query"],
                    "additionalProperties": False,
                },
            },
        },
    ]
