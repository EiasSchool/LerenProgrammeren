import time
import random
import operator

# === player stats === #
player_attack = 1
player_defense = 0
player_health = 3
player_rupees = 0
player_inventory = []

# === kamer bezocht check === #
kamer1_bezocht = False
kamer2_bezocht = False
kamer3_bezocht = False
kamer4_bezocht = False
kamer5_bezocht = False
kamer6_bezocht = False
kamer7_bezocht = False
kamer8_bezocht = False
kamer9_bezocht = False

# === functions sectie === #
# Fight function for the enemies
def enemyBattle(player_health, player_attack, player_defense, enemy_name, enemy_attack, enemy_defense, enemy_health):
    print(f'Je komt de {enemy_name} tegen!')

    while player_health > 0 and enemy_health > 0:
        player_hit_damage = max(player_attack - enemy_defense, 1)
        enemy_health -= player_hit_damage
        print(f'Je valt de {enemy_name} aan en doet {player_hit_damage} schade. De {enemy_name} heeft nu {enemy_health} health.')

        if enemy_health <= 0:
            print(f'Je hebt de {enemy_name} verslagen!')
            return player_health

        # Enemy attacks player
        enemy_hit_damage = max(enemy_attack - player_defense, 1)
        player_health -= enemy_hit_damage
        print(f'De {enemy_name} valt je aan en doet {enemy_hit_damage} schade. Je health is nu {player_health}.')

        if player_health <= 0:
            print(f'Helaas is de {enemy_name} te sterk voor je.')
            print('Game over.')
            exit()

    return player_health

# Function for the math problem
def randomCalculator():
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul
        }
    num1 = random.randint(10, 25)
    num2 = random.randint(-5, 75)
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1, num2)
    return f'{num1} {op} {num2}', answer

# === [kamer 1] === #
def kamer1():
    global kamer1_bezocht
    kamer1_bezocht = True
    print('Door de twee grote deuren loop je een gang binnen.')
    print('Het ruikt hier muf en vochtig.')
    print('Je ziet een deur voor je.')
    print('')
    time.sleep(1)
    return kamer7()

# === [kamer 7] === #
def kamer7():
    global player_rupees, kamer7_bezocht
    kamer7_bezocht = True

    print('Je loopt naar binnen')
    print('Je ziet iets op de grond')
    print('Je loopt naar naar toe')
    kansvoorRupee = random.randint(1, 10)
    if kansvoorRupee == 1:
        print('Je hebt niks gevonden het is gewoon een lege kamer')
    else:
        while True:
            try:
                neemRupee = input('Je hebt een Rupee gevonden wil je de Rupee meenemen?\n').lower()
                if neemRupee == 'ja':
                    player_rupees += 1
                    print('Je pakt het Rupee op')
                    break
                elif neemRupee == 'nee':
                    print('Je hebt de Rupee op de grond laten liggen')
                    break
                else:
                    print('Kies (ja of nee)')
            except ValueError:
                print('Kies (ja of nee)')

    while True:
        try:
            keuze_uit_twee_deuren = int(input('Je ziet twee deuren, welke zou je kiezen? 1) naar rechts of 2) rechtdoor\n'))
            if keuze_uit_twee_deuren == 1:
                return kamer8()
            elif keuze_uit_twee_deuren == 2:
                return kamer2()
            else:
                print('Kies een nummer (1 of 2)')
        except ValueError:
            print('Kies een nummer (1 of 2)')

    print('')
    time.sleep(1)

# === [kamer 2] === #
def kamer2():
    global player_rupees, kamer2_bezocht
    kamer2_bezocht = True
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een sleutel vast.')
    print('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')
    som, juist_antwoord = randomCalculator()
    print(f'Daarboven zie je een som staan {som}')
    while True:
        try:
            antwoord = int(input('Wat toest je in?\n'))
            if antwoord == juist_antwoord:
                print('Het standbeeld laat een rupee vallen en je pakt het op')
                player_rupees += 1
                break
            else:
                print('Er gebeurt niets....')
                break
        except ValueError:
            print('Voer een nummer in')
    # Choice between room 6 and 8
    while True:
        try:
            keuze_uit_twee_deuren = input('Je ziet twee deuren, welke zou je kiezen? 1) naar rechts of 2) rechtdoor\n').lower()
            if keuze_uit_twee_deuren == 'rechts' or keuze_uit_twee_deuren == '1':
                return kamer8()
            elif keuze_uit_twee_deuren == 'rechtdoor' or keuze_uit_twee_deuren == '2':
                return kamer6()
            else:
                print('Kies een nummer (1 of 2)')
        except ValueError:
            print('Kies een nummer (1 of 2)')
    print('')
    time.sleep(1)

# === [kamer 8] === #
def kamer8():
    global player_rupees, player_health, kamer8_bezocht
    kamer8_bezocht = True
    
    print('Je loopt naar binnen')
    print('Je ziet een gokmachine')
    
    while True:
        try:
            keuze = input('Wil je de gokmachine gebruiken? 1) Ja 2) Nee\n').lower()

            if keuze == 'ja' or keuze == '1':
                print('Je gebruikt de gokmachine en rolt twee dobbelstenen..')
                time.sleep(2)

                dobbelstenen1 = random.randint(1, 6)
                dobbelstenen2 = random.randint(1, 6)
                totaal = dobbelstenen1 + dobbelstenen2

                print(f'De gegooide dobbelstenen: {dobbelstenen1} en {dobbelstenen2} Totaal: {totaal}')

                if totaal > 7:
                    player_rupees *= 2
                    print(f'Gefeliciteerd je hebt je rupees verdubbeld')
                    print(f'Je totale rupees is nu: {player_rupees} rupees')
                    break
                elif totaal < 7:
                    player_health -= 1
                    print('Jammer je bent 1 health verloren')
                    if player_health <= 0:
                        print('Je health is 0 game over')
                        exit()
                    print(f'Jouw huidige health is nu: {player_health}')
                    break
                elif totaal == 7:
                    player_rupees += 1
                    player_health += 4
                    print('JACKPOT!! je hebt 1 rupee en 4 health punten verdiend')
                    break
            elif keuze == 'nee' or keuze == '2':
                print('Je wilde het risico niet nemen. Je kiest ervoor om niet te gokken')
                break
            else:
                print('Ongeldige keuze')
        except ValueError:
            print('Ongeldige keuze')
   
    keuze_uit_twee_deuren = input('Je ziet twee deuren in de verte welke wil je kiezen? 1) eerste 2) tweede\n').lower()
    if keuze_uit_twee_deuren == '1' or keuze_uit_twee_deuren == 'eerste':
        kamer3()
    elif keuze_uit_twee_deuren == '2' or keuze_uit_twee_deuren == 'tweede':
        kamer9()

    print('Je gaat naar de volgende kamer')
    print('')
    time.sleep(1)

# === [kamer 9] === #
def kamer9():
    global player_defense, player_health, kamer9_bezocht

    kamer9_bezocht = True
    print('Je komt deze kamer binnen')
    print('Deze kamer lijkt anders dan de andere kamers')
    print('Zodra je de kamer binnenkomt voel je je powerful')

    randomPerk = random.choice(['Defence', 'Health'])
    if randomPerk == 'Defence':
        player_defense += 1
        amount = 1
    elif randomPerk == 'Health':
        player_health += 2
        amount = 2
    print(f'Je hebt {amount} {randomPerk} gekregen')
    print('Je gaat naar de volgende kamer')
    print('')
    time.sleep(1)
    kamer3()

# === [kamer 3] === #
def kamer3():
    global player_defense, player_attack, player_rupees, player_inventory, kamer3_bezocht

    kamer3_bezocht = True
    print('Je ziet een goblin hij lijkt vriendelijk je benadert hem')
    print(f'De goblin wil je iets verkopen')
    print(f'Je hebt {player_rupees} rupee(s)')

    items = {
        'schild': [1, 1],
        'zwaard': [1, 1],
        'sleutel': [1, 1]
    }

    while True:
        beschikbare_items = [item for item, (cost, stock) in items.items() if player_rupees >= cost and stock > 0]

        if not beschikbare_items:
            print("Je hebt niet genoeg rupees om iets te kopen of alles is uitverkocht.")
            break

        print('De goblin biedt je de volgende items aan:')
        for i, item in enumerate(beschikbare_items, start=1):
            print(f"|{i}| {item.capitalize()} {items[item][0]} rupee(s) | Voorraad: {items[item][1]} |")

        keuze = input('Wat wil je kopen? Typ de naam van het item of "stop" om te stoppen.\n').lower()

        if keuze in beschikbare_items:
            player_rupees -= items[keuze][0]
            items[keuze][1] -= 1
            player_inventory.append(keuze)

            if keuze == 'schild':
                player_defense += 1
                print('Je hebt een schild gekocht')
                print(f'Je totale defense is nu: Defense = {player_defense}')
            elif keuze == 'zwaard':
                player_attack += 2
                print('Je hebt een zwaard gekocht')
                print(f'Je totale attack is nu: Attack = {player_attack}')
            elif keuze == 'sleutel':
                player_inventory.append('sleutel')
                print('Je hebt een sleutel gekocht')

            print(f'Je hebt nu {player_rupees} rupee(s) over.')

        elif keuze == 'stop':
            print('Je hebt ervoor gekozen om niet verder te kopen.')
            break

        else:
            print("Ongeldige keuze, kies een itemnaam of typ 'stop' om te stoppen.")

    print('Op naar de volgende deur.')
    print('')
    time.sleep(1)
    kamer4()

# === [kamer 6] === #
def kamer6():
    global player_defense, player_health, kamer6_bezocht

    kamer6_bezocht = True
    print('Je loopt tegen een zombie aan.')
        
    enemy_name = 'Zombie'
    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2

    zombieBattle = enemyBattle(player_health, player_attack, player_defense, enemy_name, zombie_attack, zombie_defense, zombie_health)

    keuze_uit_twee_deuren = input('Je ziet twee duren welke wil je kiezen? 1) eerste 2) tweede\n').lower()
    if keuze_uit_twee_deuren == '1' or keuze_uit_twee_deuren == 'eerste':
        return kamer8()
    elif keuze_uit_twee_deuren == '2' or keuze_uit_twee_deuren == 'tweede':
        return kamer3()

    print('')
    time.sleep(1)

# === [kamer 4] === #
def kamer4():
    global player_health, kamer4_bezocht

    kamer4_bezocht = True
    print('Je loopt tegen een Ghoul aan.')
    enemy_name = 'Ghoul'
    ghoul_attack = 2
    ghoul_defense = 0
    ghoul_health = 3

    ghoulBattle = enemyBattle(player_health, player_attack, player_defense, enemy_name, ghoul_attack, ghoul_defense, ghoul_health)

    print('')
    time.sleep(1)

    kamer5()

# === [kamer 5] === #
def kamer5():
    global player_inventory, kamer5_bezocht
    
    kamer5_bezocht = True
    sleutel_check = 'sleutel'

    print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
    print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')

    if sleutel_check in player_inventory:
        player_inventory.remove('sleutel')
        print('Je hebt gewonnen en de kist geopend.')
        exit()
    else:
        print('Helaas heb je niets om de kist te openen.')
        print('Game over.')
        exit()
    
    print('')
    time.sleep(1)

kamer1()
