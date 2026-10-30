from time import monotonic_ns


def monotonic_ticks() -> int:
    return monotonic_ns()
