class GardenError(Exception):
    def __init__(self, message: str = "Unknown Garden Error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant Error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown Water Error") -> None:
        super().__init__(message)


def garden_errors(num: int) -> None:
    if num == 0:
        raise PlantError("The tomato plant is wilting!")
    elif num == 1:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors(num: int) -> None:
    if num != 2:
        try:
            garden_errors(num)
        except PlantError as error:
            print(f"Caught PlantError: {error}")
        except WaterError as error:
            print(f" Caught WaterError: {error}")
    else:
        for num in range(2):
            try:
                garden_errors(num)
            except GardenError as error:
                print(f"Caught GardenError: {error}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    test_custom_errors(0)
    print("\nTesting WaterError...")
    test_custom_errors(1)
    print("\nTesting catching all garden errors...")
    test_custom_errors(2)
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
