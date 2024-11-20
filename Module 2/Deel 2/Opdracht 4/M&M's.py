import random

kleuren = ['Rood', 'Blauw', 'Groen', 'Geel', 'Bruin']
zak = {}

aantal_mm = int(input('Hoeveel M&M\'s wil je toevoegen aan de zak? '))


for i in range(aantal_mm):
    kleur = random.choice(kleuren)
    if kleur in zak:
        zak[kleur] += 1
    else:
        zak[kleur] = 1

print('De zak bevat de volgende M&M\'s:', zak)