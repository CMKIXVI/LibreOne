from libreone.system.process import Process


def test_process_instances_have_unique_ids():
    assert Process("a").id != Process("b").id
