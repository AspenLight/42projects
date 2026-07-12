class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self._height = height
        self._days = days

    def show(self):
        print(f"{self.name}: {self._height:0.1f}cm, {self._days} days old")

    def grow(self):
        self._height += 0.8

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


def main():
    print("=== Garden Security System ===")
    rose: Plant = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-3)
    rose.set_age(-2)
    print()
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
