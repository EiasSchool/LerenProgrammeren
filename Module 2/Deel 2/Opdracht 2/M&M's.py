import random
from collections import Counter

kleuren = ('oranje', 'blauw', 'groen', 'bruin')
zak = []

hoeveelheid = int(input('Hoeveel M&M\'s wil je aan de zak toevoegen? '))

for M in range(hoeveelheid):
    random_color = random.choice(kleuren)
    zak.append(random_color)

print(f'De zak bevat de volgende M&M\'s:')

color_counts = Counter(zak)

for color, count in color_counts.items():
    print(f"{color}: {count}")

print(zak)