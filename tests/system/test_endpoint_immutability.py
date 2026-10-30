from dataclasses import FrozenInstanceError

import pytest

from libreone.system.network import Endpoint


def test_endpoint_is_immutable():
    endpoint = Endpoint("localhost", 80)
    with pytest.raises(FrozenInstanceError):
        endpoint.port = 81
