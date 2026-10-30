import runpy


def test_system_module_entrypoint_imports_cleanly():
    module = runpy.run_module("libreone.system.__main__", run_name="libreone_system_test")
    assert "main" in module
