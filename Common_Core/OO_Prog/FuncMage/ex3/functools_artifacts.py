from typing import Any, Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    if operation == "add":
        return reduce(add, spells)
    if operation == "mul":
        return reduce(mul, spells)
    if operation == "max":
        return reduce(max, spells)
    if operation == "min":
        return reduce(min, spells)
    else:
        raise ValueError("Invalid operation")


def partial_enchanter(base_enchantment: Callable[..., str]
                      ) -> dict[str, Callable[..., str]]:
    return {
        "fireball": partial(base_enchantment, power=50, element="fire"),
        "ice spike": partial(base_enchantment, power=50, element="ice"),
        "lightning bolt": partial(base_enchantment, power=50,
                                  element="lightning")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("number should not be negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast_spell(spell: Any) -> str:
        return "Unknown spell type"

    @cast_spell.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast_spell.register(str)
    def _(spell: int) -> str:
        return f"Enchantment: {spell}"

    @cast_spell.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"
    return cast_spell


if __name__ == "__main__":
    print("Testing spell reducer...")
    spell_powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spell_powers, "add")}")
    print(f"Product: {spell_reducer(spell_powers, "mul")}")
    print(f"Max: {spell_reducer(spell_powers, "max")}")
    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print("\nTesting spell dispatcher...")
    cast_spell = spell_dispatcher()
    print(cast_spell(42))
    print(cast_spell("fireball"))
    print(cast_spell(["fireball", "ice spike", 42]))
    print(cast_spell(43.5))
