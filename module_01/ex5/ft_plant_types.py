class Plant:
    """
    Base class representing a generic plant.
    Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in cm.
        age (int): The age of the plant in days.
    """

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Represents a flowering plant.
    Attributes:
        color (str): The color of the flower.
    Methods:
        bloom(): Prints a message that the flower is blooming.
    """

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    Represents a tree.
    Attributes:
        trunk_diameter (int): Diameter of the trunk in cm.
    Methods:
        produce_shade(): Prints the area of shade the tree provides.
    """

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = int((self.trunk_diameter * 1.56))
        print(f"{t.name} (Tree): {t.height}cm, "
              f"{t.age} days, { t.trunk_diameter}cm diameter")
        print(f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    """
    Represents a vegetable plant.
    Attributes:
        harvest_season (str): Season when the vegetable is harvested.
        nutritional_value (str): Key nutritional value of the vegetable.
    """

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def harvest_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, ", end="")
        print(f"{self.age} days, {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


Plants = {
    "Flower": {
        "f1": ("Rose", 25, 30, "red"),
        "f2": ("Sunflower", 80, 45, "yellow")
    },
    "Tree": {
        "t1": ("Oak", 500, 1825, 50),
        "t2": ("Argan", 150, 90, 40)
    },
    "Veg": {
        "v1": ("Tomato", 80, 90, "summer", "vitamin C"),
        "v2": ("Carrot", 25, 35, "spring", "vitamin D"),
    },
}
flower = [Flower(*Plants["Flower"]["f1"]), Flower(*Plants["Flower"]["f2"])]
tree = [Tree(*Plants["Tree"]["t1"]), Tree(*Plants["Tree"]["t2"])]
vegetable = [Vegetable(*Plants["Veg"]["v1"]), Vegetable(*Plants["Veg"]["v2"])]
print("=== Garden Plant Types ===\n")
for f in flower:
    f.bloom()
print("\n")
for t in tree:
    t.produce_shade()
print("\n")
for v in vegetable:
    v.harvest_info()
