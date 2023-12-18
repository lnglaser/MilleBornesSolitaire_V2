import random


class AI_player:
    def __init__(self, info):
        self.ai_info = info

    # ai_turn will start with a simple choice between playing miles to it's score or playing a hazard
    # on the player.
    def ai_turn(self):
        # print(self.ai_info)

        # Computer has no miles and empty battle pile - should try to find green light card
        # Go through hand and find green light cards
        # Produce list of tuples with 1) index and 2) card dictionary for all green light cards
        # No miles, empty battle pile
        if self.ai_info["miles"] == 0 and self.ai_info["battle_pile"] == {}:
            print(f"ai_player - Computer's current hand: {self.ai_info['hand']}")
            chosen_cards = []
            current_hand = enumerate(self.ai_info["hand"])
            for index, card in current_hand:
                if card["value"] == "green light":
                    chosen_cards.append((index, card))
            print(f"Green light cards: {chosen_cards}")
            if chosen_cards != []:
                print(f"ai_player - returning choice: {chosen_cards[0]}")
                return chosen_cards[0]
            # No miles, empty battle pile, no green light cards
            elif chosen_cards == []:
                print(f"ai_player - no green lights, current hand:")
                current_hand = enumerate(self.ai_info["hand"])
                for index, card in current_hand:
                    print(index, card)
                    if card["card_type"] == "Hazard":
                        chosen_cards.append((index, card))
                        print(f"ai_player - Hazard cards: {chosen_cards}")
                        if chosen_cards != []:
                            print(f"ai_player - returning choice: {chosen_cards[0]}")
                            return chosen_cards[0]
                        # No miles, no green lights, no hazards
                        elif chosen_cards == []:
                            random_choice = random.randint(0, 6)
                            chosen_cards = self.ai_info["hand"][random_choice]
                            chosen_cards.update({"card_type": "Discard"})
                            print(
                                f"ai_player - no moves, discarding card: {self.ai_info['hand'][random_choice]}"
                            )
                            return chosen_cards

            # If computer has miles and green light -
            # flip between playing hazard on opponent or playing miles on self?

            # If computer has hazard -
            # Look for matching remedy, play hazard, or discard

            # Choosing between playing miles on self and playing hazard on other
        #     random_number = random.randint(1, 2)
        #     print(f"Computer rolled {random_number}")

        #     match random_number:
        #         case 1:
        #             return "Miles"
        #         case 2:
        #             return "Hazard"
        # elif self.ai_info["miles"] == 0 and self.ai_info["battle_pile"] != {}:
        #     print(f"Current battle pile: {self.ai_info['battle_pile']}")
        #     return "Hazard"

    # Delete
    def ai_miles(self):
        print("Computer played miles")

    def ai_hazard(self):
        print("Computer played hazard")

    def ai_remedy(self):
        print("Computer played remedy")

    def ai_safety(self):
        print("Computer played safety")
