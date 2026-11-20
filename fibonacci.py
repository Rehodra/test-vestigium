from functools import lru_cache


@lru_cache(maxsize=None)
def _fibonacci(index: int) -> int:
    if index < 2:
        return index
    return _fibonacci(index - 1) + _fibonacci(index - 2)


def fibonacci_series(length: int) -> list[int]:
    """Return the first ``length`` Fibonacci numbers."""
    if length < 0:
        raise ValueError("length must be non-negative")
    return [_fibonacci(index) for index in range(length)]
