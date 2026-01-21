"""Validates plant information and raises errors if invalid."""


def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water_level {water_level} is too low (min 1)")

    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


"""Runs test cases for plant health checking."""


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    try:
        plant = check_plant_health("tomato", 1, 11)
        print(plant)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 1, 10)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting bad water level...")
    try:
        check_plant_health("carrots", 15, 10)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("orange", 1, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nAll error raising tests completed!")


test_plant_checks()
