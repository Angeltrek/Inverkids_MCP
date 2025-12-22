import requests
from typing import Any, Dict, Optional
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging

from src.utils.exceptions import (
    AuthenticationError,
    AuthorizationError,
    ResourceNotFoundError,
    BackendError,
    NetworkError,
    RateLimitError,
)

logger = logging.getLogger(__name__)


class BackendClient:
    """
    Robust HTTP client for InverKids backend API.
    
    Features:
    - Automatic retry with exponential backoff
    - Comprehensive error handling
    - Request/response logging
    - Timeout management
    - Session reuse for connection pooling
    """
    
    def __init__(
        self,
        *,
        base_url: str,
        token: str,
        timeout: int = 30,
        max_retries: int = 3,
    ):
        """
        Initialize backend client.
        
        Args:
            base_url: Backend API base URL
            token: Authentication token
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts
        """
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout
        
        # Configure session with retry strategy
        self.session = requests.Session()
        
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=1,  # 1, 2, 4 seconds
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
            raise_on_status=False,
        )
        
        adapter = HTTPAdapter(
            max_retries=retry_strategy,
            pool_connections=10,
            pool_maxsize=10,
        )
        
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        
        logger.info(
            "BackendClient initialized",
            extra={
                "base_url": self.base_url,
                "timeout": self.timeout,
                "max_retries": max_retries,
            }
        )

    def _headers(self) -> Dict[str, str]:
        """Generate request headers with authentication"""
        return {
            "Authorization": self.token,
            "Content-Type": "application/json",
            "User-Agent": "InverKids-MCP/1.0",
        }
    
    def _handle_error(self, response: requests.Response, url: str) -> None:
        """
        Handle HTTP errors with specific exceptions.
        
        Args:
            response: Failed HTTP response
            url: Request URL for logging
            
        Raises:
            Appropriate InverKidsError subclass
        """
        status = response.status_code
        
        # Try to extract error message from response
        try:
            error_data = response.json()
            message = error_data.get("message") or error_data.get("error", response.text)
        except (ValueError, AttributeError):
            message = response.text or f"HTTP {status} error"
        
        logger.error(
            f"HTTP {status} error",
            extra={
                "url": url,
                "status": status,
                "message": message,
                "response_headers": dict(response.headers),
            }
        )
        
        # Map status codes to exceptions
        if status == 401:
            raise AuthenticationError(
                "Authentication failed. Token may be invalid or expired."
            )
        elif status == 403:
            raise AuthorizationError(
                "Access denied. Insufficient permissions for this resource."
            )
        elif status == 404:
            raise ResourceNotFoundError(
                resource="endpoint",
                identifier=url
            )
        elif status == 429:
            retry_after = response.headers.get("Retry-After")
            if retry_after and retry_after.isdigit():
                raise RateLimitError(retry_after=int(retry_after))
            raise RateLimitError()
        elif status >= 500:
            raise BackendError(
                f"Backend service error ({status}): {message}",
                status_code=status
            )
        else:
            raise BackendError(
                f"Request failed with status {status}: {message}",
                status_code=status
            )
    
    def _safe_json(self, response: requests.Response) -> Any:
        """
        Safely extract JSON from response.
        
        Args:
            response: HTTP response
            
        Returns:
            Parsed JSON data or None
        """
        if response.status_code == 204:
            return None

        content_type = response.headers.get("Content-Type", "")
        
        if "application/json" not in content_type:
            logger.warning(
                "Non-JSON response received",
                extra={
                    "content_type": content_type,
                    "url": response.url,
                }
            )
            return None

        try:
            return response.json()
        except ValueError as e:
            logger.error(
                "Failed to parse JSON response",
                extra={
                    "error": str(e),
                    "url": response.url,
                    "content": response.text[:200],
                }
            )
            return None

    def get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Any:
        """
        Perform GET request.
        
        Args:
            path: API endpoint path (e.g., "/api/courses")
            params: Query parameters
            timeout: Override default timeout
            
        Returns:
            JSON response data
            
        Raises:
            ValidationError: If inputs are invalid
            AuthenticationError: If authentication fails (401)
            AuthorizationError: If access is denied (403)
            ResourceNotFoundError: If resource not found (404)
            RateLimitError: If rate limit exceeded (429)
            BackendError: If backend error occurs (5xx)
            NetworkError: If network error occurs
        """
        url = f"{self.base_url}{path}"
        timeout = timeout or self.timeout
        
        try:
            logger.debug(
                "GET request",
                extra={"url": url, "params": params}
            )
            
            response = self.session.get(
                url,
                headers=self._headers(),
                params=params,
                timeout=timeout,
            )
            
            if not response.ok:
                self._handle_error(response, url)
            
            data = self._safe_json(response)
            
            logger.debug(
                "GET request succeeded",
                extra={"url": url, "status": response.status_code}
            )
            
            return data
            
        except requests.exceptions.Timeout as e:
            logger.error(f"Request timeout: {e}", extra={"url": url})
            raise NetworkError(f"Request timed out after {timeout}s: {url}")
        
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection error: {e}", extra={"url": url})
            raise NetworkError(f"Failed to connect to backend: {str(e)}")
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error: {e}", extra={"url": url})
            raise NetworkError(f"Network error: {str(e)}")
    
    def post(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Any:
        """
        Perform POST request.
        
        Args:
            path: API endpoint path
            params: Query parameters
            json: JSON body
            timeout: Override default timeout
            
        Returns:
            JSON response data
            
        Raises:
            Same as get() method
        """
        url = f"{self.base_url}{path}"
        timeout = timeout or self.timeout
        
        try:
            logger.debug(
                "POST request",
                extra={"url": url, "params": params, "has_body": json is not None}
            )
            
            response = self.session.post(
                url,
                headers=self._headers(),
                params=params,
                json=json,
                timeout=timeout,
            )
            
            if not response.ok:
                self._handle_error(response, url)
            
            data = self._safe_json(response)
            
            logger.debug(
                "POST request succeeded",
                extra={"url": url, "status": response.status_code}
            )
            
            return data
            
        except requests.exceptions.Timeout as e:
            logger.error(f"Request timeout: {e}", extra={"url": url})
            raise NetworkError(f"Request timed out after {timeout}s: {url}")
        
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection error: {e}", extra={"url": url})
            raise NetworkError(f"Failed to connect to backend: {str(e)}")
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error: {e}", extra={"url": url})
            raise NetworkError(f"Network error: {str(e)}")
    
    def close(self) -> None:
        """Close the session and cleanup resources"""
        self.session.close()
        logger.info("BackendClient session closed")
    
    def __enter__(self):
        """Context manager support"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager cleanup"""
        self.close()