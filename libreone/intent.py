"""Intent contract for AI-native request normalization."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Intent:
    name: str
    parameters: dict[str, object]
