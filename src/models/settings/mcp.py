from dataclasses import dataclass


@dataclass(frozen=True)
class MCPConfig:
    name: str = "inverkids-mcp"
    log_level: str = "INFO"
