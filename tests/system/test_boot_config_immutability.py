from dataclasses import FrozenInstanceError

import pytest

from libreone.system.boot import BootConfig, BootMode


def test_boot_config_is_immutable():
    config = BootConfig(BootMode.NORMAL)
    with pytest.raises(FrozenInstanceError):
        config.mode = BootMode.SAFE
