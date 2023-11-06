import random


class DeckBuilder:
    def __init__(self, card_data):
        self.card_id = 0
        self.card_data = card_data
        self.deck = {}

        def add_card(self, card_category):
            for i in card_category["value_and_count"]:
                for j in range(i[1]):
                    self.card_id += 1
                    self.deck[self.card_id] = {"card_type": card_category["card_type"]}
                    self.deck[self.card_id].update({"value": i[0]})

        def shuffle_deck(self, deck):
            shuffled_deck = list(deck.values())
            random.shuffle(shuffled_deck)
