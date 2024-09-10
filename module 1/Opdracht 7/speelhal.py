from termcolor import colored

aantal_personen = int(input('Aantal personen:\n'))
toegangstickets_prijs = aantal_personen * 7.45
aantal_minuten = int(input('Hoeveel minuten:\n'))
VIP_VR_GameSeat = (aantal_personen * 0.37) * (aantal_minuten / 5)

totaal = toegangstickets_prijs + VIP_VR_GameSeat

print(f'De kosten van de tickets is {colored(toegangstickets_prijs, "blue")} euro')
print(f'De kosten van de VIP VR GameSeat is {colored(f"{VIP_VR_GameSeat:.2f}", "yellow")} euro')
print(f'Dit geweldige dagje-uit met {colored(aantal_personen, "magenta")} mensen in de Speelhal met {colored(aantal_minuten, "cyan")} minuten VR kost je maar {colored(f"{totaal:.2f}", "green")} euro')
