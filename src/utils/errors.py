class ToolRoutingError(Exception):
    """
    Raised when a tool call cannot be routed safely.
    """
    pass

class DatabaseConnectionError(Exception):
    """
    Raised when there is a database connection issue.
    """
    pass

class AuthenticationError(Exception):
    """
    Raised when authentication fails.
    """
    pass