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

while True:
    random.shuffle(lootjes)
    zelfgetrokken = False
    for i in range(len(namen)):
        if lootjes[i] == namen[i]:
            zelfgetrokken = True
            break
    if not zelfgetrokken:
        break

results = dict(zip(namen, lootjes))

print("\nDe lootjes zijn getrokken! Wie wie heeft, blijft geheim. Je kunt nu een naam opgeven om te vragen wie ze hebben.")

while True:
    findName = input("\nWelke naam wil je opzoeken? (type 'stop' om te stoppen): ").strip()
    if findName.lower() == 'stop':
        print("Het programma wordt afgesloten.")
        break
    elif findName in results:
        print(f"{findName} heeft {results[findName]} getrokken.")
    else:
        print("Deze naam is niet gevonden. Probeer het opnieuw.")
