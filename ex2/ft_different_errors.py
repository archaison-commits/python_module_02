#!/usr/bin/env python3

def garden_operations(operation_number: str) -> None:
    if operation_number == "0":
        int("asd")
    elif operation_number == "1":
        10 / 0
    elif operation_number == "2":
        with open("/non/extitent/file", "r") as file:
            file.read()
    elif operation_number == "3":
        "test" + 1
    elif operation_number == "4":
        try:
            int("abc")
            10 / 0
            open("/non/extitent/file", "r")
            "test" + 1
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError):
            print("Operation completed succesfully\n")


def test_error_types() -> None:
    print("Testing operation 0...")
    try:
        garden_operations("0")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print("Testing operation 1...")
    try:
        garden_operations("1")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: division by {e}")
    print("Testing operation 2...")
    try:
        garden_operations("2")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: '{e}'")
    print("Testing operation 3...")
    try:
        garden_operations("3")
    except TypeError as e:
        print(f'Caught TypeError: "{e})')
    print("Testing operation 4...")
    garden_operations("4")
    print("All error types tested succesfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
