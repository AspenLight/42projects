from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        self.name = "Sproutling"
        self.type = "Grass"
        self.target = "itself"
        self.amount = "small"

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals {self.target} for a {self.amount} amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        self.name = "Bloomelle"
        self.type = "Grass/Fairy"
        self.target = "itself and others"
        self.amount = "large"

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals {self.target} for a {self.amount} amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        self.name = "Shiftling"
        self.type = "Normal"
        self.transformed = False
        self.morph = "a sharper form"

    def attack(self) -> str:
        if self.transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into {self.morph}!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        self.name = "Morphagon"
        self.type = "Normal/Dragon"
        self.transformed = False
        self.morph = "a draconic battle form"

    def attack(self) -> str:
        if self.transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into {self.morph}!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."
