from fruitmand import fruitmand

for fruit in fruitmand:
    if fruit['name'] == 'appel':
        weight = (fruit['weight'])
        print(f'Appel gewicht is {weight}g')