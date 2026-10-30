from enum import StrEnum

class Lifecycle(StrEnum):
    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    RETIRED = "retired"

def transition(current: Lifecycle, target: Lifecycle) -> Lifecycle:
    allowed = {
        Lifecycle.DRAFT: {Lifecycle.ACTIVE, Lifecycle.RETIRED},
        Lifecycle.ACTIVE: {Lifecycle.PAUSED, Lifecycle.RETIRED},
        Lifecycle.PAUSED: {Lifecycle.ACTIVE, Lifecycle.RETIRED},
        Lifecycle.RETIRED: set(),
    }
    if target not in allowed[current]:
        raise ValueError(f"invalid lifecycle transition: {current} -> {target}")
    return target
