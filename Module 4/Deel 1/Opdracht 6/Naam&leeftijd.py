from Function import VerzamelGegevens

personList = VerzamelGegevens()

for person in personList:
    print(f"{person["name"]}, die in {person["city"]} woont, is {person["age"]} jaar")