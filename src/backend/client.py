import requests
from typing import Any, Dict, Optional

from src.config.constants.http_constants import (
    CONTENT_TYPE_HEADER,
    CONTENT_TYPE_JSON,
    HTTP_STATUS_NO_CONTENT,
)

class BackendClient:
    def __init__(self, *, base_url: str, token: str, timeout: int = 30):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": self.token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
    
    def _safe_json(self, response: requests.Response) -> Any:
        if response.status_code == HTTP_STATUS_NO_CONTENT:
            return None

        content_type = response.headers.get("Content-Type", "")

        if "application/json" not in content_type:
            return None

        try:
            return response.json()
        except ValueError:
            return None


    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        response = requests.get(
            f"{self.base_url}{path}",
            headers=self._headers(),
            params=params,
            timeout=self.timeout,
        )
        response.raise_for_status()
        return self._safe_json(response)
    
    def post(self, path: str, params: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None) -> Any:
        response = requests.post(
            f"{self.base_url}{path}",
            headers=self._headers(),
            params=params,
            json=json,
            timeout=self.timeout,
        )
        response.raise_for_status()
        return self._safe_json(response)
