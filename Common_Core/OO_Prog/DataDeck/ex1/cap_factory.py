from abc import abstractmethod
from ex0 import CreatureFactory
from .capable_creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    @abstractmethod
    def create_base() -> Sproutling:
        return Sproutling()

    @abstractmethod
    def create_evolved() -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    @abstractmethod
    def create_base() -> Shiftling:
        return Shiftling()

    @abstractmethod
    def create_evolved() -> Morphagon:
        return Morphagon()
