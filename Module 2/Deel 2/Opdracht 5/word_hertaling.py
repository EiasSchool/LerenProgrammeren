translate = {
    'draak': 'geit',
    'vuur': 'water',
    'schild': 'reddingsvest',
    'dapper': 'bang',
    'zwaard': 'stok'
}

vertaal_tekst = input('Voer een zin in om te vertalen: ')

woorden = vertaal_tekst.split()
vertaalde_woorden = []

for woord in woorden:
    woord_sch = woord.strip(",.!?;:")

    if woord_sch.lower() in translate:
        vertaalde_woord = translate[woord_sch.lower()]
        if woord[0].isupper():
            vertaalde_woord = vertaalde_woord.capitalize()
        if woord != woord_sch:
            vertaalde_woord += woord[len(woord_sch):]
        vertaalde_woorden.append(vertaalde_woord)
    else:
        vertaalde_woorden.append(woord)

vertaalde_text = " ".join(vertaalde_woorden)

print("\Vertaalde zin:\n")
print(vertaalde_text)
