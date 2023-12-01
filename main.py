from card_data import card_data
from deck_builder_2 import DeckBuilder
from dealer import Dealer
from ai_player import AI_player

deck_builder = DeckBuilder(card_data)


# calls add_card method from deck_builder_2; loops based on number of items in card_data list
for card_category in card_data:
    deck = deck_builder.add_card(card_category)

deck = deck_builder.get_all_cards()
deck = deck_builder.shuffle_deck(deck)
# print(f"Main test:\n{deck}")

dealer = Dealer(deck)

opponent = AI_player

player_info = {
    "hand": [],
    "score": 0,
    "battle_pile": {"card_type": "Hazard", "value": "flat tire", "match_ID": 1},
    "speed_pile": "",
    "safety_pile": [],
}

opponent_info = {
    "hand": [],
    "score": 0,
    "battle_pile": {},
    "speed_pile": "",
    "safety_pile": [],
}

# May need to add variable for a turn indicator to prevent losing a turn in case player makes a mistake, and
# to make coup fourre functions possible

# Need to adjust to allow active player to play or discard drawn card as well as cards in hand

# Generate initial hands for player and opponent - retrieve hand size defined in dealer.py, and uses that
# as range for adding cards to each

for i in range(dealer.hand_size):
    player_info["hand"].append(dealer.deal_cards(deck))
    opponent_info["hand"].append(dealer.deal_cards(deck))

# Testing print statements
# print(f"Main - player hand:\n{player['hand']}")
print(f"Main - opponent hand:\n{opponent_info['hand']}")
print(f"new top card:\n{deck[0]}")


# This section will be for establishing and testing game logic - adjust to remove print
# and input statements once work on frontend begins
def player_turn():
    player_info["hand"].append(dealer.deal_cards(deck))
    print(f"Main - player hand:\n{player_info['hand']}")
    player_move = input("What would you like to do? (play/discard): ")

    # Discard a card - calls discard and deal_cards methods from dealer.py
    if player_move == "discard":
        card_number = int(input("Which card do you want to discard? (0-6)"))
        player_info["hand"] = dealer.discard(
            player_info["hand"][card_number], player_info["hand"]
        )

    # Play a card - checks which card player wants to play
    elif player_move == "play":
        card_number = int(input("Which card do you want to play? (0-6)"))

        # Adding to your score
        if player_info["hand"][card_number]["card_type"] == "Mileage":
            player_info["score"] = dealer.play_miles(
                player_info["hand"][card_number], player_info["score"]
            )
            player_info["hand"] = dealer.discard(
                player_info["hand"][card_number], player_info["hand"]
            )
            player_info["hand"].append(dealer.deal_cards(deck))
            print(f"Updated score: {player_info['score']}")

        # Playing a hazard on opponent
        elif player_info["hand"][card_number]["card_type"] == "Hazard":
            if player_info["hand"][card_number]["value"] == "speed limit":
                opponent_info["speed_pile"] = dealer.play_hazard(
                    player_info["hand"][card_number],
                    opponent_info["speed_pile"],
                )
            else:
                opponent_info["battle_pile"] = dealer.play_hazard(
                    player_info["hand"][card_number],
                    opponent_info["battle_pile"],
                )
            print(f"Opponent's battle pile: {opponent_info['battle_pile']}")
            print(f"Opponent's speed pile: {opponent_info['speed_pile']}")
            player_info["hand"] = dealer.discard(
                player_info["hand"][card_number], player_info["hand"]
            )

        # Playing a remedy on yourself
        elif player_info["hand"][card_number]["card_type"] == "Remedy":
            print(f"Player's battle pile: {player_info['battle_pile']}")
            player_info["battle_pile"] = dealer.play_remedy(
                player_info["hand"][card_number], player_info["battle_pile"]
            )
            print(print(f"Player's new battle pile: {player_info['battle_pile']}"))
            print(f"Play remedy - Player's battle pile: {player_info['battle_pile']}")
            player_info["hand"] = dealer.discard(
                player_info["hand"][card_number], player_info["hand"]
            )

        # Playing a safety on yourself
        elif player_info["hand"][card_number]["card_type"] == "Safety":
            player_info["safety_pile"] = dealer.play_safety(
                player_info["hand"][card_number], player_info["safety_pile"]
            )
            print(f"Player's safety pile: {player_info['safety_pile']}")

    print(f"new player hand:\n{player_info['hand']}")


player_turn()
