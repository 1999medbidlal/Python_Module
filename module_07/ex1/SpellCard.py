from ex0.Card import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        game_state['spell_log'].append(self.name)
        game_state['opponent_health'] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f"Deal {self.cost} {self.effect_type} to target"
        }

    def resolve_effect(self, targets: list) -> dict:
        return {'targets': targets}
