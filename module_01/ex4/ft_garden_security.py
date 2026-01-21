""""    A class to represent a plant in a garden."""


class Plant:

    def __init__(self, name):
        self.name = name
        """private attribute"""
        self.__height = 0
        self.__age = 0

    """Getter for height"""

    def get_height(self):
        return self.__height

    """Getter for age"""

    def get_age(self):
        return self.__age

    """Setter for height"""

    def set_height(self, new_height):
        if new_height < 0:
            print("\nInvalid operation attempted: height ", end="")
            print(f"{new_height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")

    """Setter for age"""

    def set_age(self, new_age):
        if new_age < 0:
            print("\nInvalid operation attempted: age ", end="")
            print(f"{new_age} days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")

    def status(self):
        print(f"Current plant: {self.name} ", end="")
        print(f"({self.get_height()}cm, ", end="")
        print(f"{self.get_age()} days)")


print("=== Garden Security System ===")
current_plant = Plant("Rose")
print(f"Plant created: {current_plant.name}")
current_plant.set_height(25)
current_plant.set_age(30)
current_plant.set_height(-5)
current_plant.status()
