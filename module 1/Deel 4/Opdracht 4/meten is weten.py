def verglijk_getallen(nr1: int, nr2: int) -> str:
    if nr1 > nr2:
        return f'Maximum: {nr1} en minimum: {nr2}'
    elif nr1 < nr2:
        return f'Maximum: {nr2} en minimum: {nr1}'
    else:
        return 'a en b zijn even groot'

a = 10
b = 5

resultaat = verglijk_getallen(a, b)
print(resultaat)


# a = int(input('Wat is de eerste getal?'))
# b = int(input('Wat is de tweede getal?'))

# if a > b:
#     Max = a
#     Min = b
#     print(f'a is het grootste getal: {Max}')
# elif a < b:
#     Min = a
#     Max = b
#     print(f'a is het kleinste getal: {Min}')
# else:
#     Max = a
#     Min = b
#     print('a en b zijn even groot')
# print()
# print(f'Het maximum is: {Max}')