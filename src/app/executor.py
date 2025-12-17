import json
from typing import List, Dict, Any

from src.backend.client import BackendClient
from src.app.router import route_tool_call
from src.llm.client import get_llm_client
from src.llm.tools.registry import get_llm_tools
from src.llm.context_builder import build_context
from src.app.tool_handlers.registry import get_tool_handler_registry
from src.config.constants.llm_constants import (
    DEFAULT_MAX_AGENT_STEPS,
    AGENT_FAILURE_MESSAGE,
    LLM_ROLE_ASSISTANT,
    LLM_ROLE_TOOL,
    LLM_KEY_TOOL_CALLS,
    LLM_KEY_CONTENT,
    LLM_KEY_TOOL_CALL_ID,
    LLM_TOOL_KEY_ID,
    LLM_TOOL_KEY_NAME,
    LLM_TOOL_KEY_ARGUMENTS,
    LLM_TOOL_KEY_FUNCTION,
    LLM_TOOL_TYPE_FUNCTION,
)


def execute_agent(prompt: str, backend_client: BackendClient) -> str:
    """
    Executes an agentic reasoning loop.

    Responsibilities:
    - Maintain conversation state
    - Dispatch tool calls
    - Return final LLM response
    """

    llm = get_llm_client()
    tools = get_llm_tools()
    tool_registry = get_tool_handler_registry()

    messages: List[Dict[str, Any]] = build_context(prompt)

    for step in range(DEFAULT_MAX_AGENT_STEPS):
        response = llm.generate(
            messages=messages,
            tools=tools,
        )

        tool_calls = response.get(LLM_KEY_TOOL_CALLS)
        if tool_calls:
            _handle_tool_calls(
                step=step,
                tool_calls=tool_calls,
                messages=messages,
                registry=tool_registry,
                backend_client=backend_client,
            )
            continue

        if LLM_KEY_CONTENT in response:
            return response[LLM_KEY_CONTENT]

        raise RuntimeError(f"Unexpected LLM response shape: {response}")

    return AGENT_FAILURE_MESSAGE

def _handle_tool_calls(
    *,
    step: int,
    tool_calls: List[Dict[str, Any]],
    messages: List[Dict[str, Any]],
    registry: Any,
    backend_client: BackendClient,
) -> None:
    """
    Executes tool calls and appends their results to the conversation.
    """

    for tool_call in tool_calls:
        print(f"[STEP {step + 1}] TOOL CALL:", tool_call)

        tool_result = route_tool_call(
            tool_call, 
            registry,
            backend_client
        )

        messages.append({
            "role": LLM_ROLE_ASSISTANT,
            LLM_KEY_TOOL_CALLS: [
                {
                    LLM_TOOL_KEY_ID: tool_call[LLM_TOOL_KEY_ID],
                    "type": LLM_TOOL_TYPE_FUNCTION,
                    LLM_TOOL_KEY_FUNCTION: {
                        LLM_TOOL_KEY_NAME: tool_call[LLM_TOOL_KEY_NAME],
                        LLM_TOOL_KEY_ARGUMENTS: tool_call[LLM_TOOL_KEY_ARGUMENTS],
                    },
                }
            ],
        })

        messages.append({
            "role": LLM_ROLE_TOOL,
            LLM_KEY_TOOL_CALL_ID: tool_call[LLM_TOOL_KEY_ID],
            "content": json.dumps(tool_result, default=str),
        })
