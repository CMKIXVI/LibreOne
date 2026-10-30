import pytest

from libreone.system.ipc import Channel


def test_empty_channel_raises_empty_error():
    channel = Channel.create()
    with pytest.raises(Exception):
        channel.receive()
