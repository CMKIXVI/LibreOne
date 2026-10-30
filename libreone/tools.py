from typing import Protocol, Any

class Tool(Protocol):
    name: str
    description: str
    async def invoke(self, arguments: dict[str, Any]) -> Any: ...
