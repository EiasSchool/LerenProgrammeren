def NaamEnLeeftijd():
    person = {}

    person["name"] = input("Wat is je naam?\n").strip()

    while True:
        try:
            person["age"] = int(input("Wat is je leeftijd?\n"))
            break
        except ValueError:
            print("Gebruik nummmers")

    return person

personInfo = NaamEnLeeftijd()

print(f"{personInfo["name"]} is {personInfo["age"]} jaar")