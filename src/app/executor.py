import json
from typing import List, Dict, Any

from src.app.router import route_tool_call
from src.llm.client import get_llm_client
from src.llm.tools.registry import get_llm_tools
from src.rag.context_builder import build_context


MAX_STEPS = 5


def execute_agent(prompt: str) -> str:
    llm = get_llm_client()
    tools = get_llm_tools()

    messages: List[Dict[str, Any]] = [
        {
            "role": "system",
            "content": "You are an academic assistant. Use tools when needed."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    for step in range(MAX_STEPS):
        response = llm.generate(messages=messages, tools=tools)

        if response.get("tool_call"):
            tool_call = response["tool_call"]
            print(f"[STEP {step+1}] TOOL CALL:", tool_call)

            tool_result = route_tool_call(tool_call)

            messages.append({
                "role": "assistant",
                "tool_calls": [
                    {
                        "id": tool_call["id"],
                        "type": "function",
                        "function": {
                            "name": tool_call["name"],
                            "arguments": tool_call["arguments"],
                        }
                    }
                ],
            })

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call["id"],
                "content": json.dumps(tool_result, default=str),
            })

            continue

        return response["content"]

    return "I could not complete the request safely."
