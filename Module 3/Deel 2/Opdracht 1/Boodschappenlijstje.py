def createShoppingList():
    shoppinglist = {}

    while True:
        item = input('Enter the item (or type "Done" to finish): ').strip().lower()
        if item == 'done':
            break

        try:
            quantity = int(input(f'Enter the quantity for {item}: '))
            if quantity <= 0:
                print('Please enter a positive number for the quantity')
                continue
        except ValueError:
            print('Please enter a valid number for the quantity')
            continue

        if item in shoppinglist:
            shoppinglist[item] += quantity
        else:
            shoppinglist[item] = quantity

    print('-[ ShoppingList ]-')
    for item, quantity in shoppinglist.items():
        print(f'{quantity}x {item.capitalize()}')
    print('------------------')

createShoppingList()