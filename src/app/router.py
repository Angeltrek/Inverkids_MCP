import json
from dataclasses import dataclass
from typing import Any, Dict, Mapping, Callable

from src.backend.client import BackendClient
from src.utils.errors import ToolRoutingError


ToolArguments = Dict[str, Any]
ToolPayload = Mapping[str, Any]
ToolHandler = Callable[[ToolArguments], Dict[str, Any]]
ToolRegistry = Mapping[str, ToolHandler]


@dataclass(frozen=True)
class ToolCall:
    name: str
    arguments: ToolArguments


def _decode_arguments(raw: Any) -> ToolArguments:
    if isinstance(raw, dict):
        return raw

    if isinstance(raw, str):
        try:
            decoded = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ToolRoutingError(
                "Tool call arguments must be valid JSON"
            ) from exc

        if not isinstance(decoded, dict):
            raise ToolRoutingError(
                "Decoded tool call arguments must be a dictionary"
            )

        return decoded

    raise ToolRoutingError(
        "Tool call arguments must be a dictionary or JSON string"
    )


def parse_tool_call(payload: ToolPayload) -> ToolCall:
    if not isinstance(payload, Mapping):
        raise ToolRoutingError("Tool call payload must be a mapping")

    name = payload.get("name")
    raw_arguments = payload.get("arguments")

    if not isinstance(name, str) or not name.strip():
        raise ToolRoutingError("Tool call must include a valid 'name'")

    arguments = _decode_arguments(raw_arguments)

    return ToolCall(
        name=name.strip(),
        arguments=arguments,
    )


def route_tool_call(
    raw_tool_call: ToolPayload,
    registry: ToolRegistry,
    backend_client: BackendClient,
) -> Dict[str, Any]:
    tool_call = parse_tool_call(raw_tool_call)

    handler = registry.get(tool_call.name)
    if handler is None:
        raise ToolRoutingError(
            f"Unsupported tool: '{tool_call.name}'"
        )

    return handler(
        tool_call.arguments,
        backend_client=backend_client,
    )
