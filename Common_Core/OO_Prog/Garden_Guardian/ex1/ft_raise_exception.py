from typing import Any


class TempError(Exception):
    pass


class HotError(TempError):
    pass


class ColdError(TempError):
    pass


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise HotError
    elif temp < 0:
        raise ColdError
    else:
        return temp


def test_temperature(test: Any) -> None:
    print(f"Input data is '{test}'")
    try:
        input_temperature(test)
    except ValueError:
        print(
             f"Caught input_temperature error:"
             f" invalid literal for int() with base 10: '{test}'\n"
             )
    except HotError:
        print(
             f"Caught input_temperature error:"
             f" {test}°C is too hot for plants (max 40°C)\n"
             )
    except ColdError:
        print(
             f"Caught input_temperature error:"
             f" {test}°C is too cold for plants (min 0°C)\n"
             )
    else:
        print(f"Temperature is now {test}°C\n")


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature("25")
    test_temperature("abc")
    test_temperature("100")
    test_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
