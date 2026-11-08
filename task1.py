"""
Task 1: Fibonacci with caching (closure)

- caching_fibonacci() returns the inner function fibonacci(n)
- fibonacci(n) returns the n-th Fibonacci number
- if n is already in the cache, return the cached value
- otherwise compute it recursively, save to the cache and return it
"""

from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """Return a fibonacci(n) function that caches computed values."""
    # The cache lives in the enclosing scope, so fibonacci() "remembers" it
    # between calls (closure).
    cache: dict[int, int] = {}

    def fibonacci(n: int) -> int:
        """Return the n-th Fibonacci number (0 for n <= 0)."""
        # bool is a subclass of int, so True/False are rejected explicitly
        if isinstance(n, bool) or not isinstance(n, int):
            raise TypeError("n must be an integer")

        # Base cases of the recursion
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Already computed earlier - take it from the cache
        if n in cache:
            return cache[n]

        # Compute recursively and save the result for the next calls
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(10) == 55
    assert fib(15) == 610
    assert fib(10) == 55  # second call is taken from the cache

    # Negative n follows the pseudocode: n <= 0 -> 0
    assert fib(-5) == 0

    # Each caching_fibonacci() call creates its own independent cache
    other_fib = caching_fibonacci()
    assert other_fib(20) == 6765

    # Big n works fast thanks to the cache (without it: ~2^100 calls)
    assert fib(100) == 354224848179261915075

    # Wrong types are rejected
    for bad_value in ("10", 2.5, None, True):
        try:
            fib(bad_value)
        except TypeError:
            pass
        else:
            raise AssertionError(f"TypeError expected for {bad_value!r}")

    print(fib(10))
    print(fib(15))
