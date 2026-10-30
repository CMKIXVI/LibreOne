"""Deterministic capability execution boundary."""
from .capabilities import CapabilityRegistry
from .context import Context
from .models import Result, Request
from .policy import Policy

class Executor:
    def __init__(self, registry: CapabilityRegistry, policy: Policy | None = None) -> None:
        self.registry = registry
        self.policy = policy or Policy()
    def execute(self, request: Request, context: Context | None = None) -> Result:
        name = request.action
        if not self.policy.permits(name): raise PermissionError(name)
        capability = self.registry.resolve(name)
        value = capability.handler(request.input, context or Context())
        return Result(request_id=request.id, value=value)
