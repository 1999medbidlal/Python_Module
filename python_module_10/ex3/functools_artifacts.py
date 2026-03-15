#!python3
from functools import reduce, lru_cache, singledispatch, partial
from typing import Callable, Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == 'add':
        res = reduce(operator.add, spells)
    elif operation == 'multiply':
        res = reduce(operator.mul, spells)
    elif operation == 'min':
        res = reduce(min, spells)
    elif operation == 'max':
        res = reduce(max, spells)
    else:
        res = 0
    return res


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchant = partial(base_enchantment, power=50, element='fire')
    ice_enchant = partial(base_enchantment, power=50, element='ice')
    lightning_enchant = partial(base_enchantment,
                                power=50,
                                element='lightning')
    return {
        'fire_enchant': fire_enchant,
        'ice_enchant': ice_enchant,
        'lightning_enchant': lightning_enchant
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:

    @singledispatch
    def spell(test: Any) -> str:
        return "Unknown spell type"

    @spell.register(int)
    def _(power: int) -> str:
        return f"Damage spell with {power} power"

    @spell.register(str)
    def _(element: str) -> str:
        return f"Enchantment: {element}"

    @spell.register(list)
    def _(cast: list) -> str:
        return (f"Casts: {cast}")

    return spell


try:
    powers = [10, 20, 30, 40]
    sum_spell = spell_reducer(powers, "add")
    prod_spell = spell_reducer(powers, "multiply")
    max_spell = spell_reducer(powers, "max")
    print("\nTesting spell reducer...")
    print(f"Sum: {sum_spell}")
    print(f"Product: {prod_spell}")
    print(f"Max: {max_spell}")
    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
except Exception as e:
    print(f"Erorr: {e}")
