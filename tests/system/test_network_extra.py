import pytest

from libreone.system.network import Endpoint


def test_endpoint_rejects_empty_host():
    with pytest.raises(ValueError):
        Endpoint("", 443)
