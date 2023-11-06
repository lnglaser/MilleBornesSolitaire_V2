from card_data import card_data
from deck_builder_2 import DeckBuilder

deck_builder = DeckBuilder(card_data)

# for card_category in card_data:
#     print(card_category)

deck = []
for card_category in card_data:
    new_cards = deck_builder.add_card(card_category=card_category)
    deck.append(new_cards)

print(deck)
