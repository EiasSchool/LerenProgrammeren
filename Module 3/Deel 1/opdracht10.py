from fruitmand import fruitmand

sortedFruitmand = (sorted(fruitmand, key=lambda fruit: fruit['weight'], reverse = True))

for fruit in sortedFruitmand:
    name = fruit['name']
    weight = fruit['weight']
    weightInKilo = weight / 1000
    
    print(f'|{name:<11} - {weightInKilo:<5.2} kg')