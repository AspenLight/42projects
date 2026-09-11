from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, AggressiveStrategy
from ex2 import NormalStrategy, DefensiveStrategy
from ex0.creatures import Creature


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    lst: list[tuple[Creature, BattleStrategy]] = []
    i = 0
    for factory, strategy in opponents:
        lst.append([factory.create_base(), strategy])
    print()
    for creature, strategy in lst:
        for opponent, opstrat in lst:
            if creature is not opponent:
                print("* Battle *")
                print(creature.describe())
                print("vs.")
                print(opponent.describe())
                print("now fight!")
                try:
                    strategy.act(strategy, creature)
                except Exception as error:
                    print(f"Battle error, aborting tournament: {error}\n")
                    return
                try:
                    opstrat.act(opstrat, opponent)
                except Exception as error:
                    print(f"Battle error, aborting tournament: {error}\n")
                    return
                print()
        lst.pop(i)
        i += 1
        if len(lst) == 1:
            return


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([[FlameFactory, NormalStrategy],
            [HealingCreatureFactory, DefensiveStrategy]])
    print("Tournament 1 (error)")
    print("[ (Flameling+Agressive), (Healing+Defensive) ]")
    battle([[FlameFactory, AggressiveStrategy],
            [HealingCreatureFactory, DefensiveStrategy]])
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Agressive) ]")
    battle([[AquaFactory, NormalStrategy],
            [HealingCreatureFactory, DefensiveStrategy],
            [TransformCreatureFactory, AggressiveStrategy]])
