from functools import wraps
from typing import Callable
import logging

from src.backend.context import get_backend_client
from src.app.validators import Validator
from src.utils.exceptions import ValidationError, InverKidsError

logger = logging.getLogger(__name__)


def with_backend_client(func: Callable) -> Callable:
    """
    Decorator that validates token and injects backend client.
    
    This decorator:
    1. Extracts and validates the token parameter
    2. Creates a BackendClient instance
    3. Injects the client as 'backend_client' parameter
    4. Removes 'token' from kwargs (already used)
    
    Usage:
        @with_backend_client
        def my_handler(backend_client=None, **kwargs):
            return backend_client.get("/api/endpoint")
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Extract token
        token = kwargs.get("token")
        if not token:
            raise ValidationError("Token is required", field="token")
        
        # Validate token
        token = Validator.validate_token(token)
        
        # Create client
        try:
            client = get_backend_client(token)
        except Exception as e:
            logger.error(f"Failed to create backend client: {e}")
            raise
        
        # Inject client and remove token
        kwargs["backend_client"] = client
        kwargs.pop("token", None)
        
        return func(*args, **kwargs)
    
    return wrapper


def with_error_handling(func: Callable) -> Callable:
    """
    Decorator that provides comprehensive error handling and logging.
    
    This decorator:
    1. Logs function entry with parameters
    2. Catches and logs all exceptions
    3. Converts unexpected errors to InverKidsError
    4. Logs function exit
    
    Usage:
        @with_error_handling
        def my_function(param1, param2):
            return do_something()
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        
        logger.debug(
            f"Entering {func_name}",
            extra={"args": args, "kwargs": kwargs}
        )
        
        try:
            result = func(*args, **kwargs)
            
            logger.debug(f"Exiting {func_name} successfully")
            
            return result
            
        except ValidationError as e:
            logger.warning(
                f"Validation error in {func_name}",
                extra={"error": str(e), "field": e.details.get("field")}
            )
            raise
            
        except InverKidsError as e:
            logger.error(
                f"InverKids error in {func_name}",
                extra={
                    "error_type": e.__class__.__name__,
                    "message": e.message,
                    "status_code": e.status_code,
                },
                exc_info=True
            )
            raise
            
        except Exception as e:
            logger.error(
                f"Unexpected error in {func_name}",
                extra={"error": str(e)},
                exc_info=True
            )
            raise InverKidsError(f"Internal error in {func_name}: {str(e)}")
    
    return wrapper


def with_logging(log_result: bool = False):
    """
    Decorator factory for detailed function logging.
    
    Args:
        log_result: Whether to log the return value
        
    Usage:
        @with_logging(log_result=True)
        def my_function(param):
            return {"data": param}
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            
            logger.info(
                f"Calling {func_name}",
                extra={
                    "function": func_name,
                    "args_count": len(args),
                    "kwargs_keys": list(kwargs.keys()),
                }
            )
            
            result = func(*args, **kwargs)
            
            if log_result:
                logger.info(
                    f"{func_name} completed",
                    extra={"result": result}
                )
            else:
                logger.info(f"{func_name} completed")
            
            return result
        
        return wrapper
    return decorator