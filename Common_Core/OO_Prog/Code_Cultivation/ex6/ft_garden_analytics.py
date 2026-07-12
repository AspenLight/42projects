class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self._height = height
        self._days = days
        self.statistic = self.Statistic()

    class Statistic():
        def __init__(self):
            self.growcalls = 0
            self.agecalls = 0
            self.showcalls = 0

        def stats(self):
            print(
                 f"Stats: {self.growcalls} grow, {self.agecalls} age"
                 f", {self.showcalls} show"
                 )

    def show(self):
        print(f"{self.name}: {self._height:0.1f}cm, {self._days} days old")
        self.statistic.showcalls += 1

    def grow(self):
        self._height += 8
        self.statistic.growcalls += 1

    def age(self):
        self._days += 1
        self.statistic.agecalls += 1

    def set_height(self, height: float):
        if (height >= 0):
            self._height = height
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, days: int):
        if (days >= 0):
            self._days = days
            print(f"Age updated: {self._days} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    @classmethod
    def anonymous(cls, name: str = "Unknown plant",
                  height: float = 0, days: int = 0):
        cls.name = name
        cls._height = height
        cls._days = days
        return cls(name, height, days)

    @staticmethod
    def year_old(days):
        if days > 365:
            print(f"Is {days} days more than a year? -> True")
        else:
            print(f"Is {days} days more than a year? -> False")


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days)
        self.color = color
        self.blooming: bool = False
        self.statistic = self.Statistic()

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if (self.blooming is True):
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def bloom(self):
        self.blooming = True


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int, trunk: float):
        self.tstatistic: Tree.Statistic = Tree.Statistic()
        super().__init__(name, height, days)
        self.trunk_diameter = trunk

    def show(self):
        super().show()
        print(f"Trunk Diameter: {self.trunk_diameter:0.1f}cm")

    def produce_shade(self):
        print(
             f"Tree {self.name} now produces a shade of"
             f" {self._height:0.1f}cm long and {self.trunk_diameter:0.1f}"
             f"cm wide"
             )
        self.tstatistic.shadecalls += 1

    class Statistic():
        def __init__(self):
            self.growcalls: int = 0
            self.agecalls: int = 0
            self.showcalls: int = 0
            self.shadecalls: int = 0

        def stats(self):
            print(
                 f"Stats: {self.growcalls} grow, {self.agecalls} age, "
                 f"{self.showcalls} show"
                 )
            print(f"{self.shadecalls} shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int, harvest: str):
        super().__init__(name, height, days)
        self.harvest = harvest
        self.nutrition: int = 0
        self.statistic = self.Statistic()

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest}")
        print(f"Nutritional value: {self.nutrition}")

    def age(self):
        super().age()
        self.nutrition += 1


class Seed(Flower):
    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days, color)
        self.amount = 0
        self.statistic = self.Statistic()

    def show(self):
        super().show()
        print(f"Seeds: {self.amount}")

    def bloom(self):
        super().bloom()
        self.amount += 42


def show_statistics(plant: Plant):
    print(f"[statistics for {plant.name}]")
    plant.statistic.stats()


def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.year_old(30)
    Plant.year_old(400)
    print("\n=== Flower")
    rose: Flower = Flower("Rose", 15, 10, "red")
    rose.show()
    show_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    show_statistics(rose)
    print("\n=== Tree")
    oak: Tree = Tree("Oak", 200, 365, 5)
    oak.show()
    show_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_statistics(oak)
    print("\n=== Seed")
    sun: Seed = Seed("Sunflower", 80, 45, "yellow")
    sun.show()
    print("[make sunflower grow, age, and bloom]")
    for n in range(20):
        sun.grow()
        sun.age()
    sun.bloom()
    sun.show()
    show_statistics(sun)
    print("\n=== Anonymous")
    tomato: Plant = Plant.anonymous()
    tomato.show()
    show_statistics(tomato)


if __name__ == "__main__":
    main()
