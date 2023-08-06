import numpy as np


def _generic_mantissa(op, x: np.ndarray, n: int) -> np.ndarray:
    def fn(x):
        s = np.sign(x)
        x = np.abs(x)
        a = np.floor(np.log2(x))
        x = x / 2**a
        assert np.all(1.0 <= x) and np.all(x < 2.0), x
        x = op(x * 2**n) / 2**n
        x = x * 2**a
        return s * x

    return np.where(x == 0.0, 0.0, fn(np.where(x == 0.0, 1.0, x)))


def round_mantissa(x: np.ndarray, n: int) -> np.ndarray:
    """Round number

    Args:
        x: number to round
        n: number of mantissa digits to keep

    Returns:
        rounded number

    Example:
        >>> round_mantissa(0.5 + 0.25 + 0.125, 0)
        array(1.)

        >>> round_mantissa(0.5 + 0.25 + 0.125, 2)
        array(0.875)
    """
    return _generic_mantissa(np.round, x, n)


def floor_mantissa(x: np.ndarray, n: int) -> np.ndarray:
    """Floor number

    Args:
        x: number to floor
        n: number of mantissa digits to keep

    Returns:
        floored number

    Example:
        >>> floor_mantissa(0.5 + 0.25 + 0.125, 0)
        array(0.5)
    """
    return _generic_mantissa(np.floor, x, n)


def ceil_mantissa(x: np.ndarray, n: int) -> np.ndarray:
    """Ceil number

    Args:
        x: number to ceil
        n: number of mantissa digits to keep

    Returns:
        ceiled number

    Example:
        >>> ceil_mantissa(0.5 + 0.25 + 0.125, 0)
        array(1.)
    """
    return _generic_mantissa(np.ceil, x, n)


def logspace(start: int, stop: int, n: int) -> np.ndarray:
    """Logarithmically spaced array between ``2**start`` and ``2**stop``.

    Args:
        start: starting exponent in base 2
        stop: ending exponent in base 2
        n: number of mantissa digits to keep

    Returns:
        logarithmically spaced array
    """
    m = np.stack(
        np.meshgrid(*[np.array([0.0, 1.0])] * n, indexing="ij"), axis=-1
    ).reshape(-1, n)
    m = 1.0 + np.sum(m * 0.5 ** (np.arange(n) + 1.0), axis=-1)
    x = m * 2 ** np.arange(start, stop)[:, None]
    return np.concatenate([x.reshape(-1), [2**stop]])
