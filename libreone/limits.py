from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Limits:
    max_input_bytes: int = 10_000_000
    max_output_bytes: int = 10_000_000
    max_steps: int = 100

    def __post_init__(self) -> None:
        if min(self.max_input_bytes, self.max_output_bytes, self.max_steps) <= 0:
            raise ValueError("limits must be positive")
