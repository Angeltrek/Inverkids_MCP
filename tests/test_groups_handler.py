import pytest
from src.app.tool_handlers.groups import (
    normalize_level,
    get_groups_by_level_handler,
    get_group_users_handler,
)


class TestGroupsHandler:
    """Tests for groups handlers"""
    
    def test_normalize_level_integer(self):
        """Test normalizing integer levels"""
        assert normalize_level(3) == "3"
        assert normalize_level(10) == "10"
    
    def test_normalize_level_string_numeric(self):
        """Test normalizing numeric string levels"""
        assert normalize_level("5") == "5"
        assert normalize_level("  8  ") == "8"
    
    def test_normalize_level_string_with_text(self):
        """Test normalizing levels with descriptive text"""
        assert normalize_level("Level 3") == "3"
        assert normalize_level("3ro grado") == "3"
        assert normalize_level("nivel-7") == "7"
    
    def test_normalize_level_no_digits(self):
        """Test normalizing level with no digits"""
        # Should return the string as-is if no digits found
        result = normalize_level("invalid")
        assert result == "invalid"
    
    def test_get_groups_by_level_handler(self, mock_backend_client, sample_groups):
        """Test getting groups by level"""
        mock_backend_client.post.return_value = sample_groups
        
        result = get_groups_by_level_handler(
            level=3,
            backend_client=mock_backend_client
        )
        
        assert result == sample_groups
        mock_backend_client.post.assert_called_once()
        call_kwargs = mock_backend_client.post.call_args.kwargs
        assert call_kwargs["json"]["level"] == "3"
    
    def test_get_group_users_handler(self, mock_backend_client):
        """Test getting group users"""
        mock_users = [
            {"id": "user_1", "name": "Student 1"},
            {"id": "user_2", "name": "Student 2"},
        ]
        mock_backend_client.post.return_value = mock_users
        
        result = get_group_users_handler(
            group_ids=["group_1", "group_2"],
            backend_client=mock_backend_client
        )
        
        assert result == mock_users
        mock_backend_client.post.assert_called_once()