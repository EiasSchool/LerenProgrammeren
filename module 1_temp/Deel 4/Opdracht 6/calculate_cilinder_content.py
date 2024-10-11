import math
from test_lib import test, report

def calculate_cilinder_content(diameter, height):
    radius = diameter / 2
    volume = (radius * radius) * math.pi * height
    return round(volume, 1)

test_gegevens = [
    (8.0, 5.0, 251.3),
    (11.0, 7.0, 665.2),
    (18.0, 7.0, 1781.3),
    (15.0, 2.0, 353.4),
    (0.0, 6.0, 0.0)
]

for diameter, height, expect_content in test_gegevens:
    calculated_content = calculate_cilinder_content(diameter,height)
    name = f'test diameter: {diameter} height: {height}'

    test(name, expect_content, calculated_content )
report()