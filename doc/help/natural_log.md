In Python, the natural logarithmic function is represented as `math.log()` and is part of the `math` module. The natural logarithm is the logarithm to the base **e**, where **e** is Euler's number (approximately equal to 2.71828). 

The natural logarithm of a number `x` is denoted as `ln(x)` and is the inverse of the exponential function. That means if you have `ln(x)`, it returns the exponent to which **e** must be raised to obtain `x`.

### Example:
To compute the natural logarithm of a number in Python:

```python
import math

x = 10
ln_x = math.log(x)

print(ln_x)
```

This will output the natural logarithm of 10.

### Key points:
- The natural logarithm is only defined for positive numbers (`x > 0`).
- `math.log(x)` computes `ln(x)` for positive values of `x`.
- If you want to compute the logarithm to a different base (e.g., base 10), you can pass the second argument to `math.log()`, like `math.log(x, base)`. For base 10, use `math.log(x, 10)`.
