#!python3
def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined() -> tuple:
        return (spell1(), spell2())
    return combined
    

def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def mega_fireball(target:str) -> int:
        return (base_spell(target) * multiplier)
    return mega_fireball

def conditional_caster(condition: callable, spell: callable) -> callable:
    pass

def spell_sequence(spells: list[callable]) -> callable:
    pass
try:
    print("\nTesting spell combiner...")
    s = spell_combiner(lambda : "Fireball hits Dragon", lambda: "Heals Dragon")
    spell = s()
    print(f"Combined spell result: " + ", ".join(spell))
    print("\nTesting power amplifier...")
    def fireball(target:str)-> int:
        return 10
    power = power_amplifier(fireball, 3)
    print(f"Original: {fireball('fireball')}, Amplified: {power('Dragon')}")
except Exception as e :
    print(f'Error: {e}')
