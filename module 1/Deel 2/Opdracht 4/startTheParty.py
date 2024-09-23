gastheer_naam = str(input('Wie is de gastheer?\n')).lower()
gasten = False
drank = True
chips = False

mijnnaam = 'Eias'.lower()
SLBer_naam = 'Rudi Van Pelt'.lower()

mijnnaam_checker = gastheer_naam == mijnnaam
SLBer_naam_checker = gastheer_naam == SLBer_naam
gastheer = bool(gastheer_naam)

#Een feest moet minimaal gasten of een gastheer hebben.
start_condition_1 = gastheer or gasten
start_condition_2 = gastheer or (gasten and drank and chips)
start_condition_3 = not (chips and not drank)
start_condition_4 = not (gasten and not (drank and chips))
start_condition_5 = not (gastheer and not drank)
start_condition_6 = not (chips and not gasten and not gastheer and not drank)

feeststart = mijnnaam_checker or (start_condition_1 and start_condition_2 and start_condition_3 and start_condition_4 and start_condition_5 and start_condition_6)
geenfeest = SLBer_naam_checker

if feeststart and not geenfeest:
    print('Start the Party')
else:
    print('No Party')