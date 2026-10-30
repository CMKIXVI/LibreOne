from pathlib import Path


class Storage:
    def __init__(self, root: str | Path) -> None:
        self.root = Path(root)

    def resolve(self, relative: str) -> Path:
        candidate = (self.root / relative).resolve()
        root = self.root.resolve()
        if candidate != root and root not in candidate.parents:
            raise ValueError("path escapes storage root")
        return candidate
