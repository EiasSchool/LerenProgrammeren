croissantjes = 17
croissant_prijs = 0.39

stokbroden = 2
stokbroden_prijs = 2.78

totaal_croissant_prijs = croissantjes * croissant_prijs
totaal_stokbroden_prijs = stokbroden * stokbroden_prijs

aantal_kortingsbonnen = 3
kortingsbonnen = 0.50 * aantal_kortingsbonnen
totaal = (totaal_croissant_prijs + totaal_stokbroden_prijs) - kortingsbonnen

print(f'De kosten van de croissantjes is {totaal_croissant_prijs:.2f} euro')
print(f'De kosten van de stokbroden is {totaal_stokbroden_prijs:.2f} euro')
print(f'De feestlunch kost je bij de bakker {totaal} euro voor de {croissantjes} croissantjes en de {stokbroden} stokbroden als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn!')