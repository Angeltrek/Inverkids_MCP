from typing import List, Dict, Any


def statistics_tools() -> List[Dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": "get_grades",
                "description": "Retrieve grades for a list of group IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["ids"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_rates",
                "description": "Retrieve answer rates for a list of group IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["ids"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_stats",
                "description": "Get aggregated statistics for groups.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "group_ids": {"type": "array", "items": {"type": "string"}},
                        "user_lang": {
                            "type": "string",
                            "description": "User language code (e.g. es, en).",
                        },
                        "user_level": {
                            "type": "string",
                            "description": "Academic level (e.g. primaria, secundaria, 1, 2, 3, 4, 5, 6, 7, 8, 9).",
                        },
                        "user_label": {
                            "type": "string",
                            "description": "White label identifier (e.g. inverkids_school_v3).",
                        },
                    },
                    "required": ["group_ids", "user_lang", "user_level", "user_label"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_stats_user",
                "description": "Get statistics for a single user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "user_lang": {
                            "type": "string",
                            "description": "User language code (e.g. es, en).",
                        },
                        "user_level": {
                            "type": "string",
                            "description": "Academic level (e.g. primaria, secundaria, 1, 2, 3, 4, 5, 6, 7, 8, 9).",
                        },
                        "user_label": {
                            "type": "string",
                            "description": "White label identifier (e.g. inverkids_school_v3).",
                        },
                    },
                    "required": ["user_id", "user_lang", "user_level", "user_label"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_group_progress",
                "description": "Retrieve learning progress for groups.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "group_ids": {"type": "array", "items": {"type": "string"}},
                        "white_label": {
                            "type": "string",
                            "description": "White label identifier (e.g. inverkids_school_v3).",
                        },
                        "exclude_extra": {"type": "boolean"},
                    },
                    "required": ["group_ids", "white_label"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_overview",
                "description": "Get overview metrics for schools.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "school_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["school_ids"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_overview_groups",
                "description": "Get overview metrics for groups.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "group_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["group_ids"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_activity_rate",
                "description": "Get activity rate for teacher-associated groups.",
                "parameters": {"type": "object", "properties": {}},
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_inactive_users",
                "description": "Retrieve inactive students for the current subscription period.",
                "parameters": {"type": "object", "properties": {}},
            },
        },
    ]
