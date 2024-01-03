import random


class AI_player:
    def __init__(self, info):
        self.ai_info = info
        self.card = ()

    def ai_turn(self):
        # Case 1 - No miles, battle pile empty - find green light
        if self.ai_info["miles"] == 0 and self.ai_info["battle_pile"] == {}:
            print(f"ai_player_2 - Computer's current hand: {self.ai_info['hand']}")
            chosen_cards = []
            current_hand = enumerate(self.ai_info["hand"])
            for index, card in current_hand:
                if card["value"] == "green light":
                    chosen_cards.append((index, card))
            print(f"Green light cards: {chosen_cards}")
        self.card = chosen_cards[0]
        return self.card

    def play_green(self):
        print(f"ai_player_2 - Computer's current hand: {self.ai_info['hand']}")
        chosen_cards = []
        current_hand = enumerate(self.ai_info["hand"])
        for index, card in current_hand:
            if card["value"] == "green light":
                chosen_cards.append((index, card))
        print(f"Green light cards: {chosen_cards}")
        self.card = chosen_cards[0]
        return self.card

    # Case 2 - No miles, battle pile empty, no green lights - play hazard

    # Case 3 - No miles, battle pile green light - play miles

    # Case 4 - No miles, battle pile green light, no mile cards - play hazard
