from fruitmand import fruitmand
from termcolor import colored

colorTranslation = {
    'yellow': 'geel',
    'green': 'groen',
    'orange': 'oranje',
    'red': 'rood',
    'brown': 'bruin'
}

longestFruit = max(fruitmand, key=lambda fruit: len(fruit['name']))

name = longestFruit['name']
weight = longestFruit['weight']
color = longestFruit['color']
weightInKilo = weight / 1000

tanslatedColor = colorTranslation.get(color, color)

print(f'De "{name.capitalize()}" ({len(name)} letters) heeft een {tanslatedColor.capitalize()} kleur en een gewicht van {weightInKilo} kg.')