import pytest
from unittest.mock import Mock, patch
from src.mcp.decorators import (
    with_backend_client,
    with_error_handling,
)
from src.utils.exceptions import ValidationError, InverKidsError


class TestDecorators:
    """Tests for decorators"""
    
    def test_with_backend_client_decorator(self):
        """Test with_backend_client decorator"""
        @with_backend_client
        def my_function(backend_client=None):
            return backend_client.base_url
        
        with patch('src.mcp.decorators.get_backend_client') as mock_get_client:
            mock_client = Mock()
            mock_client.base_url = "https://api.test.com"
            mock_get_client.return_value = mock_client
            
            result = my_function(token="test_token")
            
            assert result == "https://api.test.com"
            mock_get_client.assert_called_once_with("test_token")
    
    def test_with_backend_client_missing_token(self):
        """Test decorator with missing token"""
        @with_backend_client
        def my_function(backend_client=None):
            return "success"
        
        with pytest.raises(ValidationError):
            my_function()  # No token provided
    
    def test_with_error_handling_decorator(self):
        """Test with_error_handling decorator"""
        @with_error_handling
        def my_function():
            return "success"
        
        result = my_function()
        assert result == "success"
    
    def test_with_error_handling_catches_errors(self):
        """Test error handling decorator catches errors"""
        @with_error_handling
        def failing_function():
            raise ValueError("Something went wrong")
        
        with pytest.raises(InverKidsError):
            failing_function()