#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "A garden error occured") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "The tomate plant is wilting!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomate plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    for error in [PlantError("The tomate plant is wilting!"),
                  WaterError("Not enough water in the tank!")]:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly")

    # try:
    #     raise PlantError()
    # raise GardenError("")
# def garden() -> None:

# def plant() -> None:

# def
