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
    pass  # TODO: your solution


if __name__ == "__main__":
    fib = caching_fibonacci()
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55
    assert fib(15) == 610

    print(fib(10))
    print(fib(15))
