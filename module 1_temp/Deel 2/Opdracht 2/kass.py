print('Geef \'ja\' of \'nee\' als antwoord')
antwoord1 = input('Is de kaas geel?\n')
# de eerste vraag
if antwoord1.lower() == 'ja':
    # de tweede vraag (ja)
    antwoord2 = input('Zitten er gaten in?\n')
    if antwoord2.lower() == 'ja':
        antwoord3 = input('Is de kaas belachelijk duur?\n')
        if antwoord3.lower() == 'ja':
            print('Emmenthaler')
        else:
            print('Leerdammer')
    else:
        antwoord3 = input('Is de kaas hard als steen?\n')
        if antwoord3.lower() == 'ja':
            print('Parmigiano Reggiano')
        else:
            print('Goudse Kaas')
else:
    # de tweede vraag (nee)
    antwoord2 = input('Heeft de kaas blauwe schimmel?\n')
    if antwoord2.lower() == 'ja':
        antwoord3 = input('Heeft de kaas korst?\n')
        if antwoord3.lower() == 'ja':
            print('Blue de Rochbaron')
        else:
            print('Fourme d\'ambert')
    else:
        antwoord3 = input('Heeft de kaas korst?\n')
        if antwoord3.lower() == 'ja':
            print('Camembert')
        else:
            print('Mozzarella')