# This component will handle (at least) creating and managing players' hands,
# This will be an improvement over V1 since it can be used for the humand player and
# the computer player, instead of each getting separate decks.

# 1 - Generate a hand of cards - rescoped as return top card, with hands generated in
# main

# 2 - Play card to a pile (discard) - cards discarded never reenter play; there is no
# "resetting" the deck in case of running out of cards. Players play or discard remaining
# cards as the rules allow. The simplest way to accomplish this is to delete the card from
# the game. (might want to log the cards for other purposes?)


class Dealer:
    def __init__(self, shuffled_deck):
        self.deck = shuffled_deck
        self.hand_size = 6

    def deal_cards(self, deck):
        top_card = deck[0]
        deck.pop(0)
        return top_card

    def discard(self, card, hand):
        discarded_card = card
        print(f"card discarded: {discarded_card}")
        hand.remove(card)
        return hand

    def play_card(self, card):
        pass
