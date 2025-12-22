import pytest
import requests
from unittest.mock import Mock, patch, MagicMock
from src.backend.client import BackendClient
from src.utils.exceptions import (
    AuthenticationError,
    AuthorizationError,
    ResourceNotFoundError,
    BackendError,
    NetworkError,
    RateLimitError,
)


class TestBackendClient:
    """Tests for BackendClient"""
    
    @pytest.fixture
    def client(self):
        """Create a test client"""
        return BackendClient(
            base_url="https://api.test.com",
            token="test_token",
            timeout=10,
            max_retries=3,
        )
    
    # -------------------------------------------------------------------------
    # Initialization Tests
    # -------------------------------------------------------------------------
    
    def test_client_initialization(self):
        """Test client is initialized correctly"""
        client = BackendClient(
            base_url="https://api.test.com/",  # With trailing slash
            token="my_token",
            timeout=30,
        )
        
        assert client.base_url == "https://api.test.com"  # Slash removed
        assert client.token == "my_token"
        assert client.timeout == 30
        assert client.session is not None
    
    # -------------------------------------------------------------------------
    # GET Request Tests
    # -------------------------------------------------------------------------
    
    @patch('requests.Session.get')
    def test_get_success(self, mock_get, client):
        """Test successful GET request"""
        # Mock response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response
        
        # Make request
        result = client.get("/api/test")
        
        # Assertions
        assert result == {"data": "test"}
        mock_get.assert_called_once()
    
    @patch('requests.Session.get')
    def test_get_with_params(self, mock_get, client):
        """Test GET request with query parameters"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response
        
        result = client.get("/api/test", params={"level": "3", "lang": "es"})
        
        # Check that params were passed
        call_kwargs = mock_get.call_args.kwargs
        assert call_kwargs["params"] == {"level": "3", "lang": "es"}
    
    @patch('requests.Session.get')
    def test_get_404_error(self, mock_get, client):
        """Test GET request with 404 error"""
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 404
        mock_response.text = "Not found"
        mock_response.json.side_effect = ValueError
        mock_get.return_value = mock_response
        
        with pytest.raises(ResourceNotFoundError):
            client.get("/api/nonexistent")
    
    @patch('requests.Session.get')
    def test_get_401_error(self, mock_get, client):
        """Test GET request with authentication error"""
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 401
        mock_response.text = "Unauthorized"
        mock_response.json.side_effect = ValueError
        mock_get.return_value = mock_response
        
        with pytest.raises(AuthenticationError):
            client.get("/api/protected")
    
    @patch('requests.Session.get')
    def test_get_403_error(self, mock_get, client):
        """Test GET request with authorization error"""
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 403
        mock_response.text = "Forbidden"
        mock_response.json.side_effect = ValueError
        mock_get.return_value = mock_response
        
        with pytest.raises(AuthorizationError):
            client.get("/api/forbidden")
    
    @patch('requests.Session.get')
    def test_get_429_error(self, mock_get, client):
        """Test GET request with rate limit error"""
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 429
        mock_response.headers = {"Retry-After": "60"}
        mock_response.text = "Rate limit exceeded"
        mock_response.json.side_effect = ValueError
        mock_get.return_value = mock_response
        
        with pytest.raises(RateLimitError) as exc_info:
            client.get("/api/test")
        
        assert exc_info.value.details.get("retry_after") == 60
    
    @patch('requests.Session.get')
    def test_get_500_error(self, mock_get, client):
        """Test GET request with server error"""
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 500
        mock_response.text = "Internal server error"
        mock_response.json.side_effect = ValueError
        mock_get.return_value = mock_response
        
        with pytest.raises(BackendError) as exc_info:
            client.get("/api/test")
        
        assert exc_info.value.status_code == 500
    
    @patch('requests.Session.get')
    def test_get_timeout(self, mock_get, client):
        """Test GET request timeout"""
        mock_get.side_effect = requests.exceptions.Timeout
        
        with pytest.raises(NetworkError) as exc_info:
            client.get("/api/test")
        
        assert "timed out" in str(exc_info.value).lower()
    
    @patch('requests.Session.get')
    def test_get_connection_error(self, mock_get, client):
        """Test GET request connection error"""
        mock_get.side_effect = requests.exceptions.ConnectionError
        
        with pytest.raises(NetworkError) as exc_info:
            client.get("/api/test")
        
        assert "connect" in str(exc_info.value).lower()
    
    # -------------------------------------------------------------------------
    # POST Request Tests
    # -------------------------------------------------------------------------
    
    @patch('requests.Session.post')
    def test_post_success(self, mock_post, client):
        """Test successful POST request"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 201
        mock_response.headers = {"Content-Type": "application/json"}
        mock_response.json.return_value = {"id": "123", "created": True}
        mock_post.return_value = mock_response
        
        result = client.post("/api/create", json={"name": "Test"})
        
        assert result == {"id": "123", "created": True}
        mock_post.assert_called_once()
    
    @patch('requests.Session.post')
    def test_post_with_json_body(self, mock_post, client):
        """Test POST request with JSON body"""
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}
        mock_response.json.return_value = {}
        mock_post.return_value = mock_response
        
        body = {"level": "3", "user_type": "student"}
        client.post("/api/test", json=body)
        
        call_kwargs = mock_post.call_args.kwargs
        assert call_kwargs["json"] == body
    
    # -------------------------------------------------------------------------
    # Context Manager Tests
    # -------------------------------------------------------------------------
    
    def test_context_manager(self):
        """Test client as context manager"""
        with BackendClient(
            base_url="https://api.test.com",
            token="test",
        ) as client:
            assert client.session is not None