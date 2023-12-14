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
    def __init__(self):
        # self.deck = shuffled_deck
        self.hand_size = 6

    # Returns top card in deck
    def deal_cards(self, deck):
        top_card = deck[0]
        deck.pop(0)
        return top_card

    # Removes selected card
    def discard(self, card, hand):
        discarded_card = card
        print(f"dealer - card discarded: {discarded_card}")
        hand.remove(card)
        return hand

    # Add mileage value to score:
    def play_miles(self, card, miles, score):
        points = int(card.get("value"))
        score += points
        miles += points
        return miles, score

    def play_hazard(self, card, pile):
        if card["value"] == "speed limit" and pile != "speed limit":
            pile = "speed limit"
            # return speed_pile
        else:
            pile.update(card)
        return pile

    # Add nested conditions for various hazards and remedies?
    # To reduce individual conditions, maybe add KV pair to cards that match
    # between hazards and remedies? (maybe add extra safety card to match up
    # evenly)
    # Need to add error case to prevent end of limit card being played to battle pile?
    def play_remedy(self, card, pile):
        if card["value"] == "end of limit" and pile == "speed limit":
            pile = "end of limit"
        elif pile == {} and card["value"] == "green light":
            pile.update(card)
            print(f"dealer - battle pile: {pile}")
        elif pile["card_type"] == "Hazard" and pile["match_ID"] == card["match_ID"]:
            pile.update(card)
            print(f"dealer - battle pile: {pile}")
        return pile

    def play_safety(self, card, pile, score):
        pile.append(card)
        score += 100
        return pile, score
