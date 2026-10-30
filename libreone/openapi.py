from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class APIEndpoint:
    name: str
    method: str
    url: str

    def __post_init__(self) -> None:
        if self.method.upper() not in {"GET", "POST", "PUT", "PATCH", "DELETE"}:
            raise ValueError("unsupported HTTP method")
