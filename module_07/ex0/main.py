from .CreatureCard import CreatureCard
try:
    card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")
    print("\nCreatureCard Info:")
    print(card.get_card_info())
    player_mana = 6
    print(f"\nPlaying Fire Dragon with {player_mana} mana available:")
    print(f"Playable: {card.is_playable(player_mana)}")
    game_state = {
        'player_mana': 6,
        'battlefield': [],
    }
    print(f"Play result: {card.play(game_state)}")
    target = "Goblin Warrior"
    print(f"\n{card.name} attacks {target}:")
    print(f"Attack result: {card.attack_target(target)}")
    player_mana = 3
    print(f"\nTesting insufficient mana ({player_mana} available):")
    print(f"Playable: {card.is_playable(player_mana)}")
    print("\nAbstract pattern successfully demonstrated!")
except ValueError as e:
    print(e)
