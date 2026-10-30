from libreone.system.boot import BootMode


def test_boot_mode_values_are_unique():
    values = [mode.value for mode in BootMode]
    assert len(values) == len(set(values))
