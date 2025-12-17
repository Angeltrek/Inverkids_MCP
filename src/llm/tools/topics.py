from typing import List, Dict, Any


def topic_tools() -> List[Dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": "get_topics",
                "description": "Retrieve the list of available topics for the current user context.",
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
                "name": "get_topic_content",
                "description": "Retrieve full topic content by topic ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "topic_id": {
                            "type": "string",
                            "description": "Unique topic identifier",
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
                "name": "get_activity_content",
                "description": "Retrieve activity content by activity ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "activity_id": {
                            "type": "string",
                            "description": "Unique activity identifier",
                        },
                    },
                    "required": ["activity_id"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_text_content",
                "description": "Retrieve text content using module, topic and text numbers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "module_number": {"type": "integer"},
                        "topic_number": {"type": "integer"},
                        "text_number": {"type": "integer"},
                        "white_label": {"type": "string"},
                        "level": {"type": "string"},
                    },
                    "required": [
                        "module_number",
                        "topic_number",
                        "text_number",
                    ],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_book_content",
                "description": "Retrieve book content using module, topic and book numbers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "module_number": {"type": "integer"},
                        "topic_number": {"type": "integer"},
                        "book_number": {"type": "integer"},
                        "white_label": {"type": "string"},
                        "level": {"type": "string"},
                    },
                    "required": [
                        "module_number",
                        "topic_number",
                        "book_number",
                    ],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_video_content",
                "description": "Retrieve video content using module, topic and video numbers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "module_number": {"type": "integer"},
                        "topic_number": {"type": "integer"},
                        "video_number": {"type": "integer"},
                        "white_label": {"type": "string"},
                        "level": {"type": "string"},
                    },
                    "required": [
                        "module_number",
                        "topic_number",
                        "video_number",
                    ],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_game_content",
                "description": "Retrieve game content using module, topic and game numbers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "module_number": {"type": "integer"},
                        "topic_number": {"type": "integer"},
                        "game_number": {"type": "integer"},
                        "white_label": {"type": "string"},
                        "level": {"type": "string"},
                    },
                    "required": [
                        "module_number",
                        "topic_number",
                        "game_number",
                    ],
                    "additionalProperties": False,
                },
            },
        },
    ]
