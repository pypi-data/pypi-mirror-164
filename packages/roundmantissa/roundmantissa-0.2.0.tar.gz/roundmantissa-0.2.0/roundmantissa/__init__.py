import math

__version__ = "0.2.0"


def _generic_mantissa(op, x: float, n: int) -> float:
    if x == 0:
        return 0
    s = 1 if x >= 0 else -1
    x = abs(x)
    a = math.floor(math.log2(x))
    x = x / 2**a
    assert 1.0 <= x < 2.0, x
    x = op(x * 2**n) / 2**n
    x = x * 2**a
    return s * x


def round_mantissa(x: float, n: int) -> float:
    """Round number

    Args:
        x: number to round
        n: number of mantissa digits to keep

    Returns:
        rounded number

    Example:
        >>> round_mantissa(0.5 + 0.25 + 0.125, 0)
        1.0

        >>> round_mantissa(0.5 + 0.25 + 0.125, 2)
        0.875
    """
    return _generic_mantissa(round, x, n)


def floor_mantissa(x: float, n: int) -> float:
    """Floor number

    Args:
        x: number to floor
        n: number of mantissa digits to keep

    Returns:
        floored number

    Example:
        >>> floor_mantissa(0.5 + 0.25 + 0.125, 0)
        0.5
    """
    return _generic_mantissa(math.floor, x, n)


def ceil_mantissa(x: float, n: int) -> float:
    """Ceil number

    Args:
        x: number to ceil
        n: number of mantissa digits to keep

    Returns:
        ceiled number

    Example:
        >>> ceil_mantissa(0.5 + 0.25 + 0.125, 0)
        1.0
    """
    return _generic_mantissa(math.ceil, x, n)
