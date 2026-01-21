"""Custom error classes"""
"""GardenError - A basic error for garden problems"""


class GardenError(Exception):
    pass


"""Error related to plant issues."""


class PlantError(GardenError):
    pass


"""Error related to watering issues."""


class WaterError(GardenError):
    pass


"""Simulate a plant problem."""


def check_plant():
    raise PlantError("The tomato plant is wilting!")


"""Simulate a water problem."""


def check_water():
    raise WaterError("Not enough water in the tank!")


"""Demonstrates catching custom garden errors."""


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    try:
        print("\nTesting PlantError...")
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    try:
        print("\nTesting WaterError...")
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    try:
        print("\nTesting catching all garden errors...")
        check_plant()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_water()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


test_custom_errors()
