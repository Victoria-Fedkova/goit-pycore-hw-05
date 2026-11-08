# GoIT Python Core - Homework 05

Homework assignment #5 from the GoIT Python Core course: functional programming and built-in Python modules.

## Tasks Overview

### Task 1: Fibonacci with Caching

**File:** `task1.py`

Function `caching_fibonacci()` returns the inner function `fibonacci(n)` that keeps a cache of already computed Fibonacci numbers in a closure.

**Requirements:**

- `caching_fibonacci()` returns the inner function `fibonacci(n)`
- If `n` is already in the cache, return the cached value
- Otherwise compute it recursively, save it to the cache and return it

**Example:**

```python
fib = caching_fibonacci()
print(fib(10))  # 55
print(fib(15))  # 610
```

---

### Task 2: Profit from Text

**File:** `task2.py`

Generator `generator_numbers(text)` yields all real numbers from a text, `sum_profit(text, func)` sums them.

**Requirements:**

- Numbers are written correctly and separated by spaces on both sides
- Use a regular expression and `yield`
- `sum_profit` takes the generator function as an argument

**Example:**

```python
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")  # Загальний дохід: 1351.46
```

---

### Task 3: Log File Analyzer (optional)

**File:** `task3.py`

Script reads a log file passed as a command-line argument and prints statistics by log level.

**Requirements:**

- Path to the log file comes from `sys.argv`, an optional second argument is a level
- Functions `parse_log_line`, `load_logs`, `filter_logs_by_level`, `count_logs_by_level`, `display_log_counts`
- Handle a missing file and badly formatted lines
- Use a functional element (lambda, list comprehension, `filter`, ...)

**Example:**

```bash
python3 task3.py logfile.log error
```

```
Рівень логування | Кількість
-----------------|----------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1

Деталі логів для рівня 'ERROR':
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.
```

---

### Task 4: Console Assistant Bot with Error Handling

**File:** `task4.py`

Bot from homework 04, now every command handler is wrapped with the `input_error` decorator.

**Requirements:**

- `input_error` catches `KeyError`, `ValueError`, `IndexError` and returns a message to the user
- The bot keeps running after an error

**Commands (case-insensitive):**

- `hello` - greeting
- `add [name] [phone]` - add a contact
- `change [name] [phone]` - change a phone number
- `phone [name]` - show a phone number
- `all` - show all contacts
- `close` or `exit` - exit the bot

**Example:**

```
Enter a command: add
Enter the argument for the command
Enter a command: add Bob
Give me name and phone please.
Enter a command: add Jime 0501234356
Contact added.
Enter a command: phone
Enter the argument for the command
Enter a command: all
Jime: 0501234356
```

---

## How to Run

```bash
python3 task1.py
python3 task2.py
python3 task3.py logfile.log
python3 task3.py logfile.log error
python3 task4.py
```

`task1.py`, `task2.py` and `task4.py` contain `assert` checks that run before the main code.
No external dependencies, only the Python standard library (Python 3.10+).

## Project Structure

```
goit-pycore-hw-05/
├── task1.py           # Fibonacci with caching
├── task2.py           # Profit from text
├── task3.py           # Log analyzer
├── task4.py           # Console bot with decorator
├── logfile.log        # Test data for Task 3
├── .gitignore
└── README.md
```
