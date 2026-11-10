#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    int_tmp: int = int(temp_str)
    if not 0 <= int_tmp:
        raise ValueError(f"Caught input_temperature error: {int_tmp}°C "
                         f"is too cold for the plants (min 0°C)\n")
    elif int_tmp > 40:
        raise ValueError(f"Caght input_temperature error: {int_tmp}°C "
                         f"is too hot for the plants (max 40°C)\n")
    return int_tmp


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
    try:
        valid_temp = input_temperature("100")
        print(f"Temperature is now {valid_temp}°C\n")
    except ValueError as e:
        print(f"Caught input_tempretature error: Invalid literal "
              f"for int() with base 10: {e}")
    try:
        invalid_temp = input_temperature("-50")
        print(f"Temperature is now {invalid_temp}°C\n")
    except ValueError as e:
        print(f"Caught input_tempretature error: Invalid literal"
              f"for int() with base 10: {e}\n")
    print("All tests completed - program didn't crash")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
