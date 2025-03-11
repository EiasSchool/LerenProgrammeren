from functions import get_primes_up_to, get_first_n_primes, get_primes_between

def main():
    print("Kies een optie:")
    print("1: Alle priemgetallen tot en met een getal")
    print("2: De eerste N priemgetallen")
    print("3: Priemgetallen tussen twee getallen")

    keuze = input("Voer het nummer van de optie in: ")

    if keuze == "1":
        n = int(input("Geef een getal: "))
        result = get_primes_up_to(n)
    elif keuze == "2":
        n = int(input("Hoeveel priemgetallen wil je? "))
        result = get_first_n_primes(n)
    elif keuze == "3":
        a = int(input("Geef het eerste getal: "))
        b = int(input("Geef het tweede getal: "))
        result = get_primes_between(a, b)
    else:
        print("Ongeldige keuze.")
        return

    if result:
        print("Resultaat:", result)
    else:
        print("Er zijn geen priemgetallen gevonden.")

if __name__ == "__main__":
    main()
