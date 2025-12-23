from dataclasses import dataclass
from src.models.settings.backend import BackendConfig
from src.models.settings.mcp import MCPConfig


@dataclass(frozen=True)
class Settings:
    """Application settings"""
    backend: BackendConfig
    mcp: MCPConfig
