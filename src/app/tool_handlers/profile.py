from src.app.models.profile import GetProfileInput
from src.backend.client import BackendClient
from src.config.constants.endpoint_constants import PROFILE_GET


def get_profile_handler(args, *, backend_client: BackendClient):
    """
    Retrieve the authenticated user's profile from the backend.
    """

    # DTO kept for symmetry / future evolution
    _ = GetProfileInput()

    response = backend_client.get(PROFILE_GET)

    return response
