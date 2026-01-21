"""Waters each plant in the list and always cleans up resources."""


def water_plants(plant_list):
    try:
        for plant in plant_list:
            if plant is None:
                print(plant[0])
            else:
                print(f"Watering {plant}")
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


"""Runs test cases for watering system with and without errors."""


def test_watering_system():
    plants = ["tomato", None, "lettuce", "carrots"]
    plant1 = ["tomato", "lettuce", "carrots"]
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    print("Opening watering system")
    water_plants(plant1)
    print("Watering completed successfully!")
    print("\nTesting with error...")
    print("Opening watering system")
    water_plants(plants)
    print("\nCleanup always happens, even with errors!")


test_watering_system()
