import pytest

from libreone.system.ipc import Channel


def test_channel_round_trip():
    channel = Channel.create()
    channel.send("message")
    assert channel.receive() == "message"
    assert channel.pending == 0


def test_channel_reports_empty_receive_explicitly():
    channel = Channel.create()
    with pytest.raises(RuntimeError, match="channel is empty"):
        channel.receive()


def test_channel_close_is_terminal():
    channel = Channel.create()
    channel.send("message")
    channel.close()
    with pytest.raises(RuntimeError, match="channel is closed"):
        channel.send("another")
    with pytest.raises(RuntimeError, match="channel is closed"):
        channel.receive()
    with pytest.raises(RuntimeError, match="channel is closed"):
        _ = channel.pending
    with pytest.raises(RuntimeError, match="channel is already closed"):
        channel.close()
