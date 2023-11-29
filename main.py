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

player = {
    "hand": [],
    "score": 0,
    "battle_pile": {"card_type": "Hazard", "value": "flat tire"},
    "speed_pile": "",
    "safety_pile": [],
}

opponent = {
    "hand": [],
    "score": 0,
    "battle_pile": {},
    "speed_pile": "",
    "safety_pile": [],
}

# Generate initial hands for player and opponent - retrieve hand size defined in dealer.py, and uses that
# as range for adding cards to each

for i in range(dealer.hand_size):
    player["hand"].append(dealer.deal_cards(deck))
    opponent["hand"].append(dealer.deal_cards(deck))

# Testing print statements
print(f"Main - player hand:\n{player['hand']}")
print(f"Main - opponent hand:\n{opponent['hand']}")
print(f"new top card:\n{deck[0]}")

# This section will be for establishing and testing game logic - remove/adjust once work on frontend begins
player_move = input("What would you like to do? (play/discard): ")

if player_move == "discard":
    card_number = int(input("Which card do you want to discard? (0-5)"))
    player["hand"] = dealer.discard(player["hand"][card_number], player["hand"])
    player["hand"].append(dealer.deal_cards(deck))
elif player_move == "play":
    card_number = int(input("Which card do you want to play? (0-5)"))
    if player["hand"][card_number]["card_type"] == "Mileage":
        player["score"] = dealer.play_miles(
            player["hand"][card_number], player["score"]
        )
        player["hand"] = dealer.discard(player["hand"][card_number], player["hand"])
        player["hand"].append(dealer.deal_cards(deck))
        print(f"Updated score: {player['score']}")
    elif player["hand"][card_number]["card_type"] == "Hazard":
        opponent["battle_pile"] = dealer.play_hazard(
            player["hand"][card_number], opponent["battle_pile"]
        )
        print(f"Opponent's battle pile: {opponent['battle_pile']}")
    elif player["hand"][card_number]["card_type"] == "Remedy":
        player["battle_pile"] = dealer.play_remedy(
            player["hand"][card_number], player["battle_pile"]
        )
        print(f"Play remedy - Player's battle pile: {player['battle_pile']}")
print(f"new player hand:\n{player['hand']}")
