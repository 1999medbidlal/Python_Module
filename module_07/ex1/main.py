from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck
from ex0.CreatureCard import CreatureCard

try:
    spell = SpellCard("Lightning Bolt", 3, "Common", "damage")
    artifact = ArtifactCard("Mana Crystal", 2, "Common", 5,
                            "Permanent: +1 mana per turn")
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    cards = [spell, artifact, creature]
    deck = Deck()
    for card in cards:
        deck.add_card(card)
    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types..")
    print(f"Deck stats: {deck.get_deck_stats()}")
    print("\nDrawing and playing cards:")
    game_state = {
        'player_mana': 6,
        'battlefield': [],
        'spell_log': [],
        'artifacts': [],
        'opponent_health': 15
    }
    while deck.cards:
        deck.shuffle()
        card_pop = deck.draw_card()
        print(
            f"\nDrew: {card_pop.name} "
            f"({card_pop.__class__.__name__.replace('Card','')})"
        )
        print(f"Play result: {card_pop.play(game_state)}")
    print(
        "\nPolymorphism in action: Same interface, different card behaviors!")
except Exception as e:
    print(f"Error: {e}")
