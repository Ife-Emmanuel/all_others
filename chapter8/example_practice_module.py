def make_pizza(size, *toppings):
    """Summarize the pizza we are to make"""
    print('\nMaking a ' + str(size) +
          ' inch sized with the following toppings: ')
    for topping in toppings:
        print(topping)