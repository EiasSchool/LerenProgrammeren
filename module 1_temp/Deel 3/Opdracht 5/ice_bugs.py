def convertToEuroText (amount):
    return "€{:.2f}".format(float(amount)).replace(".", ",")

SMALL_PRICE = 1.25
MEDIUM_PRICE = 2.10

amount = int(input('Hoeveel ijsjes van {} wil je bestellen? '.format(convertToEuroText(SMALL_PRICE))))
amount = int(input('En hoeveel ijsjes van {} wil je bestellen? '.format(convertToEuroText(MEDIUM_PRICE))))
totalPrice = int(amount * SMALL_PRICE) + int(amount * MEDIUM_PRICE)

print('Dat is dan {} totaal'.format(convertToEuroText(totalPrice)))