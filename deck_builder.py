card_data = [
    {
        "card_type": "Mileage",
        "values": [25, 50, 75, 100, 200],
        "counts": [10, 10, 10, 12, 4],
    },
    {
        "card_type": "Hazard",
        "values": ["flat tire", "out of gas", "accident", "red light"],
        "counts": [3, 3, 3, 5],
    },
    {
        "card_type": "Remedy",
        "values": ["spare tire", "gas", "repairs", "green light"],
        "counts": [6, 6, 6, 14],
    },
]

for i in card_data[2]["values"]:
    print(i)
