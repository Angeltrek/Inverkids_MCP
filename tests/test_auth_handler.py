import pytest
from unittest.mock import Mock, patch
from src.app.tool_handlers.auth import login_handler
from src.utils.exceptions import ValidationError, AuthenticationError
from src.auth.session import Session


class TestAuthHandler:
    """Tests for authentication handler"""
    
    @patch('src.app.tool_handlers.auth.AuthClient')
    def test_login_success(self, mock_auth_client_class):
        """Test successful login"""
        # Setup mock
        mock_client = Mock()
        mock_session = Session(
            user={
                "id": "123",
                "name": "Test User",
                "enrollment_id": "STU001",
            },
            token="test_token_123",
        )
        mock_client.login_with_enrollment.return_value = mock_session
        mock_auth_client_class.return_value = mock_client
        
        # Execute
        result = login_handler("STU001", "password123")
        
        # Assertions
        assert result["token"] == "test_token_123"
        assert result["user"]["id"] == "123"
        assert result["user"]["name"] == "Test User"
        
        # Verify mock was called correctly
        mock_client.login_with_enrollment.assert_called_once_with(
            enrollment_id="STU001",
            password="password123"
        )
    
    def test_login_empty_enrollment_id(self):
        """Test login with empty enrollment ID"""
        with pytest.raises(ValidationError) as exc_info:
            login_handler("", "password123")
        
        assert "enrollment_id" in str(exc_info.value).lower()
    
    def test_login_empty_password(self):
        """Test login with empty password"""
        with pytest.raises(ValidationError) as exc_info:
            login_handler("STU001", "")
        
        assert "password" in str(exc_info.value).lower()
    
    def test_login_invalid_enrollment_format(self):
        """Test login with invalid enrollment format"""
        with pytest.raises(ValidationError):
            login_handler("invalid", "password123")
    
    def test_login_password_too_short(self):
        """Test login with password too short"""
        with pytest.raises(ValidationError):
            login_handler("STU001", "12345")
    
    def test_login_normalizes_enrollment_id(self):
        """Test that enrollment ID is normalized"""
        with patch('src.app.tool_handlers.auth.AuthClient') as mock_client_class:
            mock_client = Mock()
            mock_session = Session(
                user={"id": "123"},
                token="token"
            )
            mock_client.login_with_enrollment.return_value = mock_session
            mock_client_class.return_value = mock_client
            
            # Login with lowercase
            login_handler("stu001", "password123")
            
            # Should be called with uppercase
            mock_client.login_with_enrollment.assert_called_once()
            call_args = mock_client.login_with_enrollment.call_args
            assert call_args.kwargs["enrollment_id"] == "STU001"
    
    @patch('src.app.tool_handlers.auth.AuthClient')
    def test_login_backend_failure(self, mock_auth_client_class):
        """Test login when backend fails"""
        mock_client = Mock()
        mock_client.login_with_enrollment.side_effect = AuthenticationError(
            "Invalid credentials"
        )
        mock_auth_client_class.return_value = mock_client
        
        with pytest.raises(AuthenticationError):
            login_handler("STU001", "wrongpassword")