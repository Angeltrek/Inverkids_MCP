from typing import List, Dict, Any


def catalog_tools() -> List[Dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": "get_full_catalog",
                "description": (
                    "Use this tool ONLY to retrieve the complete catalog hierarchy (modules → topics → activities) for a given academic level and white label."
                    "This tool is for OVERVIEW or EXPLORATION, NOT for fetching specific topic, activity, or content details."
                    "If the user asks for specific topic or activity content, use the appropriate tools instead."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "level": {
                            "type": "string",
                            "description": "Academic level (e.g. primaria, secundaria, 1, 2, 3, 4, 5, 6, 7, 8, 9).",
                        },
                        "white_label": {
                            "type": "string",
                            "description": "White label identifier (e.g. inverkids_school_v3).",
                        },
                        "user_lang": {
                            "type": "string",
                            "description": "User language code (e.g. es, en).",
                        },
                    },
                    "required": ["level", "white_label", "user_lang"],
                    "additionalProperties": False,
                },
            },
        }
    ]
