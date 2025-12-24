from typing import Any


class InverKidsError(Exception):
    """Base exception for all InverKids MCP errors"""
    
    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        details: dict[str, Any] | None = None
    ):
        self.message = message
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)
    
    def to_dict(self) -> dict[str, Any]:
        """Convert exception to dictionary for API responses"""
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "status_code": self.status_code,
            "details": self.details,
        }


class ValidationError(InverKidsError):
    """Raised when input validation fails"""
    def __init__(self, message: str, field: str | None = None):
        super().__init__(message, status_code=400)
        if field:
            self.details["field"] = field


class AuthenticationError(InverKidsError):
    """Raised when authentication fails"""
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message, status_code=401)


class AuthorizationError(InverKidsError):
    """Raised when user lacks permission"""
    def __init__(self, message: str = "Access denied"):
        super().__init__(message, status_code=403)


class ResourceNotFoundError(InverKidsError):
    """Raised when resource is not found"""
    def __init__(self, resource: str, identifier: str | None = None):
        message = f"{resource} not found"
        if identifier:
            message += f": {identifier}"
        super().__init__(message, status_code=404)
        self.details["resource"] = resource
        if identifier:
            self.details["identifier"] = identifier


class BackendError(InverKidsError):
    """Raised when backend service fails"""
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message, status_code=status_code)


class NetworkError(InverKidsError):
    """Raised when network communication fails"""
    def __init__(self, message: str):
        super().__init__(message, status_code=503)


class RateLimitError(InverKidsError):
    """Raised when rate limit is exceeded"""
    def __init__(self, retry_after: int | None = None):
        message = "Rate limit exceeded"
        if retry_after:
            message += f". Retry after {retry_after} seconds"
        super().__init__(message, status_code=429)
        if retry_after:
            self.details["retry_after"] = retry_after