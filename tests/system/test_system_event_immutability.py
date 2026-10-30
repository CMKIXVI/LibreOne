from dataclasses import FrozenInstanceError

import pytest

from libreone.system.events import SystemEvent


def test_event_is_immutable():
    event = SystemEvent("boot")
    with pytest.raises(FrozenInstanceError):
        event.name = "other"
