naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))
geslacht = input("Ben je een A) een jonge of B) een meisje? ").lower()
favoriet_kleur = input("Wat is je favoriete kleur? ")
favoriet_getal = int(input("Wat is je favoriete getal? "))
verschil = abs(leeftijd-favoriet_getal)
jongen_of_meisje = 'haar' if geslacht == 'b' else 'zijn'

print("")
print("Mag ik je voorstellen aan", naam)
print(f"{jongen_of_meisje.capitalize()} leeftijd is:", leeftijd)
print(f"{naam}'s favoriete kleur is:", favoriet_kleur)
print(f"Het verschil tussen {jongen_of_meisje} leeftijd en {favoriet_getal} is:", verschil)
