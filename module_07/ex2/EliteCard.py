from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name, cost, rarity, attack, block):
        super().__init__(name, cost, rarity)
        self.atack = attack
        self.block = block

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Elite Card played'
        }

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.atack,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        if self.block - incoming_damage <= 0:
            alive = False
        else:
            alive = True
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': self.block,
            'still_alive': alive
        }

    def get_combat_stats(self) -> dict:
        {
            'card_played': self.name,
            'attack': self.atack,
            'defense': self.block
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        self.mana_used = 4
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.mana_used
        }

    def channel_mana(self, amount: int) -> dict:
        return {'channeled': amount, 'total_mana': amount + self.mana_used}

    def get_magic_stats(self) -> dict:
        return {'caster': self.name, 'mana': self.mana_used}
