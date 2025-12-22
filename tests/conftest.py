import pytest
from unittest.mock import Mock, MagicMock, patch
from src.backend.client import BackendClient
from src.auth.session import Session


@pytest.fixture
def mock_backend_client():
    """Mock backend client for testing"""
    client = Mock(spec=BackendClient)
    client.base_url = "https://api.test.com"
    client.token = "test_token"
    return client


@pytest.fixture
def sample_token():
    """Sample JWT token for testing"""
    return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.test_payload.signature"


@pytest.fixture
def sample_user():
    """Sample user data"""
    return {
        "id": "user_123",
        "name": "Juan Pérez",
        "email": "juan@example.com",
        "enrollment_id": "STU001",
        "role": "student",
        "level": "3",
    }


@pytest.fixture
def sample_session(sample_user, sample_token):
    """Sample authentication session"""
    return Session(user=sample_user, token=sample_token)


@pytest.fixture
def sample_courses():
    """Sample courses data"""
    return [
        {
            "id": "course_1",
            "name": "Matemáticas Básicas",
            "level": "1",
            "description": "Curso introductorio de matemáticas",
        },
        {
            "id": "course_2",
            "name": "Ciencias Naturales",
            "level": "1",
            "description": "Exploración del mundo natural",
        },
    ]


@pytest.fixture
def sample_groups():
    """Sample groups data"""
    return [
        {
            "id": "group_1",
            "name": "Grupo A",
            "level": "3",
            "student_count": 25,
        },
        {
            "id": "group_2",
            "name": "Grupo B",
            "level": "3",
            "student_count": 22,
        },
    ]