from libreone.system.events import SystemEvent


def test_event_metadata_is_isolated():
    first = SystemEvent("boot")
    second = SystemEvent("boot")
    assert first.metadata is not second.metadata
