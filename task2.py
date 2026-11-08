"""
Task 2: Profit from text (generator)

- generator_numbers(text) yields every real number found in the text
- numbers are written correctly and separated by spaces on both sides
- sum_profit(text, func) sums the numbers produced by func(text)
- use a regular expression and yield
"""

from typing import Callable, Iterator


def generator_numbers(text: str) -> Iterator[float]:
    """Yield every real number in the text."""
    pass  # TODO: your solution


def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float:
    """Return the sum of all numbers produced by func(text)."""
    pass  # TODO: your solution


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    assert total_income == 1351.46

    print(f"Загальний дохід: {total_income}")
