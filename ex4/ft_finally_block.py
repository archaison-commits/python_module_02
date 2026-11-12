#!/usr/bin/env python3

class PlantError(Exception):
    def __init__(self, message: str = "Invalid plant name to water:") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("Testing valid plants...")
    valid_plants: list[str] = ["Tomato", "Lettuce", "Carrots"]
    try:
        print("Opening watering system")
        for p in valid_plants:
            water_plant(p)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
    print("\nTesting invalid plants...")
    invalid_plants: list[str] = ["Tomato", "lettuce", "Carrots"]
    try:
        print("Opening watering system")
        for p in invalid_plants:
            water_plant(p)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
