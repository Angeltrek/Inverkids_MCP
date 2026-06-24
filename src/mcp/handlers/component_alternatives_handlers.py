from src.controllers.component_alternatives_controller import (
    ensure_component_alternative_inventory,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def ensure_component_alternative_inventory_handler(
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
    return ensure_component_alternative_inventory(
        backend_client=backend_client,
        activity_id=activity_id,
        lang=lang,
        variant_index=variant_index,
        frame_position=frame_position,
        component_position=component_position,
        target_alternatives=target_alternatives,
        scope_type=scope_type,
        scope_key=scope_key,
        trigger_source=trigger_source,
    )
