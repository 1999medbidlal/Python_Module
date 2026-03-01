from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:

    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        available_card = self.factory.create_themed_deck(3).get('deck')
        hand = ""
        for turn_draw in available_card:
            hand += f"{turn_draw.name} ({turn_draw.cost}), "
        battlefield = []
        print("\nSimulating aggressive turn...")
        print(f"Hand: [{hand[:-2]}]")
        actions = self.strategy.execute_turn(available_card, battlefield)
        self.turns_simulated += 1
        self.total_damage += actions['damage_dealt']
        self.cards_created += len(available_card)
        print("\nTurn execution:")
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        print(f"Actions: {actions}")
        return actions

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
