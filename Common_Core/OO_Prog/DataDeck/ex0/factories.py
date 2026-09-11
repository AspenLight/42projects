from abc import abstractmethod
from .creatures import Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory():
    def __init__(self) -> None:
        pass


class FlameFactory(CreatureFactory):
    @abstractmethod
    def create_base(self) -> Flameling:
        return Flameling()

    @abstractmethod
    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    @abstractmethod
    def create_base(self) -> Aquabub:
        return Aquabub()

    @abstractmethod
    def create_evolved(self) -> Torragon:
        return Torragon()
