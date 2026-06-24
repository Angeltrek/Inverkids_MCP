from src.mcp.app import mcp
from src.mcp.handlers.component_alternatives_handlers import (
    ensure_component_alternative_inventory_handler,
)


@mcp.tool(
    name="ensure_component_alternative_inventory",
    description=(
        "Request controlled generation of approved component alternatives when inventory is"
        " exhausted or invalidated. The backend enforces policy scope and budget checks."
        "Parameters:"
        "- activity_id: Internal activity identifier"
        "- lang: Content language"
        "- variant_index: Catalog variant index (default: 0)"
        "- frame_position: Optional frame index"
        "- component_position: Optional component index"
        "- target_alternatives: Desired inventory size (default: 10)"
        "- scope_type: Budget scope type such as label or school (optional)"
        "- scope_key: Budget scope key such as label name or school id (optional)"
    ),
)
def ensure_component_alternative_inventory(
    activity_id: str,
    lang: str,
    variant_index: int = 0,
    frame_position: int | None = None,
    component_position: int | None = None,
    target_alternatives: int = 10,
    scope_type: str | None = None,
    scope_key: str | None = None,
):
    return ensure_component_alternative_inventory_handler(
        activity_id=activity_id,
        lang=lang,
        variant_index=variant_index,
        frame_position=frame_position,
        component_position=component_position,
        target_alternatives=target_alternatives,
        scope_type=scope_type,
        scope_key=scope_key,
    )
