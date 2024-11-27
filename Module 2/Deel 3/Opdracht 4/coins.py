# name of student: Eias Bilal
# number of student: 99082959
# purpose of program: Om het juiste bedrag aan wisselgeld te berekenen en terug te geven met zo min mogelijk munten.
# structure of program: Het programma berekent het wisselgeld en geeft het terug in verschillende muntwaarden. Het drukt een overzicht af van teruggegeven munten.

# Lijst met muntwaarden in centen
coinValues = [500, 200, 100, 50, 20, 10, 5, 2, 1]  # €5 €2 €1 ¢50 ¢20 ¢10 ¢5 ¢2 ¢1

# Inputs voor de bedragen
toPay = int(float(input('Amount to pay: ')) * 100)  # Omrekenen naar centen ¢
paid = int(float(input('Paid amount: ')) * 100)  # Omrekenen naar centen ¢
change = paid - toPay  # Bereken het wisselgeld

# Bijhouden van teruggegeven munten
coinsReturned = {coin: 0 for coin in coinValues}  # Voor elke muntwaarde wordt het aantal teruggegeven munten bijgehouden

# Controleer of het betaalde bedrag voldoende is
if change < 0:  # Als het betaalde bedrag kleiner is dan het te betalen bedrag
    print("Betaald bedrag is onvoldoende!")  # Geef een foutmelding
else:
    # Verwerk het wisselgeld
    for coinValue in coinValues:  # Doorloop alle muntwaarden
        if change <= 0:  # Als wisselgeld is teruggegeven, stop de loop
            break
        nrCoins = change // coinValue  # Bereken het aantal munten van deze waarde
        if nrCoins > 0:  # Als er munten van deze waarde nodig zijn
            coinsReturned[coinValue] += nrCoins  # Update het aantal teruggegeven munten
            change -= nrCoins * coinValue  # Trek de waarde van de teruggegeven munten af van het resterende wisselgeld

    # Controleer of er wisselgeld overblijft
    if change > 0:  # Als wisselgeld niet volledig teruggegeven kan worden
        print(f"Wisselgeld niet teruggegeven: {change} cent")
        print("Het is mogelijk dat er geen munten meer beschikbaar zijn voor het resterende bedrag.")
    else:  # Wisselgeld succesvol teruggegeven
        print("Alle wisselgeld is succesvol teruggegeven.")

    # Overzicht van teruggegeven munten
    print("\n--- Wisselgeldverwerking voltooid ---")
    print("\nOverzicht van teruggegeven munten:")
    for coin, count in coinsReturned.items():  # Itereer door de dictionary met muntwaarden en aantallen
        if count > 0:  # Alleen munten die daadwerkelijk zijn gebruikt worden weergegeven
            print(f"{count} munt(en) van {coin} cent")
