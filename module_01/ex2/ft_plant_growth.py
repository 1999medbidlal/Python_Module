""""    A class to represent a plant in a garden."""


class Plant:
    def __init__(self, name, height, plant_age):
        """
        Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in centimeters.
        plant_age (int): The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.plant_age = plant_age
        """
        Methods:
        Print the plant's current height and age for the given day.
        Increase the plant's height and age by 1  if day is less than 7.age():
        """

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")

    def grow(self):
        self.height += 1

    def age(self):
        self.plant_age += 1


"""Create a plant"""
flower = Plant("Rose", 25, 30)
initial_height = flower.height
i = 1
day = 7
print(f"=== Day {i} ===")
flower.get_info()
while i < day:
    flower.grow()
    flower.age()
    i += 1
    if i > day - 1:
        break
print(f"=== Day {i} ===")
flower.get_info()
growth = flower.height - initial_height
print(f"Growth this week: +{growth}cm")
