croissantjes = 17
croissant_prijs = 0.39

stokbroden = 2
stokbroden_prijs = 2.78

totaal_croissant_prijs = croissantjes * croissant_prijs
totaal_stokbroden_prijs = stokbroden * stokbroden_prijs

kortingsbonnen = 0.50 * 3
totaal = (totaal_croissant_prijs + totaal_stokbroden_prijs) - kortingsbonnen

print(f'Je moet €{totaal} betalen')