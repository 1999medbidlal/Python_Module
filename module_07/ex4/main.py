from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard

platform = TournamentPlatform()
dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, "dragon_001",
                        1200)
Wizard = TournamentCard("Ice Wizard", 4, "Rare", 3, 4, "wizard_001", 1150)
print("\n=== DataDeck Tournament Platform ===")
print("\nRegistering Tournament Cards...")
platform.register_card(dragon)
platform.register_card(Wizard)
print(f"\n{dragon.name} (ID: {dragon.card_id})")
interface_dragon = [
    cls.__name__ for cls in dragon.__class__.__mro__
    if cls.__name__ not in ['TournamentCard', 'ABC', 'object']
]
print(f"- Interfaces: {interface_dragon}")
print(f"- Rating: {dragon.rating}")
print(f"- Record: {dragon.wins}-{dragon.losses}")

print(f"\n{Wizard.name} (ID: {Wizard.card_id})")
interface_wizard = [
    cls.__name__ for cls in Wizard.__class__.__mro__
    if cls.__name__ not in ['TournamentCard', 'ABC', 'object']
]
print(f"- Interfaces: {interface_wizard}")
print(f"- Rating: {Wizard.rating}")
print(f"- Record: {Wizard.wins}-{Wizard.losses}")

print("\nCreating tournament match...")
result = platform.create_match(dragon.card_id, Wizard.card_id)
print(f"Match result: {result}")
print("\nTournament Leaderboard:")
board = platform.get_leaderboard()
i = 1
for rank in board:
    print(f"{i}. {rank}")
    i += 1
print("\nPlatform Report:")
print(platform.generate_tournament_report())
print("\n=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")
