from .GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class AggressiveStrategy(GameStrategy):

    def __init__(self):
        self.targets_attacked = []
        self.available_targets = ["Enemy Player", "Enemy Dragon", "Enemy Mage"]

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        for card in hand:
            mana_used += card.cost
            if isinstance(card, ArtifactCard):
                continue
            cards_played.append(card.name)
            if isinstance(card, CreatureCard):
                damage_dealt += card.attack

            elif isinstance(card, SpellCard):
                if card.effect_type == "damage":
                    damage_dealt += card.cost
        targets_attacked = self.prioritize_targets(self.available_targets)
        battlefield.append(cards_played)
        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        for target in available_targets:
            if target == "Enemy Player":
                self.targets_attacked.append("Enemy Player")
        return self.targets_attacked
