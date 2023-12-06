import random


class AI_player:
    def __init__(self, info):
        self.ai_info = info

    # ai_turn will start with a simple choice between playing miles to it's score or playing a hazard
    # on the player.
    def ai_turn(self):
        print(self.ai_info)
        if self.ai_info["miles"] == 0 and self.ai_info["battle_pile"] == []:
            random_number = random.randint(1, 2)
            print(f"Computer rolled {random_number}")
            match random_number:
                case 1:
                    return "miles"
                case 2:
                    return "hazard"
        elif (
            self.ai_info["miles"] == 0
            and self.ai_info["battle_pile"]["card_type"] == "Hazard"
        ):
            return "hazard"

    def ai_miles(self):
        print("Computer played miles")

    def ai_hazard(self):
        print("Computer played hazard")

    def ai_remedy(self):
        print("Computer played remedy")

    def ai_safety(self):
        print("Computer played safety")
