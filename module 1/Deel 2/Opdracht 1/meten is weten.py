a = int(input('Wat is de eerste getal?'))
b = int(input('Wat is de tweede getal?'))

if a > b:
    Max = a
    Min = b
    print(f'a is het grootste getal: {Max}')
elif a < b:
    Min = a
    Max = b
    print(f'a is het kleinste getal: {Min}')
else:
    Max = a
    Min = b
    print('a en b zijn even groot')
print(f'Het minimum is: {Min}')
print(f'Het maximum is: {Max}')