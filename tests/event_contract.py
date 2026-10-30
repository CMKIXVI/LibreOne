from libreone.system.events import SystemEvent


def verify_event_contract() -> bool:
    event = SystemEvent("system.started")
    return event.name == "system.started" and event.id is not None
