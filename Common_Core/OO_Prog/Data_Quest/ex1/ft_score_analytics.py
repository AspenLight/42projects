import sys


def fill(argc: int, argv: list[str]) -> list[int]:
    i: int = 1
    new: list[int] = []
    while i < argc:
        try:
            new[len(new):] = [int(argv[i])]
        except ValueError:
            print(f"Invalid parameter: ’{argv[i]}’")
        i += 1
    return new


def main() -> None:
    argv: list[str] = sys.argv
    argc: int = len(argv)
    print("=== Player Score Analytics ===")
    scores: list[int] = fill(argc, argv)
    if len(scores) == 0:
        print(
              "No scores provided.\n"
              "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
             )
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total sccore: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"Hight score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
