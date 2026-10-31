import pytest

from libreone.system.network import Endpoint


def test_endpoint_validation():
    endpoint = Endpoint("localhost", 8080)
    assert endpoint.host == "localhost"
    assert endpoint.port == 8080


def test_endpoint_canonicalizes_hostname_and_ip():
    assert Endpoint(" Example.COM ", 443).host == "example.com"
    assert Endpoint("192.0.2.1", 443).host == "192.0.2.1"
    assert Endpoint("2001:0db8:0:0:0:0:0:1", 443).host == "2001:db8::1"
    assert Endpoint("example.com.", 443).host == "example.com"


def test_endpoint_rejects_invalid_hosts_and_types():
    with pytest.raises(TypeError):
        Endpoint(123, 443)
    with pytest.raises(ValueError):
        Endpoint("", 443)
    with pytest.raises(ValueError):
        Endpoint("bad host", 443)
    with pytest.raises(ValueError):
        Endpoint("-invalid.example", 443)
    with pytest.raises(ValueError):
        Endpoint("example..com", 443)


def test_endpoint_rejects_invalid_ports():
    with pytest.raises(TypeError):
        Endpoint("localhost", True)
    with pytest.raises(TypeError):
        Endpoint("localhost", 8080.0)
    with pytest.raises(ValueError):
        Endpoint("localhost", 0)
    with pytest.raises(ValueError):
        Endpoint("localhost", 65536)
