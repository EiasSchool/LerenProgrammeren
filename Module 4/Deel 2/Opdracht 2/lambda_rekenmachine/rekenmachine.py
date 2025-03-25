from functions import addition, subtraction, multiplication, division

choices = {
    "A": "getallen optellen",
    "B": "getallen aftrekken",
    "C": "getallen vermenigvuldigen",
    "D": "getallen delen",
    "E": "getal ophogen",
    "F": "getal verlagen",
    "G": "getal verdubbelen",
    "H": "getal halveren"
}

choices2 = {
    "A": "iets optellen",
    "B": "iets aftrekken",
    "C": "iets vermenigvuldigen",
    "D": "door iets delen",
    "E": "ophogen",
    "F": "verlagen",
    "G": "verdubbelen",
    "H": "halveren",
    "I": "niets"
}

total = None

while True:
    print("Wat wilt u doen?")
    for letter, choice in choices.items():
        print(f"{letter}: {choice}")
    
    answer = input("Kies: ").upper().strip()
    
    if total is None:
        n1 = float(input("Eerste getal: "))
    else:
        n1 = total
    
    if answer in ["A", "B", "C", "D"]:
        n2 = float(input("Tweede getal: "))
    elif answer in ["E", "F"]:
        n2 = 1
    elif answer in ["G", "H"]:
        n2 = 2
    else:
        print("Ongeldige keuze.")
        continue
    
    if answer == "A":
        total = addition(n1, n2)
    elif answer == "B":
        total = subtraction(n1, n2)
    elif answer == "C":
        total = multiplication(n1, n2)
    elif answer == "D":
        total = division(n1, n2)
    elif answer == "E":
        total = addition(n1, 1)
    elif answer == "F":
        total = subtraction(n1, 1)
    elif answer == "G":
        total = multiplication(n1, 2)
    elif answer == "H":
        total = division(n1, 2)
    
    print(f"Uitkomst: {total}")
    
    print("Wat wilt u doen met de uitkomst?")
    for letter, choice in choices2.items():
        print(f"{letter}: {choice}")
    
    answer = input("Kies: ").upper().strip()
    if answer == "I":
        break