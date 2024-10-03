#import hier je functie "from [bestandsnaamZonderExtentie] import [functieNaam]"
from test_lib import test, report
from meten_is_weten import verglijk_getallen

expected = 'Beide getallen zijn even groot' #resultaat
result = verglijk_getallen(10, 10) #roep hier je functie aan met 2 dezelfde getallen
test('TEST nr1=nr2', expected, result)

expected = '10 is groter dan 5' #resultaat
result = verglijk_getallen(10, 5) #roep hier je functie aan waar nr1 groter is dan nr2
test('TEST nr1>nr2', expected, result)

expected = '15 is groter dan 5' #resultaat
result = verglijk_getallen(5, 15) #roep hier je functie aan  waar nr1 kleiner is dan nr2
test('TEST nr1<nr2', expected, result)

if __name__ == "__main__":
    report()