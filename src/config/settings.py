from dataclasses import dataclass
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass
class BackendConfig:
    """Backend API configuration"""
    base_url: str
    timeout: int = 30
    max_retries: int = 3
    auth_timeout: int = 10


@dataclass
class MCPConfig:
    """MCP Server configuration"""
    name: str = "inverkids-mcp"
    log_level: str = "INFO"


@dataclass
class Settings:
    """Application settings loaded from environment"""
    backend: BackendConfig
    mcp: MCPConfig
    
    @classmethod
    def from_env(cls) -> "Settings":
        """Load settings from environment variables with validation"""
        base_url = os.getenv("BACKEND_BASE_URL")
        if not base_url:
            raise RuntimeError(
                "BACKEND_BASE_URL environment variable is required. "
                "Please set it in your .env file."
            )
        
        return cls(
            backend=BackendConfig(
                base_url=base_url,
                timeout=int(os.getenv("HTTP_TIMEOUT", "30")),
                max_retries=int(os.getenv("MAX_RETRIES", "3")),
                auth_timeout=int(os.getenv("AUTH_TIMEOUT", "10")),
            ),
            mcp=MCPConfig(
                name=os.getenv("MCP_NAME", "inverkids-mcp"),
                log_level=os.getenv("LOG_LEVEL", "INFO"),
            ),
        )


settings = Settings.from_env()