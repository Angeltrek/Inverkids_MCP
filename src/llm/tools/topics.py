from typing import List, Dict, Any


def topic_tools() -> List[Dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": "get_topics",
                "description": (
                    "Use this tool ONLY to list topic metadata (IDs, names, ordering) available to the current user."
                    "If the user ask for specific topic data, first fetch the topic ID using this tool."
                ),
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
                "description": (
                    "Use this tool ONLY when the user explicitly asks for the full content of a specific topic and provides or implies a topic ID."
                    "Do NOT use this tool for activities or individual learning assets"
                ),
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
                "description": (
                    "Use this tool ONLY when the user explicitly asks for the content of a specific activity and provides or implies an activity ID."
                    "Do NOT use this tool for topics or generic catalog navigation."
                ),
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
                "description": (
                    "Use this tool ONLY to retrieve a TEXT learning asset identified by module number, topic number, and text number."
                    "Do NOT use this tool for books, videos, games, topics, or activities."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "module_number": {"type": "integer"},
                        "topic_number": {"type": "integer"},
                        "text_number": {"type": "integer"},
                        "white_label": {
                            "type": "string",
                            "description": "White label identifier (e.g. inverkids_school_v3).",
                        },
                        "level": {
                            "type": "string",
                            "description": "Academic level (e.g. primaria, secundaria, 1, 2, 3, 4, 5, 6, 7, 8, 9).",
                        },
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
                "description": (
                    "Use this tool ONLY to retrieve a BOOK learning asset identified by module number, topic number, and book number."
                    "Do NOT use this tool for texts, videos, games, topics, or activities."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "module_number": {"type": "integer"},
                        "topic_number": {"type": "integer"},
                        "book_number": {"type": "integer"},
                        "white_label": {
                            "type": "string",
                            "description": "White label identifier (e.g. inverkids_school_v3).",
                        },
                        "level": {
                            "type": "string",
                            "description": "Academic level (e.g. primaria, secundaria, 1, 2, 3, 4, 5, 6, 7, 8, 9).",
                        },
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
                "description": (
                    "Use this tool ONLY to retrieve a VIDEO learning asset identified by module number, topic number, and video number."
                    "Do NOT use this tool for texts, books, games, topics, or activities."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "module_number": {"type": "integer"},
                        "topic_number": {"type": "integer"},
                        "video_number": {"type": "integer"},
                        "white_label": {
                            "type": "string",
                            "description": "White label identifier (e.g. inverkids_school_v3).",
                        },
                        "level": {
                            "type": "string",
                            "description": "Academic level (e.g. primaria, secundaria, 1, 2, 3, 4, 5, 6, 7, 8, 9).",
                        },
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
                "description": (
                    "Use this tool ONLY to retrieve a GAME learning asset identified by module number, topic number, and game number."
                    "Do NOT use this tool for text, books, videos, topics, or activities."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "module_number": {"type": "integer"},
                        "topic_number": {"type": "integer"},
                        "game_number": {"type": "integer"},
                        "white_label": {
                            "type": "string",
                            "description": "White label identifier (e.g. inverkids_school_v3).",
                        },
                        "level": {
                            "type": "string",
                            "description": "Academic level (e.g. primaria, secundaria, 1, 2, 3, 4, 5, 6, 7, 8, 9).",
                        },
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
