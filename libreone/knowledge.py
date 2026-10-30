"""Knowledge provider protocol."""
from typing import Protocol, Iterable

class KnowledgeProvider(Protocol):
    def search(self, query: str, limit: int = 10) -> Iterable[object]: ...
