import ex1


def HealTest() -> None:
    print("Testing Creature with healing capability")
    mon1 = ex1.HealingCreatureFactory.create_base()
    mon2 = ex1.HealingCreatureFactory.create_evolved()
    print("base:")
    print(mon1.describe())
    print(mon1.attack())
    print(mon1.heal())
    print("evolved:")
    print(mon2.describe())
    print(mon2.attack())
    print(mon2.heal())
    print()


def TransformTest() -> None:
    print("Testing creature with transform capability")
    mon1 = ex1.TransformCreatureFactory.create_base()
    mon2 = ex1.TransformCreatureFactory.create_evolved()
    print("base:")
    print(mon1.describe())
    print(mon1.attack())
    print(mon1.transform())
    print(mon1.attack())
    print(mon1.revert())
    print("evolved:")
    print(mon2.describe())
    print(mon2.attack())
    print(mon2.transform())
    print(mon2.attack())
    print(mon2.revert())


if __name__ == "__main__":
    HealTest()
    TransformTest()
