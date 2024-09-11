from termcolor import colored

aantal_personen = int(input('Aantal personen:\n'))
toegangstickets_prijs = int(7.45 * 100) * aantal_personen

aantal_minuten = int(input('Hoeveel minuten:\n'))
VIP_VR_GameSeat = int((0.37 * 100) * (aantal_minuten / 5)) * aantal_personen

totaal = toegangstickets_prijs + VIP_VR_GameSeat

print(f'De kosten van de tickets is {colored(toegangstickets_prijs / 100, "blue")} euro')
print(f'De kosten van de VIP VR GameSeat is {colored(VIP_VR_GameSeat / 100, "yellow")} euro')
print(f'Dit geweldige dagje-uit met {colored(aantal_personen, "magenta")} mensen in de Speelhal met {colored(aantal_minuten, "cyan")} minuten VR kost je maar {colored(totaal / 100, "green")} euro')
