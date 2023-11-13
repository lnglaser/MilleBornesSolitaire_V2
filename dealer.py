# This component will handle (at least) creating and managing players' hands,
# This will be an improvement over V1 since it can be used for the humand player and
# the computer player, instead of each getting separate decks.


class Dealer:
    def __init__(self, shuffled_deck):
        self.deck = shuffled_deck
        self.hand_size = 6

    def deal_cards(self, deck):
        for i in range(self.hand_size):
            print("card dealt")
