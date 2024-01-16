# TODO - Try making list of valid moves instead of choosing one, and have computer pick from that
# TODO - Make method just for identifying card types in hand?

import random

types_in_hand = {"Mileage": False, "Hazard": False, "Remedy": False, "Safety": False}


def check_hand_types(self, current_hand):
    current_hand = enumerate(self.ai_info["hand"])
    for index, card in current_hand:
        print(f"Checking card type of {index, card}")
        if card["card_type"] == "Mileage":
            types_in_hand["Mileage"] = True
        elif card["card_type"] == "Hazard":
            types_in_hand["Hazard"] = True
        elif card["card_type"] == "Remedy":
            types_in_hand["Remedy"] = True
        elif card["card_type"] == "Safety":
            types_in_hand["Safety"] = True
        return types_in_hand


def play_green(self, current_hand, chosen_cards):
    current_hand = enumerate(self.ai_info["hand"])
    for index, card in current_hand:
        if card["value"] == "green light":
            chosen_cards.append((index, card))
    print(f"Green light cards: {chosen_cards}")
    self.card = chosen_cards[0]
    return self.card


def play_hazard(self, current_hand, chosen_cards):
    current_hand = enumerate(self.ai_info["hand"])
    for index, card in current_hand:
        if card["card_type"] == "Hazard":
            chosen_cards.append((index, card))
    print(f"Hazard cards: {chosen_cards}")
    if chosen_cards == []:
        return
    else:
        self.card = chosen_cards[0]
        return self.card


def play_miles(self, current_hand, chosen_cards):
    current_hand = enumerate(self.ai_info["hand"])
    for index, card in current_hand:
        if card["card_type"] == "Mileage":
            chosen_cards.append((index, card))
    print(f"Mileage cards: {chosen_cards}")
    if chosen_cards == []:
        return
    else:
        self.card = chosen_cards[0]
        return self.card


class AI_player:
    def __init__(self, info):
        self.ai_info = info
        self.card = ()

    def ai_turn(self):
        # Enumerate current hand here instead of in each method above (update - hand not passing in?):
        print(f"ai_player_2 - Computer's current hand: ")
        current_hand = enumerate(self.ai_info["hand"])
        for index, card in current_hand:
            print(index, card)
        chosen_cards = []
        card = ()
        types_in_hand = check_hand_types(self, current_hand)
        # Move 1 - Identify cases to play a green light:
        # a) No miles, blank battle pile
        # b) Battle pile is a non-green light remedy
        print(types_in_hand)
        if (self.ai_info["miles"] == 0 and self.ai_info["battle_pile"] == {}) or (
            self.ai_info["battle_pile"]["card_type"] == "Remedy"
            and self.ai_info["battle_pile"]["value"] != "green light"
        ):
            card = play_green(self, current_hand, chosen_cards)
        # Case 2 - No miles, battle pile empty, no green lights - play hazard
        elif (
            self.ai_info["miles"] == 0
            and self.ai_info["battle_pile"] == {}
            and card == ()
        ):
            card = play_hazard(self, current_hand, chosen_cards)
        # Case 3 - No miles, battle pile green light - play miles
        if card == ():
            card = play_miles(self, current_hand, chosen_cards)
        return card

        # Case 3 - No miles, battle pile green light - play miles

        # Case 4 - No miles, battle pile green light, no mile cards - play hazard
