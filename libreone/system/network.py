from dataclasses import dataclass
import ipaddress
import re


_HOSTNAME_LABEL = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?$")


@dataclass(frozen=True)
class Endpoint:
    host: str
    port: int

    def __post_init__(self) -> None:
        if not isinstance(self.host, str):
            raise TypeError("endpoint host must be a string")
        host = self.host.strip()
        if not host:
            raise ValueError("endpoint host cannot be empty")
        if len(host) > 253:
            raise ValueError("endpoint host is too long")
        if not isinstance(self.port, int) or isinstance(self.port, bool):
            raise TypeError("endpoint port must be an integer")
        if not 1 <= self.port <= 65535:
            raise ValueError("endpoint port must be between 1 and 65535")
        canonical = self._canonical_host(host)
        object.__setattr__(self, "host", canonical)

    @staticmethod
    def _canonical_host(host: str) -> str:
        try:
            return ipaddress.ip_address(host).compressed
        except ValueError:
            pass
        if host.endswith("."):
            host = host[:-1]
        if not host:
            raise ValueError("endpoint host cannot be empty")
        labels = host.split(".")
        if any(not label or not _HOSTNAME_LABEL.fullmatch(label) for label in labels):
            raise ValueError("endpoint host is not a valid hostname or IP address")
        return host.lower()

    def validate(self) -> None:
        self._canonical_host(self.host)
        if not isinstance(self.port, int) or isinstance(self.port, bool) or not 1 <= self.port <= 65535:
            raise ValueError("endpoint port must be between 1 and 65535")
