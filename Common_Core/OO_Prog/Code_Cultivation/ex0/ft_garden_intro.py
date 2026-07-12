class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self.height = height
        self.days = days


def main():
    print("=== Welcome to My Garden ===")
    rose: Plant = Plant("Rose", 25, 30)
    print(f"Plant: {rose.name}")
    print(f"Height: {rose.height}cm")
    print(f"Age: {rose.days} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    main()
