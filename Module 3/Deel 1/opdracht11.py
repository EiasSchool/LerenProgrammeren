from fruitmand import fruitmand

colors = set(fruit['color'] for fruit in fruitmand)

while True:
    colorChoice = input(f'Welke kleur wil je kiezen? ({', '.join(colors)}): ').lower()
    if colorChoice in colors:
        break
    else:
        print(f'De kleur {colorChoice} zit er niet in de fruitmand, probeer opnieuw')

roundCount = 0
nonRoundCount = 0

for fruit in fruitmand:
    if fruit['color'] == colorChoice:
        if fruit['round']:
            roundCount += 1
        else:
            nonRoundCount += 1

if roundCount > nonRoundCount:
    print(f'Er zijn {roundCount - nonRoundCount} meer ronde vruchten dan niet ronde vruchten in de kleur {colorChoice}')
elif roundCount < nonRoundCount:
    print(f'Er zijn {nonRoundCount - roundCount} minder ronde vruchten dan niet ronde vruchten in de kleur {colorChoice}')
else:
    print(f'Er zijn {roundCount} ronde vruchten en {nonRoundCount} niet ronde vruchten in de kleur {colorChoice}')