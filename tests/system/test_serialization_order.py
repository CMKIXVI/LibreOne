from libreone.system.serialization import encode


def test_serialization_is_key_ordered():
    assert encode({"b": 2, "a": 1}) == '{"a":1,"b":2}'
