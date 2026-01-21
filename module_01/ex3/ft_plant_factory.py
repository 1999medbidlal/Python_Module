"""" A class to represent a plant in a garden."""


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

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


Plants = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cactus", 5, 90),
    Plant("Sunflower", 80, 45),
    Plant("Fern", 15, 120)
]
print("=== Plant Factory Output ===")
for creat in Plants:
    creat.get_info()
print(f"\nTotal plants created: {len(Plants)}")
