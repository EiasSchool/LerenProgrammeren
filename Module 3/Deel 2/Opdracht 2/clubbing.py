PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = {
    'cola': PRIJS_COLA,
    'bier': PRIJS_BIER,
    'champagne': PRIJS_CHAMPAGNE
}
VIP_LIST = ('jeroen', 'jouke', 'rudi')


def toon_bericht(bericht):
    print(bericht)

def clubbing():
    userItems = []
    
    while True:
        try:
            age = int(input('Hoe oud ben je?\n'))
            break
        except ValueError:
            toon_bericht('Je kan alleen volledige nummers gebruiken')
    
    if age < 18:
        toon_bericht('Sorry, je mag niet naar binnen')
        toon_bericht(f'Probeer het in {18 - age} jaar nog eens')
        return
    
    naam = input('Wat is je naam?\n').lower()
    is_vip = naam in VIP_LIST
    
    if is_vip and age >= 21:
        bandje = 'blauw'
    elif is_vip:
        bandje = 'rood'
    elif age >= 21:
        userItems.append('stempel')
        toon_bericht('Je krijgt van mij een stempel')
    else:
        toon_bericht('Sorry, je mag niet naar binnen')
        return
    
    if is_vip:
        userItems.append(bandje)
        toon_bericht(f'Ok, je bent {age} jaar oud en VIP. Je krijgt van mij een {bandje} bandje')
    
    drankje = input('Wat wil je drinken?\n').lower()
    
    if drankje not in DRANKJES:
        toon_bericht('Sorry, geen idee wat je bedoelt, hier een glaasje water')
        return
    
    if drankje == 'cola':
        if any(item in ['blauw', 'rood'] for item in userItems):
            toon_bericht('Alstublieft, complimenten van het huis')
        else:
            toon_bericht(f'Alstublieft je cola, dat is dan €{PRIJS_COLA:.2f}')
    
    elif drankje == 'bier':
        if any(item in ['blauw', 'rood', 'stempel'] for item in userItems):
            toon_bericht(f'Alstublieft je bier, dat is dan €{PRIJS_BIER:.2f}')
        else:
            toon_bericht('Sorry, je mag geen alcohol bestellen onder de 21')
    
    elif drankje == 'champagne':
        if 'blauw' in userItems:
            toon_bericht(f'Alstublieft je champagne, dat is dan €{PRIJS_CHAMPAGNE:.2f}')
        else:
            toon_bericht('Sorry, alleen VIPs mogen champagne bestellen')
    
clubbing()
