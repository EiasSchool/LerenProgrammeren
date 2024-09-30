#vraagt de user hoeveel pizza's hij wilt van elke afmetingen
aantal_small_pizza = int(input('Hoeveel small pizza\'s wilt u?\n'))
aantal_medium_pizza = int(input('Hoeveel medium pizza\'s wilt u?\n'))
aantal_large_pizza = int(input('Hoeveel large pizza\'s wilt u?\n'))

#de prijzen van elke pizza
prijs_small = 6.99
prijs_medium = 9.50
prijs_large = 12.75

#berekent het totaal voor elke pizza
totaal_small_pizza = aantal_small_pizza * prijs_small
totaal_medium_pizza = aantal_medium_pizza * prijs_medium
totaal_large_pizza = aantal_large_pizza * prijs_large

#berekent het totaal
totaal = totaal_small_pizza + totaal_medium_pizza + totaal_large_pizza

#print de kassabon in de console
print(f'''
************** KASSA BON **************
Pizza's small:\t {aantal_small_pizza} x {prijs_small:.2f}\t= {totaal_small_pizza:.2f}
Pizza's medium:\t {aantal_medium_pizza} x {prijs_medium:.2f}\t= {totaal_medium_pizza:.2f}
Pizza's large:\t {aantal_large_pizza} x {prijs_large:.2f}\t= {totaal_large_pizza:.2f}
---------------------------------------
Te betalen:\t\t\t{totaal:.2f}
''')