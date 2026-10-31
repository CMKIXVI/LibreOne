from os import PathLike
from pathlib import Path


class Storage:
    def __init__(self, root: str | PathLike[str]) -> None:
        if not isinstance(root, (str, PathLike)):
            raise TypeError("storage root must be a path")
        self.root = Path(root).resolve()

    def resolve(self, relative: str | PathLike[str]) -> Path:
        if not isinstance(relative, (str, PathLike)):
            raise TypeError("storage path must be a path")
        candidate = (self.root / Path(relative)).resolve()
        if candidate != self.root and self.root not in candidate.parents:
            raise ValueError("path escapes storage root")
        return candidate
