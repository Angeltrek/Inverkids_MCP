from src.infrastructure.config.constants.endpoint_constants import (
    MCP_COMPONENT_ALTERNATIVES_ENSURE_INVENTORY,
)
from src.infrastructure.http.backend_client import BackendClient


def ensure_component_alternative_inventory(
    *,
    backend_client: BackendClient,
    activity_id: str,
    lang: str,
    variant_index: int,
    frame_position: int | None = None,
    component_position: int | None = None,
    target_alternatives: int = 10,
    scope_type: str | None = None,
    scope_key: str | None = None,
    trigger_source: str = "mcp",
):
    payload = {
        "activity_id": activity_id,
        "lang": lang,
        "variant_index": variant_index,
        "target_alternatives": target_alternatives,
        "trigger_source": trigger_source,
    }

    if frame_position is not None:
        payload["frame_position"] = frame_position

    if component_position is not None:
        payload["component_position"] = component_position

    if scope_type is not None:
        payload["scope_type"] = scope_type

    if scope_key is not None:
        payload["scope_key"] = scope_key

    return backend_client.post(
        MCP_COMPONENT_ALTERNATIVES_ENSURE_INVENTORY,
        json=payload,
    )
