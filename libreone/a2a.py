from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class AgentEndpoint:
    name: str
    endpoint: str
    protocol: str = "a2a"
