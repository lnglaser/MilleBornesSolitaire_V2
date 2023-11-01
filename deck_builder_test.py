card_data = [
    {
        "card_type": "Mileage",
        "values": [25, 50, 75, 100, 200],
        "counts": [10, 10, 10, 12, 4],
    },
    {
        "card_type": "Hazard",
        "values": ["flat tire", "out of gas", "accident", "speed limit", "red light"],
        "counts": [3, 3, 3, 4, 5],
    },
    {
        "card_type": "Remedy",
        "values": ["spare tire", "gas", "repairs", "end of limit", "green light"],
        "counts": [6, 6, 6, 6, 14],
    },
    {
        "card_type": "Safety",
        "values": ["puncture-proof", "extra tank", "driving ace", "right of way"],
        "counts": [1, 1, 1, 1],
    },
]

deck = {}
card_id = 0

for value in card_data[0]["values"]:
    matching_index = card_data[0]["values"].index(value)
    # print(card_data[0]["values"][matching_index])
    print(card_data[0]["counts"][matching_index])
    for i in range(card_data[0]["counts"][matching_index]):
        print(card_data[0]["card_type"], card_data[0]["values"][matching_index])
