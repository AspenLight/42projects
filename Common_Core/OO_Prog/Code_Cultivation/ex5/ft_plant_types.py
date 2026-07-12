class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self._height = height
        self._days = days

    def show(self):
        print(f"{self.name}: {self._height:0.1f}cm, {self._days} days old")

    def grow(self):
        self._height += 2.1

    def age(self):
        self._days += 1

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


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days)
        self.color = color
        self.blooming: bool = False

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
        super().__init__(name, height, days)
        self.trunk_diameter = trunk

    def show(self):
        super().show()
        print(f"Trunk Diameter: {self.trunk_diameter:0.1f}cm")

    def produce_shade(self):
        print(
             f"Tree {self.name} now produces a shade of {self._height:0.1f}"
             f"cm long and {self.trunk_diameter:0.1f}cm wide"
             )


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int, harvest: str):
        super().__init__(name, height, days)
        self.harvest = harvest
        self.nutrition: int = 0

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest}")
        print(f"Nutritional value: {self.nutrition}")

    def age(self):
        super().age()
        self.nutrition += 1


def main():
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose: Flower = Flower("Rose", 15, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak: Tree = Tree("Oak", 200, 365, 5)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato: Vegetable = Vegetable("Tomato", 5, 10, "April")
    tomato.show()
    print("[make the tomato grow and age for 20 days]")
    for n in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
