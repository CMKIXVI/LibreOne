from .boot import BootConfig
from .config import SystemConfig
from .state import SystemPhase, SystemState


class Bootstrap:
    def __init__(self, system: SystemState | None = None) -> None:
        self.state = system or SystemState()

    def initialize(self, config: SystemConfig | None = None, boot: BootConfig | None = None) -> None:
        del config, boot
        self.state.transition(SystemPhase.BOOTING)
        self.state.transition(SystemPhase.INITIALIZING)
        self.state.transition(SystemPhase.RUNNING)
