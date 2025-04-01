import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import JOURNEY_IN_DAYS

#schrijf je test hier

expected = True

if JOURNEY_IN_DAYS == 10:
    resault = True

test('Journey in days - test', expected, resault)

if __name__ == "__main__":
    report()