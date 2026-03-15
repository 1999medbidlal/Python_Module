#!python3
from typing import Callable
import time
from functools import wraps


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        value = end - start
        print(f"Spell completed in {value:.3f} seconds")
        return res

    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            power = kwargs.get('power', args[-1])
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):
            i = 1
            while i <= max_attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print(
                        f"Spell failed, retrying... (attempt "
                        f"{i}/{max_attempts})"
                    )
                i += 1
            return "Spell casting failed after max_attempts attempts"

        return wrapper

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        i = 0
        j = 0
        for c in name:
            if ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')
                    or c == ' '):
                j += 1
            else:
                i += 1
        if i > 0:
            return False
        elif j < 3:
            return False
        else:
            return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


try:

    @spell_timer
    def fireball() -> str:
        return "Result: Fireball cast!"

    spell = fireball()
    print("\nTesting spell timer...")
    print(spell)
    print("\nTesting MageGuild...")
    mage = MageGuild()
    print(mage.validate_mage_name('ahmed'))
    print(mage.validate_mage_name('ah12'))
    print(mage.cast_spell('Lightning', 15))
    print(mage.cast_spell('fireball', 5))
except Exception as e:
    print(f"Error: {e}")
