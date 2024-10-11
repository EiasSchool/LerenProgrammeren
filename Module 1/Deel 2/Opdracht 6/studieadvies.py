from studieadviestext import *

print(STUDIEDOKTER_TITEL)

# vraag1 = int(input(f'{AANTAL_WEKEN_VRAAG}\n'))
vraag1 = int(input(f'{COMPETENTIE_STELLING_1}\n{OPTIES}\n'))
vraag2 = int(input(f'{COMPETENTIE_STELLING_2}\n{OPTIES}\n'))
vraag3 = int(input(f'{COMPETENTIE_STELLING_3}\n{OPTIES}\n'))
vraag4 = int(input(f'{COMPETENTIE_STELLING_4}\n{OPTIES}\n'))
vraag5 = int(input(f'{COMPETENTIE_STELLING_5}\n{OPTIES}\n'))
vraag6 = int(input(f'{COMPETENTIE_STELLING_6}\n{OPTIES}\n'))
vraag7 = int(input(f'{COMPETENTIE_STELLING_7}\n{OPTIES}\n'))
gemiddelde_score = (vraag1 + vraag2 + vraag3 + vraag4 + vraag5 + vraag6 + vraag7)//7

print(COMPETENTIE_ADVIES_TITEL)
if gemiddelde_score <= 2:
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif gemiddelde_score <= 3:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)
