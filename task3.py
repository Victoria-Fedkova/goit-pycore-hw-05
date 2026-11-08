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
from collections import Counter
from datetime import datetime

LEVELS = ("INFO", "DEBUG", "ERROR", "WARNING")
USAGE = "Використання: python3 task3.py <шлях_до_лог_файлу> [рівень]"


def parse_log_line(line: str) -> dict:
    """Parse one log line into date, time, level and message.

    Raises ValueError if the line does not match
    'YYYY-MM-DD HH:MM:SS LEVEL message'.
    """
    # maxsplit=3 keeps spaces inside the message
    parts = line.strip().split(maxsplit=3)
    if len(parts) < 4:
        raise ValueError("очікується 'дата час РІВЕНЬ повідомлення'")

    date, time, level, message = parts

    # strptime checks both the format and real values (no 2024-13-45)
    try:
        datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise ValueError(f"некоректні дата/час '{date} {time}'") from None

    level = level.upper()
    if level not in LEVELS:
        raise ValueError(f"невідомий рівень '{parts[2]}'")

    return {"date": date, "time": time, "level": level, "message": message}


def load_logs(file_path: str) -> list:
    """Read a log file and return a list of parsed records.

    Empty lines are skipped, badly formatted lines are reported and skipped.
    File errors (missing file, no access, ...) are raised to the caller.
    """
    logs = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            try:
                logs.append(parse_log_line(line))
            except ValueError as error:
                print(
                    f"Рядок {line_number} пропущено: {error}",
                    file=sys.stderr,
                )
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """Return only the records of the given level (case-insensitive)."""
    level = level.upper()
    return list(filter(lambda log: log["level"] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    """Return {level: number of records} for every known level."""
    counter = Counter(log["level"] for log in logs)
    # Every level is present, even with 0, so the table is always complete
    return {level: counter[level] for level in LEVELS}


def display_log_counts(counts: dict) -> None:
    """Print the counts as a table."""
    print(f"{'Рівень логування':<17}| Кількість")
    print(f"{'-' * 17}|{'-' * 10}")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")


def display_log_details(logs: list, level: str) -> None:
    """Print all records of one level."""
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    if not logs:
        print("Записів цього рівня немає.")
        return
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main() -> None:
    """Read arguments, analyze the log file and print the results."""
    if len(sys.argv) not in (2, 3):
        print(USAGE, file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    level = sys.argv[2].upper() if len(sys.argv) == 3 else None

    # Check the level before reading the file
    if level is not None and level not in LEVELS:
        print(
            f"Невідомий рівень '{sys.argv[2]}'. Доступні: {', '.join(LEVELS)}",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        logs = load_logs(file_path)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено", file=sys.stderr)
        sys.exit(1)
    except IsADirectoryError:
        print(f"'{file_path}' - це папка, а не файл", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Немає доступу до файлу '{file_path}'", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Файл '{file_path}' не є текстовим (UTF-8)", file=sys.stderr)
        sys.exit(1)
    except OSError as error:
        print(f"Не вдалося прочитати файл: {error}", file=sys.stderr)
        sys.exit(1)

    if not logs:
        print("У файлі немає коректних записів логу.")
        return

    display_log_counts(count_logs_by_level(logs))

    if level is not None:
        display_log_details(filter_logs_by_level(logs, level), level)


if __name__ == "__main__":
    main()
