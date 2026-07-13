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


def transform_data(content: str) -> str:
    return "\n".join(line + "#" for line in content.splitlines())


def save_data(content: str, name: str) -> None:
    print(f"Saving data to '{name}'")
    try:
        newfile = open(name, "w")
    except (FileNotFoundError, PermissionError) as error:
        print(
              f"[STDERR] Error opening file '{name}':"
              f" {error}", file=sys.stderr
              )
        print("Data not saved.")
    else:
        newfile.write(content)
        newfile.close()
        print(f"Data saved in file '{name}'.")


def get_newfile() -> str:
    print("Enter new file name (or empty): ", end="", flush=True)
    name = sys.stdin.readline().splitlines()[0]
    return name


def main() -> None:
    argv = sys.argv
    argc = len(argv)
    if argc != 2:
        print("Usage: ft_stream_management.py <file>")
        return
    file_name = argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    file = get_file(file_name)
    if not file:
        return
    content = file.read()
    print(f"---\n\n{content}\n\n---")
    file.close()
    print(f"File '{file_name}' closed.\n")
    print("Transform data:")
    content = transform_data(content)
    print(f"---\n\n{content}\n\n---")
    new_file_name = get_newfile()
    if not new_file_name:
        print("Not saving data.")
    else:
        save_data(content, new_file_name)


if __name__ == "__main__":
    main()
