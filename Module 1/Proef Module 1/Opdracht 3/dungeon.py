import time, math
import random
import operator

# === player stats === #
player_attack = 1
player_defense = 0
player_health = 3
player_inventory = []

# === functions sectie === #
#fight function voor de vijanden
def enemeyBattle(player_health, player_attack, player_defense, enemy_name, enemy_attack, enemy_defense, enemy_health):
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

#function voor de som voor de sleutel
def randomCalculator():
    ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul
        }
    num1 = random.randint(10,25)
    num2 = random.randint(-5,75)
    op = random.choice(list(ops.keys()))
    antwoord = ops.get(op)(num1,num2)
    return f'{num1} {op} {num2}', antwoord

#random item function
def randomItem():
    item = {
        'schild': player_defense,
        'zwaard': player_attack,
    }
    deItem = random.choice(list(item.keys()))
    return deItem

# === [kamer 1] === #
def kamer1():
    print('Door de twee grote deuren loop je een gang binnen.')
    print('Het ruikt hier muf en vochtig.')
    print('Je ziet een deur voor je.')
    print('')
    time.sleep(1)

# === [kamer 2] === #
def kamer2():
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een sleutel vast.')
    print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    som, juist_antwoord = randomCalculator()
    print(f'Daarboven zie je een som staan {som}')
    while True:
        try:
            antwoord = int(input('Wat toest je in?\n'))
            if antwoord == juist_antwoord:
                print('Het stadbeeld laat de sleutel vallen en je pakt het op')
                player_inventory.append('sleutel')
                break
            else:
                print('Er gebeurt niets....')
                break
        except ValueError:
            print('Please enter a number')
    #keuze tussen kamer 6 en 3
    while True:
        try:
            keuze_uit_twee_deuren = int(input('Je ziet twee deuren, welke zou je kiezen? 1 of 2\n'))
            if keuze_uit_twee_deuren == 1:
                kamer3()
                break
            elif keuze_uit_twee_deuren == 2:
                kamer6()
                break
            else:
                print('Please choose a number (1 or 2)')
        except ValueError:
            print('Please choose a number (1 or 2)')
    print('')
    time.sleep(1)

# === [kamer 3] === #
def kamer3():
    global player_defense, player_attack
    item = randomItem()
    if item == 'schild':
        player_inventory.append('schild')
        player_defense += 1
        effect = '+1 op je defense'
        stat = f'Je totale defense is nu: Defense = {player_defense}.'
    elif item == 'zwaard':
        player_inventory.append('zwaard')
        player_attack += 2
        effect = '+2 op je attack'
        stat = f'Je totale attack is nu: Attack = {player_attack}.'

    print('Je duwt hem open en stap een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een {item}, dit item gaf je {effect}.')
    print(f'Je pakt het {item} op en houd het bij je.')
    print(f'{stat}')
    print('Op naar de volgende deur.')
    print('')
    time.sleep(1)

# === [kamer 6] === #
def kamer6():
    print('Je loopt tegen een zombie aan.')
        
    enemy_name = 'Zombie'
    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2

    zombieBattle = enemeyBattle(player_health, player_attack, player_defense, enemy_name, zombie_attack, zombie_defense, zombie_health)

    print('')
    time.sleep(1)

# === [kamer 4] === #
def kamer4():
    print('Je loopt tegen een Ghoul aan.')
    enemy_name = 'Ghoul'
    ghoul_attack = 2
    ghoul_defense = 0
    ghoul_health = 3

    ghoulBattle = enemeyBattle(player_health, player_attack, player_defense, enemy_name, ghoul_attack, ghoul_defense, ghoul_health)

    print('')
    time.sleep(1)

# === [kamer 5] === #
def kamer5():
    sleutel_check = 'sleutel'

    print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
    print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')

    if sleutel_check in player_inventory:
        player_inventory.remove('sleutel')
        print('Je hebt gewonnen en de kist geopend.')
    else:
        print('Helaas heb je niets om de kist te openen.')
        print('Game over.')

kamer1()
kamer2()
kamer4()
kamer5()