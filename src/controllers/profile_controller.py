from src.infrastructure.http.backend_client import BackendClient
from src.infrastructure.config.constants.endpoint_constants import PROFILE_GET


def get_profile(backend_client: BackendClient):
    return backend_client.get(PROFILE_GET)
