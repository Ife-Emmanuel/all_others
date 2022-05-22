def printprocess (toppings, size=30):
    print('I made a ' + str(size) + ' sized pizza  ' + ' with the following toppings: ')
    for i, topping in enumerate(toppings):
        print(str(i + 1) + '. ' + str(topping))
