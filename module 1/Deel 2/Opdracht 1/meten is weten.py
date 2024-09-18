a = int(input('Wat is de eerste getal?'))
b = int(input('Wat is de tweede getal?'))

if a > b:
    Max = a
    print(f'a is het grootste getal: {Max}')
elif a < b:
    Min = a
    print(f'a is het kleinste getal: {Min}')
else:
    print('a en b zijn even groot')