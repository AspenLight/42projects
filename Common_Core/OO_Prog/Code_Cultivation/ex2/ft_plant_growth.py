class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self.height = height
        self.days = days

    def show(self):
        print(
             f"{self.name}: {round(float(self.height), 1)}cm"
             f", {self.days} days old"
             )

    def grow(self):
        self.height += 0.8

    def age(self):
        self.days += 1


def main():
    print("=== Garden Plant Growth ===")
    rose: Plant = Plant("Rose", 25, 30)
    growth: float = 0

    rose.show()
    for n in range(1, 8):
        print(f"=== Day {n} ===")
        rose.grow()
        rose.age()
        rose.show()
        growth += 0.8
    print(f"Growth this week: {growth}cm")


if __name__ == "__main__":
    main()
