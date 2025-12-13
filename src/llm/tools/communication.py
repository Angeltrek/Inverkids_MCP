from typing import List, Dict, Any


def communication_tools() -> List[Dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": "request_guardian_contact",
                "description": "Request guardian or teacher contact action.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reason": {"type": "string"},
                        "channel": {
                            "type": "string",
                            "enum": ["email", "whatsapp", "internal"],
                        },
                    },
                    "required": ["reason", "channel"],
                    "additionalProperties": False,
                },
            },
        }
    ]
