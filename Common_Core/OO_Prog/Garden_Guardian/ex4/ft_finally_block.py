class GardenError(Exception):
    def __init__(self, message: str = "Unknown Garden Error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant Error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown Water Error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == str.capitalize(plant_name):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    valid_plants: list[str] = ["Tomato", "Lettuce", "Carrots"]
    invalid_plants: list[str] = ["Tomato", "lettuce", "Carrots"]
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    test_watering_system(valid_plants)
    print("\nTesting invalid plants...")
    test_watering_system(invalid_plants)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
