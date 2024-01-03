from os import system
from card_data import card_data
from deck_builder_2 import DeckBuilder
from dealer import Dealer

# from ai_player import AI_player
from ai_player_2 import AI_player
import test_hands as th

deck_builder = DeckBuilder(card_data)


# calls add_card method from deck_builder_2; loops based on number of items in card_data list
for card_category in card_data:
    deck = deck_builder.add_card(card_category)

deck = deck_builder.get_all_cards()
deck = deck_builder.shuffle_deck(deck)
# print(f"Main test:\n{deck}")

# dealer = Dealer(deck)

player_info = {
    "hand": [],
    "score": 0,
    "miles": 0,
    "battle_pile": {"card_type": "Hazard", "value": "flat tire", "match_ID": 1},
    "speed_pile": "",
    "safety_pile": [],
}

opponent_info = {
    "hand": [],
    "score": 0,
    "miles": 0,
    "battle_pile": {},
    "speed_pile": "",
    "safety_pile": [],
}

dealer = Dealer()
opponent = AI_player(opponent_info)
# May need to add variable for a turn indicator to prevent losing a turn in case player makes a mistake, and
# to make coup fourre functions possible

# Need to adjust to allow active player to play or discard drawn card as well as cards in hand

# Generate initial hands for player and opponent - retrieve hand size defined in dealer.py, and uses that
# as range for adding cards to each

for i in range(dealer.hand_size):
    player_info["hand"].append(dealer.deal_cards(deck))
    # opponent_info["hand"].append(dealer.deal_cards(deck))
    opponent_info["hand"] = th.test_hand_has_green


# This section will be for establishing and testing game logic - adjust to remove print
# and input statements once work on frontend begins
def player_turn():
    player_info["hand"].append(dealer.deal_cards(deck))
    print(f"main - Player's current hand:")
    for i in player_info["hand"]:
        print(i)
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

        # Adding miles to your score
        if player_info["hand"][card_number]["card_type"] == "Mileage":
            points_update = dealer.play_miles(
                player_info["hand"][card_number],
                player_info["miles"],
                player_info["score"],
            )
            player_info["miles"] = points_update[0]
            player_info["score"] = points_update[1]

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

        # Playing a remedy on yourself
        elif player_info["hand"][card_number]["card_type"] == "Remedy":
            player_info["battle_pile"] = dealer.play_remedy(
                player_info["hand"][card_number], player_info["battle_pile"]
            )

        # Playing a safety on yourself
        elif player_info["hand"][card_number]["card_type"] == "Safety":
            safety_update = dealer.play_safety(
                player_info["hand"][card_number],
                player_info["safety_pile"],
                player_info["score"],
            )
            player_info["safety_pile"] = safety_update[0]
            player_info["score"] = safety_update[1]

        player_info["hand"] = dealer.discard(
            player_info["hand"][card_number], player_info["hand"]
        )


keep_going = True
while keep_going == True:
    while player_info["miles"] < 1000:
        next_turn = input("Do you want to keep playing? (Y/N): ").lower()
        if next_turn == "n":
            keep_going == False
        system("clear")
        print(f"main - Player's score: {player_info['score']}")
        print(f"main - Player's miles: {player_info['miles']}")
        print(f"main - Player's battle pile: {player_info['battle_pile']}")
        print(f"main - Player's speed pile: {player_info['speed_pile']}")
        print(f"main - Player's safety pile: {player_info['safety_pile']}")
        player_turn()
        opponent_info["hand"].append(dealer.deal_cards(deck))
        print(f"main - Computer's current hand: {opponent_info['hand']}")
        ai_choice = opponent.ai_turn()
        print(f"main - AI choice result: {ai_choice}")
        ai_choice_type = ai_choice[1]["card_type"]
        print(f"main - AI choice card type: {ai_choice_type}")
        print(f"main - card chosen: {opponent_info['hand'][ai_choice[0]]}")
        match ai_choice_type:
            case "Remedy":
                opponent_info["battle_pile"] = dealer.play_remedy(
                    opponent_info["hand"][ai_choice[0]], opponent_info["battle_pile"]
                )
            case "Hazard":
                if opponent_info["hand"][ai_choice[0]]["value"] == "speed limit":
                    player_info["speed_pile"] = dealer.play_hazard(
                        opponent_info["hand"][ai_choice[0]],
                        player_info["speed_pile"],
                    )
                else:
                    player_info["battle_pile"] = dealer.play_hazard(
                        opponent_info["hand"][ai_choice[0]],
                        player_info["battle_pile"],
                    )
            case "Discard":
                pass
        opponent_info["hand"] = dealer.discard(
            opponent_info["hand"][ai_choice[0]], opponent_info["hand"]
        )
        # opponent_info["battle_pile"] = dealer.play_remedy(
        #     opponent_info["hand"][ai_choice[0]], opponent_info["battle_pile"]
        # )
        print(f"main - Computer battle pile: {opponent_info['battle_pile']}")
