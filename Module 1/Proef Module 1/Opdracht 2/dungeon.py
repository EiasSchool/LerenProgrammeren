import time, math
import random
import operator

player_attack = 1
player_defense = 0
player_health = 3
player_inventory = []

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)
# === [kamer 2] === #
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

print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
som, juist_antwoord = randomCalculator()
print(f'Daarboven zie je een som staan {som}')
antwoord = int(input('Wat toest je in?\n'))

if antwoord == juist_antwoord:
    print('Het stadbeeld laat de sleutel vallen en je pakt het op')
    player_inventory.append('sleutel')
else:
    print('Er gebeurt niets....')

print('Je zie een deur achter het standbeeld.')
print('')
time.sleep(1)
# === [kamer 6] === #
zombie_attack = 1
zombie_defense = 0
zombie_health = 2

print('Je loopt tegen een zombie aan.')

zombie_hit_damage = max(zombie_attack - player_defense, 0)
if zombie_hit_damage == 0:
    print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)

    player_hit_damage = max(player_attack - zombie_defense, 0)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        player_health -= zombie_hit_damage * (player_attack_amount)
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()

print('')
time.sleep(1)
# === [kamer 3] === #
def randomItem():
    item = {
        'schild': player_defense,
        'zwaard': player_attack,
    }
    deItem = random.choice(list(item.keys()))
    return deItem

item = randomItem()
if item == 'schild':
    player_defense += 1
    effect = '+1 op je defense'
    stat = f'Je totale defense is nu: Defense = {player_defense}.'
elif item == 'zwaard':
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
# === [kamer 4] === #
zombie_attack = 2
zombie_defense = 0
zombie_health = 3

print('Je loopt tegen een zombie aan.')

zombie_hit_damage = max(zombie_attack - player_defense, 0)
if zombie_hit_damage == 0:
    print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)

    player_hit_damage = max(player_attack - zombie_defense, 0)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        player_health -= zombie_hit_damage * (player_attack_amount)
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()

print('')
time.sleep(1)
# === [kamer 5] === #
sleutel_check = 'sleutel'

print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')

if sleutel_check in player_inventory:
    print('Je hebt gewonnen en de kist geopend.')
else:
    print('Helaas heb je niets om de kist te openen.')
    print('Game over.')
# === [kamer 6] === #
