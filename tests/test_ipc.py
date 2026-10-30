from libreone.system.ipc import Channel


def test_channel_round_trip():
    channel = Channel.create()
    channel.send("message")
    assert channel.receive() == "message"
