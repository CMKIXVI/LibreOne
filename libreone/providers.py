from typing import Protocol, Any

class ModelProvider(Protocol):
    async def generate(self, *, messages: list[dict[str, Any]], model: str, **kwargs: Any) -> Any: ...
