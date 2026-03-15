#!python3
from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combined(*args, **kwargs) -> tuple:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def mega_fireball(*args, **kwargs) -> int:
        return (base_spell(*args, **kwargs) * multiplier)

    return mega_fireball


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    def new_function(*args, **kwargs) -> str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"

    return new_function


def spell_sequence(spells: list[Callable]) -> Callable:

    def sequence(*args, **kwargs) -> list:
        return [s(*args, **kwargs) for s in spells]

    return sequence


try:
    print("\nTesting spell combiner...")
    comb = spell_combiner(lambda target: f"Fireball hits {target}",
                          lambda target: f"Heals {target}")
    spell = comb('Dragon')
    print("Combined spell result: ", end="")
    print(*spell, sep=", ")
    print("\nTesting power amplifier...")

    def fireball(target: str) -> int:
        return 10

    power = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon')}, Amplified: {power('Dragon')}")
except Exception as e:
    print(f'Error: {e}')
