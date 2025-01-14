# naam van student: Eias Bilal
# studentnummer: 99082959
# doel van het programma: Het berekenen van het optimale aantal munten om wisselgeld terug te geven.
# structuur van het programma: Invoer -> Bereken Wisselgeld -> Geef Munten -> Samenvatting

# Lijst met muntwaarden in centen, inclusief 1, 2 en 5-euro munten.
coinValues = [500, 200, 100, 50, 20, 10, 5, 2, 1] 

# Zet het te betalen bedrag en het betaalde bedrag om naar centen voor nauwkeurige berekeningen.
toPay = int(float(input('Te betalen bedrag: ')) * 100) 
paid = int(float(input('Betaald bedrag: ')) * 100) 
change = paid - toPay # Bereken het totale wisselgeld.

# Woordenboek om bij te houden hoeveel munten van elk type zijn teruggegeven.
returnedCoins = {coin: 0 for coin in coinValues}

# Lus totdat al het wisselgeld is teruggegeven of er geen munten meer over zijn.
while change > 0 and len(coinValues) > 0: 
    coinValue = coinValues.pop(0)  # Pak de hoogste resterende muntwaarde.
    nrCoins = change // coinValue  # Bereken het maximale aantal munten van dit type dat kan worden gebruikt
    
    if nrCoins > 0:  # Ga alleen verder als er minstens één munt van dit type kan worden teruggegeven
        print('Geef maximaal', nrCoins, 'munten van', coinValue, 'cent!')
        
        # Zorg ervoor dat de ingevoerde waarde niet meer is dan nodig is.
        while True:
            try:
                nrCoinsReturned = int(input(f'Hoeveel munten van {coinValue} cent heeft u teruggegeven? '))
                if nrCoinsReturned <= nrCoins and nrCoinsReturned * coinValue <= change:
                    break  # Geldige invoer, breek de lus
                else:
                    print(f'Fout: Je kunt maximaal {nrCoins} munten van {coinValue} cent geven.')
            except ValueError:
                print("Fout: Voer een geldig getal in.")
        
        returnedCoins[coinValue] += nrCoinsReturned  # Werk het aantal teruggegeven munten voor dit type bij
        change -= nrCoinsReturned * coinValue  # Trek de waarde van de teruggegeven munten af van het resterende wisselgeld

# Na de lus, controleer of al het wisselgeld is teruggegeven.
if change > 0: 
    print('Niet al het wisselgeld is teruggegeven:', str(change) + ' cent')  # Meld als niet al het wisselgeld is teruggegeven.
else:
    print('Alle wisselgeld is teruggegeven!')  # Bevestig dat het exacte wisselgeld is teruggegeven.

# Print een kassabon met een samenvatting van alle teruggegeven munten.
print('\n************** KASSA BON **************')
for coin, count in returnedCoins.items():
    if count > 0:  # Print alleen muntsoorten die daadwerkelijk zijn gebruikt.
        value_in_euros = coin / 100
        total_value = count * value_in_euros
        print(f'Munten van {value_in_euros:.2f} euro: {count} x {value_in_euros:.2f} = {total_value:.2f} euro')

print('---------------------------------------')
if change > 0:
    remaining = change / 100
    print(f'Niet teruggegeven: {remaining:.2f} euro')
else:
    total_returned = sum((coin * count) for coin, count in returnedCoins.items()) / 100
    print(f'Te betalen: {total_returned:.2f} euro')
