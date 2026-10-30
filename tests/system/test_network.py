import pytest

from libreone.system.network import Endpoint


def test_endpoint_validation():
    assert Endpoint("localhost", 8080).port == 8080
    with pytest.raises(ValueError):
        Endpoint("localhost", 0)
    with pytest.raises(ValueError):
        Endpoint("localhost", 65536)
