#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    return int(temp_str)


def test_temperature() -> None:
    try:
        valid_temp: int = input_temperature("25")
        print(f"Temperature is now {valid_temp}°C\n")
    except ValueError as e:
        print(f"Caught input_tempretature error: Invalid literal "
              f"for int() with base 10: {e}")
    try:
        invalid_temp: int = input_temperature("abc")
        print(f"Temperature is now {invalid_temp}°C\n")
    except ValueError as e:
        print(f"Caught input_tempretature error: Invalid literal"
              f"for int() with base 10: {e}\n")
    print("All tests completed - program didn't crash")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
