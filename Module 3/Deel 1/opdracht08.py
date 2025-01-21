from fruitmand import fruitmand

totalWeight = 0

for fruit in fruitmand:
    totalWeight += fruit['weight']
print(f'Totale gewitcht van de fruitmand: {totalWeight}')

watermelon = {'name': 'watermeloen', 'weight': 2500, 'color': 'green', 'round': True}

fruitmand.append(watermelon)

totalWeight += watermelon['weight']
print(f'Totale gewitcht van de fruitmand (met watermeloen): {totalWeight}')
