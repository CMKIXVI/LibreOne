import pytest

from libreone.system.serialization import decode


def test_invalid_json_is_rejected():
    with pytest.raises(Exception):
        decode("not-json")
