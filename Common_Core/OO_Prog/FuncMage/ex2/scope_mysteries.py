from typing import Any, Callable


def mage_counter() -> Callable[[], int]:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    def spellpower(plus: int) -> int:
        nonlocal initial_power
        initial_power += plus
        return initial_power
    return spellpower


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(name: str) -> str:
        item = enchantment_type + " " + name
        return item
    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        if key in vault:
            return vault[key]
        else:
            return "Memory not found"
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    counter_a = mage_counter()
    counter_b = mage_counter()
    spellpower = spell_accumulator(100)
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    memvault = memory_vault()
    store = memvault["store"]
    recall = memvault["recall"]
    print("Testing mage counter...")
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print("\nTesting spell accumulator...")
    print(f"Base 100, add 20: {spellpower(20)}")
    print(f"Base 100, add 30: {spellpower(30)}")
    print("\nTesting enchantment factory...")
    print(flaming("Sword"))
    print(frozen("Shield"))
    print("\nTesting memory vault...")
    print("Store 'secret' = 42")
    store("secret", 42)
    print(f"Recall 'secret': {recall("secret")}")
    print(f"Recall 'unknown': {recall("unknown")}")
