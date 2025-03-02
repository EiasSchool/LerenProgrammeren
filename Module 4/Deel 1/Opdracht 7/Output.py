from Function import VerzamelGegevens
from termcolor import colored

personList = VerzamelGegevens()

for person in personList:
    personName = colored(person["name"], "green")
    personAge = person["age"]
    personCity = colored(person["city"], "yellow")

    if personAge > 18:
        print(f"In {personCity} woont {personName}, die {colored(f"al {personAge - 18} jaar", "red")} volwassen is.")
    elif personAge == 18:
        print(f"In {personCity} woont {personName}, die {colored('net', 'red')} volwassen is.")
    else:
        print(f"In {personCity} woont {personName}, die {colored('nog niet', 'red')} volwassen is.")