"""Base class for all garden errors"""


class GardenError(Exception):
    pass


"""Error related to plant issues."""


class PlantError(GardenError):
    pass


"""Error related to watering issues."""


class WaterError(GardenError):
    pass


"""Manages plants, watering, and health checks in a garden."""


class GardenManager:

    def __init__(self, name, water_level, sunlight_hours):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

    """Add  a plant to the garden and check water and plant health"""

    def add_plants(self):
        try:
            if self.name == "":
                raise PlantError("Plant name cannot be empty!")
            else:
                print(f"Added {self.name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self, plant_list):
        print("Opening watering system")
        try:
            for plant in plant_list:
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        try:
            if self.water_level > 10:
                raise WaterError(
                    f"Water level {self.water_level} is too high (max 10)")
            print(f"{self.name}: healthy (water: {self.water_level}, "
                  f"sun: {self.sunlight_hours})")
        except WaterError as e:
            print(f"Error checking {self.name}: {e}")


"""Demonstrates"""


def management_system():
    print("=== Garden Management System ===")
    plant1 = GardenManager("tomato", 5, 8)
    plant2 = GardenManager("lettuce", 15, 12)
    plant3 = GardenManager("", 0, 12)
    plants = [plant1, plant2]
    print("\nAdding plants to garden...")
    plant1.add_plants()
    plant2.add_plants()
    plant3.add_plants()
    print("\nWatering plants...")
    plant1.water_plants(plants)
    print("\nChecking plant health...")
    plant1.check_plant_health()
    plant2.check_plant_health()
    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


management_system()
