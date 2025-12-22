from src.backend.client import BackendClient
from src.config.constants.endpoint_constants import PROFILE_GET


def get_profile_handler(
    *,
    backend_client: BackendClient,
):
    """
    Retrieve the authenticated user's profile from the backend.
    """
    return backend_client.get(PROFILE_GET)
