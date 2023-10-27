# card_data = [
#     {
#         "card_type": "Mileage",
#         "values": [25, 50, 75, 100, 200],
#         "counts": [10, 10, 10, 12, 4],
#     },
#     {
#         "card_type": "Hazard",
#         "values": ["flat tire", "out of gas", "accident", "speed limit", "red light"],
#         "counts": [3, 3, 3, 5],
#     },
#     {
#         "card_type": "Remedy",
#         "values": ["spare tire", "gas", "repairs", "end of limit", "green light"],
#         "counts": [6, 6, 6, 14],
#     },
#     {
#         "card_type": "Safety",
#         "values": ["puncture-proof", "extra tank", "driving ace", "right of way"],
#         "counts": [1, 1, 1, 1],
#     },
# ]

card_id = 0

deck = {}

for i in range(46):
    card_id += 1
    deck[card_id] = {"card_type": "mileage"}
    if card_id > 0 and card_id <= 10:
        deck[card_id].update({"value": 25})
    elif card_id >= 11 and card_id <= 20:
        deck[card_id].update({"value": 50})
    elif card_id >= 21 and card_id <= 30:
        deck[card_id].update({"value": 75})
    elif card_id >= 31 and card_id <= 42:
        deck[card_id].update({"value": 100})
    elif card_id >= 43 and card_id <= 46:
        deck[card_id].update({"value": 200})

for i in range(14):
    card_id += 1
    deck[card_id] = {"card_type": "hazard"}
    if card_id >= 47 and card_id <= 49:
        deck[card_id].update({"value": "flat tire"})
    if card_id >= 53 and card_id <= 55:
        deck[card_id].update({"value": "out of gas"})
    if card_id >= 56 and card_id <= 58:
        deck[card_id].update({"value": "accident"})
print(card_id, deck[card_id])
