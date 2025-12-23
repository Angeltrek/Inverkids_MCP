from src.infrastructure.decorators import with_error_handling
from src.controllers.auth_controller import login


@with_error_handling
def login_handler(enrollment_id: str, password: str):
    return login(enrollment_id, password)
