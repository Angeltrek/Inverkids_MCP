from src.app.services.auth_service import AuthService


def login(enrollment_id: str, password: str):
    return AuthService.login(enrollment_id, password)
