from functools import wraps
from typing import Callable
import logging

logger = logging.getLogger(__name__)


def with_logging(log_result: bool = False):
    """
    Adds structured logging around function execution.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__

            logger.info(
                "Function call",
                extra={
                    "function": func_name,
                    "args_count": len(args),
                    "kwargs_keys": list(kwargs.keys()),
                },
            )

            result = func(*args, **kwargs)

            if log_result:
                logger.info(
                    "Function completed",
                    extra={
                        "function": func_name,
                        "result": result,
                    },
                )
            else:
                logger.info(
                    "Function completed",
                    extra={"function": func_name},
                )

            return result

        return wrapper
    return decorator
