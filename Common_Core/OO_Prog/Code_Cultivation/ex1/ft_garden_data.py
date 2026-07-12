class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self.height = height
        self.days = days

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def main():
    print("=== Garden Plant Registry ===")
    rose: Plant = Plant("Rose", 25, 30)
    sun: Plant = Plant("Sunflower", 80, 45)
    cactus: Plant = Plant("Cactus", 15, 120)
    rose.show()
    sun.show()
    cactus.show()


if __name__ == "__main__":
    main()
