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
    print("=== Plant Factory Output ===")
    rose: Plant = Plant("Rose", 25, 30)
    oak: Plant = Plant("Oak", 200, 365)
    cactus: Plant = Plant("Cactus", 5, 90)
    sun: Plant = Plant("Sunflower", 80, 45)
    fern: Plant = Plant("Fern", 15, 120)
    plants = [rose, oak, cactus, sun, fern]
    for n in plants:
        print("Created: ", end="")
        n.show()


if __name__ == "__main__":
    main()
