import math

import pytest

from libreone.system.serialization import decode, encode


def test_serialization_is_deterministic():
    value = {"b": 2, "a": 1}
    assert encode(value) == '{"a":1,"b":2}'
    assert decode(encode(value)) == value


def test_serialization_rejects_non_finite_numbers():
    for value in (math.inf, -math.inf, math.nan):
        with pytest.raises(ValueError):
            encode(value)


def test_decode_accepts_utf8_bytes():
    assert decode(b'{"value":"ok"}') == {"value": "ok"}


def test_decode_rejects_invalid_input_type():
    with pytest.raises(TypeError, match="serialized value must be str or bytes"):
        decode(123)
