from functools import lru_cache
from typing import List


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number using memoization.

    0-indexed: fibonacci(0) = 0, fibonacci(1) = 1, fibonacci(2) = 1, etc.
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative integers.")
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_series(n: int) -> List[int]:
    """Generate the Fibonacci series containing the first n terms."""
    if n < 0:
        raise ValueError("Number of terms cannot be negative.")
    return [fibonacci(i) for i in range(n)]


def test_fibonacci() -> None:
    """Test function for Fibonacci calculation with memoization."""
    # Test base cases
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

    # Test small values
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765

    # Test memoization speed / larger value
    assert fibonacci(50) == 12586269025

    # Test series generation
    assert fibonacci_series(0) == []
    assert fibonacci_series(1) == [0]
    assert fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]

    # Test error handling
    try:
        fibonacci(-1)
        assert False, "Expected ValueError for negative input"
    except ValueError:
        pass

    try:
        fibonacci_series(-5)
        assert False, "Expected ValueError for negative count"
    except ValueError:
        pass

    print("All tests passed successfully!")


if __name__ == "__main__":
    test_fibonacci()
