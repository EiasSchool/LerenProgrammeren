import math
from test_lib import test, report

def afronden(bedrag):
    stuivers = 0.05
    totaal = round(bedrag / stuivers) * stuivers
    return round(totaal, 2)

test_gegevens = [
    (2.24, 2.25),
    (13.01, 13.00),
    (7.76, 7.75),
    (4.43, 4.45),
    (0.98, 1.00)
]

for bedrag, verwacht_bedrag in test_gegevens:
    berekend_bedrag = afronden(bedrag)
    name = f'test bedrag: {bedrag}'

    test(name, verwacht_bedrag, berekend_bedrag)

report()
