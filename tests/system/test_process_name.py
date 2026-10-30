from libreone.system.process import Process


def test_process_preserves_name():
    assert Process("ai-runtime").name == "ai-runtime"
