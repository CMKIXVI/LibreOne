from enum import Enum

from .errors import StateError


class SystemPhase(str, Enum):
    OFF = "off"
    BOOTING = "booting"
    INITIALIZING = "initializing"
    RUNNING = "running"
    STOPPING = "stopping"
    FAILED = "failed"


class SystemState:
    def __init__(self) -> None:
        self.phase = SystemPhase.OFF

    def transition(self, target: SystemPhase) -> None:
        allowed = {
            SystemPhase.OFF: {SystemPhase.BOOTING},
            SystemPhase.BOOTING: {SystemPhase.INITIALIZING, SystemPhase.FAILED},
            SystemPhase.INITIALIZING: {SystemPhase.RUNNING, SystemPhase.FAILED},
            SystemPhase.RUNNING: {SystemPhase.STOPPING, SystemPhase.FAILED},
            SystemPhase.STOPPING: {SystemPhase.OFF, SystemPhase.FAILED},
            SystemPhase.FAILED: {SystemPhase.OFF, SystemPhase.BOOTING},
        }
        if target not in allowed[self.phase]:
            raise StateError(f"invalid transition: {self.phase.value} -> {target.value}")
        self.phase = target
