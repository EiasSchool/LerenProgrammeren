a = int(input('Wat is de eerste getal?'))
b = int(input('Wat is de tweede getal?'))

if a > b:
    Max = a
    Min = b
    print(f'a is het grootste getal: {Max}')
    print(f'Het minimum is: {Min}')
    print(f'Het maximum is: {Max}')
elif a < b:
    Min = a
    Max = b
    print(f'a is het kleinste getal: {Min}')
    print(f'Het minimum is: {Min}')
    print(f'Het maximum is: {Max}')
else:
    print('a en b zijn even groot')