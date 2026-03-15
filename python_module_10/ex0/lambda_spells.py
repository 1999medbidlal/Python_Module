#!python3
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    result = sorted(artifacts,
                    key=lambda artifact: artifact["power"],
                    reverse=True)
    return result


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered = filter(lambda mage: mage["power"] >= min_power, mages)
    return list(filtered)


def spell_transformer(spells: list[str]) -> list[str]:
    result = map(lambda s: f"* {s} *", spells)
    return list(result)


def mage_stats(mages: list[dict]) -> dict:
    values_power = list(map((lambda m: m['power']), mages))
    static = {
        'max_power': max(values_power),
        'min_power': min(values_power),
        'avg_power': round(sum(values_power) / len(values_power), 2)
    }
    return static


try:
    artifacts = [
        {
            "name": "Crystal Orb",
            "power": 85,
            "type": "armor"
        },
        {
            "name": "Fire Staff",
            "power": 92,
            "type": "focus"
        },
    ]
    spells = ["fireball", "heal", "shield"]
    print("\nTesting artifact sorter...")
    res = artifact_sorter(artifacts)
    total = len(res)
    i = 0
    while i < total - 1:
        c = i
        n = i + 1
        print(f"{res[c]['name']} ({res[c]['power']} power) ", end="")
        if i < total - 1:
            print("comes before", end="")
        print(f" {res[n]['name']} ({res[n]['power']} power)")
        if i < total - 2:
            print("comes before ", end="")
        i += 2
    print("\nTesting spell transformer...")
    spell = spell_transformer(spells)
    for s in spell:
        print(s, end=" ")
    print()
except Exception as e:
    print(f"Error: {e}")
