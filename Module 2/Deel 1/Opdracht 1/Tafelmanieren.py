while True:
    try:
        getal = int(input('Geef een getal:\n'))
        break
    except ValueError:
        print('Voer heel getal in')

for i in range(1, 11):
    print(f'{i} x {getal} = {getal*i}')