import runpy


def test_system_main_module_loads():
    module = runpy.run_module("libreone.system.__main__", run_name="libreone.system.__main__")
    assert module is not None
