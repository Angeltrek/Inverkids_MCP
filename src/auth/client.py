import requests
from typing import Any, Dict

from .session import Session
from src.utils.errors import AuthenticationError
from src.config.constants.endpoint_constants import LOGIN


class AuthClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def login_with_enrollment(
        self,
        *,
        enrollment_id: str,
        password: str,
    ) -> Session:
        response = requests.post(
            f"{self.base_url}{LOGIN}",
            json={
                "enrollment_id": enrollment_id,
                "password": password,
            },
            timeout=self.timeout,
        )

        if not response.ok:
            raise AuthenticationError(response.text)

        data: Dict[str, Any] = response.json()

        token = self._extract_token(data)
        return Session(user=data, token=token)

    def _extract_token(self, payload: Dict[str, Any]) -> str:
        """
        Adjust this once you confirm the serializer fields.
        Common names: auth_token, token, session_token
        """
        token = payload.get("auth_token") or payload.get("token")
        if not token:
            raise AuthenticationError("No auth token returned by backend")

        return token.strip()
