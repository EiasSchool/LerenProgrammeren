def NaamEnLeeftijd():
    person = {}

    person["name"] = input("Wat is je naam?\n").strip()
    person["city"] = input("In welke stad woon je?\n").capitalize()

    while True:
        try:
            person["age"] = int(input("Wat is je leeftijd?\n"))
            break
        except ValueError:
            print("Gebruik nummmers")
    
    return person

def VerzamelGegevens():
    storedInfo = []
    
    while True:
        storedInfo.append(NaamEnLeeftijd())

        continueQuestion = input("Toets enter om door te gaan of stop om te printen:\n").lower()

        if continueQuestion == "stop":
            break

    return storedInfo