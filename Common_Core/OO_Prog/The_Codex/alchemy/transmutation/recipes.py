from alchemy import potions, elements
from ..potions import create_fire


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{elements.create_air()}'"
            f" and '{potions.strength_potion()}' mixed with '{create_fire()}'")
