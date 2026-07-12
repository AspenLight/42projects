from typing import Any


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(test: Any) -> None:
    try:
        input_temperature(test)
    except ValueError:
        print(
             f"Caught input_temperature error:"
             f" invalid literal for int() with base 10: '{test}'\n"
             )
    else:
        print(f"Temperature is now {test}°C\n")


def main() -> None:
    test_var = "25"
    print("=== Garden Temperature ===\n")
    print(f"Input data is '{test_var}'")
    test_temperature(test_var)
    test_var = "abc"
    print(f"Input data is '{test_var}'")
    test_temperature(test_var)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
