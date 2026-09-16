from typing import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def icespike(target: str, power: int) -> str:
    return f"Ice Spike hits {target} for {power} damage"


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]
                   ) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable[[str, int], str], multiplier: int
                    ) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        power = power * multiplier
        return base_spell(target, power)
    return amplified


def conditional_caster(condition: bool, spell: Callable[[str, int], str]
                       ) -> Callable[[str, int], str]:
    def conditional(target: str, power: int) -> str:
        if condition is True:
            return spell(target, power)
        else:
            return "Spell Fizzled"
    return conditional


def spell_sequence(spells: list[Callable[[str, int], str]]
                   ) -> Callable[[str, int], list[str]]:
    def sequenced(target: str, power: int) -> list[str]:
        lst: list[str] = []
        for spell in spells:
            lst.append(spell(target, power))
        return lst
    return sequenced


if __name__ == "__main__":
    print("Testing spell combiner...")
    target = "Dragon"
    power = 10
    combined = spell_combiner(fireball, heal)
    print(combined(target, power))
    print("Testing power amplifier...")
    amplified = power_amplifier(icespike, 3)
    print(f"Original: {icespike(target, power)}, "
          f"Amplified: {amplified(target, power)}")
