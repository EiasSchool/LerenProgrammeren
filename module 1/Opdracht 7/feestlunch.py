from termcolor import colored

croissantjes = int(input('Aantal croissantjes:\n'))
croissant_prijs = int(float(input('Wat is de prijs van de croissant in euro’s:\n')) * 100)

stokbroden = int(input('Aantal stokbroden:\n'))
stokbroden_prijs = int(float(input('Wat is de prijs van de stokbroden in euro’s:\n')) * 100)

totaal_croissant_prijs = croissantjes * croissant_prijs
totaal_stokbroden_prijs = stokbroden * stokbroden_prijs

aantal_kortingsbonnen = int(input('Aantal kortingsbonnen:\n'))
kortingsbonnen = int(0.50 * 100) * aantal_kortingsbonnen

totaal = (totaal_croissant_prijs + totaal_stokbroden_prijs) - kortingsbonnen

print(f'De kosten van de croissantjes is {colored(totaal_croissant_prijs / 100, "yellow")} euro')
print(f'De kosten van de stokbroden is {colored(totaal_stokbroden_prijs / 100, "blue")} euro')
print(f'De feestlunch kost je bij de bakker {colored(totaal / 100, "green")} euro voor de {colored(croissantjes, "magenta")} croissantjes en de {colored(stokbroden, "cyan")} stokbroden als de {colored(aantal_kortingsbonnen, "red")} kortingsbonnen nog geldig zijn!')
