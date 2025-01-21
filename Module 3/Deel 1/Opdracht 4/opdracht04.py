from fruitmand import fruitmand
import random

numberFruit = int(input('Hoeveel fruit namen wil je zien?\n'))

for fruit in range(numberFruit):
    fruitNames = random.choice(fruitmand)['name']
    print(fruitNames)