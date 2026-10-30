import pytest
from libreone.system.network import Endpoint


def test_endpoint_rejects_invalid_port():
    with pytest.raises(ValueError):
        Endpoint("localhost", 70000)
