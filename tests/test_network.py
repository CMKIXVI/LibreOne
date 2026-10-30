from libreone.system.network import Endpoint


def test_endpoint_validation():
    endpoint = Endpoint("localhost", 8080)
    assert endpoint.host == "localhost"
    assert endpoint.port == 8080
