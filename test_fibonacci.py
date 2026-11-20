from fibonacci import fibonacci_series


def test_fibonacci_series() -> None:
    assert fibonacci_series(0) == []
    assert fibonacci_series(1) == [0]
    assert fibonacci_series(8) == [0, 1, 1, 2, 3, 5, 8, 13]


def test_fibonacci_series_rejects_negative_length() -> None:
    try:
        fibonacci_series(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative lengths must raise ValueError")
