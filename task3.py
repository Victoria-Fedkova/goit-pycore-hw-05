"""
Task 3 (optional): Log file analyzer

Usage:
    python3 task3.py <path_to_logfile> [level]

- count records per level (INFO, ERROR, DEBUG, WARNING) and print a table
- if a level is given, also print all records of that level
- handle a missing file and badly formatted lines
- use a functional element: lambda, list comprehension, filter, ...
"""

import sys


def parse_log_line(line: str) -> dict:
    """Parse one log line into date, time, level and message."""
    pass  # TODO: your solution


def load_logs(file_path: str) -> list:
    """Read a log file and return a list of parsed records."""
    pass  # TODO: your solution


def filter_logs_by_level(logs: list, level: str) -> list:
    """Return only the records of the given level."""
    pass  # TODO: your solution


def count_logs_by_level(logs: list) -> dict:
    """Return {level: number of records}."""
    pass  # TODO: your solution


def display_log_counts(counts: dict) -> None:
    """Print the counts as a table."""
    pass  # TODO: your solution


def main() -> None:
    """Read arguments, analyze the log file and print the results."""
    pass  # TODO: your solution


if __name__ == "__main__":
    main()
