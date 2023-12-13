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
        if self.ai_info["miles"] == 0 and self.ai_info["battle_pile"] == {}:
            print(f"Computer's current hand: {self.ai_info['hand']}")
            green_lights = []
            current_hand = enumerate(self.ai_info["hand"])
            for index, card in current_hand:
                if card["value"] == "green light":
                    green_lights.append((index, card))
            print(f"Green light cards: {green_lights}")
            if green_lights != []:
                print(f"returning choice: {green_lights[0]}")
                return green_lights[0]
            # If computer has miles and green light -
            # flip between playing hazard on opponent or playing miles on self?

            # If computer has hazard -
            # Look for matching remedy, play hazard, or discard

            # Choosing between playing miles on self and playing hazard on other
            random_number = random.randint(1, 2)
            print(f"Computer rolled {random_number}")

            match random_number:
                case 1:
                    return "Miles"
                case 2:
                    return "Hazard"
        elif self.ai_info["miles"] == 0 and self.ai_info["battle_pile"] != {}:
            print(f"Current battle pile: {self.ai_info['battle_pile']}")
            return "Hazard"

    # Delete
    def ai_miles(self):
        print("Computer played miles")

    def ai_hazard(self):
        print("Computer played hazard")

    def ai_remedy(self):
        print("Computer played remedy")

    def ai_safety(self):
        print("Computer played safety")
