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
        # Produce list of tuples with "green light" and index that matches card position in hand
        if self.ai_info["miles"] == 0 and self.ai_info["battle_pile"] == {}:
            print(f"Computer's current hand: {self.ai_info['hand']}")
            hand_search = [
                ((card.get("value", None)), self.ai_info["hand"].index(card))
                for card in self.ai_info["hand"]
                if card["value"] == "green light"
            ]

            print(f"Computer remedy cards: {hand_search}")
            # Choosing between playing miles on self and playing hazard on other
            random_number = random.randint(1, 2)
            print(f"Computer rolled {random_number}")
            match random_number:
                case 1:
                    return "miles"
                case 2:
                    return "hazard"
        elif self.ai_info["miles"] == 0 and self.ai_info["battle_pile"] != {}:
            print(f"Current battle pile: {self.ai_info['battle_pile']}")
            return "hazard"

    def ai_miles(self):
        print("Computer played miles")

    def ai_hazard(self):
        print("Computer played hazard")

    def ai_remedy(self):
        print("Computer played remedy")

    def ai_safety(self):
        print("Computer played safety")
