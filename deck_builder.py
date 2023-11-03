import random

card_data = [
    {
        "card_type": "Mileage",
        "value_and_count": [
            (25, 10),
            (50, 10),
            (75, 10),
            (100, 12),
            (200, 4),
        ],
    },
    {
        "card_type": "Hazard",
        "value_and_count": [
            ("flat tire", 3),
            ("out of gas", 3),
            ("accident", 3),
            ("speed limit", 4),
            ("red light", 5),
        ],
    },
    {
        "card_type": "Remedy",
        "value_and_count": [
            ("spare tire", 6),
            ("gas", 6),
            ("repairs", 6),
            ("end of limit", 6),
            ("green light", 14),
        ],
    },
    {
        "card_type": "Safety",
        "value_and_count": [
            ("puncture-proof", 1),
            ("extra tank", 1),
            ("driving ace", 1),
            ("right of way", 1),
        ],
    },
]

deck = {}
card_id = 0


def add_card(card_category):
    for i in card_category["value_and_count"]:
        for j in range(i[1]):
            global card_id
            card_id += 1
            deck[card_id] = {"card_type": card_category["card_type"]}
            deck[card_id].update({"value": i[0]})


for category in card_data:
    add_card(category)

for card in deck:
    print(card, deck[card])

shuffled_deck = list(deck.values())
random.shuffle(shuffled_deck)

for card in shuffled_deck:
    print(card["card_type"], card["value"])

for card in range(len(shuffled_deck)):
    print(card, shuffled_deck[card])
