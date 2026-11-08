"""
Task 2: Profit from text (generator)

- generator_numbers(text) yields every real number found in the text
- numbers are written correctly and separated by spaces on both sides
- sum_profit(text, func) sums the numbers produced by func(text)
- use a regular expression and yield
"""

import re
from typing import Callable, Iterator

# A real number with a decimal part, e.g. 1000.01 or 324.00.
# (?<!\S) / (?!\S) mean "a whitespace or the start/end of the text" around it,
# so numbers glued to other characters ("27.45,", "v1.5", "1.2.3") are skipped.
NUMBER_PATTERN = re.compile(r"(?<!\S)\d+\.\d+(?!\S)")


def generator_numbers(text: str) -> Iterator[float]:
    """Yield every real number in the text."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # finditer is lazy too, so the text is processed match by match
    for match in NUMBER_PATTERN.finditer(text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float:
    """Return the sum of all numbers produced by func(text)."""
    # round() removes float noise like 1351.4599999999998
    return round(sum(func(text)), 2)


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    assert total_income == 1351.46

    # generator_numbers really is a generator and yields floats
    assert list(generator_numbers(text)) == [1000.01, 27.45, 324.0]

    # Numbers at the very start and end of the text are found
    assert sum_profit("10.5 і 20.5", generator_numbers) == 31.0

    # Tabs and new lines are whitespace too
    assert sum_profit("дохід\t1.25\n2.75\n", generator_numbers) == 4.0

    # Not separated by spaces -> not a number by the task rules
    glued = "ціни: 10.50, 20.75. v1.5 1.2.3 abc"
    assert sum_profit(glued, generator_numbers) == 0

    # No numbers or an empty text -> 0
    assert sum_profit("У цьому тексті немає чисел.", generator_numbers) == 0
    assert sum_profit("", generator_numbers) == 0

    # Wrong type of text
    try:
        sum_profit(None, generator_numbers)
    except TypeError:
        pass
    else:
        raise AssertionError("TypeError expected for None")

    print(f"Загальний дохід: {total_income}")
