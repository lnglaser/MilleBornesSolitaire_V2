# TODO - Try making list of valid moves instead of choosing one, and have computer pick from that

import random


def play_green(self, current_hand, chosen_cards):
    current_hand = enumerate(self.ai_info["hand"])
    for index, card in current_hand:
        print(f"green check: {index, card}")
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
        # Case 1 - No miles, battle pile empty - find green light
        if self.ai_info["miles"] == 0 and self.ai_info["battle_pile"] == {}:
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
