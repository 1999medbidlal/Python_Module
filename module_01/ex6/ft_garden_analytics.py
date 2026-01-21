#!python3
class Plant:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grows(self):
        self.height += 1

    def to_string(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):

    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = "blooming"

    def to_string(self) -> str:
        return f"{super().to_string()}, {self.color} flowers ({self.blooming})"


class PrizeFlower(FloweringPlant):

    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def to_string(self) -> str:
        return f"{super().to_string()}, Prize points: {self.prize_points}"


"""fin bulid Plant → FloweringPlant → PrizeFlower """


class GardenManager:
    total_gardens = 0
    garden_scores = {}
    all_garden = []

    def __init__(self, name_garden):
        self.name_garden = name_garden
        self.plants = []
        self.sum_height = 0
        self.growth = 0
        self.reg = 0
        self.flower = 0
        self.prize = 0
        GardenManager.total_gardens += 1
        GardenManager.all_garden.append(self)

    def add_plant(self, plant):
        self.plants.append(plant)
        if plant.__class__ is Plant:
            self.reg += 1
        elif plant.__class__ is FloweringPlant:
            self.flower += 1
        elif plant.__class__ is PrizeFlower:
            self.prize += 1

    def helping_grow(self):
        for plant in self.plants:
            self.growth += 1
            self.sum_height += 1
            plant.grows()

    def calculate_score(self) -> int:
        self.score = 0
        for key in self.plants:
            if key.__class__ is Plant:
                self.score += key.height
            elif key.__class__ is FloweringPlant:
                self.score += key.height + 15
            elif key.__class__ is PrizeFlower:
                self.score += key.height + 15 + key.prize_points
        GardenManager.garden_scores[self.name_garden] = self.score
        return self.score

    """class method"""

    def report_total_gardens(cls) -> int:
        return cls.total_gardens

    report_total_gardens = classmethod(report_total_gardens)

    def create_garden_network(cls) -> list:
        return cls.all_garden

    create_garden_network = classmethod(create_garden_network)
    """Nested Classes"""

    class GardenStats:
        """staticmethode"""

        def display_add_plant(manger):
            for plant in manger.plants:
                print(f"Added {plant.name} to {manger.name_garden}'s garden")

        display_add_plant = staticmethod(display_add_plant)

        def display_growth(manger):
            print(f"\n{manger.name_garden} is helping all plants grow...")
            for plant in manger.plants:
                print(f"{plant.name} grew 1cm")

        display_growth = staticmethod(display_growth)

        def info_update(manger):
            print(f"\n===  {manger.name_garden}'s Garden Report ===")
            print("Plants in garden:")
            for p in manger.plants:
                print(p.to_string())

        info_update = staticmethod(info_update)

        def info_plants(manger):
            print(f"\nPlants added: {manger.sum_height}, "
                  f"Total growth: {manger.growth}cm")
            print(f"Plant types: {manger.reg} regular, "
                  f"{manger.flower} flowering, {manger.prize} prize flowers")

        info_plants = staticmethod(info_plants)

        def validate_heights(manger) -> str:
            for p in manger.plants:
                if (p.height < 0):
                    print("\nHeight validation test: False")
                    return
            print("\nHeight validation test: True")

        validate_heights = staticmethod(validate_heights)

        def display_score_totale(manger):
            i = 0
            j = manger.report_total_gardens()
            gardens = manger.create_garden_network()
            print("Garden scores - ", end="")
            for garden in gardens:
                score = garden.calculate_score()
                print(f"{garden.name_garden}: {score}", end="")
                if i < j - 1:
                    print(", ", end="")
                else:
                    print("")
                i += 1
            print(f"Total gardens managed: {j}")

        display_score_totale = staticmethod(display_score_totale)


print("=== Garden Management System Demo ===\n")
""" create objets plants """
p1 = Plant("Oak Tree", 100)
p2 = FloweringPlant("Rose", 25, "red")
p3 = PrizeFlower("Sunflower", 50, "yellow", 10)
p4 = Plant("Small Bush", 45)
p5 = FloweringPlant("Lily", 30, "white")
"""add manger Alice and Bob"""
manger_alice = GardenManager("Alice")
manger_bob = GardenManager("Bob")
"""add plants to garden Alice and Bob"""
manger_alice.add_plant(p1)
manger_alice.add_plant(p2)
manger_alice.add_plant(p3)
manger_bob.add_plant(p4)
manger_bob.add_plant(p5)
"""display plants to add"""
GardenManager.GardenStats.display_add_plant(manger_alice)

"""help plants to grow in garden alice and bob"""
manger_alice.helping_grow()
manger_bob.helping_grow()
GardenManager.GardenStats.display_growth(manger_alice)
"""alice garden report"""
GardenManager.GardenStats.info_update(manger_alice)
GardenManager.GardenStats.info_plants(manger_alice)
GardenManager.GardenStats.validate_heights(manger_alice)
GardenManager.GardenStats.display_score_totale(GardenManager)
