from .FantasyCardFactory import FantasyCardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine

cards = {
    'creatures': {
        'dragon': CreatureCard("Fire Dragon", 5, "Legendary", 7, 5),
        'goblin': CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
    },
    'spells': {
        'fireball': SpellCard("Lightning Bolt", 3, "Uncommon", "damage")
    },
    'artifacts': {
        'mana_ring':
        ArtifactCard("Mana Crystal", 2, "Common", 5,
                     "Permanent: +1 mana per turn")
    }
}
factory = FantasyCardFactory()
strategy = AggressiveStrategy()
engine = GameEngine()

try:
    for type in cards:
        for name, card in cards[type].items():
            factory.register_card(type, name, card)
    print("\n=== DataDeck Game Engine ===")
    print("\nConfiguring Fantasy Card Game...")
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")
    engine.configure_engine(factory, strategy)
    engine.simulate_turn()
    print("\nGame Report:")
    print(engine.get_engine_status())
    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
except Exception as e:
    print(f"Error:{e}")
    exit(1)
