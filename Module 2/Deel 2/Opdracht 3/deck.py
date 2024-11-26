import random

kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']
rangen = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'heer', 'aas']

deck = [f'{rang} van {kleur}' for rang in rangen for kleur in kleuren] + ['joker', 'joker']

random.shuffle(deck)

for kaart in range(7):

    print(f'kaart {kaart + 1}: {deck.pop(0)}')

print(f'\nAantal overgebelven kaarten: {len(deck)}')
print(f'Overgebleven kaarten: {deck}')