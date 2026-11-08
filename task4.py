"""
Task 4: Console Assistant Bot with error handling

- every user input error is handled by the input_error decorator
- input_error catches KeyError, ValueError, IndexError
  and returns a message to the user ("Enter user name",
  "Give me name and phone please", ...)
- the bot keeps running after an error
- every command handler is wrapped with @input_error
"""

from functools import wraps
from typing import Callable

NOT_FOUND = "Contact not found."
NEED_NAME_PHONE = "Give me name and phone please."
NEED_ARGUMENT = "Enter the argument for the command"


def input_error(func: Callable) -> Callable:
    """Turn KeyError, ValueError, IndexError into messages for the user."""

    @wraps(func)  # keeps the name and docstring of the wrapped handler
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return NOT_FOUND
        except ValueError as error:
            # A handler may pass its own text: raise ValueError("...")
            return str(error) or NEED_NAME_PHONE
        except IndexError:
            return NEED_ARGUMENT

    return inner


def parse_input(user_input: str) -> tuple[str, ...]:
    """Split user input into a lowercase command and its arguments."""
    if not user_input.strip():
        return ("",)
    cmd, *args = user_input.split()
    return cmd.lower(), *args


def validate_phone(phone: str) -> None:
    """Raise ValueError if the phone is not 7-15 digits with optional '+'."""
    digits = phone.removeprefix("+")
    if not digits.isdigit() or not 7 <= len(digits) <= 15:
        raise ValueError(
            "Phone must contain 7-15 digits (optionally starting with +)."
        )


@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Add a contact: add <name> <phone>."""
    if not args:
        raise IndexError
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        raise ValueError(
            f"Contact '{name}' already exists. Use 'change' to update it."
        )
    validate_phone(phone)
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Change the phone of an existing contact: change <name> <phone>."""
    if not args:
        raise IndexError
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name not in contacts:
        raise KeyError(name)
    validate_phone(phone)
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """Return the phone of a contact: phone <name>."""
    name = args[0]  # IndexError if the name is missing
    if len(args) > 1:
        raise ValueError("Enter only the name: phone <name>")
    return contacts[name]  # KeyError if there is no such contact


@input_error
def show_all(contacts: dict[str, str]) -> str:
    """Return all contacts, one 'name: phone' per line."""
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    """Run the request-response loop of the assistant bot."""
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        try:
            user_input = input("Enter a command: ")
        except (KeyboardInterrupt, EOFError):
            # Ctrl+C / Ctrl+D close the bot politely, without a traceback
            print("\nGood bye!")
            break

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "":
            print("Enter a command.")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    book: dict[str, str] = {}

    # parse_input
    assert parse_input("ADD John 1234567890") == ("add", "John", "1234567890")
    assert parse_input("   ") == ("",)
    assert parse_input("  all  ") == ("all",)

    # Happy path
    assert add_contact(["John", "1234567890"], book) == "Contact added."
    assert book["John"] == "1234567890"
    new_phone = "+380501234567"
    assert change_contact(["John", new_phone], book) == "Contact updated."
    assert show_phone(["John"], book) == "+380501234567"
    assert show_all(book) == "John: +380501234567"
    assert show_all({}) == "No contacts saved."

    # add: no args / not enough / too many / duplicate / bad phone
    assert add_contact([], book) == NEED_ARGUMENT
    assert add_contact(["Bob"], book) == NEED_NAME_PHONE
    assert add_contact(["Bob", "1", "2"], book) == NEED_NAME_PHONE
    assert "already exists" in add_contact(["John", "1111111111"], book)
    assert book["John"] == "+380501234567"  # not overwritten
    assert "digits" in add_contact(["Bob", "abc"], book)
    assert "digits" in add_contact(["Bob", "123"], book)
    assert "Bob" not in book

    # change: no args / not enough / unknown contact / bad phone
    assert change_contact([], book) == NEED_ARGUMENT
    assert change_contact(["John"], book) == NEED_NAME_PHONE
    assert change_contact(["Ann", "1234567890"], book) == NOT_FOUND
    assert "digits" in change_contact(["John", "phone"], book)

    # phone: no args / unknown contact / too many args
    assert show_phone([], book) == NEED_ARGUMENT
    assert show_phone(["Ann"], book) == NOT_FOUND
    assert "only the name" in show_phone(["John", "extra"], book)

    # Decorator keeps the original function name
    assert add_contact.__name__ == "add_contact"

    main()
