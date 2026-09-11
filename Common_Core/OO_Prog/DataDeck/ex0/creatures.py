from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self) -> None:
        self.name: str
        self.type: str

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Creature")


class Flameling(Creature):
    def __init__(self) -> None:
        self.name: str = "Flameling"
        self.type: str = "Fire"

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        self.name: str = "Pyrodon"
        self.type: str = "Fire/Flying"

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        self.name: str = "Aquabub"
        self.type: str = "Water"

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        self.name: str = "Torragon"
        self.type: str = "Water"

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"
