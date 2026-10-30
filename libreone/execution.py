from dataclasses import dataclass
from typing import Any
from .capabilities import Capability
from .context import Context
from .policy import Policy

@dataclass(frozen=True, slots=True)
class ExecutionResult:
    value: Any
    capability: str

class Executor:
    def __init__(self, policy: Policy) -> None:
        self.policy = policy

    def run(self, capability: Capability, context: Context, **kwargs: Any) -> ExecutionResult:
        self.policy.authorize(capability.risk, capability.scopes)
        return ExecutionResult(capability.handler(context=context, **kwargs), capability.name)
