import logging
from collections.abc import Callable
from functools import wraps

from src.app.validators import validate_token
from src.infrastructure.http.backend_provider import get_backend_client
from src.utils.exceptions import ValidationError

logger = logging.getLogger(__name__)


def with_backend_client(func: Callable) -> Callable:
    """
    Injects a BackendClient based on a validated token.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = kwargs.get("token", None)

        if token:
            try:
                token = validate_token(token)
            except ValidationError:
                logger.error("Invalid token provided")
                raise

        try:
            client = get_backend_client(token)
        except Exception:
            logger.error("Failed to create backend client", exc_info=True)
            raise

        kwargs["backend_client"] = client

        return func(*args, **kwargs)

    return wrapper
