`pip install -U roundmantissa`

# roundmantissa

Tiny library :baby_chick: that rounds floating point numbers based on the length of their mantissa.

```
5.0 = 4.0 + 1.0 = (1 + 1/4) * 2**2 = b1.01 * 2**2
```

```
round_mantissa(5.0, 0) = b1. * 2**2
round_mantissa(5.0, 1) = b1.0 * 2**2
round_mantissa(5.0, 2) = b1.01 * 2**2
```

:hatched_chick: :hatched_chick: :hatched_chick:
