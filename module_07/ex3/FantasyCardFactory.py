from .CardFactory import CardFactory
from ex0.Card import Card


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.supports_types = {'creatures': {}, 'spells': {}, 'artifacts': {}}
        self.all_cards = []

    def register_card(self, card_type: str, name: str, card: Card) -> None:
        if card_type in self.supports_types:
            self.supports_types[card_type][name] = card
            self.all_cards.append(card)
        else:
            raise KeyError(f"the key {card_type} isn't in supports_types")

    def create_creature(self, name_or_power) -> Card:
        if name_or_power in self.supports_types['creatures']:
            return self.supports_types['creatures'][name_or_power]
        else:
            raise ValueError("Unknown creature")

    def create_spell(self, name_or_power) -> Card:
        if name_or_power in self.supports_types['spells']:
            return self.supports_types['spells'][name_or_power]
        else:
            raise ValueError("Unknown creature")

    def create_artifact(self, name_or_power) -> Card:
        if name_or_power in self.supports_types['artifacts']:
            return self.supports_types['artifacts'][name_or_power]
        else:
            raise ValueError("Unknown creature")

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        creatures = list(self.supports_types['creatures'].keys())
        spells = list(self.supports_types['spells'].keys())
        artifacts = list(self.supports_types['artifacts'].keys())

        i = 0
        while len(deck) < size:

            if i < len(creatures):
                deck.append(self.create_creature(creatures[i]))

            if len(deck) >= size:
                break

            if i < len(spells):
                deck.append(self.create_spell(spells[i]))

            if len(deck) >= size:
                break

            if i < len(artifacts):
                deck.append(self.create_artifact(artifacts[i]))
            i += 1
        return {'deck': deck, 'size': size}

    def get_supported_types(self) -> dict:
        supported = {}
        values = []
        for type in self.supports_types:
            for name in self.supports_types[type]:
                values.append(name)
            supported[type] = values
            values = []
        return supported
