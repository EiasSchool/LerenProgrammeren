import time
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    silver = copper2silver(amount)
    return silver2gold(silver)

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
    pass

def getNumberOfTentsNeeded(people:int) -> int:
    pass

def getTotalRentalCost(horses:int, tents:int) -> float:
    pass

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

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