from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]
                    ) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda elem: elem["power"], reverse=True)


def power_filter(mages: list[dict[str, Any]], min_power: int
                 ) -> list[dict[str, Any]]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda style: f"* {style} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    return {'max_power': max(mages, key=lambda elem: elem["power"]),
            'min_power': min(mages, key=lambda elem: elem["power"]),
            'avg_power': round(sum(m["power"] for m in mages) / len(mages), 2)}


if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts = [{'name': "Crystal Orb", 'power': 85, 'type': "crystal"},
                 {'name': "Fire Staff", 'power': 92, 'type': "fire"}]
    artifacts = artifact_sorter(artifacts)
    print(f"{artifacts[0]["name"]} ({artifacts[0]["power"]} power)"
          f" comes before {artifacts[1]["name"]} "
          f"({artifacts[1]["power"]} power)")
    print("Testing spell transformer...")
    spells = ["fireball", "heal", "shield"]
    spells = spell_transformer(spells)
    print(*spells)
    print("Testing mage stats with artifact list...")
    print(mage_stats(artifacts))
