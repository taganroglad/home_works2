items = {
    'Палатка': 2,
    'Спальный мешок': 1,
    'Газовая горелка': 0.5,
    'Кружка': 0.2,
    'Сухие продукты': 1,
    'Фонарик': 0.3
}

max_weight = 4
backpack = {}
total_weight = 0

for item, weight in items.items():
    if total_weight + weight <= max_weight:
        backpack[item] = weight
        total_weight += weight

print(backpack)
