from libreone.system.events import SystemEvent


def test_events_get_unique_ids():
    first = SystemEvent("boot")
    second = SystemEvent("boot")
    assert first.id != second.id
