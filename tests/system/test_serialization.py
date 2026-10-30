from libreone.system.serialization import decode, encode


def test_canonical_json_round_trip():
    value = {"z": 1, "a": [True, "LibreOne"]}
    encoded = encode(value)
    assert encoded == '{"a":[true,"LibreOne"],"z":1}'
    assert decode(encoded) == value
