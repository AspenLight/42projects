import random


class Player:
    players: list[Player] = []

    def __init__(self, name: str):
        self.name = name
        self.achievements = gen_player_achievements()
        Player.players.append(self)

    def __str__(self) -> str:
        return self.name

    def get_unique(self) -> set[str]:
        players = Player.get_players()
        others_achievements = []
        for player in players:
            if player != self:
                others_achievements.append(player.achievements)
        return self.achievements.difference(*others_achievements)

    def get_missing(self) -> set[str]:
        all_achievements = set(get_all_achievements())
        return all_achievements.difference(self.achievements)

    @classmethod
    def get_players(cls) -> list[Player]:
        return Player.players

    @classmethod
    def get_common(cls) -> set[str]:
        all_achievements = set(get_all_achievements())
        players = Player.get_players()
        players_achievements = []
        for player in players:
            players_achievements.append(player.achievements)
        return all_achievements.intersection(*players_achievements)


def get_all_achievements() -> set[str]:
    return {
        "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
        "Survivor", "Master Explorer", "Treasure Hunter",
        "Unstoppable", "First Steps", "Collector Supreme",
        "Untouchable", "Sharp Mind", "Boss Slayer"}


def gen_player_achievements() -> set[str]:
    all_achievements = list(get_all_achievements())
    random_number = random.randrange(4, len(all_achievements))
    return set(random.sample(all_achievements, random_number))


def main() -> None:
    alice = Player("Alice")
    bob = Player("Bob")
    charlie = Player("Charlie")
    dylan = Player("Dylan")
    players = [alice, bob, charlie, dylan]
    all_achievements: set[str] = get_all_achievements()
    print("=== Achievement Tracker System ===")
    print()
    for player in players:
        print(f"Player {player}: {player.achievements}")
    print()
    print(f"All distinct achievements: {all_achievements}")
    print()
    print(f"Common achievements: {Player.get_common()}")
    print()
    for player in players:
        print(f"Only {player} has: {player.get_unique()}")
    print()
    for player in players:
        print(f"{player} is missing: {player.get_missing()}")


if __name__ == "__main__":
    main()
