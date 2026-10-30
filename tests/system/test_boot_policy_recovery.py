import pytest

from libreone.system.boot import BootMode
from libreone.system.boot_policy import BootPolicy


def test_recovery_can_be_disabled():
    with pytest.raises(PermissionError):
        BootPolicy(allow_recovery=False).authorize(BootMode.RECOVERY)
