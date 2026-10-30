from libreone.system.storage import Storage


def test_storage_rejects_path_escape(tmp_path):
    storage = Storage(tmp_path)
    try:
        storage.resolve("../outside")
    except ValueError:
        return
    raise AssertionError("storage path escape was accepted")
