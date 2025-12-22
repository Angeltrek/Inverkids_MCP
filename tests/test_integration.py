import pytest
from unittest.mock import patch, Mock
from src.app.tool_handlers.auth import login_handler
from src.app.tool_handlers.courses import get_courses_handler
from src.backend.context import get_backend_client


class TestIntegration:
    """Integration tests for complete workflows"""
    
    @patch('src.app.tool_handlers.auth.AuthClient')
    @patch('src.backend.client.requests.Session')
    def test_login_and_get_courses_flow(self, mock_session_class, mock_auth_client_class):
        """Test complete flow: login -> get courses"""
        # Mock login
        from src.auth.session import Session
        mock_auth = Mock()
        mock_auth.login_with_enrollment.return_value = Session(
            user={"id": "123", "name": "Test"},
            token="test_token"
        )
        mock_auth_client_class.return_value = mock_auth
        
        # Step 1: Login
        login_result = login_handler("STU001", "password123")
        token = login_result["token"]
        
        assert token == "test_token"
        
        # Mock courses request
        mock_session = Mock()
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}
        mock_response.json.return_value = [{"id": "course_1", "name": "Math"}]
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session
        
        # Step 2: Get courses with token
        client = get_backend_client(token)
        courses = get_courses_handler(backend_client=client)
        
        assert len(courses) == 1
        assert courses[0]["name"] == "Math"