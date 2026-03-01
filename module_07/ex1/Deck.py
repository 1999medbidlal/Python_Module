from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
import random


class Deck:

    def __init__(self):
        self.cards = []
        self.total_cards = 0
        self.spells = 0
        self.artifacts = 0
        self.creatures = 0
        self.costs = 0

    def add_card(self, card: Card) -> None:
        self.total_cards += 1
        self.cards.append(card)
        self.costs += card.cost
        if isinstance(card, SpellCard):
            self.spells += 1
        elif isinstance(card, ArtifactCard):
            self.artifacts += 1
        elif isinstance(card, CreatureCard):
            self.creatures += 1

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                self.total_cards -= 1
                self.costs -= card.cost
                if isinstance(card, SpellCard):
                    self.spells -= 1
                elif isinstance(card, ArtifactCard):
                    self.artifacts -= 1
                elif isinstance(card, CreatureCard):
                    self.creatures -= 1
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError('Cannot draw from an empty deck')
        card = self.cards.pop(0)
        self.total_cards -= 1
        self.costs -= card.cost
        if isinstance(card, SpellCard):
            self.spells -= 1
        elif isinstance(card, ArtifactCard):
            self.artifacts -= 1
        elif isinstance(card, CreatureCard):
            self.creatures -= 1
        return card

    def get_deck_stats(self) -> dict:
        if self.total_cards == 0:
            avg_cost = 0
        else:
            avg_cost = float(f"{self.costs / self.total_cards:.1f}")
        return {
            'total_cards': self.total_cards,
            'creatures': self.creatures,
            'spells': self.spells,
            'artifacts': self.artifacts,
            'avg_cost': avg_cost
        }
