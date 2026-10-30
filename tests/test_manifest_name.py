import pytest
from libreone.system.manifest import SystemManifest


def test_manifest_rejects_other_product_name():
    with pytest.raises(ValueError):
        SystemManifest(name="Other")
