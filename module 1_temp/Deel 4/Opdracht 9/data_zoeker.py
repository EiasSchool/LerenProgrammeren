from test_lib import test, report

def get_value(data: str, separator: str, position: int) -> str:
  splitted_strings = data.split(separator)

  if 0 <= position < len(splitted_strings):
        return splitted_strings[position]
  else:
     return ''

test_gegevens = [
    ('Sofie:8,Emma:7,Ahmed:9,Daan:6', ',', 2, 'Ahmed:9'),
    ('cat,dog,mouse,bird', ',', 1, 'dog'),
    ('apple|orange|banana|grape', '|', 3, 'grape'),
    ('one two three', ' ', 2, 'three'),
    ('item1:item2:item3', ':', 5, ''),
    ('A,B,C', ',', -1, ''),
]

for data, separator, position, expected in test_gegevens:
    result = get_value(data, separator, position)
    name = f'test data: {data}, separator: "{separator}", position: {position}'
    test(name, expected, result)

report()
