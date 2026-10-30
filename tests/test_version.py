from libreone.system.version import SYSTEM_VERSION


def test_system_version_is_semver_like():
    parts = SYSTEM_VERSION.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)
