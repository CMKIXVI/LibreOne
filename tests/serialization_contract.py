from libreone.system.serialization import decode, encode


def verify_serialization_contract() -> bool:
    value = {"name": "LibreOne", "version": 1}
    return decode(encode(value)) == value
