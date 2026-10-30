"""In-process memory boundary; durable backends remain replaceable."""
class Memory:
    def __init__(self) -> None: self._data: dict[str, object] = {}
    def put(self, key: str, value: object) -> None: self._data[key] = value
    def get(self, key: str, default: object = None) -> object: return self._data.get(key, default)
    def delete(self, key: str) -> None: self._data.pop(key, None)
