"""
Task 4: Console Assistant Bot with error handling

- every user input error is handled by the input_error decorator
- input_error catches KeyError, ValueError, IndexError
  and returns a message to the user ("Enter user name",
  "Give me name and phone please", ...)
- the bot keeps running after an error
- every command handler is wrapped with @input_error
"""

from typing import Callable


def input_error(func: Callable) -> Callable:
    """Turn KeyError, ValueError, IndexError into messages for the user."""
    pass  # TODO: your solution


def parse_input(user_input: str) -> tuple[str, ...]:
    """Split user input into a lowercase command and its arguments."""
    pass  # TODO: your solution


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Add a contact: add <name> <phone>."""
    pass  # TODO: your solution


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Change the phone of an existing contact: change <name> <phone>."""
    pass  # TODO: your solution


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """Return the phone of a contact: phone <name>."""
    pass  # TODO: your solution


def show_all(contacts: dict[str, str]) -> str:
    """Return all contacts, one 'name: phone' per line."""
    pass  # TODO: your solution


def main() -> None:
    """Run the request-response loop of the assistant bot."""
    pass  # TODO: your solution


if __name__ == "__main__":
    main()
