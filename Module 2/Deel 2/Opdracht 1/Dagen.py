dagen = ('Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag')
weekenddagen = dagen[5:6]
werkdagen = dagen[0:5]
werkdagen_str = ', '.join(werkdagen[:-1]) + ' & ' + werkdagen[-1]
omgekeerdDagen = ' -> '.join(reversed(dagen))
omgekeerdWerkdagen = reversed(dagen[0:5])

print('Alle dagen van de week zijn:')

for dag in dagen:
    print(f'- {dag}')

print(f'\nDe weekenddagen zijn: {dagen[5]} & {dagen[6]}.\n')
print(f'De werkdagen zijn: {werkdagen_str}.\n')
print(f'Alle dagen van de week in omgekeerde volgorde zijn: {omgekeerdDagen}.\n')
print(f'De werkdagen in omgekeerde volgorde zijn:')
for dag in omgekeerdWerkdagen:
    print(f'- {dag}')

print(f'\nDe weekenddagen in een omgekeerde volgorde zijn: {dagen[6]} + {dagen[5]}\n')