from src.auth.client import AuthClient
from src.app.validators import Validator
from src.config.settings import settings
import logging

logger = logging.getLogger(__name__)


def login_handler(enrollment_id: str, password: str) -> dict:
    """
    Authenticate user with enrollment ID and password.
    
    This handler validates inputs, authenticates the user against the
    backend, and returns user data with an authentication token.
    
    Args:
        enrollment_id: Student/teacher enrollment ID (format: ABC123)
        password: User password (minimum 6 characters)
        
    Returns:
        Dictionary containing:
        - user: User profile data
        - token: Authentication token for subsequent requests
        
    Raises:
        ValidationError: If inputs are invalid
        AuthenticationError: If authentication fails
        NetworkError: If connection to backend fails
        
    Example:
        >>> result = login_handler("STU001", "mypassword")
        >>> token = result["token"]
        >>> user_name = result["user"]["name"]
    """
    # Validate inputs
    enrollment_id = Validator.validate_enrollment_id(enrollment_id)
    Validator.validate_password(password)
    
    logger.info(
        "Login attempt",
        extra={"enrollment_id": enrollment_id}
    )
    
    try:
        # Create auth client
        auth = AuthClient(
            base_url=settings.backend.base_url,
            timeout=settings.backend.auth_timeout,
        )
        
        # Authenticate
        session = auth.login_with_enrollment(
            enrollment_id=enrollment_id,
            password=password,
        )
        
        logger.info(
            "Login successful",
            extra={
                "enrollment_id": enrollment_id,
                "user_id": session.user.get("id"),
            }
        )
        
        return {
            "user": session.user,
            "token": session.token,
        }
        
    except Exception as e:
        logger.error(
            "Login failed",
            extra={
                "enrollment_id": enrollment_id,
                "error": str(e),
            },
            exc_info=True
        )
        raise