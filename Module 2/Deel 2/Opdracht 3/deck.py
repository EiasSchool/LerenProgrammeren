import random

kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']
rangen = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'heer', 'aas']

deck = [f'{rang} van {kleur}' for rang in rangen for kleur in kleuren] + ['joker', 'joker']

random.shuffle(deck)

eerste_7_kaarten = deck[:7]
overgebleven_kaarten = deck[7:]

for kaart in range(7):
    print(f'kaart {kaart + 1}: {eerste_7_kaarten[kaart]}')

print(f'\nAantal overgebelven kaarten: {len(overgebleven_kaarten)}')
print(f'Overgebleven kaarten: {overgebleven_kaarten}')