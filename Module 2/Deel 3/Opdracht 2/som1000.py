currentNumber = 50
total = 0
counter = 1

while total <= 1000:
    total += currentNumber
    numbsAdded = [str (i) for i in range(50, currentNumber + 1)]
    print(f"{counter}. {' + '.join(numbsAdded)} = {total}")
    currentNumber += 1
    counter += 1