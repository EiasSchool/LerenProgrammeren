gastheer = False
gasten = False
drank = False
chips = True

#Een feest moet minimaal gasten of een gastheer hebben.
start_condition_1 = gastheer or gasten
start_condition_2 = gastheer or (gasten and drank and chips)
start_condition_3 = not (chips and not drank)
start_condition_4 = not (gasten and not (drank and chips))
start_condition_5 = not (gastheer and not drank)
start_condition_6 = not (chips and not gasten and not gastheer and not drank)

if start_condition_1 and start_condition_2 and start_condition_3 and start_condition_4 and start_condition_5 and start_condition_6:
    print('Start the Party')
else:
    print('No Party')