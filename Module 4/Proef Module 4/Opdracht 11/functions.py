import math
import time
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY, COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY, COST_INN_HUMAN_SILVER_PER_NIGHT, COST_INN_HORSE_COPPER_PER_NIGHT

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return silver2gold(copper2silver(amount))

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    totalGold = 0
    if 'copper' in personCash:
        totalGold += copper2gold(personCash['copper'])
    if 'silver' in personCash:
        totalGold += silver2gold(personCash['silver'])
    if 'gold' in personCash:
        totalGold += personCash['gold']
    if 'platinum' in personCash:
        totalGold += platinum2gold(personCash['platinum'])

    return round(totalGold, 2)

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    human_copper = people * COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS
    horse_copper = horses * COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS
    return round(copper2gold(human_copper + horse_copper), 2)

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    new_list = []
    for dictionary in list:
        if key in dictionary:
            if dictionary[key] == value:
                new_list.append(dictionary)
    return new_list

def getAdventuringPeople(people:list) -> list:
   adventuring_people = getFromListByKeyIs(people, 'adventuring', True)
   return adventuring_people

def getShareWithFriends(friends:list) -> list:
    sharing_friends = getFromListByKeyIs(friends, 'shareWith', True)
    return sharing_friends

def getAdventuringFriends(friends:list) -> list:
    adventuring = getAdventuringPeople(friends)
    sharing = getShareWithFriends(friends)
    result = []
    for friend in adventuring:
        if friend in sharing:
            result.append(friend)
    return result

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    horse_cost_silver = horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS
    horse_cost_gold = silver2gold(horse_cost_silver)

    weeks_needed = math.ceil(JOURNEY_IN_DAYS / 7)
    tent_cost_gold = tents * COST_TENT_GOLD_PER_WEEK * weeks_needed
    return horse_cost_gold + tent_cost_gold

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    # item_strings = []
    # for item in items:
    #     unit = item['unit']
    #     name = item['name']
    #     amount = item['amount']

    #     if unit.strip() == '':
    #         item_str = f"{amount} {name}"
    #     else:
    #         item_str = f"{amount}{unit} {name}"
        
    #     item_strings.append(item_str)

    # if len(item_strings) == 1:
    #     return item_strings[0]
    # else:
    #     joined = ', '.join(item_strings[:-1])
    #     return f"{joined} & {item_strings[-1]}"
    zin = ""
    for index, item in enumerate(items):
        unit = item['unit']
        name = item['name']
        amount = item['amount']

        zin += f"{amount}{unit} {name}"
        if index < len(items) - 2:
            zin += ", "
        elif index < len(items) - 1:
            zin += " & "
    return zin
        


def getItemsValueInGold(items:list) -> float:
    total = 0.0
    for item in items:
        price = item['price']
        amount = item['amount']
        price_type = price['type']
        price_amount = price['amount']

        if price_type == 'copper':
            total += copper2gold(price_amount * amount)
        elif price_type == 'silver':
            total += silver2gold(price_amount * amount)
        elif price_type == 'gold':
            total += price_amount * amount
        elif price_type == 'platinum':
            total += platinum2gold(price_amount * amount)

    return round(total, 2)


##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    total = 0.0
    for person in people:
        total += getPersonCashInGold(person['cash'])
    return round(total, 2)

##################### O10 #####################

def getInterestingInvestors(investors):
    return [investor for investor in investors if investor['profitReturn'] <= 10]

def getAdventuringInvestors(investors):
    interesting_investors = getInterestingInvestors(investors)
    return [investor for investor in interesting_investors if investor.get('adventuring', False)]

def getTotalInvestorsCosts(investors, gear):
    if not investors or not gear:
        return 0.0
    
    total = 0.0
    for investor in getAdventuringInvestors(investors):
        total += (
            copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS) +
            copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS) +
            silver2gold(COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS) +
            COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7) +
            getItemsValueInGold(gear)
        )
    
    return round(total, 2)


##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold, people, horses):
    nights = 0
    while getJourneyInnCostsInGold(nights + 1, people, horses) <= leftoverGold:
        nights += 1
    
    return nights


def getJourneyInnCostsInGold(nightsInInn, people, horses):
    if nightsInInn == 0:
        return 0.0

    total_cost = (
        silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT * people * nightsInInn) +
        copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT * horses * nightsInInn)
    )
    
    return round(total_cost, 2)

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()