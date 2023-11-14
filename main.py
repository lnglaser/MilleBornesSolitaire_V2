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

print(f"hand test:{dealer.hand_size}")

player_hand = []
opponent_hand = []

# Generate initial hands for player and opponent
for i in range(dealer.hand_size):
    player_hand.append(dealer.deal_cards(deck))
    opponent_hand.append(dealer.deal_cards(deck))

print(f"main - player hand test:\n{player_hand}")
print(f"main - opponent hand test:\n{opponent_hand}")
print(f"new top card:\n{deck[0]}")
