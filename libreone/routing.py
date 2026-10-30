from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Route:
    provider: str
    model: str
    reason: str

class Router:
    def choose(self, *, model: str, provider: str | None = None) -> Route:
        return Route(provider or "default", model, "explicit provider" if provider else "default route")
