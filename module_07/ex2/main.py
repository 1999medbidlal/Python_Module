from .EliteCard import EliteCard
from .Combatable import Combatable
from .Magical import Magical
from ex0.Card import Card


def get_method(cls):
    method = []
    for name, _ in cls.__dict__.items():
        if not name.startswith('_'):
            method.append(name)
    return method


print("\n=== DataDeck Ability System ===")
print("\nEliteCard capabilities:")
classes = [Card, Combatable, Magical]
for cls in classes:
    print(f"-{cls.__name__}: {get_method(cls)}")
elite_card = EliteCard(' Arcane Warrior', 7, 'Legendary', 5, 3)
print("\nPlaying Arcane Warrior (Elite Card):")
print("\nCombat phase:")
print(f"Attack result: {elite_card.attack('Enemy')}")
print(f"Defense result: {elite_card.defend(2)}")
print("\nMagic phase:")
print(f"Spell cast: {elite_card.cast_spell('Fireball',['Enemy1', 'Enemy2'])}")
print(f"Mana channel: {elite_card.channel_mana(3)}")
print("\nMultiple interface implementation successful!")
