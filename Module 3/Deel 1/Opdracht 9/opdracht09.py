from fruitmand import fruitmand

for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove(fruit)

for color in set(fruit['color'] for fruit in fruitmand):
    print(color)