from .TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self):
        self.cards = {}
        self.marches_player = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        if card1.attacks >= card2.attacks:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1
        winner.update_wins(1)
        loser.update_losses(1)
        winner.rating += 16
        loser.rating -= 16
        self.marches_player += 1
        return {
            'winner': winner.card_id,
            'loser': loser.card_id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

    def get_leaderboard(self) -> list:
        all_cards = list(self.cards.values())
        leaderboard = []
        while all_cards:
            max_card = all_cards[0]
            for card in all_cards:
                if card.rating > max_card.rating:
                    max_card = card
            leaderboard.append(f"{max_card.name} - Rating: {max_card.rating} "
                               f"({max_card.wins}-{max_card.losses})")
            all_cards.remove(max_card)
        return leaderboard

    def generate_tournament_report(self) -> dict:
        all_card = self.cards.values()
        total_card = len(all_card)
        value_rating = 0
        for card in all_card:
            value_rating += card.rating
        return {
            'total_cards': total_card,
            'matches_played': self.marches_player,
            'avg_rating': f"{value_rating / total_card:.0f}",
            'platform_status': 'active'
        }
