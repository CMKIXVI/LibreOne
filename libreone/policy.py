"""Minimal policy contract for capability execution."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Policy:
    allow_external_models: bool = False
    allow_network: bool = True
    allow_host_processes: bool = False

    def permits(self, capability: str) -> bool:
        if capability == "external_model": return self.allow_external_models
        if capability == "host_process": return self.allow_host_processes
        if capability == "network": return self.allow_network
        return True
