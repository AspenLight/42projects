import random


def set_capitalize(lst: list[str]) -> list[str]:
    return [item.capitalize() for item in lst]


def set_scoreboard(players: list[str]) -> dict[str, int]:
    return {players: random.randrange(1000) for player in players}


def get_average_score(scoreboard: dict[str, int]) -> float:
    total_score = sum(scoreboard.values())
    players_number = len(scoreboard)
    return round(total_score / players_number, 2)


def get_highscores(scoreboard: dict[str, int]) -> dict[str, int]:
    avg = get_average_score(scoreboard)
    return {
        player: score for player, score in scoreboard.items()
        if score > avg}


def main() -> None:
    players = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin', 'Liam'
        ]
    capit = set_capitalize(players)
    scoreboard = set_scoreboard(capit)
    avg = get_average_score(scoreboard)
    highscores = get_highscores(scoreboard)
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capit}\n")
    print(f"Score dict: {scoreboard}")
    print(f"Score average is {avg}")
    print(f"High scores: {highscores}")


if __name__ == "__main__":
    main()
