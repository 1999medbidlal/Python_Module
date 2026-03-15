#!python3
from typing import Callable, Any


def mage_counter() -> Callable:
    x = 0

    def calls():
        nonlocal x
        x += 1
        return x

    return calls


def spell_accumulator(initial_power: int) -> Callable:

    def accumulates_power(power: int) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power

    return accumulates_power


def enchantment_factory(enchantment_type: str) -> Callable:

    def name_factory(name: str) -> str:
        return f'{enchantment_type} {name}'

    return name_factory


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        valid = False
        for keys in memory:
            if keys == key:
                valid = True
        if valid:
            return memory[key]
        else:
            return "Memory not found"

    return {'store': store, 'recall': recall}


try:
    print("\nTesting mage counter...")
    counter = mage_counter()
    i = 1
    while i < 4:
        print(f"Call {i}: {counter()}")
        i += 1
    print("\nTesting enchantment factory...")
    enchantment1 = enchantment_factory('Flaming')
    enchantment2 = enchantment_factory('Frozen')
    print(enchantment1('Sword'))
    print(enchantment2('Shield'))
except Exception as e:
    print(f"Erorr: {e}")
