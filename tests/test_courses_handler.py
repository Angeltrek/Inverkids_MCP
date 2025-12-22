import pytest
from unittest.mock import Mock
from src.app.tool_handlers.courses import (
    get_courses_handler,
    get_courses_by_user_type_handler,
)


class TestCoursesHandler:
    """Tests for courses handlers"""
    
    def test_get_courses_handler(self, mock_backend_client, sample_courses):
        """Test getting all courses"""
        mock_backend_client.get.return_value = sample_courses
        
        result = get_courses_handler(backend_client=mock_backend_client)
        
        assert result == sample_courses
        mock_backend_client.get.assert_called_once_with("/api/courses")
    
    def test_get_courses_by_user_type_handler(self, mock_backend_client, sample_courses):
        """Test getting courses by user type"""
        mock_backend_client.get.return_value = sample_courses
        
        result = get_courses_by_user_type_handler(
            user_type="student",
            backend_client=mock_backend_client
        )
        
        assert result == sample_courses
        mock_backend_client.get.assert_called_once()
        call_kwargs = mock_backend_client.get.call_args.kwargs
        assert call_kwargs["params"]["user_type"] == "student"