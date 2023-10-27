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

# deck = []
# for i in card_data[0]["values"]:
#     print(i)

# for number_of_cards in card_data[0]["counts"]:
#     card_number = 0
#     for count in range(number_of_cards):
#         print("Count: ", count)
#         card = {
#             "card_type": card_data[0]["card_type"],
#             "value": card_data[0]["values"][0],
#         }
#         card_number += 1
#         print(f"{card_number}: {card}")

# for i in card_data[0]["counts"]:
#     current_count = i
#     print(current_count)
#     for j in range(0, current_count):
#         card = {
#             "card_type": card_data[0]["card_type"],
#             "value": card_data[0]["values"],
#         }
#         print(card)


card_id = 0

deck = {}

for i in range(46):
    card_id += 1
    deck[card_id] = {"card_type": "Mileage"}
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

    print(card_id, deck[card_id])

print(deck)
