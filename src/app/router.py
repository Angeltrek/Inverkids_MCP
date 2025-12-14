import json
from dataclasses import dataclass
from typing import Any, Dict

from src.utils.errors import ToolRoutingError
from src.app.tool_handlers.registry import get_tool_handler_registry


@dataclass(frozen=True)
class ToolCall:
    name: str
    arguments: Dict[str, Any]

def parse_tool_call(raw: Dict[str, Any]) -> ToolCall:
    if not isinstance(raw, dict):
        raise ToolRoutingError("Tool call must be a dictionary")

    name = raw.get("name")
    arguments = raw.get("arguments")

    if not isinstance(name, str) or not name.strip():
        raise ToolRoutingError("Tool call missing valid 'name'")

    if isinstance(arguments, str):
        try:
            arguments = json.loads(arguments)
        except json.JSONDecodeError as exc:
            raise ToolRoutingError(
                "Tool call 'arguments' is not valid JSON"
            ) from exc

    if not isinstance(arguments, dict):
        raise ToolRoutingError("Tool call 'arguments' must be a dictionary")

    return ToolCall(name=name, arguments=arguments)


def route_tool_call(raw_tool_call: Dict[str, Any]) -> Dict[str, Any]:
    tool_call = parse_tool_call(raw_tool_call)

    registry = get_tool_handler_registry()
    handler = registry.get(tool_call.name)

    if handler is None:
        raise ToolRoutingError(f"Tool '{tool_call.name}' is not supported")

    return handler(tool_call.arguments)
