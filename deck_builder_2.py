import random


class DeckBuilder:
    def __init__(self, card_data):
        self.card_id = 0
        self.card_data = card_data
        # self.deck = {}
        self.all_cards = {}

    def add_card(self, card_category):
        for i in card_category["value_and_count"]:
            for j in range(i[1]):
                self.card_id += 1
                self.all_cards[self.card_id] = {"card_type": card_category["card_type"]}
                self.all_cards[self.card_id].update({"value": i[0]})
                print(f"Test from deck_builder_2: {self.all_cards[self.card_id]}")

    def shuffle_deck(self, deck):
        shuffled_deck = list(self.all_cards.values())
        random.shuffle(shuffled_deck)

    def get_all_cards(self):
        print(f"all cards test: {self.all_cards}")
        return self.all_cards
