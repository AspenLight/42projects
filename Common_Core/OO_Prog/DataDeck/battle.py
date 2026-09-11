from ex0 import CreatureFactory, AquaFactory, FlameFactory


def factory_test(factory: CreatureFactory) -> None:
    print("Testing factory")
    mon1 = factory.create_base()
    mon2 = factory.create_evolved()
    print(mon1.describe())
    print(mon1.attack())
    print(mon2.describe())
    print(mon2.attack())
    print()


def battle(flame: FlameFactory, aqua: AquaFactory) -> None:
    print("Testing battle")
    mon1 = flame.create_base()
    mon2 = aqua.create_base()
    print(mon1.describe())
    print("vs.")
    print(mon2.describe())
    print("fight!")
    print(mon1.attack())
    print(mon2.attack())


if __name__ == "__main__":
    factory_test(FlameFactory)
    factory_test(AquaFactory)
    battle(FlameFactory, AquaFactory)
