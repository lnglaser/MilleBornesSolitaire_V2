card_data = [
    {
        "card_type": "Mileage",
        "values": [25, 50, 75, 100, 200],
        "counts": [10, 10, 10, 12, 4],
    },
    {
        "card_type": "Hazard",
        "values": ["flat tire", "out of gas", "accident", "speed limit", "red light"],
        "counts": [3, 3, 3, 5],
    },
    {
        "card_type": "Remedy",
        "values": ["spare tire", "gas", "repairs", "end of limit", "green light"],
        "counts": [6, 6, 6, 14],
    },
    {
        "card_type": "Safety",
        "values": ["puncture-proof", "extra tank", "driving ace", "right of way"],
        "counts": [1, 1, 1, 1],
    },
]

deck = []
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

for i in card_data[0]["counts"]:
    current_count = i
    print(current_count)
    for j in range(0, current_count):
        card = {
            "card_type": card_data[0]["card_type"],
            "value": card_data[0]["values"],
        }
        print(card)
