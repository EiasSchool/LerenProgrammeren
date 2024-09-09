aantal_personen = 4
toegangstickets_prijs = aantal_personen * 7.45
aantal_minuten = 45
VIP_VR_GameSeat = (aantal_personen * 0.37) * (aantal_minuten / 5)

totaal = toegangstickets_prijs + VIP_VR_GameSeat

print(f'De kosten van de tickets is {toegangstickets_prijs:.2f} euro')
print(f'De kosten van de VIP VR GameSeat is {VIP_VR_GameSeat:.2f} euro')
print(f'Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met {aantal_minuten} minuten VR kost je maar {totaal:.2f} euro')