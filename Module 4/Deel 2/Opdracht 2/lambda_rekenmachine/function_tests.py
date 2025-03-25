from functions import addition, subtraction, multiplication, division
from calculations import CALCULATIONS
from test_lib import test, report

getal1 = 3.0
getal2 = 2.0

expected = addition(getal1, getal2)
result_lambda = CALCULATIONS['addition'](getal1, getal2)
test('Test addition function', expected, result_lambda)

expected = subtraction(getal1, getal2)
result_lambda = CALCULATIONS['subtraction'](getal1, getal2)
test('Test subtraction function', expected, result_lambda)

expected = multiplication(getal1, getal2)
result_lambda = CALCULATIONS['multiplication'](getal1, getal2)
test('Test multiplication function', expected, result_lambda)

expected = division(getal1, getal2)
result_lambda = CALCULATIONS['division'](getal1, getal2)
test('Test division function', expected, result_lambda)

report()