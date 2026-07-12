import sys
import typing


def get_file(file_name: str) -> None | typing.IO[str]:
    print(f"Accessing file '{file_name}'")
    try:
        file = open(file_name, "r")
    except (FileNotFoundError, PermissionError) as error:
        print(f"Error opening file '{file_name}': {error}")
        return None
    else:
        return file


def main() -> None:
    argv = sys.argv
    argc = len(argv)
    if argc != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    file_name = argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    file = get_file(file_name)
    if not file:
        return
    content = file.read()
    print(f"---\n{content}\n---")
    file.close()
    print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
