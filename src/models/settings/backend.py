from dataclasses import dataclass


@dataclass(frozen=True)
class BackendConfig:
    base_url: str
    timeout: int = 30
    max_retries: int = 3
    auth_timeout: int = 10
