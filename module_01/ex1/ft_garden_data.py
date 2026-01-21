"""Plant class that serves as a blueprint for any plant"""


class Plant:
    def __init__(self, name, height, age):
        """
        Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in centimeters.
        plant_age (int): The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)
print("=== Garden Plant Registry ===")
print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old")
print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old")
print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")
