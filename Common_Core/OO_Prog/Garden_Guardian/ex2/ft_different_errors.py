def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        1 / 0
    elif (operation_number == 2):
        open("/non/existent/file", "r")
    elif (operation_number == 3):
        42 + "string"


def test_error_types(num: int) -> None:
    print(f"Testing operation {num}...")
    try:
        garden_operations(num)
    except ValueError:
        print(
             "Caught ValueError: "
             "invalid literal for int() with base 10: 'abc'"
             )
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print(
             "Caught FileNotFoundError: "
             "[Errno 2] No such file or directory: '/non/existent/file'"
             )
    except TypeError:
        print(
             "Caught TypeError: "
             "can only concatenate str (not \"int\") to str"
             )
    else:
        print("Operation completed successfully")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types(0)
    test_error_types(1)
    test_error_types(2)
    test_error_types(3)
    test_error_types(4)
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()
