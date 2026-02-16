from dataclasses import dataclass


@dataclass(frozen=True)
class MCPConfig:
    name: str
    log_level: str
    host: str = "0.0.0.0"
    port: int = 8000
