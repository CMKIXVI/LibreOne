from libreone.system.serialization import decode, encode


def test_serialization_is_deterministic():
    value = {"b": 2, "a": 1}
    assert encode(value) == encode(value)
    assert decode(encode(value)) == value
