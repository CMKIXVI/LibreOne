from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True, slots=True)
class KnowledgeItem:
    key: str
    content: Any
    source: str
    confidence: float = 1.0

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
