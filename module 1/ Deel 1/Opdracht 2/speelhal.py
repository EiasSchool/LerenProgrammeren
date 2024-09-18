aantal_personen = 4
toegangstickets_prijs = aantal_personen * 7.45
aantal_minuten = 45
VIP_VR_GameSeat = (aantal_personen * 0.37) * (aantal_minuten / 5)

totaal = toegangstickets_prijs + VIP_VR_GameSeat

print(f'De totaal is €{totaal:.2f}')