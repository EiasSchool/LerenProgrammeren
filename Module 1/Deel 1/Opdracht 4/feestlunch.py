from termcolor import colored

croissantjes = 17
croissant_prijs = 0.39

stokbroden = 2
stokbroden_prijs = 2.78

totaal_croissant_prijs = croissantjes * croissant_prijs
totaal_stokbroden_prijs = stokbroden * stokbroden_prijs

aantal_kortingsbonnen = 3
kortingsbonnen = 0.50 * aantal_kortingsbonnen
totaal = (totaal_croissant_prijs + totaal_stokbroden_prijs) - kortingsbonnen

print(f'De kosten van de croissantjes is {colored(totaal_croissant_prijs, "yellow")} euro')
print(f'De kosten van de stokbroden is {colored(totaal_stokbroden_prijs, "blue")} euro')
print(f'De feestlunch kost je bij de bakker {colored(totaal, "green")} euro voor de {colored(croissantjes, "magenta")} croissantjes en de {colored(stokbroden, "cyan")} stokbroden als de {colored(aantal_kortingsbonnen, "red")} kortingsbonnen nog geldig zijn!')
