from typing import List
from src.controllers.virtual_modules_controller import (
    create_virtual_module,
    get_virtual_modules,
    get_virtual_module_detail,
)
from src.infrastructure.decorators import (
    with_backend_client,
    with_error_handling,
)
from src.infrastructure.http.backend_client import BackendClient
from typing import List, Dict, Optional


@with_error_handling
@with_backend_client
def create_virtual_module_handler(
    *,
    backend_client: BackendClient,
    pbl_name: Dict[str, str],
    module_number: int,
    level: str,
    name: Dict[str, str],
    description: Dict[str, str],
    topic_ids: List[str],
    white_label: Optional[str] = "inverkids_school_v3",
):
    return create_virtual_module(
        backend_client=backend_client,
        pbl_name=pbl_name,
        module_number=module_number,
        level=level,
        name=name,
        description=description,
        topic_ids=topic_ids,
        white_label=white_label,
    )


@with_error_handling
@with_backend_client
def get_virtual_modules_handler(
    *,
    backend_client: BackendClient,
    limit: int,
    offset: int,
):
    return get_virtual_modules(
        backend_client=backend_client,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_virtual_module_detail_handler(
    *,
    backend_client: BackendClient,
    virtual_module_id: str,
):
    return get_virtual_module_detail(
        backend_client=backend_client,
        virtual_module_id=virtual_module_id,
    )
