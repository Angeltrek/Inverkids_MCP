"""
Lambda entrypoint for the Agentic RAG service.

Phase 1 responsibility:
- Validate that the service is alive
- Establish the handler contract
- Provide a stable foundation for future features

This file intentionally contains no business logic.
"""

from typing import Any, Dict

from src.config.service_constants import (
    SERVICE_NAME,
    SERVICE_PHASE,
    STATUS_ALIVE,
)

from src.config.http_constants import (
    CONTENT_TYPE_HEADER,
    CONTENT_TYPE_JSON,
    HTTP_STATUS_OK,
)


def _build_response(
    body: Dict[str, Any],
    status_code: int = HTTP_STATUS_OK,
) -> Dict[str, Any]:
    """
    Standard HTTP-style response builder.
    """

    return {
        "statusCode": status_code,
        "headers": {
            CONTENT_TYPE_HEADER: CONTENT_TYPE_JSON,
        },
        "body": body,
    }


def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    AWS Lambda handler.
    """

    response_body = {
        "service": SERVICE_NAME,
        "status": STATUS_ALIVE,
        "phase": SERVICE_PHASE,
    }

    return _build_response(response_body)
