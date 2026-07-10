from typing import Generator
import random


def gen_event() -> Generator[tuple[str, ...]]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "climb", "swim", "release", "use"]
    while True:
        player = players[random.randrange(len(players))]
        action = actions[random.randrange(len(actions))]
        lst = [player, action]
        yield tuple(lst)


def consume_event(lst: list[tuple[str, ...]]) -> Generator[tuple[str, ...]]:
    while (lst):
        random_item = random.randrange(len(lst))
        yield lst.pop(random_item)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    events = gen_event()
    for i in range(1000):
        print(
             f"Event {i}: Player {next(events)[0]} did action {next(events)[1]}"
             )
    lst = []
    for i in range(10):
        lst.append(next(events))
    print(f"Built list of 10 events: {lst}")
    for event in consume_event(lst):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {lst}")


if __name__ == "__main__":
    main()
