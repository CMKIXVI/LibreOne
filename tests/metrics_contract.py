from libreone.system.metrics import Counter


def verify_metrics_contract() -> bool:
    counter = Counter()
    counter.increment()
    counter.increment(2)
    return counter.value == 3
