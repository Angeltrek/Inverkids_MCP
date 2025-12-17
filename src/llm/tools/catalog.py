from typing import List, Dict, Any


def catalog_tools() -> List[Dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": "get_full_catalog",
                "description": (
                    "Retrieve the full learning catalog including modules, "
                    "topics, and activities for a given level and white label."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "level": {
                            "type": "string",
                            "description": "Academic level (e.g. primaria, secundaria).",
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
