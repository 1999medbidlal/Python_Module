from .Card import Card


class CreatureCard(Card):
    type = "Creature"

    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or not isinstance(health, int):
            raise ValueError("attack and health must be integers")
        elif attack <= 0 or health <= 0:
            raise ValueError("attack and health must be positive numbers > 0")
        else:
            self.attack = attack
            self.health = health

    def play(self, game_state: dict) -> dict:
        game_state['battlefield'].append(self.name)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def attack_target(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }

    def get_card_info(self) -> dict:
        base_info = super().get_card_info()
        base_info['type'] = self.type
        base_info['attack'] = self.attack
        base_info['health'] = self.health
        return base_info
