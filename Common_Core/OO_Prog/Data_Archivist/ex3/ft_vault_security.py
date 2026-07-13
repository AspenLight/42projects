def secure_archive(file_name: str, actions: str = "r",
                   new_content: str = "42") -> tuple[bool, str]:
    try:
        with open(file_name, actions) as file:
            if "w" in actions or "+" in actions:
                file.write(new_content)
            if "r" in actions:
                content = file.read()
    except (FileNotFoundError, PermissionError) as error:
        result = (False, f"{error}")
    else:
        if "w" in actions or "+" in actions:
            result = (True, "Content successfully written to file")
        if "r" in actions:
            result = (True, content)
    return result


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("master.passwd"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt"))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("test", "w", "test"))


if __name__ == "__main__":
    main()
