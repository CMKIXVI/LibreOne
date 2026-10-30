from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True, slots=True)
class Message:
    role: str
    content: str
    metadata: dict[str, Any]

    def __post_init__(self) -> None:
        if self.role not in {"system", "user", "assistant", "tool"}:
            raise ValueError("unsupported message role")
