from card_data import card_data
from deck_builder_2 import DeckBuilder

deck_builder = DeckBuilder(card_data)

# for card_category in card_data:
#     print(card_category)

# deck = []
# for card_category in card_data:
#     print(f"card category: {card_category}")
#     new_cards = deck_builder.add_card(card_category=card_category)
#     print("main test - new cards")
#     print(new_cards)
# deck.append(new_cards)

for card_category in card_data:
    deck = deck_builder.add_card(card_category)
# deck = deck_builder.add_card(card_data[0])
deck = deck_builder.get_all_cards()
print(deck)
