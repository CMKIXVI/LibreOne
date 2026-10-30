from libreone.system.events import SystemEvent


def test_events_have_unique_ids_and_timestamps():
    first = SystemEvent("boot")
    second = SystemEvent("boot")
    assert first.id != second.id
    assert first.timestamp is not None
