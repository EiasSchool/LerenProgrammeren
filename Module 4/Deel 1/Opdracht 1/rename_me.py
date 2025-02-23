def isEven(number:int) -> bool:
    return number % 2 == 0

def reverseText(text:str) -> str:
    sentence = text.split()
    words = sentence[::-1]
    reversedText = ' '.join(words)
    return reversedText

def uniqueCharactersCounter(text:str) -> int:
    uniqueCharacters = set(text)
    charactersAmount = len(uniqueCharacters)
    return charactersAmount

def avgWordLength(sentence:str) -> float:
    words = sentence.split()
    
    total = 0
    for word in words:
        total += len(word)

    avgLength = total / len(words)
    return avgLength

def multiplicationTable(number:int, limit:int=10) -> None:
    for multiplier in range(1, limit+1):
        resault = multiplier * number
        print(f'{multiplier} x {number} = {resault}')

print(isEven(5)) #geeft True als het nummer even is en False als het oneven is
print(reverseText("I ate an apple")) #keert de zin om bijvoorbeeld als je typt: "i ate an apple" wordt "apple an ate i"
print(uniqueCharactersCounter("apple")) #geeft de lengte van het woord/zin zonder de gedupliceerde letters te berekenen
print(avgWordLength("Hello its me"))  #geeft de gemiddelde lengte van woorden in een zin als float
multiplicationTable(10, 1) #geef de vermenigvuldigingstabel voor het getal dat je eerst typt en hoe lang je het wilt hebben