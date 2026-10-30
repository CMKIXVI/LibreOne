from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class MCPServer:
    name: str
    endpoint: str
    transport: str = "streamable-http"

    def __post_init__(self) -> None:
        if not self.name.strip() or not self.endpoint.strip():
            raise ValueError("MCP server name and endpoint are required")
