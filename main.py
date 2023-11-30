from card_data import card_data
from deck_builder_2 import DeckBuilder
from dealer import Dealer

deck_builder = DeckBuilder(card_data)


# calls add_card method from deck_builder_2; loops based on number of items in card_data list
for card_category in card_data:
    deck = deck_builder.add_card(card_category)

deck = deck_builder.get_all_cards()
deck = deck_builder.shuffle_deck(deck)
# print(f"Main test:\n{deck}")

dealer = Dealer(deck)

player = {
    "hand": [],
    "score": 0,
    "battle_pile": {"card_type": "Hazard", "value": "flat tire", "match_ID": 1},
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

# May need to add variable for a turn indicator to prevent losing a turn in case player makes a mistake

# Generate initial hands for player and opponent - retrieve hand size defined in dealer.py, and uses that
# as range for adding cards to each

for i in range(dealer.hand_size):
    player["hand"].append(dealer.deal_cards(deck))
    opponent["hand"].append(dealer.deal_cards(deck))

# Testing print statements
print(f"Main - player hand:\n{player['hand']}")
print(f"Main - opponent hand:\n{opponent['hand']}")
print(f"new top card:\n{deck[0]}")

# This section will be for establishing and testing game logic - adjust to remove print
# and input statements once work on frontend begins
player_move = input("What would you like to do? (play/discard): ")

# Discard a card
if player_move == "discard":
    card_number = int(input("Which card do you want to discard? (0-5)"))
    player["hand"] = dealer.discard(player["hand"][card_number], player["hand"])
    player["hand"].append(dealer.deal_cards(deck))

# Play a card
elif player_move == "play":
    card_number = int(input("Which card do you want to play? (0-5)"))

    # Adding to your score
    if player["hand"][card_number]["card_type"] == "Mileage":
        player["score"] = dealer.play_miles(
            player["hand"][card_number], player["score"]
        )
        player["hand"] = dealer.discard(player["hand"][card_number], player["hand"])
        player["hand"].append(dealer.deal_cards(deck))
        print(f"Updated score: {player['score']}")

    # Playing a hazard on opponent
    elif player["hand"][card_number]["card_type"] == "Hazard":
        if player["hand"][card_number]["value"] == "speed limit":
            opponent["speed_pile"] = dealer.play_hazard(
                player["hand"][card_number],
                opponent["battle_pile"],
                opponent["speed_pile"],
            )
        else:
            opponent["battle_pile"] = dealer.play_hazard(
                player["hand"][card_number],
                opponent["battle_pile"],
                opponent["speed_pile"],
            )

        print(f"Opponent's battle pile: {opponent['battle_pile']}")
        print(f"Opponent's speed pile: {opponent['speed_pile']}")
        player["hand"] = dealer.discard(player["hand"][card_number], player["hand"])
        player["hand"].append(dealer.deal_cards(deck))

    # Playing a remedy on yourself
    elif player["hand"][card_number]["card_type"] == "Remedy":
        print(f"Player's battle pile: {player['battle_pile']}")
        player["battle_pile"] = dealer.play_remedy(
            player["hand"][card_number], player["battle_pile"]
        )
        print(print(f"Player's new battle pile: {player['battle_pile']}"))
        print(f"Play remedy - Player's battle pile: {player['battle_pile']}")
        player["hand"] = dealer.discard(player["hand"][card_number], player["hand"])
        player["hand"].append(dealer.deal_cards(deck))

print(f"new player hand:\n{player['hand']}")
