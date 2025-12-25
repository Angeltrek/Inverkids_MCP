import logging
from collections.abc import Callable
from functools import wraps

from src.utils.exceptions import InverKidsError, ValidationError

logger = logging.getLogger(__name__)


def with_error_handling(func: Callable) -> Callable:
    """
    Centralized error handling and normalization.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__

        try:
            return func(*args, **kwargs)

        except ValidationError:
            logger.warning(
                "Validation error",
                extra={"function": func_name},
            )
            raise

        except InverKidsError as e:
            logger.error(
                "InverKids error",
                extra={
                    "function": func_name,
                    "error_type": e.__class__.__name__,
                    "status_code": e.status_code,
                },
                exc_info=True,
            )
            raise

        except Exception as e:
            logger.error(
                "Unhandled exception",
                extra={"function": func_name},
                exc_info=True,
            )
            raise InverKidsError(
                f"Internal error in {func_name}: {str(e)}"
            )

    return wrapper
