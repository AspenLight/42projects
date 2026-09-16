from functools import wraps
from typing import Any, Callable
import time


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrap(*args: list[Any], **kwargs: dict[str, Any]) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        runtime = end - start
        print(f"Spell completed in {runtime:.3f} seconds")
        return result
    return wrap


def power_validator(min_power: int) -> Callable[..., Any]:
    def metawrap(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrap(*args: list[Any], **kwargs: int) -> Any:
            power: int = kwargs["power"]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrap
    return metawrap


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def metawrap(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrap(*args: list[Any], **kwargs: dict[str, Any]) -> Any:
            for n in range(1, max_attempts+1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    if n != max_attempts:
                        print("Spell failed, retrying..."
                              f" (attempt {n}/{max_attempts})")
            return (f"Spell casting failed after {max_attempts} attempts")
        return wrap
    return metawrap


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) > 3:
            for char in name:
                if not (char.isalpha() or char == " "):
                    return False
            return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power")


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Fireball cast!"


@retry_spell(3)
def badspell() -> None:
    raise ValueError("AAAAAAAAA")


if __name__ == "__main__":
    print("Testing spell timer...")
    guild = MageGuild()
    print(f"Result: {fireball()}")
    print("\nTesting retrying spell...")
    print(badspell())
    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Barnabus"))
    print(MageGuild.validate_mage_name("L337Coder"))
    print(guild.cast_spell("Lightning", power=15))
    print(guild.cast_spell("Lightning", power=7))
