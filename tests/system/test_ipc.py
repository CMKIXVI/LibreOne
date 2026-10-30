import pytest

from libreone.system.ipc import Channel


def test_channel_round_trip():
    channel = Channel.create()
    channel.send("hello")
    assert channel.receive() == "hello"
    with pytest.raises(Exception):
        channel.receive()
