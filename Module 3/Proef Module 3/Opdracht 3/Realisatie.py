import random

namen = []

while len(namen) < 3:
    naam = input("Geef een naam:\n")
    if naam not in namen:
        namen.append(naam)
    else:
        print('Deze naam bestaat al, probeer een andere naam.')

while True:
    verder = input("Wil je nog een naam toevoegen? (ja/nee)\n").strip().lower()
    if verder == "nee":
        break
    elif verder == 'ja':
        naam = input("Geef een naam:\n")
        if naam not in namen:
            namen.append(naam)
        else:
            print("Deze naam bestaat al, probeer een andere naam.")
    else:
        print("Antwoord met 'ja' of 'nee'.")

lootjes = namen.copy()
random.shuffle(lootjes)

while any(namen[i] == lootjes[i] for i in range(len(namen))):
    random.shuffle(lootjes)

for i in range(len(namen)):
    print(f"{namen[i]} heeft {lootjes[i]} getrokken.")