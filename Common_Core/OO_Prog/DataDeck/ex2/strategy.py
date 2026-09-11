from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capable_creatures import Shiftling, Morphagon, Sproutling, Bloomelle


class BattleError(Exception):
    def __init__(self, message: str = "Unknown Battle Error") -> None:
        super().__init__(message)


class BattleStrategy(ABC):
    def __init__(self) -> None:
        self.valid: bool

    @abstractmethod
    def act(self, mon: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, mon: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.valid = True

    def is_valid(self, mon: Creature) -> bool:
        self.valid = True
        return True

    def act(self, mon: Creature) -> None:
        print(mon.attack())


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.valid = False

    def is_valid(self, mon: Creature) -> bool:
        if type(mon) is (Shiftling or Morphagon):
            self.valid = True
            return True
        else:
            self.valid = False
            return False

    def act(self, mon: Creature) -> None:
        if self.is_valid(self, mon) is True:
            print(mon.transform())
            print(mon.attack())
            print(mon.revert())
        else:
            raise BattleError(f"Invalid Creature '{mon.name}' for"
                              " this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.valid = False

    def is_valid(self, mon: Creature) -> bool:
        if type(mon) is (Sproutling or Bloomelle):
            self.valid = True
            return True
        else:
            self.valid = False
            return False

    def act(self, mon: Creature) -> None:
        if self.is_valid(self, mon) is True:
            print(mon.attack())
            print(mon.heal())
        else:
            raise BattleError(f"Invalid Creature '{mon.name}' for"
                              " this defensive strategy")
