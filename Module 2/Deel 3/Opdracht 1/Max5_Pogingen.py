from termcolor import colored

correct_password = 'Eias123'

for i in range(5):
    enterpass = input('Voer het wachtwoord in: ')
    if enterpass == correct_password:
        print(f'Het wachtwoord is {colored("correct!", "green")} je had {colored(i + 1, "yellow")} pogingen nodig om het op te lossen')
        break
    elif i < 4:
        print(f'Het wachtwoord dat je hebt ingevoerd is {colored("fout", "red")} probeer het opnieuw')
else:
    print('Je hebt het maximale aantal pogingen overschreden')
