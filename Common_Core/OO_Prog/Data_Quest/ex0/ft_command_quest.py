import sys


def main() -> None:
    i: int = 1
    argv: list[str] = sys.argv
    argc: int = len(argv)
    print("=== Command Quest ===")
    print(f"Program name: {argv[0]}")
    if argc > 1:
        print(f"Arguments received: {argc - 1}")
        while i < argc:
            print(f"Argument {i}: {argv[i]}")
            i += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
