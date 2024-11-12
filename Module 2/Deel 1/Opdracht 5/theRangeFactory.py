aantal_lijstjes = int(input('Hoeveel lijstjes wilt u zien? '))
lijstjes = []

for nummer in range(1, aantal_lijstjes + 1):
    lengte = int(input(f'Hoelang moet lijst {nummer} zijn? '))
    lijst = list(range(nummer, nummer + nummer * lengte, nummer))
    lijstjes.append(lijst)

print(lijstjes)