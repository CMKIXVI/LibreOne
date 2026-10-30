from .bootstrap import Bootstrap
from .config import SystemConfig


def main() -> None:
    Bootstrap().initialize(SystemConfig.from_environment())


if __name__ == "__main__":
    main()
