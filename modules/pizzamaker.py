ddef makerpizza(size, *toppings):
    print('The ' + str(size) + ' sized pizza has the following'
                          'the following toppings : ')
    for topping in toppings:
        print(topping)