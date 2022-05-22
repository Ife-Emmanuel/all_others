from pizzamakemodule import printprocess  as pp

toppings = []
print('Enter \'q\' to exit if topping is completed')
while True:
    required_topping = input('Enter the toppings you want for your pizza : ')
    if required_topping == 'q':
        break
    else:
        toppings.append(required_topping)


pp(toppings, 32)