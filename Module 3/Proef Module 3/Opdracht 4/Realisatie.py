import random

namen = []

while len(namen) < 3:
    naam = input("Geef een naam\n").strip().lower()
    if naam not in namen:
        namen.append(naam)
    else:
        print('Deze naam bestaat al probeer een andere naam')

while True:
    verder = input("Wil je nog een naam toevoegen ja/nee\n").strip().lower()
    if verder == "nee":
        break
    elif verder == 'ja':
        naam = input("Geef een naam\n").strip().lower()
        if naam not in namen:
            namen.append(naam)
        else:
            print("Deze naam bestaat al probeer een andere naam")
    else:
        print("Antwoord met ja of nee")

lootjes = namen.copy()
random.shuffle(lootjes)

while True:
    random.shuffle(lootjes)
    goed = True
    for i in range(len(namen)):
        if lootjes[i] == namen[i]:
            goed = False
            break
    if goed:
        break

results = {}
for i in range(len(namen)):
    results[namen[i]] = lootjes[i]

print("De lootjes zijn getrokken je kunt nu een naam opgeven om te vragen wie ze hebben\n")

while True:
    findName = input("Welke naam wil je opzoeken type stop om te stoppen\n").strip().lower()
    if findName == 'stop':
        print("Het programma wordt afgesloten")
        break
    elif findName in results:
        print(f"{findName.capitalize()} heeft {results[findName].capitalize()} getrokken")
    else:
        print("Deze naam is niet gevonden Probeer het opnieuw")