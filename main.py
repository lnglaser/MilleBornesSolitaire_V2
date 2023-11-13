from card_data import card_data
from deck_builder_2 import DeckBuilder
from dealer import Dealer

deck_builder = DeckBuilder(card_data)


# calls add_card method from deck_builder_2; loops based on number of items in card_data list
for card_category in card_data:
    deck = deck_builder.add_card(card_category)

deck = deck_builder.get_all_cards()
deck = deck_builder.shuffle_deck(deck)
print(f"Main test:\n{deck}")

dealer = Dealer(deck)
hand = dealer.deal_cards(deck)
