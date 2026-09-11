from abc import ABC, abstractmethod


class HealCapability(ABC):
    def __init__(self) -> None:
        self.target: str

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.transformed: bool
        self.morph: str

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
